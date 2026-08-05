import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://mp.weixin.qq.com/s/u5K18wwIeerm2-huxaiGDA" target="_blank">微信公眾號</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-05</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>阿里巴巴發布 Qwen3.8-Max，一位 AI Maker 在真實任務場景中測試後，給出了令人信服的使用感受：國產模型與頭部閉源模型的差距已經非常小，他願意將 Qwen3.8-Max 作為主力模型使用。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>測試者的核心觀點</h4>
                <p>作者批評了「國模與硅谷閉源模型不在一個梯隊」的慣性思維。從時間維度看，國產模型已從早年「不堪一擊」到現在「站穩腳跟」，在國際社區也贏得了尊重。Sam Altman 也曾承認開源生態的價值——讓各國各行業不必完全依賴少數美國公司。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚙️</div>
            <div class="tech-card-content">
                <h4>Qwen3.8-Max 核心配置</h4>
                <p><strong>2.4T 總參數</strong>（兆級）、95B 激活參數、稀疏 MoE 架構、100 萬 Tokens 上下文、原生多模態支持。2.4T 參數規模在國內僅有兩個模型達到，工程難度極高。從 2T 擴展到 3T，和從 200B 擴展到 300B，難度完全不在一個量級。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💻</div>
            <div class="tech-card-content">
                <h4>真實任務測試</h4>
                <p><strong>Coding 任務</strong>：讓 AI 完成一個實際產品 App，包括找 Logo、二次加工、用戶名密碼兼容，跑了兩個多小時，一次性交出成品<br><strong>辦公主務</strong>：讓 AI 生成課件 PPT，AI 直接採用千問辦公主頁配色，最終成品「很有美感」</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>今年為何是拐點</h4>
                <p>不只是 Qwen3.8-Max，之前發布的 Kimi K3 以及後續將發布的國產模型，都說明國產模型與頭部閉源模型的差距已非常小。Coding 和辦公，將是接下來半年的重點中的重點。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點配置</h4>
            <p>Qwen3.8-Max：2.4T 總參數、95B 激活參數、稀疏 MoE 架構、<strong>100 萬 Tokens 上下文</strong>、原生多模態——放在今天的模型裡，這已經是頂配級別。</p>
        </div>

        <div class="quote-box">
            <p>「兩年前，我們討論國產模型，還是能不能用、差距有多大。現在，我們已經開始把它們和全球最強的模型放在一起，比較能力、價格和真實任務的完成效果。這個變化來得比我預期得要快。」</p>
            <cite>— AI Maker 測評者</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這次 Qwen 把辦公放到除 Coding 之外第二重要的位置。OpenAI Codex、Anthropic Claude Cowork 都在遷移到專業知識工作場景（文件處理、研究、分析、交付）。國產模型競爭也從 Coding 逐漸進入白領工作場景。從業者心理也在轉變：不再預設落後，而是同等標準比較。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2024 年</div>
                <div class="timeline-title">國模早期階段</div>
                <div class="timeline-desc">討論國產模型問的是「能不能用、差距有多大」</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年初</div>
                <div class="timeline-title">Kimi K3 發布</div>
                <div class="timeline-desc">Kimi K3 發布，顯示國產模型能力大幅提升</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-08</div>
                <div class="timeline-title">Qwen3.8-Max 發布</div>
                <div class="timeline-desc">阿里巴巴發布 Qwen3.8-Max，2.4T 參數達到頂配</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-08</div>
                <div class="timeline-title">千問辦公發布</div>
                <div class="timeline-desc">阿里發布千問辦公，進軍白領工作場景</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來半年</div>
                <div class="timeline-title">Coding + 辦公競爭升級</div>
                <div class="timeline-desc">國內外模型將在 Coding 和辦公主務上激烈競爭</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>Qwen3.8-Max</th>
                    <th>對標頂級閉源模型</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>總參數</td>
                    <td class="highlight-col">2.4T</td>
                    <td>同量級</td>
                </tr>
                <tr>
                    <td>上下文窗口</td>
                    <td class="highlight-col">100 萬 Tokens</td>
                    <td>相近水平</td>
                </tr>
                <tr>
                    <td>多模態</td>
                    <td class="highlight-col">原生支持</td>
                    <td>標配</td>
                </tr>
                <tr>
                    <td>開源/閉源</td>
                    <td class="highlight-col">開源</td>
                    <td>多為閉源</td>
                </tr>
                <tr>
                    <td>辦公能力</td>
                    <td>千問辦公加持</td>
                    <td class="highlight-col">Claude Cowork、Codex 競爭</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '對阿里新模型 Qwen3.8-Max 的真實評價。',
    'h1': '對阿里新模型 Qwen3.8-Max<br>的真實評價',
    'subtitle': '2.4T 參數、性價比碾壓——國產模型拐點已至',
    'source_url': 'https://mp.weixin.qq.com/s/u5K18wwIeerm2-huxaiGDA',
    'source_name': '微信公眾號',
    'pub_date': '2026-08-05',
    'img_alt': '對阿里新模型 Qwen3.8-Max 的真實評價',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260805_135028',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
