#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3363518/72-hong-kong-professionals-use-ai-weekly-double-global-average-survey" target="_blank">SCMP 南華早報</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-10</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>香港科技大學調查發現，超過七成香港在職專業人士每週使用 AI 工具，比率達全球平均的兩倍，但基層員工對 AI 取代工作的焦慮感也更強。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>AI 採用率領先全球</h4>
                <p>72.7% 的受訪香港在職專業人士表示每周使用 AI 工具（每日或每週），比率是全球平均 31% 的兩倍多，反映香港打工仔對新技術的接受程度極高。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>生成式 AI 工具最受歡迎</h4>
                <p>ChatGPT、Copilot 和 Gemini 等生成式 AI 工具最被廣泛採用，81.7% 受訪者有使用，主要用於文件草擬、資訊摘要及創意工作輔助。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>基層員工焦慮感更深</h4>
                <p>調查發現不同職級員工對 AI 的看法存在差異，基層員工對 AI 可能取代其工作的焦慮感更高，管理層需關注如何緩解員工不安情緒。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📉</div>
            <div class="tech-card-content">
                <h4>進階應用使用率偏低</h4>
                <p>儘管普及率高，但只有約四分之一受訪者定期使用更高級的 AI 應用，如數據分析、圖像或影片生成，以及代理型 AI 系統。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點數據</h4>
            <p>香港專業人士 AI 週使用率達 <strong>72.7%</strong>，遠超全球平均 <strong>31%</strong>，但進階工具採用率僅約 <strong>25%</strong>。</p>
        </div>

        <div class="quote-box">
            <p>「香港打工仔的 AI 採用率領先全球，但如何從『普遍使用』邁向『深度應用』，將是企業提升競爭力的關鍵。」</p>
            <cite>— 香港科技大學調查研究團隊</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>香港在 AI 採用方面已領先全球，但未來挑戰在於如何提升進階工具的使用率。企業需要同時關注員工對 AI 取代的焦慮，特別是基層員工的心理狀態。管理層的開放態度與支持，對推動更深層次的 AI 應用至關重要。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 3-4 月</div>
                <div class="timeline-title">港科大进行调查</div>
                <div class="timeline-desc">香港科技大學訪問 3,722 名在職專業人士</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">受訪者年齡</div>
                <div class="timeline-title">30-49 歲為主</div>
                <div class="timeline-desc">超過六成受訪者年齡介乎 30 至 49 歲</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">畢馬威全球調查</div>
                <div class="timeline-desc">畢馬威（KPMG）發布全球平均 AI 使用率為 31%</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 8 月</div>
                <div class="timeline-title">研究結果公布</div>
                <div class="timeline-desc">港科大調查結果顯示香港比率達全球兩倍</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來趨勢</div>
                <div class="timeline-title">進階 AI 應用待推廣</div>
                <div class="timeline-desc">數據分析、代理型 AI 等進階工具使用率仍有待提升</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>香港</th>
                    <th>全球平均</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>每週 AI 使用率</td>
                    <td class="highlight-col">72.7%</td>
                    <td>31%</td>
                </tr>
                <tr>
                    <td>生成式 AI 工具使用率</td>
                    <td class="highlight-col">81.7%</td>
                    <td>—</td>
                </tr>
                <tr>
                    <td>進階 AI 應用使用率</td>
                    <td>~25%</td>
                    <td>—</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '72% 香港專業人士每週使用 AI　調查顯示比率達全球平均兩倍 | SCMP',
    'h1':          '72% 香港專業人士每週使用 AI<br>調查顯示比率達全球平均兩倍',
    'subtitle':    '港科大調查：香港在職專業人士 AI 採用率領先全球，但基層員工焦慮感更深',
    'source_url':  'https://www.scmp.com/news/hong-kong/hong-kong-economy/article/3363518/72-hong-kong-professionals-use-ai-weekly-double-global-average-survey',
    'source_name': 'SCMP 南華早報',
    'pub_date':    '2026-08-10',
    'img_alt':     '香港專業人士使用 AI 工作場景',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260811_085432',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 重建成功")
else:
    print(f"❌ HTML 重建失敗：{errors}")
    sys.exit(1)
