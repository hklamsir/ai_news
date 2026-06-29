import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.auckland.ac.nz/en/news/2026/06/29/ai-in-health-scholar-brings-clarity-and-caution-to-pacific-symposium.html" target="_blank">University of Auckland</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-29</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>AI 正在快速改變全球醫療系統，但對於毛利族和太平洋島嶼社群，確保 AI 的安全性、公平性和有效性仍是重大挑戰。Professor Robyn Whittaker 強調 AI 潛力巨大，但陷阱同樣巨大，需要建立強健的治理框架。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>預測分析（Predictive Analytics）</h4>
                <p>COVID-19 期間，預測演算法被用來識別最有可能住院的太平洋島嶼患者，讓社區健康中心能優先安排護理。但這類工具非常依賴高質量、在地相關的數據和穩健的數位基礎設施。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">👁️</div>
            <div class="tech-card-content">
                <h4>電腦視覺（Computer Vision）</h4>
                <p>AI 驅動的醫學影像技術，如視網膜篩檢工具，可在社區環境中部署，有潛力改善醫療服務的可及性。但仍面臨系統過時、實施挑戰和社區信任等障礙。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>生成式 AI（Generative AI）</h4>
                <p>被形容為「遊戲規則改變者」，也是「狂野西部」——訓練於龐大且未受監管的網路數據。本質上是機率性而非事實性的，可能產生令人信服但不正確的輸出。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>核心挑戰：數據代表性不足</h4>
                <p>全球使用的許多 AI 系統所訓練的數據集並未能充分代表毛利族和太平洋島嶼人口。「這些工具幾乎不可能已經在毛利族和太平洋社區進行過適當測試。」</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>紐西蘭和許多太平洋國家目前<strong>缺乏專門規範醫療 AI 的立法</strong>。Professor Whittaker 的團隊正在帶領全國性努力，通過多學科專家顧問小組評估 AI 工具，專注於安全性、倫理、公平性和太平洋視角。</p>
        </div>

        <div class="quote-box">
            <p>「巨大的潛力，也伴隨巨大的陷阱。我們需要共同努力，確保 AI 以對所有人安全、倫理和公平的方式實施。」</p>
            <cite>— Professor Robyn Whittaker, University of Auckland</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Te Poutoko Ora a Kiwa 聯合主任 Sir Collin Tukuitonga 教授表示：「對我們的社區來說，這不僅僅是創新的問題，而是確保新技術不會擴大現有不平等，而是支持整個太平洋地區更好、更公平的健康結果。」</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">COVID-19 期間</div>
                <div class="timeline-title">預測分析應用</div>
                <div class="timeline-desc">識別高風險太平洋患者，優先安排社區護理</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月 24 日</div>
                <div class="timeline-title">太平洋健康研討會</div>
                <div class="timeline-desc">Professor Whittaker 發表主題演講，Fale Pasifika</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">進行中</div>
                <div class="timeline-title">AI 工具評估</div>
                <div class="timeline-desc">多學科專家顧問小組評估安全性、倫理、公平性</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">待完成</div>
                <div class="timeline-title">立法規範</div>
                <div class="timeline-desc">建立醫療 AI 的專門法規框架</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">公平健康結果</div>
                <div class="timeline-desc">確保 AI 不擴大不平等，支持太平洋地區公平健康</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>AI 應用領域</th>
                    <th>優勢</th>
                    <th>挑戰</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>預測分析</td>
                    <td>識別高風險患者，優化資源分配</td>
                    <td class="highlight-col">依賴高質量在地數據</td>
                </tr>
                <tr>
                    <td>電腦視覺</td>
                    <td>社區部署便捷，提高可及性</td>
                    <td class="highlight-col">系統過時、社區信任不足</td>
                </tr>
                <tr>
                    <td>生成式 AI</td>
                    <td>減輕臨床文書負擔</td>
                    <td class="highlight-col">機率性輸出、數據治理不足</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'AI in Health: scholar brings clarity and caution to Pacific symposium – University of Auckland',
    'h1':          'AI 醫療：承諾與警覺<br>太平洋健康論壇的反思',
    'subtitle':    '毛利族與太平洋島嶼社群的 AI 醫療挑戰：數據代表性不足與治理框架缺口',
    'source_url':  'https://www.auckland.ac.nz/en/news/2026/06/29/ai-in-health-scholar-brings-clarity-and-caution-to-pacific-symposium.html',
    'source_name': 'University of Auckland',
    'pub_date':    '2026-06-29',
    'img_alt':     'Professor 在學術研討會上演講 AI 醫療，左側為太平洋文化元素，右側為 AI 類神經網路視覺化',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260629_094411',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print("❌ HTML 組裝失敗")
    for e in errors:
        print(f"   {e}")