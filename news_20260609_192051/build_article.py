import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.hk01.com/財經快訊/60358512/彭博-內地擬斥2萬億人民幣建數據中心-8成晶片用華為擠走nvidia" target="_blank">HK01（彭博）</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-09</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>《彭博》報道，內地計劃在未來五年內投資約 <strong>2 萬億元人民幣</strong>在全國建設數據中心，目標是依靠本土供應商提供至少 <strong>80% 的技術</strong>（包括華為晶片），從而將 Nvidia 和 AMD 擠出市場。</p>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>2 萬億投資計劃</h4>
                <ul>
                    <li>內地計劃在未來五年投資約 <strong>2 萬億元人民幣</strong>建設數據中心</li>
                    <li>包括國發改委在內的政府機構正在制定全國建立互聯互通計算中心網絡的藍圖</li>
                    <li>中國移動和中國電信等國有企業將營運大部分數據中心</li>
                    <li>資金主要透過<strong>主權債務融資</strong>，包括期限超過 10 年的超長期政府債券</li>
                </ul>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🇨🇳</div>
            <div class="tech-card-content">
                <h4>本土化策略：80% 採用華為晶片</h4>
                <ul>
                    <li>計劃目標：至少 <strong>80% 的技術</strong>來自本土供應商（包括華為）</li>
                    <li>旨在將 <strong>Nvidia（英偉達）和 AMD 擠出市場</strong></li>
                    <li>這是今年稍早宣布的「六大網路」計劃的關鍵組成部分</li>
                    <li>涵蓋水、電到運算等關鍵基礎設施的建設</li>
                </ul>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚡</div>
            <div class="tech-card-content">
                <h4>與電網整合：總投資或達 5 萬億</h4>
                <ul>
                    <li>中方還計劃將<strong>電網與該項目整合</strong></li>
                    <li>這可能使預計總投資<strong>至少達到 5 萬億元</strong></li>
                    <li>目標：2028 年前將分散的數據設施連接到統一網絡</li>
                    <li>推動 AI 在醫療、交通、城市管理等公共領域的應用</li>
                </ul>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏢</div>
            <div class="tech-card-content">
                <h4>私人企業參與</h4>
                <ul>
                    <li>2 萬億元預算<strong>不包括</strong>阿里巴巴和騰訊等私人企業的支出</li>
                    <li>目前尚不清楚統一數據中心網絡如何與私人數據中心協同運作</li>
                    <li>中國企業很可能成為最大受益者</li>
                </ul>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>這項投資顯示北京決心在 AI 領域突破美國封鎖，即便其他領域支出因政府債務攀升而縮減。中國最新的五年規劃（涵蓋至 2030 年）提出了建置全國運算網路的構想，北京承諾優先發展資料基礎設施。</p>
        </div>

        <div class="quote-box">
            <p>「將其提升為國家戰略，可以確保政策協調一致，並調動資金。」</p>
            <cite>— Forrester Research 首席分析師 Charlie Dai</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Forrester Research 首席分析師 Charlie Dai 指出，統一的運算網路將匯集分散的區域資源，使企業能更廣泛獲取高效能運算資源，有助加快 AI 模型迭代速度。在美中科技競爭背景下，這項投資顯示北京決心在 AI 領域突破美國封鎖，即使面對債務壓力，仍將 AI 基礎設施列為國家戰略優先。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年初</div>
                <div class="timeline-title">六大網路計劃宣布</div>
                <div class="timeline-desc">中國宣布涵蓋水、電到運算等關鍵基礎設施的「六大網路」建設計劃</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">彭博披露 2 萬億數據中心計劃</div>
                <div class="timeline-desc">報道指內地計劃未來五年投資 2 萬億元人民幣建設數據中心</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">國有企業參與營運</div>
                <div class="timeline-desc">中國移動和中國電信等國企將營運並確保數據中心互聯互通</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2028 年前</div>
                <div class="timeline-title">統一網絡截止期限</div>
                <div class="timeline-desc">目標是將分散的數據設施連接到統一網絡</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2030 年</div>
                <div class="timeline-title">五年規劃收官</div>
                <div class="timeline-desc">中國最新五年規劃涵蓋至 2030 年，優先發展資料基礎設施</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>對比項目</th>
                    <th>中國數據中心策略</th>
                    <th>美國晶片供應商</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>市場佔比目標</td>
                    <td class="highlight-col">80% 本土供應商</td>
                    <td>被逐步排除</td>
                </tr>
                <tr>
                    <td>主要晶片供應商</td>
                    <td class="highlight-col">華為等本土廠商</td>
                    <td>Nvidia、AMD</td>
                </tr>
                <tr>
                    <td>投資金額</td>
                    <td class="highlight-col">2-5 萬億元（含電網）</td>
                    <td>—</td>
                </tr>
                <tr>
                    <td>資金來源</td>
                    <td class="highlight-col">主權債務、超長期國債</td>
                    <td>—</td>
                </tr>
                <tr>
                    <td>營運主體</td>
                    <td class="highlight-col">國有企業</td>
                    <td>私人企業</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '彭博︰內地擬斥2萬億人民幣建數據中心　8成晶片用華為擠走Nvidia',
    'h1':          '彭博︰內地擬斥2萬億建數據中心<br>8成晶片用華為擠走Nvidia',
    'subtitle':    '北京 AI 基建大計：2萬億投資、80%本土晶片、整合電網總規模或達5萬億',
    'source_url':  'https://www.hk01.com/財經快訊/60358512/彭博-內地擬斥2萬億人民幣建數據中心-8成晶片用華為擠走nvidia',
    'source_name': 'HK01',
    'pub_date':    '2026-06-09',
    'img_alt':     '中國2萬億數據中心投資計劃概念圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260609_192051',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print("錯誤：")
    for e in errors:
        print(f"  - {e}")