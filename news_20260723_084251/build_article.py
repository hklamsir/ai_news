import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/07/08/these-ai-startups-are-growing-revenue-at-faster-and-faster-rates/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-08</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>AI 新創公司正以史上罕見的速度催生營收里程碑，Anthropic、Sierra、Mercor 相繼公布爆炸性增長數據，揭示 AI 產業已進入「營收加速膨脹」的新階段。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>Anthropic：470 億美元營收運行率</h4>
                <p>2026 年 5 月底宣布營收運行率突破 470 億美元，距離上次超越 300 億美元僅不到兩個月。2025 年 7 月為 40 億美元，約一年時間增長近 12 倍，被形容為「史上罕見」的增速。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💬</div>
            <div class="tech-card-content">
                <h4>Sierra：企業客服 AI 代理黑馬</h4>
                <p>Sierra 專門為企業構建客服 AI 代理。首個 1 億美元 ARR 花了 7 個季度，但再增加另一個 1 億美元 ARR 只用了 2 個季度，增速同樣驚人。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🚀</div>
            <div class="tech-card-content">
                <h4>Mercor：三年不到突破 20 億美元</h4>
                <p>Mercor 僱用領域專家訓練 AI 模型，2026 年 6 月宣布 Gross Annualized Revenue 突破 20 億美元，距離突破 10 億美元僅 4 個月。公司成立不足三年。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📈</div>
            <div class="tech-card-content">
                <h4>共同趨勢：所有公司營收增長都在加速</h4>
                <p>TechCrunch 指出，名單上所有新創公司不論如何定義「增長」，都報告其營收增長正在加速，凸顯 AI 產業已進入一個由收入爆炸性增長定義的新時代。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點數據</h4>
            <ul>
                <li><strong>Anthropic</strong>：470 億美元營收運行率（2026年5月）</li>
                <li><strong>Sierra</strong>：第二個 1 億美元 ARR 僅用 2 季度</li>
                <li><strong>Mercor</strong>：20 億美元年度營收（成立不足三年）</li>
            </ul>
        </div>

        <div class="quote-box">
            <p>「In recent months, this model maker's revenue has been at such a historic velocity that it has mesmerized the entire AI sector.」</p>
            <cite>— TechCrunch 描述 Anthropic 營收增速</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Anthropic 的 470 億美元營收運行率距離兩個月前的 300 億美元已大幅跳升，增速絲毫未見放緩。AI 產業正進入一個由收入爆炸性增長定義的新時代，投資人與觀察家均在密切關注這波熱潮是否能持續。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2025 年 7 月</div>
                <div class="timeline-title">Anthropic 40 億美元運行率</div>
                <div class="timeline-desc">Anthropic 營收運行率達到 40 億美元</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年底</div>
                <div class="timeline-title">Anthropic 90 億美元運行率</div>
                <div class="timeline-desc">半年內從 40 億增至 90 億美元</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 3 月</div>
                <div class="timeline-title">Anthropic 300 億美元運行率</div>
                <div class="timeline-desc">再增至 300 億美元，距離 90 億僅數月</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 5 月</div>
                <div class="timeline-title">Anthropic 470 億美元運行率</div>
                <div class="timeline-desc">不到兩個月從 300 億增至 470 億美元</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 5 月底</div>
                <div class="timeline-title">Sierra 公布營收里程碑</div>
                <div class="timeline-desc">共同創辦人 Bret Taylor 宣布第二個 1 億美元 ARR</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">Mercor 突破 20 億美元</div>
                <div class="timeline-desc">距離 10 億美元僅 4 個月，公司成立不足三年</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>公司</th>
                    <th>營收里程碑</th>
                    <th>達成時間</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Anthropic</td>
                    <td>40 億 → 470 億美元運行率</td>
                    <td class="highlight-col">約 10 個月（12 倍增長）</td>
                </tr>
                <tr>
                    <td>Sierra</td>
                    <td>第二個 1 億美元 ARR</td>
                    <td class="highlight-col">僅 2 季度（首個為 7 季度）</td>
                </tr>
                <tr>
                    <td>Mercor</td>
                    <td>10 億 → 20 億美元</td>
                    <td class="highlight-col">僅 4 個月</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'AI 新創公司營收增長正在加速 | TechCrunch',
    'h1':          'AI 新創公司<br>營收增長正在加速',
    'subtitle':    'Anthropic、Sierra、Mercor 相繼公布爆炸性增長數據，揭示 AI 產業進入新階段',
    'source_url':  'https://techcrunch.com/2026/07/08/these-ai-startups-are-growing-revenue-at-faster-and-faster-rates/',
    'source_name': 'TechCrunch',
    'pub_date':    '2026-07-08',
    'img_alt':     'AI 新創公司營收加速增長示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260723_084251',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
