import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/06/02/openai-launches-new-codex-tools-for-white-collar-work/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-03</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要 + 深度優化</p>
        </div>

        <div class="alert-box">
            <h4>⚠️ 資料來源說明</h4>
            <p>本文內容主要基於 TechCrunch 報導，引用 OpenAI 官方博客及內部報告《The Next Era of Knowledge Work》進行深度解讀。</p>
        </div>

        <div class="quote-box">
            <p>「AI 正在成為組織內部執行越來越多有意義工作的核心。真正的挑戰是幫助企業將這些系統整合到他們的基礎設施和工作流程中。」</p>
            <cite>— Denise Dresser，OpenAI 首席營收長</cite>
        </div>

        <h3>🎯 核心突破卡片</h3>
        <div class="tech-cards">
            <div class="tech-card">
                <div class="tech-card-icon">📊</div>
                <h4>500 萬用戶</h4>
                <p>Codex 每周活躍用戶突破 500 萬，較 2 月桌面應用發布時增長超過 6 倍。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">👔</div>
                <h4>白領佔 20%</h4>
                <p>知識工作者目前佔用戶約 20%，增速是開發者的 3 倍，成長最快速的用戶群組。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🔌</div>
                <h4>六大插件</h4>
                <p>全新插件覆蓋數據分析、創意製作、銷售、產品設計、股票投資並購銀行業務。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🌐</div>
                <h4>Sites 功能</h4>
                <p>Codex 輸出成果可直接發布為托管互動網站，合作夥伴包括 Wix、Base44、Replit、Figma 等。</p>
            </div>
        </div>

        <h3>📊 插件類型對比</h3>
        <table class="comparison-table">
            <thead>
                <tr><th>插件名稱</th><th>適用場景</th><th>核心功能</th><th>目標用戶</th></tr>
            </thead>
            <tbody>
                <tr><td>📈 Data Analytics</td><td>數據分析</td><td>整合數據源、自動化報表</td><td class="highlight-col">數據分析師</td></tr>
                <tr><td>🎨 Creative Production</td><td>創意製作</td><td>內容生成、多媒體創作</td><td class="highlight-col">設計師/創意人員</td></tr>
                <tr><td>💼 Sales</td><td>銷售支援</td><td>客戶管理、銷售預測</td><td class="highlight-col">營銷團隊</td></tr>
                <tr><td>📐 Product Design</td><td>產品設計</td><td>原型生成、設計協作</td><td class="highlight-col">PM/設計師</td></tr>
                <tr><td>📊 Equity Investing</td><td>股票投資</td><td>財務分析、投資建議</td><td class="highlight-col">投資分析師</td></tr>
                <tr><td>🏦 Investment Banking</td><td>併購銀行</td><td>盡職調查、交易評估</td><td class="highlight-col">金融專業人士</td></tr>
            </tbody>
        </table>

        <h3>📅 OpenAI Codex 企業化時間軸</h3>
        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 2 月</div>
                <div class="timeline-title">桌面應用發布</div>
                <div class="timeline-desc">Codex 桌面應用正式推出，用戶數量開始快速增長。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 3 月</div>
                <div class="timeline-title">插件系統上線</div>
                <div class="timeline-desc">OpenAI 為 Codex 引入插件支援，縮小與 Anthropic Claude Code 的差距。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 5 月</div>
                <div class="timeline-title">企業 Agent 程序</div>
                <div class="timeline-desc">Anthropic 推出針對金融服務的 Agent，企業 AI 競爭升溫。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">六大插件發布</div>
                <div class="timeline-desc">OpenAI 發布針對白領工作的六大專業插件，正式進軍企業市場。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月（同步）</div>
                <div class="timeline-title">Deployment Company</div>
                <div class="timeline-desc">OpenAI 成立合營公司，獲逾 40 億美元融資，瞄準全球企業深度整合。</div>
            </div>
        </div>

        <h3>🌟 新功能：Sites 與 Annotations</h3>
        <p>除了六大插件，OpenAI 還推出了两个重要新功能：</p>
        <ul>
            <li><strong>Sites 功能</strong>：允許 Codex 直接將工作成果發布為托管互動網站，不再局限於本地文件輸出。合作夥伴包括 Wix、Base44、Replit、Lovable、Figma 和 Emergent。</li>
            <li><strong>Annotations 功能</strong>：用戶可標記文件或檔案中的特定部分，實現更精確的命令和上下文操作。</li>
        </ul>

        <div class="highlight-box">
            <h4>✨ 關鍵洞察</h4>
            <p>OpenAI 過去以消費者市場為主，此次一口氣發布六大人工插件，加上 Deployment Company 的 40 億美元增援，顯示其正以前所未有的力度進軍企業 AI 市場。知識工作者已佔用戶總數 20% 且增長迅速，白領 AI 革命正在加速。</p>
        </div>

        <div class="alert-box">
            <h4>⚠️ 競爭態勢</h4>
            <p>Anthropic早在 2 月已推出企業 Agent 程序，5 月更推出金融導向 Agent。OpenAI 此時推出白領插件，是回應競爭對手的戰略性舉措，企業 AI 市場競爭將更加激烈。</p>
        </div>
"""

metadata = {
    'title': 'OpenAI launches new Codex tools for white-collar work | TechCrunch',
    'h1': 'OpenAI 進軍白領市場<br>Codex 六大新插件登陸企業',
    'subtitle': '知識工作者佔用戶 20%、增速達開發者 3 倍！OpenAI 與 Anthropic 企業 AI 爭霸戰開打',
    'source_url': 'https://techcrunch.com/2026/06/02/openai-launches-new-codex-tools-for-white-collar-work/',
    'source_name': 'TechCrunch',
    'pub_date': '2026-06-03',
    'img_alt': 'OpenAI Codex 白領工作 AI 工具概念圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260603_083900',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")
