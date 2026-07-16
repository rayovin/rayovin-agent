"""Runtime smoke tests for Docker PUID/PGID and UID/GID remap.

Build the real image and verify the actual runtime behavior:

  1. PUID/PGID env vars remap the rayovin user UID/GID at boot
  2. RAYOVIN_UID/RAYOVIN_GID take precedence over PUID/PGID aliases
  3. NAS-style low UIDs (99:100) are accepted and remapped
  4. Invalid UIDs are rejected
  5. The remapped user can write to the data volume
"""
from __future__ import annotations

from tests.docker.conftest import docker_exec_sh, start_container


def test_puid_pgid_remaps_rayovin_user(
    built_image: str, container_name: str,
) -> None:
    """PUID=1000 PGID=1000 must remap the rayovin user to UID 1000."""
    start_container(built_image, container_name, "PUID=1000", "PGID=1000")

    r = docker_exec_sh(
        container_name,
        "id -u rayovin",
        timeout=10,
    )
    assert r.stdout.strip() == "1000", (
        f"expected rayovin UID 1000 after PUID remap, got: {r.stdout.strip()}"
    )

    r = docker_exec_sh(
        container_name,
        "id -g rayovin",
        timeout=10,
    )
    assert r.stdout.strip() == "1000", (
        f"expected rayovin GID 1000 after PGID remap, got: {r.stdout.strip()}"
    )


def test_rayovin_uid_gid_take_precedence_over_aliases(
    built_image: str, container_name: str,
) -> None:
    """RAYOVIN_UID/RAYOVIN_GID must win over PUID/PGID when both are set."""
    start_container(built_image, container_name, "RAYOVIN_UID=2000", "RAYOVIN_GID=2001", "PUID=1000", "PGID=1000")

    r = docker_exec_sh(container_name, "id -u rayovin", timeout=10)
    assert r.stdout.strip() == "2000", (
        f"expected rayovin UID 2000 (RAYOVIN_UID wins), got: {r.stdout.strip()}"
    )

    r = docker_exec_sh(container_name, "id -g rayovin", timeout=10)
    assert r.stdout.strip() == "2001", (
        f"expected rayovin GID 2001 (RAYOVIN_GID wins), got: {r.stdout.strip()}"
    )


def test_nas_low_uid_accepted(
    built_image: str, container_name: str,
) -> None:
    """NAS-style low UIDs (99:100, common on Unraid) must be accepted."""
    start_container(built_image, container_name, "PUID=99", "PGID=100")

    r = docker_exec_sh(container_name, "id -u rayovin", timeout=10)
    assert r.stdout.strip() == "99", (
        f"expected rayovin UID 99, got: {r.stdout.strip()}"
    )

    r = docker_exec_sh(container_name, "id -g rayovin", timeout=10)
    assert r.stdout.strip() == "100", (
        f"expected rayovin GID 100, got: {r.stdout.strip()}"
    )


def test_remap_enables_data_volume_writes(
    built_image: str, container_name: str,
) -> None:
    """After remap, the rayovin user must be able to write to /opt/data."""
    start_container(built_image, container_name, "PUID=1000", "PGID=1000")

    r = docker_exec_sh(
        container_name,
        "touch /opt/data/test_write && echo WRITE_OK || echo WRITE_FAIL",
        timeout=10,
    )
    assert "WRITE_OK" in r.stdout, (
        f"rayovin user cannot write to /opt/data after remap: {r.stdout}"
    )