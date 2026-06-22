import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techtrenches.dev/p/when-your-vendor-becomes-your-competitor" target="_blank">Tech Trenches</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-16</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>當 AI 模型供應商親自下場做應用服務，獨立工程公司的生存空間備受挤压。OpenAI 砸下 40 億美元、Anthropic 砸下 15 億美元親自提供企業 AI 人類監督服務，標志著 AI 行業從「工具供應商」轉變為「競爭對手」的商業模式轉向。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🏢</div>
            <div class="tech-card-content">
                <h4>供應商變競爭對手</h4>
                <p>OpenAI 只用了 18 個月從工具供應商轉變為競爭對手服務公司。2026 年 5 月推出 DeployCo，斥資 40 億美元專門提供自家模型的人類監督服務，目標客戶正是那些已有數千家公司正幫其部署 AI 的企業。Anthropic 亦在同期以 15 億美元推出類似服務。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💸</div>
            <div class="tech-card-content">
                <h4>55 億美元的人類監督</h4>
                <p>OpenAI 的 DeployCo（40 億美元）和 Anthropic 的類似服務（15 億美元），合計 55 億美元打造企業人類監督服務。這個數字揭示了 AI 巨頭對應用層的主動出擊，代價是那些原本扮演中間人角色的獨立工程公司。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📉</div>
            <div class="tech-card-content">
                <h4>獨立工程公司的困境</h4>
                <p>這些公司的核心價值在於了解客戶基礎設施、擁有真實部署經驗和客户信任。但當模型供應商本身擁有這些優勢、並以資金規模碾壓時，其資訊優勢蕩然無存。150 名工程師分散到數千個投資組合公司，很快就捉襟見肘。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔗</div>
            <div class="tech-card-content">
                <h4>併購建立生態系</h4>
                <p>DeployCo 推出後一個月，OpenAI 再收購 Ona——一家在企業自有用雲端內安全運行 AI 代理的公司。一次收購是產品，兩次收購是模式。OpenAI 正在通過併購渗透部署層，因為純模型本身無法觸及這一層。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 關鍵數據</h4>
            <p>OpenAI：<strong>40 億美元</strong>（DeployCo）<br>Anthropic：<strong>15 億美元</strong>（人類監督服務）<br>總計：<strong>55 億美元</strong>打造企業人類監督服務</p>
        </div>

        <div class="quote-box">
            <p>「你的供應商就是你的競爭對手，擁有你所無法比擬的資金、你無法看見的產品藍圖，以及你無法接觸的客戶群。」</p>
            <cite>— Denis Stetskov, Tech Trenches</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Sam Altman 和 Dario Amodei 花了兩年預測 AI 將取代大部分勞動力，如今自家公司正以 55 億美元親自示範：中間人角色的獨立 AI 部署公司，其生存空間正被供應商直接鯨吞。AWS 和 Salesforce 當年選擇與合作夥伴分享利潤，共同銷售，而非消滅它們；但 DeployCo 是被設計為競爭者，而非平台。這個 55 億美元的「坦白」，等於是告訴整個行業：純做應用的中間人，已經沒有存在的理由。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2024-2025</div>
                <div class="timeline-title">AI 巨頭預言置換</div>
                <div class="timeline-desc">Sam Altman 和 Dario Amodei 公開預測 AI 將取代大部分勞動力</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 5 月</div>
                <div class="timeline-title">OpenAI DeployCo</div>
                <div class="timeline-desc">OpenAI 砸 40 億美元推出 DeployCo，直接提供自家模型的企業監督服務</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 5 月（稍早）</div>
                <div class="timeline-title">Anthropic 跟進</div>
                <div class="timeline-desc">Anthropic 以 15 億美元推出類似服務，時間比 OpenAI 更早但更低調</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">OpenAI 收購 Ona</div>
                <div class="timeline-desc">收購在企業自有用雲端運行 AI 代理的公司，渗透部署層</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">18 個月</div>
                <div class="timeline-title">OpenAI 的轉變</div>
                <div class="timeline-desc">從工具供應商到競爭對手服務公司的轉變僅用了 18 個月</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>公司</th>
                    <th>行動</th>
                    <th>金額</th>
                    <th>目標</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>OpenAI</td>
                    <td class="highlight-col">推出 DeployCo</td>
                    <td>40 億美元</td>
                    <td>直接提供企業 AI 人類監督服務</td>
                </tr>
                <tr>
                    <td>Anthropic</td>
                    <td class="highlight-col">推出類似服務</td>
                    <td>15 億美元</td>
                    <td>企業人類監督服務</td>
                </tr>
                <tr>
                    <td>OpenAI</td>
                    <td class="highlight-col">收購 Ona</td>
                    <td>未披露</td>
                    <td>在企業自有雲端運行 AI 代理</td>
                </tr>
                <tr>
                    <td>AWS / Salesforce</td>
                    <td>合作而非競爭</td>
                    <td>—</td>
                    <td>利潤分享、共同銷售，生態系共存</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '當你的供應商變成你的競爭對手：AI 的 55 億美元告白',
    'h1':          '當供應商變成<br>競爭對手',
    'subtitle':    'OpenAI 砸 40 億、Anthropic 砸 15 億親自做應用服務，獨立工程公司空間被鯨吞',
    'source_url':  'https://techtrenches.dev/p/when-your-vendor-becomes-your-competitor',
    'source_name': 'Tech Trenches',
    'pub_date':    '2026-06-16',
    'img_alt':     'AI巨頭變競爭對手示意圖，OpenAI/Anthropic 大樓巨大，小型獨立工程公司被淹沒',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260622_094604',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
