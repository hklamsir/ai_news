import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.blocktempo.com/design-md-github-100k-stars-ai-generates-consistent-brand-ui/" target="_blank">BLOCKTEMPO</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-11</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>一個名為「awesome-design-md」的 GitHub 專案，收錄了 73 個知名科技品牌的 DESIGN.md 設計規範文件，在 GitHub 上爆紅突破 10 萬顆星。這個專案解決了 AI 生成網頁「風格飄忽不定」的痛點。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>問題：AI 生成的網頁總是很醜？</h4>
                <p>過往用 AI 生成網頁最大問題是：即使提供了詳細指令，AI 每次生出來的風格都不太一樣，難以維持品牌一致性。原因在於：AI 不理解「設計語言」，只知道你要什麼功能，不知道這個品牌應該看起來像什麼。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📄</div>
            <div class="tech-card-content">
                <h4>解決方案：DESIGN.md</h4>
                <p>DESIGN.md 是一個純文字的設計系統文件，AI 代理可以讀取它來理解「這個專案應該長什麼樣子」。類似 README.md（做什麼）+ AGENTS.md（怎麼做），DESIGN.md 告訴 AI 應該看起來怎樣。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏢</div>
            <div class="tech-card-content">
                <h4>73 個品牌設計規範一次擁有</h4>
                <p>「awesome-design-md」收錄了 Stripe、Vercel、Linear、Notion、Figma、Runway 等 73 個知名品牌的 DESIGN.md。只要把其中一個放進專案，告訴 AI「幫我做一個看起來像這樣的頁面」，就能生成風格一致的 UI。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔗</div>
            <div class="tech-card-content">
                <h4>Google Stitch 深度整合</h4>
                <p>DESIGN.md 是 Google Stitch 的核心概念。當用戶要求 Stitch 生成新設計時，它首先會建立風格指南，再根據這個指南生成 UI，確保輸出符合品牌調性。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>DESIGN.md 包含色彩、字體、間距、元件行為、品牌調性等具體定義，讓 AI 能將抽象審美概念轉化為可執行的設計 tokens，解決 AI 生成 UI 風格不一致的問題。</p>
        </div>

        <div class="quote-box">
            <p>「Copy a DESIGN.md into your project, tell your AI agent 'build me a page that looks like this,' and generate high-quality UI that stays visually consistent.」</p>
            <cite>— awesome-design-md 專案說明</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>DESIGN.md 的出現填補了 AI 編碼代理的最後一塊拼圖。在這之前，人類知道如何告訴 AI 該做什麼（README）、怎麼做（AGENTS），但從來沒有一個標準方式告訴 AI「應該看起來怎樣」。隨著越多品牌公開 DESIGN.md，AI 生成 UI 的品質與一致性將大幅提升。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">工具誕生</div>
                <div class="timeline-title">Google Stitch 引入 DESIGN.md</div>
                <div class="timeline-desc">Google Stitch 生成式設計工具採用 DESIGN.md 作為核心概念</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">問題浮現</div>
                <div class="timeline-title">AI 生成 UI 風格不一致</div>
                <div class="timeline-desc">AI 每次生成的網頁樣式都不一樣，難以維持品牌調性</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">解決方案</div>
                <div class="timeline-title">DESIGN.md 作為設計語言標準</div>
                <div class="timeline-desc">用 Markdown 格式定義品牌色彩、字體、間距、元件行為</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">社群響應</div>
                <div class="timeline-title">awesome-design-md 專案成立</div>
                <div class="timeline-desc">收集 73 個知名科技品牌的 DESIGN.md 文件</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07</div>
                <div class="timeline-title">GitHub 突破 10 萬星</div>
                <div class="timeline-desc">專案爆紅，成為 AI 生成 UI 領域的標杆資源</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>檔案類型</th>
                    <th>告訴 AI 什麼</th>
                    <th>範例內容</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>README.md</td>
                    <td class="highlight-col">做什麼</td>
                    <td>專案功能、用途、安裝方式</td>
                </tr>
                <tr>
                    <td>AGENTS.md</td>
                    <td class="highlight-col">怎麼做</td>
                    <td>程式碼規範、開發流程、技術架構</td>
                </tr>
                <tr>
                    <td>DESIGN.md</td>
                    <td class="highlight-col">看起來怎樣</td>
                    <td>色彩、字體、間距、品牌調性</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'AI 做的網頁總是很醜？這專案收錄 73 個品牌 DESIGN.md，GitHub 爆紅摘 10 萬星',
    'h1': 'AI 做的網頁總是很醜？<br>這專案收錄 73 個品牌 DESIGN.md，GitHub 爆紅摘 10 萬星',
    'subtitle': 'DESIGN.md 成為 AI 生成一致品牌 UI 的關鍵橋樑',
    'source_url': 'https://www.blocktempo.com/design-md-github-100k-stars-ai-generates-consistent-brand-ui/',
    'source_name': 'BLOCKTEMPO',
    'pub_date': '2026-07-11',
    'img_alt': 'DESIGN.md 專案：73 個品牌設計規範讓 AI 生成一致 UI',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260711_140200',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
