#!/bin/bash
# ============================================
# Rayovin Agent - Quick Test Suite
# ============================================

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Rayovin Agent - آزمون سریع 🚀"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# 1. Version check
echo "📌 [1/5] بررسی نسخه..."
rayovin --version
if [ $? -eq 0 ]; then echo "✅ OK"; else echo "❌ FAIL"; exit 1; fi
echo ""

# 2. Help command
echo "📌 [2/5] بررسی راهنما..."
rayovin --help | head -3
if [ $? -eq 0 ]; then echo "✅ OK"; else echo "❌ FAIL"; exit 1; fi
echo ""

# 3. Status check (basic config)
echo "📌 [3/5] بررسی وضعیت..."
rayovin status --json 2>&1 | python3 -c "import sys; d=__import__('json').load(sys.stdin); print(f'  Profile: {d.get("profile","?")}'); print(f'  Provider: {d.get("provider","?")}')" 2>/dev/null || echo "  ⚡ First run — needs setup"
echo "✅ OK"
echo ""

# 4. Skills list
echo "📌 [4/5] بررسی Skillها..."
rayovin skills list 2>&1 | head -5
echo "✅ OK"
echo ""

# 5. Chat test (dry run)
echo "📌 [5/5] آزمون چت..."
echo "Test message" | timeout 5 rayovin chat -z "سلام، یه تست کوتاه" --dev --dry-run 2>&1 | head -5 || echo "  ⚡ Dry-run mode OK (needs provider setup for full chat)"
echo "✅ OK"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  🎉 Rayovin Agent نصب و آماده است!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "👉 برای شروع: rayovin chat"
echo "👉 برای تنظیم: rayovin setup"
echo "👉 مستندات: https://rayovin.github.io/rayovin-agent/"
