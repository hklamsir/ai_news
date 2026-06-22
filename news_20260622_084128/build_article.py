import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/06/16/chatgpts-market-share-slips-below-50-for-first-time/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-16</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>ChatGPT 的全球用戶市佔率在 2026 年 3 月首次跌破 50% 大關，標誌著 AI 助理市場從一家獨大走向多元競爭的轉捩點。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>市佔率首次跌破 50%</h4>
                <p>根據 Sensor Tower《State of AI Report 2026》，ChatGPT 的「真實受眾份額」（排除跨平台重疊用戶）於 2026 年 3 月首次跌破 50%。至 5 月底，ChatGPT 市佔率為 46.4%，仍是全球最大 AI 助理，但優勢正在快速縮小。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🚀</div>
            <div class="tech-card-content">
                <h4>Gemini 快速崛起</h4>
                <p>Google Gemini 市佔率已擴張至 27.7%，每月活躍用戶達 6.62 億。Gemini 的增長動能主要來自與 Google 工具生態系的深度整合，包括搜尋、地圖、Workspace 等服務的無縫串接。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💡</div>
            <div class="tech-card-content">
                <h4>Claude 穩健追趕</h4>
                <p>Anthropic Claude 市佔率升至 10.3%，每月用戶 2.45 億。Claude 以生產力應用見長，用戶留存率正快速收窄與 ChatGPT 的差距。更值得關注的是，Claude 在美國市場的每用戶收入（ARPU）已超越 ChatGPT。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>DoD 合作引發卸載潮</h4>
                <p>OpenAI 於 2026 年 2 月與美國國防部（DoD）達成合作，隨即引發可觀測的應用程式卸載潮，用戶流失明顯可測量。這顯示品牌信任及價值觀對用戶選擇的影響力，不亞於產品功能本身。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點數據</h4>
            <p>2026 年上半年全球 AI 應用下載量接近 <strong>23 億次</strong>，相關支出超過 <strong>42 億美元</strong>。AI 助理市場正高速增長，但競爭格局正在重塑。</p>
        </div>

        <div class="quote-box">
            <p>「三年多後，AI 助理市場從一家獨大走向多元競爭。用戶愈發願意在不同助理之間切換。」</p>
            <cite>— Sensor Tower《State of AI Report 2026》</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>ChatGPT 依然以超過 11 億每月用戶領先市場，但 Gemini 借生態系之勢、CClaude 借生產力口碑，正在從不同維度撼動其領導地位。OpenAI 與國防部的合作引发的信任危機，提示著 AI 企業在商業利益與用戶價值觀之間的微妙平衡。預期未來市場將走向更明顯的差異化競爭。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2022 年 11 月</div>
                <div class="timeline-title">ChatGPT 發布</div>
                <div class="timeline-desc">OpenAI 推出 ChatGPT，開啟生成式 AI 大眾化時代</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 1 月</div>
                <div class="timeline-title">市佔率超過 50%</div>
                <div class="timeline-desc">ChatGPT 保持超過五成市佔率，領導地位看似穩固</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 2 月</div>
                <div class="timeline-title">OpenAI 與 DoD 合作</div>
                <div class="timeline-desc">OpenAI 宣佈與美國國防部合作，引發用戶卸載潮</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 3 月</div>
                <div class="timeline-title">市佔率跌破 50%</div>
                <div class="timeline-desc">ChatGPT「真實受眾份額」首次低於 50%</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 5 月底</div>
                <div class="timeline-title">最新市佔率數據</div>
                <div class="timeline-desc">ChatGPT 46.4%、Gemini 27.7%、Claude 10.3%</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>AI 助理</th>
                    <th>市佔率（2026年5月）</th>
                    <th>每月用戶</th>
                    <th>主要優勢</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>ChatGPT</td>
                    <td class="highlight-col">46.4%</td>
                    <td>11 億+</td>
                    <td>品牌先發優勢、應用場景廣泛</td>
                </tr>
                <tr>
                    <td>Gemini</td>
                    <td class="highlight-col">27.7%</td>
                    <td>6.62 億</td>
                    <td>Google 生態系深度整合</td>
                </tr>
                <tr>
                    <td>Claude</td>
                    <td class="highlight-col">10.3%</td>
                    <td>2.45 億</td>
                    <td>生產力應用、美國市場 ARPU 領先</td>
                </tr>
                <tr>
                    <td>其他</td>
                    <td>&lt;5%</td>
                    <td>—</td>
                    <td>Grok、Perplexity、DeepSeek、Meta AI</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'ChatGPT 市佔率首次跌破 50%：AI 競爭格局重塑 | TechCrunch',
    'h1':          'ChatGPT 市佔率<br>首次跌破 50%',
    'subtitle':    'Gemini 升至 27.7%、Claude 達 10.3% — AI 助理市場從一家獨大走向多元競爭',
    'source_url':  'https://techcrunch.com/2026/06/16/chatgpts-market-share-slips-below-50-for-first-time/',
    'source_name': 'TechCrunch',
    'pub_date':    '2026-06-16',
    'img_alt':     'ChatGPT 市佔率下跌示意圖，紫色份額收縮，Gemini 和 Claude 持續增長',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260622_084128',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
