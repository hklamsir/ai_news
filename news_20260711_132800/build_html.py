import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.bnext.com.tw/article/91477/openai-gpt-5-6-chatgpt-work-launch" target="_blank">BNEXT</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-11</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>OpenAI 正式發布 GPT-5.6 模型家族，一次推出三個版本（Sol、Luna、Terra），並同步推出企業級辦公代理 ChatGPT Work，正式向 Anthropic 的 Claude Cowork 正面宣戰。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>三大版本：Sol、Luna、Terra</h4>
                <p>GPT-5.6 一次推出三種版本：<strong>Sol</strong>（旗艦版，內建「Ultra」模式可調動子模型協同作業）、<strong>Luna</strong>（速度優化版，適合需要快速回應的場景）、<strong>Terra</strong>（平衡版，在效能與效率間取得最佳平衡，適合日常使用）。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💼</div>
            <div class="tech-card-content">
                <h4>ChatGPT Work：辦公室超級代理</h4>
                <p>OpenAI 首款企業級辦公代理，結合 ChatGPT 與 Codex 引擎，可自動生成網站、報告、試算表、簡報等文件，跨 Slack、Google Drive、Microsoft 365 等應用執行多步驟工作流程，可連續執行任務數小時。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚡</div>
            <div class="tech-card-content">
                <h4>效能亮眼：Sol 性價比勝過 Claude Fable 5</h4>
                <p>根據 Sam Altman 在 CNBC 訪問中透露：Sol 在代理程式編碼任務的 token 效率比前代提升 <strong>54%</strong>，在 AI Index 上几乎追平 Claude Fable 5，但成本僅為三分之一，在程式碼基準測試中領先。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>反應兩極：有人視為史上最佳</h4>
                <p>MagicPath AI 執行長 Pietro Schirano（已測試數月）表示：「毫不誇張，這是我用過最好的模型。」但部分測試者則偏好 Anthropic 的 Claude Fable，認為其原始智慧更強。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>GPT-5.6 Sol 在代理程式編碼任務的 token 效率提升 <strong>54%</strong>，成本僅為 Claude Fable 5 的三分之一，性價比極高。</p>
        </div>

        <div class="quote-box">
            <p>「毫不誇張，這是我用過最好的模型。」</p>
            <cite>— Pietro Schirano，MagicPath AI 執行長</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>OpenAI 這次產品線布局完整，從旗艦到輕量一應俱全，結合 ChatGPT Work 直接將「代理式 AI」推向一般消費者與企業用戶。在 Anthropic 推出 Claude Cowork 後，兩大 AI 公司的辦公代理大戰正式開打，預計將加速 AI 在職場的普及。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026-07-09</div>
                <div class="timeline-title">GPT-5.6 正式發布</div>
                <div class="timeline-desc">OpenAI 發布 GPT-5.6 模型家族（Sol、Luna、Terra）</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-09</div>
                <div class="timeline-title">ChatGPT Work 上線</div>
                <div class="timeline-desc">企業級辦公代理 ChatGPT Work 同步推出</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-09</div>
                <div class="timeline-title">川普政府要求延後發布</div>
                <div class="timeline-desc">Axios 報導強大版本是在政府要求後分期推出</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-10</div>
                <div class="timeline-title">Forbes 深度分析</div>
                <div class="timeline-desc">Forbes 報導 GPT-5.6 與 ChatGPT Work 的詳細功能與市場影響</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-11</div>
                <div class="timeline-title">BNEXT 全面報導</div>
                <div class="timeline-desc">台灣 BNEXT 發布中文完整報導</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>GPT-5.6 Sol</th>
                    <th>Claude Fable 5</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>AI Index 表現</td>
                    <td class="highlight-col">几乎追平</td>
                    <td>領先</td>
                </tr>
                <tr>
                    <td>成本</td>
                    <td class="highlight-col">三分之一</td>
                    <td>較高</td>
                </tr>
                <tr>
                    <td>程式碼基準</td>
                    <td class="highlight-col">領先</td>
                    <td>落後</td>
                </tr>
                <tr>
                    <td>定位</td>
                    <td class="highlight-col">代理式辦公應用</td>
                    <td>通用智慧</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'OpenAI發表GPT-5.6、ChatGPT Work！新模型效率大升級，三大版本與辦公代理一次看',
    'h1': 'OpenAI發表GPT-5.6、ChatGPT Work！<br>新模型效率大升級，三大版本與辦公代理一次看',
    'subtitle': '三版本 Sol / Luna / Terra 全面登場，企業辦公代理大戰開打',
    'source_url': 'https://www.bnext.com.tw/article/91477/openai-gpt-5-6-chatgpt-work-launch',
    'source_name': 'BNEXT',
    'pub_date': '2026-07-11',
    'img_alt': 'OpenAI GPT-5.6 發布：三大版本與 ChatGPT Work 辦公代理',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260711_132800',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
