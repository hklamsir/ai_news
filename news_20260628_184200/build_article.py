import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.stheadline.com/knowledge/3585629/%E8%87%AA%E4%B8%BB%E5%AD%B8%E7%BF%92VS%E9%81%8E%E5%BA%A6%E4%BE%9D%E8%B3%B4-%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%87%89%E7%94%A8AI%E6%99%82%E9%9D%A2%E5%B0%8D%E7%94%9A%E9%BA%BC%E6%8C%91%E6%88%B0%E6%95%99%E5%AD%B8%E6%9C%89%E5%BF%83%E4%BA%BA" target="_blank">星島頭條</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-28</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>香港教育局推出「『智』啟學教」50萬撥款助中小學發展AI教育，但如何避免學生過度依賴AI、保持自主學習能力，成為教育界最關注的核心挑戰。教師的角色正從知識傳授者轉變為學習引導者。</p>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>教育局50萬撥款資助學校發展AI</h4>
                <p>教育局於2025年底推出「『智』啟學教」撥款計劃，每間學校可申請50萬元，用於購置AI軟硬件、平台服務或開發教學方案，並要求至少融入3個學科、每科發展兩個教學案例。香港教育大學過去半年已培訓逾500名教師。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>AI行政應用：聊天機械人分擔繁重事務</h4>
                <p>AI在行政工作上已見成效，聊天機械人可處理家長查詢請假程序、成績單申請等事務，減輕教師行政負擔，讓他們能更專注於教學本身。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">✍️</div>
            <div class="tech-card-content">
                <h4>中文寫作：語音轉文字需小心使用</h4>
                <p>學生雖可通過語音轉換成文字輔助創作，但仍需自行將口語轉為書面語，避免過度依賴AI直接修改，以真正提升語言能力。AI只是輔助工具，不能替代語言學習的核心過程。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚖️</div>
            <div class="tech-card-content">
                <h4>數學科的雙刃劍效應</h4>
                <p>香港教育大學江紹祥教授指出，學習動機較低的學生容易直接向AI索取答案，反而削弱學習成效；能力較強的學生則傾向減少使用AI以保留思考空間。教師需按學生能力差異導引AI的使用方式與時機。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>AI無法取代教師，反而促使教育專業轉型。教師的角色從知識傳授者轉變為學習引導者，需更靈活運用AI工具，針對不同學生設計教學方案，並加強與家長的溝通。未來AI聊天機械人亦可成為家校合作的橋樑。</p>
        </div>

        <div class="quote-box">
            <p>「人工智能為教育帶來效率與創新，但其核心價值仍在於促進學生思考與自主學習。」</p>
            <cite>— 香港教育大學人工智能及數碼能力教育中心</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>AI融入教育已是大勢所趨，但如何善用其效率同時避免學生過度依賴，是每所學校必須面對的課題。隨著「『智』啟學教」撥款計劃的推行，預計更多學校將開始系統性整合AI教學工具，而教師的專業發展與培訓將成為成敗關鍵。教育界需要在技術應用與人的互動之間找到平衡點。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2023 年</div>
                <div class="timeline-title">香港教育大學成立AI教育中心</div>
                <div class="timeline-desc">香港教育大學成立「人工智能及數碼能力教育中心」，推動中小學階段的AI教育</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年底</div>
                <div class="timeline-title">教育局推出50萬撥款計劃</div>
                <div class="timeline-desc">教育局推出「『智』啟學教」撥款計劃，每間學校可申請50萬元資助AI發展</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年上半年</div>
                <div class="timeline-title">逾500名教師完成培訓</div>
                <div class="timeline-desc">香港教育大學AI教育中心過去半年培訓逾500名教師，協助將AI工具融入各學科</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年中</div>
                <div class="timeline-title">AI教育應用成效與挑戰並存</div>
                <div class="timeline-desc">學校開始系統性整合AI教學工具，同時關注學生過度依賴AI的潛在風險</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來方向</div>
                <div class="timeline-title">教師角色轉型與家校合作</div>
                <div class="timeline-desc">教師從知識傳授者轉為學習引導者，AI聊天機械人成為家校合作橋樑</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>應用場景</th>
                    <th>AI 優勢</th>
                    <th class="highlight-col">潛在風險</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>行政工作</td>
                    <td>處理家長查詢、成績單申請等繁瑣事務</td>
                    <td class="highlight-col">需確保數據安全與私隱保護</td>
                </tr>
                <tr>
                    <td>中文寫作</td>
                    <td>語音轉文字輔助創作，降低書寫門檻</td>
                    <td class="highlight-col">學生可能過度依賴，直接用AI修改而非自主提升</td>
                </tr>
                <tr>
                    <td>數學解題</td>
                    <td>逐步展示解題過程，協助自學</td>
                    <td class="highlight-col">動機低的學生直接索取答案，失去思考機會</td>
                </tr>
                <tr>
                    <td>家校溝通</td>
                    <td>AI聊天機械人成橋樑，家長更了解教學內容</td>
                    <td class="highlight-col">需注意AI回覆的準確性與適當性</td>
                </tr>
                <tr>
                    <td>教師角色</td>
                    <td>減輕行政負擔，專注教學設計</td>
                    <td class="highlight-col">教師需提升數碼能力以有效運用AI工具</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '自主學習VS過度依賴 中小學應用AI時面對甚麼挑戰？｜教學有心人',
    'h1': '自主學習 VS 過度依賴<br>中小學應用 AI 時面對甚麼挑戰？',
    'subtitle': '教育局50萬撥款資助AI教育，但如何避免學生過度依賴、保持自主學習能力成核心課題',
    'source_url': 'https://www.stheadline.com/knowledge/3585629/%E8%87%AA%E4%B8%BB%E5%AD%B8%E7%BF%92VS%E9%81%8E%E5%BA%A6%E4%BE%9D%E8%B3%B4-%E4%B8%AD%E5%B0%8F%E5%AD%B8%E6%87%89%E7%94%A8AI%E6%99%82%E9%9D%A2%E5%B0%8D%E7%94%9A%E9%BA%BC%E6%8C%91%E6%88%B0%E6%95%99%E5%AD%B8%E6%9C%89%E5%BF%83%E4%BA%BA',
    'source_name': '星島頭條',
    'pub_date': '2026-06-28',
    'img_alt': '中小學AI教育課堂場景',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260628_184200',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print("❌ HTML 組裝失敗")
    for err in errors:
        print(f"   {err}")