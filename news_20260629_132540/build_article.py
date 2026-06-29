import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://news.mingpao.com/pns/%E6%B8%AF%E8%81%9E/article/20260629/s00002/1782663276476" target="_blank">明報</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-29</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>中文大學醫學院和工程學院團隊歷時4年研發出L3監督式自主AI清除腎石手術機械人，可在醫生監督下自動執行腎臟內導航、辨識腎石及吸走碎石等操作。今年2月底完成首宗人體手術，目標明年增至150至200宗手術。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>L3 監督式自主 AI 手機械人</h4>
                <p>如同汽車自動駕駛的L3等級，機械人在醫生監督下自動執行高精度、重複性操作，包括腎臟內導航、腎石辨識定位、激光碎石及負壓吸走碎石。醫生保留最終決策權。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔬</div>
            <div class="tech-card-content">
                <h4>AI 厚度估算突破</h4>
                <p>直徑僅3毫米的軟式輸尿管鏡需容納多種組件，只能用單鏡頭。團隊利用超過1000個手術影片訓練AI模型，現時腎石辨識準確率超過99%，厚度估算準確率超過95%。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚡</div>
            <div class="tech-card-content">
                <h4>人機協作優勢</h4>
                <p>手術效果更穩定一致、減輕醫生體力負擔、縮短手術及訓練時間。更可一次手術處理直徑超過3厘米的腎石（以往需多次手術）。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>商業化之路</h4>
                <p>已申請10個專利，累積研發經費至少數百萬元。計劃明年做150至200宗手術，2028至2030年間取得中、美、歐盟醫療器械認證，正式量產。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>「RIRS手術機械人」已獲「產學研1+計劃」資助。今年內至少3位醫生使用原型，完成10至15宗手術；明年增至5至10個原型，進行多中心臨床測試。</p>
        </div>

        <div class="quote-box">
            <p>「這種人機協作模式能夠顯著地提升有關手術效果的穩定和一致程度，大大減輕醫生的體力和專注力負擔。」</p>
            <cite>— 劉青陽醫生，中大醫學院外科學系助理教授</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>團隊目標2028至2030年間陸續取得中國內地、美國、歐盟的醫療器械認證，正式量產推出市場。即使交由內地代工廠生產，售價也很難低於100萬元。但腎石越大，使用機械人節省時間的優勢越明顯。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2022 年</div>
                <div class="timeline-title">組成研發團隊</div>
                <div class="timeline-desc">10多人跨醫學院和工程學院團隊成立</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">第二代原型</div>
                <div class="timeline-desc">在兩個屍體上測試，初步驗證可行性和效果</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 2 月</div>
                <div class="timeline-title">首宗人體手術</div>
                <div class="timeline-desc">威爾斯親王醫院成功完成第一次人體 RIRS 手術</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年內</div>
                <div class="timeline-title">第三代原型定型</div>
                <div class="timeline-desc">完成10至15宗手術，發展至第四代定型設計</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2028-2030 年</div>
                <div class="timeline-title">取得認證量產</div>
                <div class="timeline-desc">取得中、美、歐盟醫療器械認證，正式量產</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>傳統 RIRS 手術</th>
                    <th>RIRS 手術機械人</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>腎石辨識</td>
                    <td>醫生人手操作</td>
                    <td class="highlight-col">AI 自動辨識（準確率 >99%）</td>
                </tr>
                <tr>
                    <td>腎石厚度估算</td>
                    <td>難以準確估算</td>
                    <td class="highlight-col">AI 估算（準確率 >95%）</td>
                </tr>
                <tr>
                    <td>最大處理腎石</td>
                    <td>直徑 3 厘米（需多次手術）</td>
                    <td class="highlight-col">一次手術處理更大腎石</td>
                </tr>
                <tr>
                    <td>醫生負擔</td>
                    <td>體力、專注力損耗大</td>
                    <td class="highlight-col">顯著減輕</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'AI年代：中大研L3式清除腎石AI機械人',
    'h1':          'AI 年代：中大研<br>L3式清除腎石AI機械人',
    'subtitle':    '中文大學研發 L3 監督式自主 AI 手術機械人，首宗人體手術成功完成',
    'source_url':  'https://news.mingpao.com/pns/%E6%B8%AF%E8%81%9E/article/20260629/s00002/1782663276476',
    'source_name': '明報',
    'pub_date':    '2026-06-29',
    'img_alt':     'AI 腎石手術機械人，手術室場景，醫生在控制台監控機械人進行微創手術',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260629_132540',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print("❌ HTML 組裝失敗")
    for e in errors:
        print(f"   {e}")