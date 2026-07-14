import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/07/13/anthropic-starts-localizing-claude-pricing-for-india-its-biggest-market-after-the-us/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-13</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Anthropic 在印度推出盧比計價的 Claude 訂閱方案，印度是僅次於美國的全球第二大市場，佔全球 Claude 使用量的 5.8%，定價本地化可降低用戶進入障礙。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📱</div>
            <div class="tech-card-content">
                <h4>印度定價詳情</h4>
                <p>Claude Pro 在印度定價為每月 ₹2,000（約 21 美元），按年計費；美國定價為每月 17 美元。Claude Max 起始價格為每月 ₹11,999（約 125 美元），美國為 100 美元。Team 方案每位用戶每月 ₹2,399（約 25 美元），美國為 20 美元。印度價格已含當地稅項。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🇮🇳</div>
            <div class="tech-card-content">
                <h4>支付方式限制</h4>
                <p>Anthropic 尚未啟用印度統一支付介面（UPI）付款，用戶仍需透過信用卡或 Apple/Google 應用商店帳單系統支付。這與 OpenAI 形成對比——OpenAI 在 8 月為 ChatGPT 推出印度盧比定價時已支援 UPI。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏢</div>
            <div class="tech-card-content">
                <h4>印度業務擴張</h4>
                <p>Anthropic 今年 2 月在班加羅爾設立辦公室，並於 1 月任命前微軟印度董事總經理 Irina Ghose 領導印度業務。公司亦在近月與印度 IT 服務巨頭 Infosys 和 Tata Consultancy Services 達成合作，擴大企業 AI 部署。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>擴張挫折</h4>
                <p>Anthropic 在 6 月突然暫停向非美國實體提供 Fable 5 和 Mythos 5 模型，迫使部分印度開發者和初創創辦人考慮替代方案。Fable 5 的限制已解除，但 Mythos 5 的訪問權限仍受限制。</p>
            </div>
        </div>


        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>印度佔全球 Claude 使用量的 5.8%，是僅次於美國的第二大市場。Anthropic 在印度面臨來自 OpenAI 的競爭，後者已支援 UPI 支付。</p>
        </div>

        <div class="quote-box">
            <p>「India accounts for 5.8% of global Claude usage, making it the service's second-largest market after the U.S., according to Anthropic.」</p>
            <cite>— TechCrunch</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>印度作為全球人口最多的國家，成為 AI 公司的必爭之地。定價本地化可降低用戶進入障礙，減少外幣結算的麻煩。隨著更多 AI 企業針對印度市場推出本地定價方案，預計將加速 AI 在當地的普及。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2025 年 10 月</div>
                <div class="timeline-title">宣佈設立班加羅爾辦公室</div>
                <div class="timeline-desc">Anthropic 宣佈將在印度班加羅爾設立辦公室</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 1 月</div>
                <div class="timeline-title">任命印度負責人</div>
                <div class="timeline-desc">任命前微軟印度董事總經理 Irina Ghose 領導印度業務</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 2 月</div>
                <div class="timeline-title">班加羅爾辦公室正式成立</div>
                <div class="timeline-desc">Anthropic 在班加羅爾正式設立印度辦公室</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">模型訪問受限</div>
                <div class="timeline-desc">突然暫停向非美國實體提供 Fable 5 和 Mythos 5 模型</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月</div>
                <div class="timeline-title">印度定價本地化</div>
                <div class="timeline-desc">正式推出印度盧比計價的 Claude 訂閱方案</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>方案</th>
                    <th>印度價格（₹）</th>
                    <th>印度價格（美元）</th>
                    <th>美國價格（美元）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Claude Pro</td>
                    <td>₹2,000/月</td>
                    <td class="highlight-col">約 $21</td>
                    <td>$17</td>
                </tr>
                <tr>
                    <td>Claude Max</td>
                    <td>₹11,999/月</td>
                    <td class="highlight-col">約 $125</td>
                    <td>$100</td>
                </tr>
                <tr>
                    <td>Claude Team</td>
                    <td>₹2,399/月/人</td>
                    <td class="highlight-col">約 $25</td>
                    <td>$20/人</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Anthropic 在印度推出 Claude 定價本地化，第二大市場僅次於美國',
    'h1':          'Anthropic 在印度推出<br>Claude 定價本地化',
    'subtitle':    '印度佔全球 Claude 使用量 5.8%，僅次於美國的第二大市場',
    'source_url':  'https://techcrunch.com/2026/07/13/anthropic-starts-localizing-claude-pricing-for-india-its-biggest-market-after-the-us/',
    'source_name': 'TechCrunch',
    'pub_date':    '2026-07-13',
    'img_alt':     '印度專業人士使用 Claude AI 助手，背景為現代化科技辦公室',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260714_113800',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 建立成功")
else:
    print(f"❌ HTML 建立失敗：{errors}")
