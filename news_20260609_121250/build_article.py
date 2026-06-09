import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.bnext.com.tw/article/91199/ai-power-grid-infrastructure-crisis" target="_blank">BNEXT</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-09</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>AI 資料中心已成為吃電怪獸，電力基礎設施建設遠遠跟不上 AI 發展速度。從變壓器缺貨、併網塞車，到地緣政治夾擊下的供應鏈危機，一場看不見的電力戰爭正在全球開打。</p>

        <div class="tech-card">
            <div class="tech-card-icon">⚡</div>
            <div class="tech-card-content">
                <h4>AI 資料中心：用電量飆升的吃電怪獸</h4>
                <ul>
                    <li><strong>電力密度是傳統資料中心的 10 倍</strong>：仲量聯行（JLL）報告指出，AI 訓練設施所需電力密度遠超傳統資料中心</li>
                    <li><strong>2030 年 AI 工作負載將佔全球資料中心總容量的一半以上</strong>，相較 2025 年呈翻倍成長</li>
                    <li><strong>美國科技巨頭投入近 7,000 億美元</strong>（微軟、Google、亞馬遜、Meta、Oracle）確保基礎設施與供電網絡穩定</li>
                    <li><strong>2030 年將帶動高達 80 億美元的資本投入</strong>用於 AI 基礎設施</li>
                </ul>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔌</div>
            <div class="tech-card-content">
                <h4>變壓器缺貨與併網塞車</h4>
                <p>這場危機的本質在於<strong>基礎設施建設趕不上科技迭代速度</strong>：</p>
                <ul>
                    <li>資料中心硬體建設只需 <strong>12-18 個月</strong></li>
                    <li>但成功併入電網卻需要苦等 <strong>5-7 年</strong></li>
                    <li><strong>超過四分之一</strong>的新建資料中心專案因電力問題被迫延宕</li>
                    <li>德州與美國中西部等待併網的容量，預估到 2030 年將飆升至 <strong>173GW</strong></li>
                </ul>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>變壓器競爭白熱化</h4>
                <ul>
                    <li>美國發電機升壓變壓器（GSU）需求 <strong>2019-2025 年成長 274%</strong></li>
                    <li>電力變壓器需求增加<strong>116%</strong></li>
                    <li>供應缺口分別為 <strong>6%</strong> 和 <strong>30%</strong></li>
                    <li>過去交期約 <strong>50 週</strong>的大型電力變壓器，如今已拉長至 <strong>120 週以上</strong></li>
                </ul>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏛️</div>
            <div class="tech-card-content">
                <h4>美國政府的應對</h4>
                <p>2026 年 4 月，美國總統川普援引《國防生產法》第 303 條：</p>
                <ul>
                    <li>將大規模電網基礎設施列為<strong>國防必需品</strong></li>
                    <li>授權緊急聯邦資金擴大本土供應鏈關鍵部件產能</li>
                </ul>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>美國缺乏超高壓變壓器的本土製造能力，全球70-90% 的關鍵電網零組件產能集中在中國。在關稅壁壘與地緣政治角力下，美國科技巨頭在最核心的電力傳輸設備上供應鏈異常脆弱。</p>
        </div>

        <div class="quote-box">
            <p>「一座資料中心的實體建築只需要 12 到 18 個月就能完工，但是要讓這座資料中心成功併入現有電網，卻需要苦等五到七年的時間。」</p>
            <cite>— Bessemer Venture Partners 報告</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>AI 基礎設施的電力危機正在演變成國家戰略安全問題。從變壓器交付週期到併網排隊時間，處處顯示基礎設施建設周期與摩爾定律式的科技迭代存在巨大鴻溝。在地緣政治與技術瓶頸的雙重夾擊下，誰能解決電力供應問題，誰就能在 AI 競賽中搶得先機。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2019 年</div>
                <div class="timeline-title">變壓器需求起飛</div>
                <div class="timeline-desc">AI 資料中心需求開始快速增長，變壓器需求開始攀升</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">AI 基礎設施資本支出爆發</div>
                <div class="timeline-desc">美國科技巨頭宣布2025-2026 年投入近 7,000 億美元</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年初</div>
                <div class="timeline-title">電網營運商發出警告</div>
                <div class="timeline-desc">美國多個區域電網營運商警告大型負載併網排隊急速暴增</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 4 月</div>
                <div class="timeline-title">川普援引《國防生產法》</div>
                <div class="timeline-desc">將大規模電網基礎設施列為國防必需品</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2030 年</div>
                <div class="timeline-title">AI 工作負載將佔資料中心總量一半以上</div>
                <div class="timeline-desc">全球 AI 基礎設施資本投入估計達 80 億美元</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>對比項目</th>
                    <th>傳統資料中心</th>
                    <th>AI 資料中心</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>電力密度</td>
                    <td>基準</td>
                    <td class="highlight-col">10 倍</td>
                </tr>
                <tr>
                    <td>建設週期</td>
                    <td>12-18 個月</td>
                    <td class="highlight-col">12-18 個月</td>
                </tr>
                <tr>
                    <td>併網等待時間</td>
                    <td>數年</td>
                    <td class="highlight-col">5-7 年（更長）</td>
                </tr>
                <tr>
                    <td>2030 年容量佔比</td>
                    <td>不到一半</td>
                    <td class="highlight-col">一半以上</td>
                </tr>
                <tr>
                    <td>變壓器交期</td>
                    <td>約 50 週</td>
                    <td class="highlight-col">120 週以上（短缺）</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'AI熱潮下的缺電潮：儲能、電網、變壓器為何變新戰略物資？',
    'h1':          'AI熱潮下的缺電潮<br>儲能、電網、變壓器為何變新戰略物資？',
    'subtitle':    '吃電怪獸崛起：變壓器缺貨、併網塞車、地緣政治夾擊，電力危機威脅 AI 發展',
    'source_url':  'https://www.bnext.com.tw/article/91199/ai-power-grid-infrastructure-crisis',
    'source_name': 'BNEXT',
    'pub_date':    '2026-06-09',
    'img_alt':     'AI 資料中心缺電危機示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260609_121250',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print("錯誤：")
    for e in errors:
        print(f"  - {e}")