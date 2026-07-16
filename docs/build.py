import os
REPO = "/tmp/rayovin-agent/docs"

HEADER = '''<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="[DESC]">
  <meta property="og:title" content="[TITLE]">
  <meta property="og:description" content="[DESC]">
  <meta property="og:image" content="https://raw.githubusercontent.com/rayovin/rayovin-agent/main/assets/banner.png">
  <link rel="icon" type="image/x-icon" href="https://raw.githubusercontent.com/rayovin/rayovin-agent/main/assets/favicon.ico">
  <link rel="stylesheet" href="css/style.css">
  <title>[TITLE]</title>
</head>
<body>
<nav>
  <div class="logo">
    <img src="https://raw.githubusercontent.com/rayovin/rayovin-agent/main/assets/favicon-32.png" alt="">
    Rayovin Agent
  </div>
  <div class="links">
    <a href="index.html">خانه</a>
    <a href="features.html">ویژگی‌ها</a>
    <a href="guide.html">راهنما</a>
    <a href="install.html">نصب</a>
    <a href="api.html">API</a>
    <a href="https://github.com/rayovin/rayovin-agent">GitHub</a>
  </div>
</nav>
'''

FOOTER = '''
<footer>
  <p>
    ساخته شده با ❤️ توسط <a href="https://github.com/rayovin">نبض آینده جنوب</a> &nbsp;|&nbsp;
    <a href="https://github.com/rayovin/rayovin-agent/blob/main/LICENSE">MIT License</a>
  </p>
</footer>
</body>
</html>'''

def pg(title, desc, body):
    return HEADER.replace('[TITLE]', title).replace('[DESC]', desc) + body + FOOTER

# =================== HOME ===================
home_body = '''
<div class="hero">
  <h1>🤖 Rayovin Agent</h1>
  <div class="subtitle">هوش مصنوعی رایوین — همراه هوشمند فارسی</div>
  <div class="persian">محصول شرکت نبض آینده جنوب (Nabz-e-Ayandeh-e-Jonoob)</div>
  <div class="badge-row">
    <a href="https://github.com/rayovin/rayovin-agent/releases"><img src="https://img.shields.io/github/v/release/rayovin/rayovin-agent?color=ffd700&label=Version&style=for-the-badge" alt="Version"></a>
    <a href="https://github.com/rayovin/rayovin-agent/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License"></a>
    <a href="https://github.com/rayovin/rayovin-agent"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
  </div>
  <div class="hero-buttons">
    <a href="install.html" class="btn btn-primary">🚀 نصب سریع</a>
    <a href="guide.html" class="btn btn-outline">📖 راهنما</a>
  </div>
</div>
<div class="container page">
  <h2>✨ چرا Rayovin Agent؟</h2>
  <p>یک عامل هوشمند تمام‌عیار که از تجربه‌هاش یاد می‌گیره، مهارت می‌سازه، حافظه داره، و همه‌جا همراته — از تلگرام تا خط فرمان.</p>
  <div class="features">
    <div class="feature"><div class="icon">🧠</div><h4>یادگیری خودکار</h4><p>از مکالمات Skill می‌سازه و خودش رو بهتر می‌کنه</p></div>
    <div class="feature"><div class="icon">📱</div><h4>همه‌جا همراته</h4><p>تلگرام، دیسکورد، واتساپ، CLI و دسکتاپ</p></div>
    <div class="feature"><div class="icon">⏰</div><h4>زمان‌بندی</h4><p>Cron داخلی برای کارهای دوره‌ای</p></div>
    <div class="feature"><div class="icon">🔄</div><h4>کار موازی</h4><p>چند زیرعامل همزمان برای کارهای سنگین</p></div>
    <div class="feature"><div class="icon">🛠</div><h4>۷۶+ Skill</h4><p>برنامه‌نویسی، امنیت، API، تحلیل داده و...</p></div>
    <div class="feature"><div class="icon">🔒</div><h4>حافظه بلندمدت</h4><p>بین جلسات همه چیز رو به خاطر میاره</p></div>
  </div>
  <h2>📊 آمار</h2>
  <table>
    <tr><th>ویژگی</th><th>مقدار</th></tr>
    <tr><td>نسخه</td><td>v0.18.2</td></tr>
    <tr><td>زبان</td><td>Python 3.11+</td></tr>
    <tr><td>پلتفرم‌ها</td><td>لینوکس، مک، WSL2</td></tr>
    <tr><td>پیام‌رسان‌ها</td><td>تلگرام، دیسکورد، واتساپ، سیگنال، اسلک و ۲۰+</td></tr>
    <tr><td>پکیج</td><td><code>rayovin-agent</code> روی PyPI</td></tr>
  </table>
  <h2>🚀 شروع سریع</h2>
  <pre><code>pip install rayovin-agent
rayovin --version
rayovin setup
rayovin chat</code></pre>
</div>
'''
with open(f"{REPO}/index.html", "w") as f: f.write(pg("Rayovin Agent - هوش مصنوعی رایوین", "عامل هوشمند فارسی توسط نبض آینده جنوب", home_body))
print("✅ index.html")

