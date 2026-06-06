import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-06</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Google 將在 2026 年 10 月至 2029 年 6 月期間，每月向 <strong>SpaceX</strong> 支付 <strong>9.2 億美元</strong>，租用約 <strong>11 萬顆 NVIDIA GPU、CPU、記憶體及相關元件</strong>。這是继 Anthropic 之後，SpaceX 再次與大型科技公司達成的大規模算力租賃協議。</p>

        <h3>📊 關鍵數據</h3>
        <ul>
            <li>💰 <strong>月租費用：</strong>9.2 億美元（約新台幣 300 億元）</li>
            <li>📅 <strong>合約期：</strong>2026 年 10 月 至 2029 年 6 月（共 33 個月）</li>
            <li>🖥️ <strong>硬體規模：</strong>約 110,000 顆 NVIDIA GPU + CPU + 記憶體</li>
            <li>📍 <strong>資料中心：</strong>SpaceX 旗下 xAI 的 Colossus 資料中心（田納西州曼菲斯附近）</li>
            <li>🚪 <strong>終止條款：</strong>2026 年 12 月 31 日後，雙方可於 90 天通知後終止合約</li>
            <li>📈 <strong>SpaceX 估值：</strong>IPO 前估值約 1.75 萬億美元（歷史最大規模）</li>
            <li>💎 <strong>Google 持股：</strong>IPO 後持股價值預計超過 1,000 億美元</li>
        </ul>

        <h3>🤝 交易背景：Anthropic 模式複製</h3>
        <p>這項協議與 SpaceX 在 5 月底與 <strong>Anthropic</strong> 宣佈的合約結構相似。Anthropic 同意在 2029 年前每月向 SpaceX 支付 <strong>12.5 億美元</strong>，租用同一座 Colossus 資料中心的算力。該資料中心原本是 xAI（現為 SpaceX 旗下公司）為自家 AI 訓練而建設。</p>
        <p>兩份合約的條款都包含相同的<strong>90 天終止條款</strong>（2026 年 12 月 31 日後生效），讓雙方在市場變化時有退出機制。</p>

        <h3>🖥️ xAI 的 Colossus 資料中心</h3>
        <p>Colossus 資料中心位於田納西州曼菲斯附近，是目前世界上最大的 AI 訓練設施之一。SpaceX 當初興建这座資料中心是為了支援 xAI 的大語言模型訓練計畫，如今則轉型為對外出租算力的商業模式。</p>
        <p>這也解釋了為什麼 SpaceX 能夠在短期內提供如此龐大的 GPU 集群——這些設施原本就是為了訓練 Grok 等 xAI 模型而建設，現在則成為 SpaceX 新的重要營收來源。</p>

        <h3>🚀 SpaceX IPO 前夕的大動作</h3>
        <p>這項算力租賃協議宣佈的時間點，正值 SpaceX 股票預計在那斯達克交易所掛牌交易的前一週。根據美國證券交易委員會（SEC）的文件，SpaceX 計劃集資約 <strong>750 億美元</strong>，估值達到約 <strong>1.75 萬億美元</strong>——這將是史上最大規模的 IPO。</p>
        <p>在此之前，Google 已是 SpaceX 的長期投資者。隨著 SpaceX 即將 IPO，Google 在 Musk 公司的持股預計將價值超過 <strong>1,000 億美元</strong>。</p>

        <h3>💡 為什麼 Google 要向 SpaceX 租用算力？</h3>
        <p>這項交易反映了目前 AI 產業的一個核心趨勢：<strong>算力供給落後於需求</strong>。即使是 Google 這樣擁有龐大雲端基礎設施的公司，在麥 GPU 供應緊張的情況下，也選擇向外租用算力。</p>
        <p>租用而非自建的好處包括：</p>
        <ul>
            <li>⚡ <strong>速度：</strong>無需等待漫長的資料中心建設週期</li>
            <li>💵 <strong>彈性：</strong>可根據需求快速擴展或縮減</li>
            <li>🔧 <strong>維護：</strong>由 SpaceX 负责硬體維護與升級</li>
            <li>📊 <strong>規模：</strong>11 萬顆 GPU 的規模難以快速自建</li>
        </ul>

        <h3>📈 對比：Anthropic vs Google 的算力協議</h3>
        <table class="comparison-table">
            <thead>
                <tr>
                    <th>合作方</th>
                    <th>月租費用</th>
                    <th>合約期</th>
                    <th>終止條款</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Anthropic</td>
                    <td class="highlight-col">12.5 億美元</td>
                    <td>至 2029 年</td>
                    <td>90 天通知（2026/12/31 後）</td>
                </tr>
                <tr>
                    <td>Google</td>
                    <td>9.2 億美元</td>
                    <td>2026/10 - 2029/06</td>
                    <td>90 天通知（2026/12/31 後）</td>
                </tr>
            </tbody>
        </table>

        <h3>🌍 更大格局：AI 算力基礎設施之爭</h3>
        <p>這筆交易的規模凸顯了 AI 時代「算力即話語權」的事實。誰能提供最多的 GPU 誰就能吸引最多的客戶。SpaceX/xAI 通過建设 Colossus 資料中心，在短短幾年內就已經追上了傳統雲端巨頭的算力規模。</p>
        <p>對 Google 而言，雖然面臨算力緊張，但也透過這筆投資間接受益於 SpaceX 的成長。一旦 SpaceX IPO，Google 的持股將價值連城。</p>

        <div class="tech-cards">
            <div class="tech-card">
                <div class="tech-card-icon">💰</div>
                <h4>每月 9.2 億美元</h4>
                <p>Google 租用 SpaceX 算力的月費，合約總價值超過 300 億美元</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🖥️</div>
                <h4>11 萬顆 GPU</h4>
                <p>涵蓋約 110,000 顆 NVIDIA GPU、CPU、記憶體及相關元件</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🚀</div>
                <h4>SpaceX IPO 估值 1.75 萬億</h4>
                <p>即將創下史上最大規模 IPO，Google 持股將價值超過 1,000 億美元</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🤖</div>
                <h4>xAI Colossus 資料中心</h4>
                <p>位於田納西州曼菲斯，為 xAI 建設的全球最大 AI 訓練設施之一</p>
            </div>
        </div>

        <div class="highlight-box">
            <p>💬 <strong>交易意義：</strong>這筆交易不僅是迄今最大規模的算力租賃合約之一，也標誌著 SpaceX 從火箭公司轉型為 AI 基礎設施公司的關鍵一步。</p>
        </div>
"""

metadata = {
    'title': 'Google 將每月向 SpaceX 支付 9.2 億美元租用算力',
    'h1': 'Google 將每月向 SpaceX 支付 9.2 億美元租用算力',
    'subtitle': '為期 33 個月、總值超過 300 億美元！涵蓋 11 萬顆 NVIDIA GPU 的超大規模算力租賃協議',
    'source_url': 'https://techcrunch.com/2026/06/05/google-will-pay-spacex-920m-per-month-for-compute/',
    'source_name': 'TechCrunch',
    'pub_date': '2026-06-06',
    'img_alt': 'Google 將每月向 SpaceX 支付 9.2 億美元租用算力',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260606_124707',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 重建成功")
else:
    print("❌ HTML 重建失敗")
    for e in errors:
        print(f"  - {e}")