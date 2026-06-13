import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.gmanetwork.com/news/scitech/technology/987870/ai-powered-robot-assistant-helps-germans-shop/story/" target="_blank">GMA News (Reuters)</a></p>
            <p><strong>📅 發布日期</strong>：2026-05-16</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>德國巴伐利亞小鎮 Pocking 的一家五金賣場，出現了一名來自中國的 AI 機械人「Schotti」。它能走能說，帶客人走到正確貨架，每小時「工資」僅 1.70 歐元，正在重新定義零售業的人機協作模式。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>中國製造的 AI 機械人</h4>
                <p>Schotti 由中國製造，由 Florian Weichschbaummer 及其團隊在 labland.ai 編程訓練。實驗室自稱為「3D 列印、機械人與 AI 解決方案」公司。機械人身穿店員制服，前方掛著一部平板電腦。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🗺️</div>
            <div class="tech-card-content">
                <h4>認路又能對話</h4>
                <p>Schotti 已學習賣場平面圖，能回答顧客「產品在哪裡」的問題，並引導他們走到正確貨架。測試始於 2026 年 4 月，與 2025 年 10 月的前代機種不同——舊版只能走或只能說，Schotti 同時具備兩種能力。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💶</div>
            <div class="tech-card-content">
                <h4>時薪 1.70 歐元的員工</h4>
                <p>Schotti 的採購價為 80,000 歐元（約 93,600 美元），攤分服務年限後，每小時「工資」僅約 1.70 歐元（約 1.99 美元）。Bild 報紙引述 Weichselbaumer 稱：「這是店裡最便宜的員工。」</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>距離完全自主尚遠</h4>
                <p>目前 Schotti 每週只現身賣場 2-3 次，且大量動作仍由 labland.ai 團隊成員遙距操控。Weichselbaumer 強調：「目的不是取代人類，而是用機械人改善員工和人們的處境。」</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 一機多角色實驗</h4>
            <p>Schotti 目前同時在電信門市擔任「歡迎經理」，使用女性聲線打招呼，引導客人到咖啡機或下一位可用員工。labland.ai 正在測試同一機械人如何適應不同角色，同時學習與人類協作。</p>
        </div>

        <div class="quote-box">
            <p>「With every route it takes, it becomes a little smarter.」</p>
            <cite>— Florian Weichselbaumer, labland.ai 創辦人</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這宗個案顯示，AI 機械人走進零售業的真實瓶頸不在技術，而在成本與效益的平衡。時薪 1.70 歐元的「員工」或許是過渡方案，但隨著學習能力提升、機械造價下降，全自主導購機械人的出現只是時間問題。重點是：如何做到人機共贏，而非單純取代。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2025-10</div>
                <div class="timeline-title">第一代機械人測試</div>
                <div class="timeline-desc">Pocking 五金賣場首次引進機械人，但該機種只能走或只能說，功能有限。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-04</div>
                <div class="timeline-title">Schotti 上線</div>
                <div class="timeline-desc">中國製造的 Schotti 開始在同一家五金賣場測試，具備行走與對話雙重能力。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-05</div>
                <div class="timeline-title">電信門市部署</div>
                <div class="timeline-desc">Schotti 被派駐電信門市，擔任「歡迎經理」，首次測試一機多角色適應能力。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-05-16</div>
                <div class="timeline-title">Reuters 報導</div>
                <div class="timeline-desc">Reuters 發布新聞，引述 Bild 報紙關於 Schotti 每小時工資 1.70 歐元的資料。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">持續學習</div>
                <div class="timeline-desc">Schotti 每執行一次路線就學習一點，逐步提升自主導航與應對能力。</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>傳統店員</th>
                    <th>Schotti 機械人</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>時薪成本</td>
                    <td>德國最低工資約 12 歐元/小時</td>
                    <td class="highlight-col">約 1.70 歐元/小時</td>
                </tr>
                <tr>
                    <td>功能</td>
                    <td>導購、諮詢、推銷</td>
                    <td class="highlight-col">導購、回答問題、 引導至貨架</td>
                </tr>
                <tr>
                    <td>自主程度</td>
                    <td>完全自主</td>
                    <td class="highlight-col">仍需遙距操控，逐步學習</td>
                </tr>
                <tr>
                    <td>上崗時間</td>
                    <td>需要培訓</td>
                    <td class="highlight-col">編程後可快速部署</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'AI-powered robot assistant helps Germans shop',
    'h1':          '德國五金賣場<br>AI 機械人時薪僅 1.70 歐元',
    'subtitle':    '中國製造的機械人 Schotti 正在德國巴伐利亞小鎮學習導購，每小時「工資」不到 2 歐元。零售業的人機協作實驗，正在從實驗室走向賣場。',
    'source_url':  'https://www.gmanetwork.com/news/scitech/technology/987870/ai-powered-robot-assistant-helps-germans-shop/story/',
    'source_name': 'GMA News (Reuters)',
    'pub_date':    '2026-05-16',
    'img_alt':     'AI 機械人 Schotti 在德國五金賣場幫助顧客購物',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260613_222023',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print("Errors:")
    for e in errors:
        print(f"  - {e}")