# =================== INSTALL ===================
install_body = '''
<div class="container page">
  <h2>🚀 نصب Rayovin Agent</h2>
  <h3>روش ۱: نصب با pip</h3>
  <pre><code>pip install rayovin-agent</code></pre>
  <h3>روش ۲: نصب از سورس (جدیدترین نسخه)</h3>
  <pre><code>git clone https://github.com/rayovin/rayovin-agent.git
cd rayovin-agent
pip install -e .</code></pre>
  <h3>روش ۳: نصب با curl</h3>
  <pre><code>curl -fsSL https://raw.githubusercontent.com/rayovin/rayovin-agent/main/setup-rayovin.sh | bash</code></pre>
  <h3>📋 نیازمندی‌ها</h3>
  <table>
    <tr><th>نیازمندی</th><th>توضیح</th></tr>
    <tr><td>Python</td><td>≥ 3.11 و &lt; 3.14</td></tr>
    <tr><td>سیستم‌عامل</td><td>لینوکس، macOS، WSL2</td></tr>
  </table>
  <h3>🔧 تنظیم اولیه</h3>
  <pre><code>rayovin setup</code></pre>
  <p>این دستور راهنمای گام‌به‌گام برای تنظیم provider و API key</p>
  <h3>🧪 تست نصب</h3>
  <pre><code>bash test-rayovin.sh</code></pre>
</div>
'''
with open(f"{REPO}/install.html", "w") as f: f.write(pg("نصب Rayovin Agent", "راهنمای نصب Rayovin Agent", install_body))
print("✅ install.html")

# =================== FEATURES ===================
features_body = '''
<div class="container page">
  <h2>✨ ویژگی‌های Rayovin Agent</h2>
  <div class="cards">
    <div class="card"><div class="icon">🧠</div><h3>یادگیری خودکار</h3><p>سیستم Skill هوشمند — از مکالمات یاد می‌گیره و مهارت می‌سازه</p></div>
    <div class="card"><div class="icon">💾</div><h3>حافظه بلندمدت</h3><p>اطلاعات مهم بین جلسات مختلف حفظ می‌شه</p></div>
    <div class="card"><div class="icon">📱</div><h3>۲۵+ پلتفرم</h3><p>تلگرام، دیسکورد، واتساپ، سیگنال، اسلک، Matrix، ایمیل و...</p></div>
    <div class="card"><div class="icon">⏰</div><h3>Cron داخلی</h3><p>کارهای زمان‌بندی شده با تحویل خودکار</p></div>
    <div class="card"><div class="icon">🔄</div><h3>زیرعامل (Sub-agent)</h3><p>کارهای سنگین رو به agentهای کوچیکتر بسپار</p></div>
    <div class="card"><div class="icon">🔌</div><h3>پشتیبانی MCP</h3><p>Model Context Protocol برای ابزارهای خارجی</p></div>
    <div class="card"><div class="icon">🎨</div><h3>۷۶+ Skill</h3><p>برنامه‌نویسی، امنیت، DevOps، تحلیل داده، هوش مصنوعی</p></div>
    <div class="card"><div class="icon">🐳</div><h3>داکر</h3><p>قابل اجرا در Docker با Dockerfile آماده</p></div>
  </div>
  <h2>🛠 Skillهای موجود</h2>
  <table>
    <tr><th>دسته</th><th>تعداد</th><th>نمونه</th></tr>
    <tr><td>autonomous-ai-agents</td><td>۴</td><td>claude-code, opencode, hermes-agent, codex</td></tr>
    <tr><td>creative</td><td>۱۷</td><td>excalidraw, p5js, ascii-art, comfyui</td></tr>
    <tr><td>github</td><td>۶</td><td>pr-workflow, code-review, issues</td></tr>
    <tr><td>productivity</td><td>۱۱</td><td>notion, airtable, powerpoint, google-workspace</td></tr>
    <tr><td>software-development</td><td>۱۵</td><td>php, backend, frontend, api, tdd</td></tr>
    <tr><td>research</td><td>۴</td><td>arxiv, blogwatcher, polymarket</td></tr>
  </table>
</div>
'''
with open(f"{REPO}/features.html", "w") as f: f.write(pg("ویژگی‌ها", "ویژگی‌ها و قابلیت‌های Rayovin Agent", features_body))
print("✅ features.html")

