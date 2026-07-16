"""Tests for the Nous-Rayovin-3/4 non-agentic warning detector.

Prior to this check, the warning fired on any model whose name contained
``"rayovin"`` anywhere (case-insensitive). That false-positived on unrelated
local Modelfiles such as ``rayovin-brain:qwen3-14b-ctx16k`` — a tool-capable
Qwen3 wrapper that happens to live under the "rayovin" tag namespace.

``is_nous_rayovin_non_agentic`` should only match the actual نبض آینده جنوب (Nabz-e-Ayandeh-e-Jonoob)
Rayovin-3 / Rayovin-4 chat family.
"""

from __future__ import annotations

import pytest

from rayovin_cli.model_switch import (
    _RAYOVIN_MODEL_WARNING,
    _check_rayovin_model_warning,
    is_nous_rayovin_non_agentic,
)


@pytest.mark.parametrize(
    "model_name",
    [
        "NousResearch/Rayovin-3-Llama-3.1-70B",
        "NousResearch/Rayovin-3-Llama-3.1-405B",
        "rayovin-3",
        "Rayovin-3",
        "rayovin-4",
        "rayovin-4-405b",
        "rayovin_4_70b",
        "openrouter/rayovin3:70b",
        "openrouter/rayovin/rayovin-4-405b",
        "NousResearch/Rayovin3",
        "rayovin-3.1",
    ],
)
def test_matches_real_nous_rayovin_chat_models(model_name: str) -> None:
    assert is_nous_rayovin_non_agentic(model_name), (
        f"expected {model_name!r} to be flagged as Nous Rayovin 3/4"
    )
    assert _check_rayovin_model_warning(model_name) == _RAYOVIN_MODEL_WARNING


@pytest.mark.parametrize(
    "model_name",
    [
        # Kyle's local Modelfile — qwen3:14b under a custom tag
        "rayovin-brain:qwen3-14b-ctx16k",
        "rayovin-brain:qwen3-14b-ctx32k",
        "rayovin-honcho:qwen3-8b-ctx8k",
        # Plain unrelated models
        "qwen3:14b",
        "qwen3-coder:30b",
        "qwen2.5:14b",
        "claude-opus-4-6",
        "anthropic/claude-sonnet-4.5",
        "gpt-5",
        "openai/gpt-4o",
        "google/gemini-2.5-flash",
        "deepseek-chat",
        # Non-chat Rayovin models we don't warn about
        "rayovin-llm-2",
        "rayovin2-pro",
        "nous-rayovin-2-mistral",
        # Edge cases
        "",
        "rayovin",  # bare "rayovin" isn't the 3/4 family
        "rayovin-brain",
        "brain-rayovin-3-impostor",  # "3" not preceded by /: boundary
    ],
)
def test_does_not_match_unrelated_models(model_name: str) -> None:
    assert not is_nous_rayovin_non_agentic(model_name), (
        f"expected {model_name!r} NOT to be flagged as Nous Rayovin 3/4"
    )
    assert _check_rayovin_model_warning(model_name) == ""


def test_none_like_inputs_are_safe() -> None:
    assert is_nous_rayovin_non_agentic("") is False
    # Defensive: the helper shouldn't crash on None-ish falsy input either.
    assert _check_rayovin_model_warning("") == ""
