import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-27</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>美國政府對 Anthropic 最先進的 AI 模型實施出口禁令後，東京與北京的至少兩家新創公司迅速填補市場空缺。Sakana AI 推出「Fugu」協調模型、中國 360 發布網安 AI 工具，本地化 AI 生態正在亞洲加速成形。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🐡</div>
            <div class="tech-card-content">
                <h4>Sakana AI 推出 Fugu：構建「集體智慧」防禦</h4>
                <p>東京 Sakana AI 共同創辦人 David Ha 將 Fugu 定位為對抗單一供應商風險的策略，而非單純的市場瓜分。Fugu 專為協調多個模型的代理使用而設計，他稱之為「超越更大模型的下一個前沿」。「獲取頂尖模型可以在一夜之間消失，集體智慧是對抗這種權力集中的務實對沖。」</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔒</div>
            <div class="tech-card-content">
                <h4>中國 360 發布網安 AI 工具，暗示戰略資產價值</h4>
                <p>據 Reuters 報導，360 創辦人周鴻禕將漏洞發現 AI 稱為「國家戰略資產」，警告「單向透明」的風險。360 發布了兩款 AI 安全工具：Tulongfeng（自動發現軟件漏洞）與 Yitianzhen（自動化網絡防禦和事件響應），直接對標美國被禁的漏洞發現 AI 能力。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📈</div>
            <div class="tech-card-content">
                <h4>Anthropic 的高速成長與出口禁令兩難</h4>
                <p>Anthropic 本身正處於歷史性增長軌道，2026 年 5 月 ARR 已突破 470 億美元。但 FT 分析指出，Anthropic 在 2026 年的溝通中「風險」一詞出現了 336 次。Meta 前首席 AI 科學家 Yann LeCun 批評這是「荒謬的恐懼販賣」最終奏效。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌏</div>
            <div class="tech-card-content">
                <h4>部分禁令解除，市場空缺仍存</h4>
                <p>Politico 報導指，美國政府已於 6 月 26 日部分解除對 Mythos 5 的出口禁令，開放給 100 多家「可信賴合作夥伴」，但 Fable 5 仍被封鎖。Sakana AI 發言人強調新產品發布「完全巧合」，但公司網站已開始以「先進能力，遠離出口管制」為口號宣傳。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Sakana AI 的 Fugu 模型可協調多個模型的代理使用，被視為「超越更大模型的下一個前沿」。中國 360 的 Tulongfeng 和 Yitianzhen 則直接瞄準漏洞發現和網絡防禦的戰略市場。專家警告，長期而言美國企業的全球市場份額可能因此下滑。</p>
        </div>

        <div class="quote-box">
            <p>「Access to top models can disappear overnight. Collective intelligence is the practical hedge against this concentration of power.」</p>
            <cite>— David Ha,共同創辦人兼 CEO,Sakana AI</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這波亞洲 AI 新創的崛起，暴露了依賴單一國家供應商的結構性風險。隨著出口管制成為新常態，本地化 AI 生態系統正在加速形成。對於亞洲企業和政府機構而言，「先進能力，遠離出口管制」的口號吸引力日增，這將催生更多區域性 AI 自主供應鏈，同時加劇全球 AI 地緣政治的競爭態勢。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月 12 日</div>
                <div class="timeline-title">美國實施出口禁令</div>
                <div class="timeline-desc">特朗普政府以國家安全為由，禁止非美國居民使用 Anthropic 的 Mythos 和 Fable 5 模型</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月中旬</div>
                <div class="timeline-title">Sakana AI 發布 Fugu</div>
                <div class="timeline-desc">東京 Sakana AI 推出協調模型 Fugu，定位為「集體智慧」對沖策略</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月中旬</div>
                <div class="timeline-title">中國 360 發布安全 AI</div>
                <div class="timeline-desc">360 發布 Tulongfeng 和 Yitianzhen，瞄準漏洞發現和網絡防禦市場</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月 26 日</div>
                <div class="timeline-title">部分禁令解除</div>
                <div class="timeline-desc">美國政府部分解除 Mythos 5 禁令，開放給 100 多家可信賴合作夥伴，Fable 5 仍被封鎖</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月 27 日</div>
                <div class="timeline-title">TechCrunch 報導發布</div>
                <div class="timeline-desc">亞洲新創填補市場空缺的報導引發業界關注</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>公司 / 模型</th>
                    <th>類型</th>
                    <th class="highlight-col">主要功能</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Sakana AI - Fugu</td>
                    <td>協調模型（Orchestration Model）</td>
                    <td class="highlight-col">整合多個模型代理使用，被視為「超越更大模型的下一個前沿」</td>
                </tr>
                <tr>
                    <td>中國 360 - Tulongfeng</td>
                    <td>網絡安全 AI</td>
                    <td class="highlight-col">自動發現軟件漏洞，被稱為「國家戰略資產」</td>
                </tr>
                <tr>
                    <td>中國 360 - Yitianzhen</td>
                    <td>網絡防禦 AI</td>
                    <td class="highlight-col">自動化網絡防禦和事件響應</td>
                </tr>
                <tr>
                    <td>Anthropic - Mythos 5</td>
                    <td>前沿模型（部分解除）</td>
                    <td class="highlight-col">超強漏洞發現能力，已對 100+ 可信賴合作夥伴重新開放</td>
                </tr>
                <tr>
                    <td>Anthropic - Fable 5</td>
                    <td>前沿模型（仍被封鎖）</td>
                    <td class="highlight-col">更嚴格限制版本，外國用戶仍無法訪問</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': "Asian AI startups launch Mythos-like models as Anthropic's export ban drags on - TechCrunch",
    'h1': "Asian AI Startups 推出 Mythos-Like 模型<br>Anthropic 出口禁令持續發酵",
    'subtitle': '美國禁令後亞洲新創填補市場空缺，本地化 AI 生態加速成形',
    'source_url': 'https://techcrunch.com/2026/06/27/asian-ai-startups-launch-mythos-like-models-as-anthropics-export-ban-drags-on/',
    'source_name': 'TechCrunch',
    'pub_date': '2026-06-27',
    'img_alt': 'Asian AI startups 應對美國出口禁令',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260628_171855',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print("❌ HTML 組裝失敗")
    for err in errors:
        print(f"   {err}")