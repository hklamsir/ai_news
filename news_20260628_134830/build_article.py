import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://fc.bnext.com.tw/articles/view/4726" target="_blank">數位時代</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-28</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>拉亞漢堡執行長徐沛源從科技業跨足傳統餐飲，透過 AI 與數位轉型，成功帶領這個老字號品牌逆風翻盤。店數下降長達 8、9 年後，2025 年重新站回 500 大關，2026 年更正式走出低谷，同店業績 24 個月內成長近 50%。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🚀</div>
            <div class="tech-card-content">
                <h4>從科技業到早餐店：用「速度戰」逆轉劣勢</h4>
                <p>徐沛源受日本企業家顛覆傳統產業周期啟發，深信「真正企業競爭的核心是速度，而不是單純的技術」。他將 AI 深植於企業營運，徹底顛覆傳統新品開發流程——過去動輒耗時半年的新品開發，如今壓縮至短短 3 周內完成並推向市場。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚙️</div>
            <div class="tech-card-content">
                <h4>AI 接管後勤：庫存、財報、排班全部自動化</h4>
                <p>在營運端，AI 系統全面接管了最讓加盟主頭痛的物料庫存、財報結算與繁瑣的排班任務。當沉重的後勤包袱被卸下，門市老闆得以專注於服務顧客，總部則有充足量能發動大型行銷戰。徐沛源指出，每一次新品上市，在第五周之後大概都還可保有 10% 以上的業績推升。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📱</div>
            <div class="tech-card-content">
                <h4>「預約點餐」收服加盟主，瓦解轉型阻力</h4>
                <p>徐沛源觀察到消費者「想要準時拿到早餐」這一點，為拉亞漢堡的 App 點餐系統加入「預約」功能——客人前一天預約，門市就能在指定時間備餐。一位退役軍人出身的加盟店長形容：「現在每天早上點開系統接單，順暢地就像是在開戰鬥機一樣。」</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">❤️</div>
            <div class="tech-card-content">
                <h4>後台 AI 衝效率、前台遞溫度</h4>
                <p>徐沛源強調，導入高科技的終極目的並非讓實體店面變得冷冰冰。當 AI 接管了追求極致效率與繁瑣後勤的苦差事，門市人員才能真正「騰出手來」，把客人當作真正的朋友來款待。「AI 的價值，就是要保護那些追求效率的工作；而我們省下來的餘裕，則要去創造真正無可取代的服務，在數位時代保留早餐店的感情。」</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>拉亞漢堡同店業績在 24 個月內整體成長將近 50%，新品開發週期從半年壓縮至 3 周，2025 年開店數重新站回 500 大關，成功迎來新開店數超越關店數的黃金交叉。</p>
        </div>

        <div class="quote-box">
            <p>「我們不要成為全世界最好的，我只要成為他家附近最好的早餐店。」</p>
            <cite>— 徐沛源，拉亞漢堡執行長</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這套「後台靠 AI 衝效率、前台靠員工遞溫度」的數位戰法，為傳統餐飲業的 AI 轉型提供了寶貴的參考模板。當 AI 系統全面接管了追求極致效率與繁瑣後勤的苦差事，門市人員才能真正「騰出手來」，把客人當作真正的朋友來款待——這正是科技帶給餐飲業的最大價值。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2023 年</div>
                <div class="timeline-title">店數低谷</div>
                <div class="timeline-desc">拉亞漢堡店數下降長達 8、9 年，2023 年跌至谷底</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2024 年</div>
                <div class="timeline-title">AI 系統全面上線</div>
                <div class="timeline-desc">AI 接管庫存、財報、排班等後勤任務，釋放門市人力</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">重返 500 大關</div>
                <div class="timeline-desc">開店數重新站回 500 大關，同店業績開始大幅成長</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025-2026</div>
                <div class="timeline-title">黃金交叉</div>
                <div class="timeline-desc">新開店數正式超越關店數，24 個月同店業績成長近 50%</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">走出低谷持續成長</div>
                <div class="timeline-desc">正式宣告走出低谷，2026 AI TAIWAN 未來商務展分享成功經驗</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>轉型前</th>
                    <th class="highlight-col">轉型後（AI 導入）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>新品開發週期</td>
                    <td>約 6 個月</td>
                    <td class="highlight-col">3 周</td>
                </tr>
                <tr>
                    <td>同店業績成長</td>
                    <td>負成長</td>
                    <td class="highlight-col">24 個月成長近 50%</td>
                </tr>
                <tr>
                    <td>後勤作業</td>
                    <td>人工處理（庫存/財報/排班）</td>
                    <td class="highlight-col">AI 全自動接管</td>
                </tr>
                <tr>
                    <td>開店數趨勢</td>
                    <td>連跌 8-9 年</td>
                    <td class="highlight-col">2025 年重返 500 大關</td>
                </tr>
                <tr>
                    <td>新品上市效果</td>
                    <td>熱潮過後快速消退</td>
                    <td class="highlight-col">第五周後仍保有 10% 業績推升</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '店數連跌 8 年、同店業績卻靠 AI 漲 5 成！拉亞漢堡的 AI 轉型：把後台交給機器，溫度留給人｜未來商務',
    'h1': '店數連跌 8 年、同店業績卻靠 AI 漲 5 成！<br>拉亞漢堡的 AI 轉型：把後台交給機器，溫度留給人',
    'subtitle': '從科技業跨足早餐連鎖，徐沛源如何用 AI 與數位轉型帶領老字號品牌逆風翻盤？',
    'source_url': 'https://fc.bnext.com.tw/articles/view/4726',
    'source_name': '數位時代',
    'pub_date': '2026-06-28',
    'img_alt': '拉亞漢堡 AI 轉型示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260628_134830',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print("❌ HTML 組裝失敗")
    for err in errors:
        print(f"   {err}")