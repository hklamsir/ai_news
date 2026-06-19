import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/06/16/probably-raises-9m-to-build-a-more-reliable-kind-of-ai/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-16</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>AI 創業公司 Probably 獲得 a16z 900 萬美元種子輪融資，透過「確定性驗證器」消除 LLM 幻覺問題，目標將 AI 準確率提升至 99.99%。</p>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>900 萬美元種子輪</h4>
                <p>Probably 獲得 Andreessen Horowitz（a16z）領投的 900 萬美元種子輪融資，專注解決 AI 可靠性問題。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎯</div>
            <div class="tech-card-content">
                <h4>消除 AI 幻覺</h4>
                <p>創辦人 Peter Elias 表示，公司目標是確保錯誤資訊永遠不會到達用戶，達到 99.99% 準確率，媲美傳統確定性軟件。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚙️</div>
            <div class="tech-card-content">
                <h4>「數據科學機甲」系統</h4>
                <p>通過確定性驗證器（Deterministic Validator）在 AI 回應離開模型前進行嚴格驗證，即時拒絕與數據庫不符的結果，並提供引用來源和完整審計追蹤。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💡</div>
            <div class="tech-card-content">
                <h4>小模型、高效率</h4>
                <p>系統可在比前沿模型落後四個等級的模型上運行，可使用普通桌上型電腦而非數據中心，大幅降低 Token 成本。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>在 AI 支出不斷上升、企業開始重新評估 AI 預算的背景下，Probably 的方案可在較小模型上實現高精度，大幅降低成本。</p>
        </div>

        <div class="quote-box">
            <p>「公司的目標是防止幻覺和簡單的事實錯誤到達用戶，實現 99.99% 的準確率——這在確定性系統中很常見，但對 AI 來說要困難得多。」</p>
            <cite>— Peter Elias，Probably 創辦人</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>如果 Probably 能兌現承諾，我們將進入一個「智能」機器人錯誤被完全消除的時代。這項技術不僅適用於數據科學，還可擴展至會計、醫療等任何對精確度敏感的場景。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">現在</div>
                <div class="timeline-title">LLM 幻覺問題</div>
                <div class="timeline-desc">主流 AI 模型如 ChatGPT 有時會自信地提供錯誤答案</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">現在</div>
                <div class="timeline-title">Probably 成立</div>
                <div class="timeline-desc">Peter Elias 創立公司，專注解決 AI 可靠性問題</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-06-16</div>
                <div class="timeline-title">900 萬美元融資</div>
                <div class="timeline-desc">獲得 a16z 領投的種子輪資金</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">進行中</div>
                <div class="timeline-title">產品開發</div>
                <div class="timeline-desc">數據科學工具已可運行，提供引用和審計追蹤</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">應用擴展</div>
                <div class="timeline-desc">技術將擴展至會計、醫療等高精確度需求場景</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>傳統 LLM</th>
                    <th>Probably 方案</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>準確率</td>
                    <td>較低，存在幻覺</td>
                    <td class="highlight-col">99.99%</td>
                </tr>
                <tr>
                    <td>運行環境</td>
                    <td>需要數據中心</td>
                    <td class="highlight-col">桌上型電腦即可</td>
                </tr>
                <tr>
                    <td>Token 成本</td>
                    <td>高</td>
                    <td class="highlight-col">大幅降低</td>
                </tr>
                <tr>
                    <td>結果驗證</td>
                    <td>無</td>
                    <td class="highlight-col">確定性驗證器</td>
                </tr>
                <tr>
                    <td>引用追蹤</td>
                    <td>無</td>
                    <td class="highlight-col">完整審計追蹤</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Probably raises $9M to build a more reliable kind of AI',
    'h1':          'Probably 獲 a16z 900萬美元融資<br>要讓 AI 不再「一本正經胡说八道」',
    'subtitle':    'AI 創業公司透過「確定性驗證器」消除幻覺，目標達到 99.99% 準確率',
    'source_url':  'https://techcrunch.com/2026/06/16/probably-raises-9m-to-build-a-more-reliable-kind-of-ai/',
    'source_name': 'TechCrunch',
    'pub_date':    '2026-06-16',
    'img_alt':     'AI 幻覺消除示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260619_110700',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print(f"❌ 錯誤：{errors}")