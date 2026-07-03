import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.engadget.com/2207360/cloudflare-will-filter-out-web-crawlers-that-serve-ai-companies/" target="_blank">Engadget</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-03</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Cloudflare 宣佈自動封鎖「混合用途」網頁爬蟲，這些爬蟲同時為搜尋引擎和 AI 代理/訓練服務抓取內容，預設啟動保護並推出「按使用收費」新商業模式。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🛡️</div>
            <div class="tech-card-content">
                <h4>混合用途爬蟲的問題</h4>
                <p>許多網頁爬蟲同時做兩件事：為搜尋引擎建立索引，以及為 AI 聊天機器人抓取內容訓練。Cloudflare 認為這種模式對網站所有者不公平，因為他們的內容被同時用於商業搜尋和 AI 訓練，但只有搜尋功能為網站帶來流量。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>Pay Per Crawl 升級為 Pay Per Use</h4>
                <p>2025 年推出的「按爬蟲收費」（Pay Per Crawl）功能現在升級為「按使用收費」（Pay Per Use）。不再按網頁是否被爬取收費，而是當網站內容出現在 AI 聊天機器人的回答中時，網站所有者獲得報酬。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤝</div>
            <div class="tech-card-content">
                <h4>合作夥伴：Ceramic.AI 與 You.com</h4>
                <p>目前已有 Ceramic.AI 和 You.com 與 Cloudflare 達成合作協議。Cloudflare 希望更多 AI 公司加入其「按使用收費」生態系統，讓網站所有者能從 AI 應用其內容的行為中獲得報酬。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>非人類流量已成為主流</h4>
                <p>Cloudflare 執行長 Matthew Prince 表示：「既然大多數網際網路流量已是非人類的，我們必須走得更快、更遠，才能形成可持續的生態系統。」他強調新工具為網站所有者提供更高的透明度和商業機會。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Cloudflare 的策略轉變：從可選功能變成預設保護，並推出按 AI 使用內容收費的新商業模式，而非傳統的按爬蟲次數收費。</p>
        </div>

        <div class="quote-box">
            <p>「既然大多數網際網路流量已是非人類的，我們必須走得更快、更遠，才能形成可持續的生態系統。Cloudflare 的新工具和合作關係為網站所有者提供更高的透明度和商業機會，同時也讓有明確意圖的 AI 爬蟲公司受益。」</p>
            <cite>— Matthew Prince，Cloudflare 執行長兼共同創辦人</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Cloudflare 希望能促使混合用途爬蟲將搜尋功能和 AI 代理/訓練功能分開處理，鼓勵 AI 公司更透明地說明爬蟲用途。這代表網站所有者對其內容在 AI 時代的使用方式將有更大的控制权和商業談判空間。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">Pay Per Crawl 推出</div>
                <div class="timeline-desc">Cloudflare 推出「按爬蟲收費」功能，讓網站預設封鎖 AI 爬蟲，除非公司付費。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-03</div>
                <div class="timeline-title">宣佈自動封鎖混合用途爬蟲</div>
                <div class="timeline-desc">Cloudflare 宣佈將自動封鎖同時為搜尋引擎和 AI 代理/訓練服務抓取內容的爬蟲。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-03</div>
                <div class="timeline-title">Pay Per Use 升級</div>
                <div class="timeline-desc">功能升級為「按使用收費」，按網站內容在 AI 回答中出現的次數收費，而非按爬取次數。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-03</div>
                <div class="timeline-title">首批合作夥伴</div>
                <div class="timeline-desc">Cloudflare 宣佈與 Ceramic.AI 和 You.com 建立合作關係，擴大「按使用收費」生態系統。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">業界標準化期望</div>
                <div class="timeline-desc">Cloudflare 希望能促使混合用途爬蟲將搜尋功能和 AI 代理/訓練功能分開，鼓勵 AI 公司更透明。</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>收費模式</th>
                    <th>Pay Per Crawl（舊版）</th>
                    <th class="highlight-col">Pay Per Use（新版）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>收費依據</td>
                    <td>網頁是否被爬取</td>
                    <td class="highlight-col">內容是否出現在 AI 回答中</td>
                </tr>
                <tr>
                    <td>付款時機</td>
                    <td>每次爬取時</td>
                    <td class="highlight-col">每次 AI 引用時</td>
                </tr>
                <tr>
                    <td>網站控制權</td>
                    <td>可選擇退出</td>
                    <td class="highlight-col">預設保護，可選擇加入收費</td>
                </tr>
                <tr>
                    <td>適用對象</td>
                    <td>所有 AI 爬蟲</td>
                    <td class="highlight-col">願意付費的 AI 公司</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Cloudflare will filter out web crawlers that serve AI companies - Engadget',
    'h1':          'Cloudflare 將過濾<br>AI 公司網頁爬蟲',
    'subtitle':    '混合用途爬蟲成攻擊目標　按使用收費新模式上路',
    'source_url':  'https://www.engadget.com/2207360/cloudflare-will-filter-out-web-crawlers-that-serve-ai-companies/',
    'source_name': 'Engadget',
    'pub_date':    '2026-07-03',
    'img_alt':     'Cloudflare 將過濾 AI 爬蟲示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260703_101851',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print(f"❌ HTML 生成失敗：{errors}")