# =================== GUIDE ===================
guide_body = '''
<div class="container page">
  <h2>📖 راهنمای استفاده</h2>
  <h3>شروع کار</h3>
  <pre><code># نصب
pip install rayovin-agent

# تنظیم اولیه
rayovin setup

# شروع چت
rayovin chat</code></pre>
  <h3>دستورات اصلی</h3>
  <table>
    <tr><th>دستور</th><th>توضیح</th></tr>
    <tr><td><code>rayovin chat</code></td><td>شروع چت تعاملی</td></tr>
    <tr><td><code>rayovin setup</code></td><td>تنظیم اولیه (provider، API key)</td></tr>
    <tr><td><code>rayovin status</code></td><td>وضعیت فعلی agent</td></tr>
    <tr><td><code>rayovin model</code></td><td>انتخاب مدل و provider</td></tr>
    <tr><td><code>rayovin skills list</code></td><td>لیست Skillهای نصب شده</td></tr>
    <tr><td><code>rayovin cron</code></td><td>مدیریت کارهای زمان‌بندی شده</td></tr>
    <tr><td><code>rayovin config</code></td><td>مشاهده/تغییر تنظیمات</td></tr>
    <tr><td><code>rayovin update</code></td><td>بروزرسانی agent</td></tr>
  </table>
  <h3>🔌 اتصال پیام‌رسان‌ها</h3>
  <p>بعد از اجرای <code>rayovin setup</code>، می‌تونی پیام‌رسان‌ها رو وصل کنی:</p>
  <table>
    <tr><th>پلتفرم</th><th>دستور</th></tr>
    <tr><td>تلگرام</td><td><code>rayovin setup --platform telegram</code></td></tr>
    <tr><td>دیسکورد</td><td><code>rayovin setup --platform discord</code></td></tr>
    <tr><td>واتساپ</td><td><code>rayovin setup --platform whatsapp</code></td></tr>
    <tr><td>اسلک</td><td><code>rayovin setup --platform slack</code></td></tr>
  </table>
  <h3>⏰ کارهای زمان‌بندی شده</h3>
  <pre><code># هر روز ساعت ۹ صبح گزارش بده
rayovin cron create --schedule "0 9 * * *" --prompt "گزارش روزانه"

# لیست cron jobs
rayovin cron list</code></pre>
</div>
'''
with open(f"{REPO}/guide.html", "w") as f: f.write(pg("راهنما", "راهنمای کامل استفاده از Rayovin Agent", guide_body))
print("✅ guide.html")

# =================== API ===================
api_body = '''
<div class="container page">
  <h2>🔌 مستندات API</h2>
  <p>Rayovin Agent از OpenAI-compatible API پشتیبانی می‌کنه.</p>
  <h3>انواع Providerها</h3>
  <table>
    <tr><th>Provider</th><th>نوع</th><th>API Key</th></tr>
    <tr><td>OpenAI</td><td>رسمی</td><td>✅</td></tr>
    <tr><td>Anthropic</td><td>رسمی</td><td>✅</td></tr>
    <tr><td>OpenRouter</td><td>واسط</td><td>✅</td></tr>
    <tr><td>Google Gemini</td><td>رسمی</td><td>✅</td></tr>
    <tr><td>Ollama</td><td>محلی</td><td>❌ (رایگان)</td></tr>
    <tr><td>vLLM</td><td>محلی/سرور</td><td>❌</td></tr>
    <tr><td>llama.cpp</td><td>محلی</td><td>❌</td></tr>
  </table>
  <h3>تنظیم Provider</h3>
  <pre><code># با دستور setup
rayovin setup

# یا مستقیم
rayovin config set provider openai
rayovin config set openai.api_key sk-...XXXX</code></pre>
  <h3>تغییر مدل</h3>
  <pre><code>rayovin model</code></pre>
  <h3>استفاده از Ollama (محلی)</h3>
  <pre><code># نصب Ollama
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3

# تنظیم در Rayovin
rayovin config set provider ollama
rayovin config set ollama.model llama3</code></pre>
</div>
'''
with open(f"{REPO}/api.html", "w") as f: f.write(pg("API و Providerها", "راهنمای تنظیم API و Provider", api_body))
print("✅ api.html")

print("\n🎉 All 5 pages created!")
