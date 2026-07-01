#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://cn.nytimes.com/china/20260701/china-ai-jobs-birthright-hormuz/zh-hant/" target="_blank">紐約時報中文網</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-01</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>紐約時報分析文章探討中國應對AI革命的就業與社會穩定策略。在武漢無人駕駛計程車衝擊司機生計引發抗議後，中國政府積極出台措施，包括AI失業保險、職業培訓、法院判決保護被AI替代的員工，以及學者提出的「AI馬克思主義」理論，旨在保障就業的同時發展AI。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🚗</div>
            <div class="tech-card-content">
                <h4>無人駕駛計程車與社會穩定</h4>
                <p>在全球最大的無人駕駛汽車露天試驗場武漢，計程車司機兩年前首次抱怨無人駕駛計程車車隊規模日益擴大，引發網路抗議。中國在工作自動化方面比大多數國家擁有更豐富經驗：超過200萬台工業機器人在工作，無人駕駛快遞車在街道穿梭，服務機器人在酒店餐廳招待顧客。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚖️</div>
            <div class="tech-card-content">
                <h4>法庭判例保護勞動力</h4>
                <p>今年4月，某法院裁決科技公司用AI軟體取代員工後將其解僱屬於違法行為。杭州市中級人民法院在判詞中寫道：「人工智慧技術的發展本應用於解放勞動、促進就業、造福民生，勞動法允許用人單位承接技術變革進行更新轉型，但亦應顧及保障勞動者的合法權益。」</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📋</div>
            <div class="tech-card-content">
                <h4>政府多管齊下</h4>
                <p>人力資源和社會保障部承諾為「重點行業提供定向就業支持」；全國人大代表呼籲建立「AI失業保險」制度；官方推動職業培訓幫助勞動者適應AI為中心的工作市場；政府向企業施加巨大壓力避免裁員。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🧠</div>
            <div class="tech-card-content">
                <h4>AI馬克思主義理論</h4>
                <p>中國學者開拓了一個稱為「AI馬克思主義」的領域，試圖用馬克思主義視角剖析：在AI革命之後，究竟是誰或什麼創造了價值？是機器？是發明機器的人？還是操作機器的人？</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>布魯金斯學會專家陳凱欣指出中國的經驗表明，政策制定者對這項技術擁有主動干預的權力，能夠引導其發展方向，而非僅僅聽任命運安排。美國由科技公司主導追求超級智能；中國由國家驅動，追求經濟自給自足的同時確保人類就業。</p>
        </div>

        <div class="quote-box">
            <p>「人工智慧技術的發展本應用於解放勞動、促進就業、造福民生。」</p>
            <cite>— 杭州市中級人民法院判詞</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>人類的選擇依然至關重要。兩種截然不同的人工智慧未來願景正在現實世界中實時上演：美國的公司主導模式與中國的國家驅動模式，將為全球AI治理提供截然不同的參照。中國的「AI馬克思主義」理論與實際政策相結合，反映出這個全球第二大經濟體對AI時代的就業和社會穩定問題的深度思考。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">兩年前</div>
                <div class="timeline-title">武漢司機首次抗議</div>
                <div class="timeline-desc">武漢計程車司機首次抱怨無人駕駛計程車車隊規模擴大，在網路上引發反對聲浪</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025年3月</div>
                <div class="timeline-title">人大代表倡議AI失業保險</div>
                <div class="timeline-desc">全國人大代表呼籲建立「AI失業保險」制度作為被轉崗工人的安全網</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026年4月</div>
                <div class="timeline-title">法院裁決保護被AI替代員工</div>
                <div class="timeline-desc">法院裁決科技公司用AI軟體取代員工後將其解僱屬於違法行為</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026年7月</div>
                <div class="timeline-title">紐約時報深度分析</div>
                <div class="timeline-desc">紐約時報發布「AI馬克思主義」分析文章，探討中國應對AI革命的獨特策略</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">現在</div>
                <div class="timeline-title">中國工廠超過200萬台機器人</div>
                <div class="timeline-desc">中國在工作自動化方面擁有全球最豐富的實際經驗</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>美國模式</th>
                    <th>中國模式</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>主導者</td>
                    <td class="highlight-col">科技公司（如OpenAI）</td>
                    <td>國家驅動</td>
                </tr>
                <tr>
                    <td>目標</td>
                    <td class="highlight-col">追求超級智能</td>
                    <td>經濟自給自足 + 社會穩定</td>
                </tr>
                <tr>
                    <td>與就業關係</td>
                    <td class="highlight-col">市場自然調節</td>
                    <td>政府積極干預保障就業</td>
                </tr>
                <tr>
                    <td>AI應用範圍</td>
                    <td class="highlight-col">新興科技產業為主</td>
                    <td>涵蓋所有行業（從機器人到鋼鐵水泥）</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '「AI馬克思主義」：中國如何應對人工智慧革命',
    'h1': '「AI馬克思主義」：<br>中國如何應對AI革命',
    'subtitle': '從法庭判例到失業保險 中國的AI就業策略',
    'source_url': 'https://cn.nytimes.com/china/20260701/china-ai-jobs-birthright-hormuz/zh-hant/',
    'source_name': '紐約時報中文網',
    'pub_date': '2026-07-01',
    'img_alt': '中國AI與就業場景示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260701_220200',
    article_content=article_content,
    metadata=metadata
)

print(f"\n結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")