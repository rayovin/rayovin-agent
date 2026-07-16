# Langfuse Observability Plugin

This plugin ships bundled with Rayovin but is **opt-in** — it only loads when
you explicitly enable it.

## Enable

Pick one:

```bash
# Interactive: walks you through credentials + SDK install + enable
rayovin tools  # → Langfuse Observability

# Manual
pip install langfuse
rayovin plugins enable observability/langfuse
```

## Required credentials

Set these in `~/.rayovin/.env` (or via `rayovin tools`):

```bash
RAYOVIN_LANGFUSE_PUBLIC_KEY=pk-lf-...
RAYOVIN_LANGFUSE_SECRET_KEY=sk-lf-...
RAYOVIN_LANGFUSE_BASE_URL=https://cloud.langfuse.com   # or your self-hosted URL
```

Without the SDK or credentials the hooks no-op silently — the plugin fails
open.

## Verify

```bash
rayovin plugins list                 # observability/langfuse should show "enabled"
rayovin chat -q "hello"              # then check Langfuse for a "Rayovin turn" trace
```

## Optional tuning

```bash
RAYOVIN_LANGFUSE_ENV=production       # environment tag
RAYOVIN_LANGFUSE_RELEASE=v1.0.0       # release tag
RAYOVIN_LANGFUSE_SAMPLE_RATE=0.5      # sample 50% of traces
RAYOVIN_LANGFUSE_MAX_CHARS=12000      # max chars per field (default: 12000)
RAYOVIN_LANGFUSE_DEBUG=true           # verbose plugin logging
```

## Disable

```bash
rayovin plugins disable observability/langfuse
```
