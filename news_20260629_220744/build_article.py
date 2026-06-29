import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://news.cnyes.com/news/id/6515798" target="_blank">鉅亨網</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-29</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>DeepSeek 創辦人梁文鋒受 Anthropic Claude Mythos 震撼，決定大轉向——完成 500 億人民幣（約 74 億美元）巨額融資後，個人再掏出 200 億元人民幣占總額五分之二，確保主導權，宣布團隊翻倍至 600 人，全力衝刺 AGI。</p>

        <div class="tech-card">
            <div class="tech-card-icon">⚡</div>
            <div class="tech-card-content">
                <h4>Claude Mythos 成導火線</h4>
                <p>Anthropic 2026 年 4 月發布的 Claude Mythos 預覽版展現的強大能力，讓梁文鋒意識到前沿 AI 已進入「堆算力、堆數據」的國家級規模競賽時代。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>200億「自我定價」</h4>
                <p>梁文鋒個人出资 200 億元人民幣（約五分之二），被視為「自我定價」策略——在接受資本市場的同時，保留對公司的絕對控制權。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🚀</div>
            <div class="tech-card-content">
                <h4>團隊翻倍至600人</h4>
                <p>DeepSeek 宣布所有部門招人「至少翻倍」，從 300 人擴張至 600 人以上，重點加強 AI 系統開發與自主智能體研究。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔧</div>
            <div class="tech-card-content">
                <h4>華為晶片適配</h4>
                <p>DeepSeek 正全力適配華為晶片，試圖在 NVIDIA CUDA 架構之外重構底層軟體。適配工作曾導致長達 15 個月未發布新模型。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>梁文鋒強調 DeepSeek 戰略核心不變：<strong>繼續開源、保持低價、專注 AGI</strong>。目前 DeepSeek 已成為美國開發者群體中成長最快、性價比最高（比 Anthropic 便宜 20 到 50 倍）的模型之一。</p>
        </div>

        <div class="quote-box">
            <p>「DeepSeek 的戰略核心不會改變：繼續開源、保持低價、專注 AGI。」</p>
            <cite>— 梁文鋒，DeepSeek 創辦人</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>DeepSeek 的大轉向標誌著中國 AI 發展進入新階段——從高效小團隊模式轉向國家級規模競賽。梁文鋒認為編程工具僅是過渡性產品，通往 AGI 的終極目標不應偏離。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">長期以來</div>
                <div class="timeline-title">堅持非商業化</div>
                <div class="timeline-desc">DeepSeek 堅持自掏腰包、不做商業化的路線</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 4 月</div>
                <div class="timeline-title">Claude Mythos 震撼</div>
                <div class="timeline-desc">Anthropic 發布 Claude Mythos 預覽版，觸發轉向念頭</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">500億巨額融資</div>
                <div class="timeline-desc">DeepSeek 完成 74 億美元（約 500 億人民幣）融資</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">梁文鋒200億注資</div>
                <div class="timeline-desc">梁文鋒個人出资 200 億元，確保主導權</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">團隊擴張</div>
                <div class="timeline-desc">團隊從 300 人擴張至 600 人以上，專注 AGI 研發</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>轉向前</th>
                    <th>轉向後</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>資金模式</td>
                    <td>自掏腰包、不接受外部資本</td>
                    <td class="highlight-col">接受外部資本（梁文鋒持股五分之二）</td>
                </tr>
                <tr>
                    <td>團隊規模</td>
                    <td>約 300 人</td>
                    <td class="highlight-col">擴張至 600 人以上</td>
                </tr>
                <tr>
                    <td>技術路線</td>
                    <td>高效小團隊研發</td>
                    <td class="highlight-col">國家級規模競賽</td>
                </tr>
                <tr>
                    <td>開源策略</td>
                    <td>完全開源</td>
                    <td class="highlight-col">繼續開源、保持低價</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '受Claude Mythos震撼 梁文鋒自掏200億元人民幣開啟AGI豪賭 | 鉅亨網 - A股港股',
    'h1':          '梁文鋒豪擲200億<br>開啟AGI大轉向',
    'subtitle':    'DeepSeek 受 Claude Mythos 震撼，74 億美元融資後再個人注資 200 億人民幣',
    'source_url':  'https://news.cnyes.com/news/id/6515798',
    'source_name': '鉅亨網',
    'pub_date':    '2026-06-29',
    'img_alt':     'DeepSeek 梁文鋒 AI 實驗室象徵巨額投資與 AGI 決心',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260629_220744',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print("❌ HTML 組裝失敗")
    for e in errors:
        print(f"   {e}")