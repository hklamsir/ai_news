import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.hk01.com/%E7%A0%94%E6%95%B8%E6%89%80/60349936/ai%E6%90%B6%E9%A3%AF%E7%A2%97-22-%E4%BC%81%E6%A5%AD%E6%96%99%E6%B8%9B%E4%BA%BA%E6%89%8B-%E5%89%B5%E6%96%B0%E6%8A%80%E8%A1%93%E9%83%BD%E9%87%8D%E7%81%BD-%E9%8A%B7%E5%94%AE-pm%E5%B7%A8%E7%A8%AE%E6%9C%80%E5%AE%89%E5%85%A8" target="_blank">香港01</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-03</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要 + 深度優化</p>
        </div>

        <div class="alert-box">
            <h4>⚠️ 數據來源</h4>
            <p>數據來自畢馬威（KPMG）《2026香港就業市場展望》調查，訪問281名企業高管及專業人士（當中41%任職管理層），於2026年1月進行。</p>
        </div>

        <div class="quote-box">
            <p>「企業現時更側重推動收入增長和市場擴張，因此銷售和創收職位更受青睞。」</p>
            <cite>— 畢馬威《2026香港就業市場展望》</cite>
        </div>

        <h3>🎯 核心突破卡片</h3>
        <div class="tech-cards">
            <div class="tech-card">
                <div class="tech-card-icon">📊</div>
                <h4>22% 企業料減人手</h4>
                <p>22%受訪者預計所在企業今年員工人數將減少，較去年上升，首席級管理人員更高達29%。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🤖</div>
                <h4>67% 企業採用 AI</h4>
                <p>67%受訪者表示其企業正採用AI，較去年53%增加14個百分點，24%已廣泛應用AI，按年增兩倍。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">📉</div>
                <h4>編程行政職位跌 80-90%</h4>
                <p>大學畢業生全職職位空缺從8萬跌至3.1萬，編程、行政等容易被AI取代的職位跌幅最嚴重。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">💼</div>
                <h4>銷售/PM 工種最安全</h4>
                <p>有計劃增加人手的企業優先招聘銷售、項目經理等創收及業務營運職位。</p>
            </div>
        </div>

        <h3>📊 減人手重災行業 vs 安全工種</h3>
        <table class="comparison-table">
            <thead>
                <tr><th>類別</th><th>行業/職位</th><th>原因</th></tr>
            </thead>
            <tbody>
                <tr><td>🔴 重災區</td><td>工業、創新技術、專業服務</td><td class="highlight-col">25%+ 受訪者預期減人手</td></tr>
                <tr><td>🔴 重災區</td><td>財務、會計、人力資源</td><td class="highlight-col">自動化轉型 + 成本控制</td></tr>
                <tr><td>🟢 安全區</td><td>銷售、創收職位</td><td class="highlight-col">企業側重推動收入增長</td></tr>
                <tr><td>🟢 安全區</td><td>項目經理、營運分析師</td><td class="highlight-col">管理 AI 驅動複雜業務流程</td></tr>
                <tr><td>🟢 安全區</td><td>AI、雲端工程、網絡安全</td><td class="highlight-col">專業技術人才仍渴市</td></tr>
            </tbody>
        </table>

        <h3>📅 AI 應用趨勢時間軸</h3>
        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2022 年</div>
                <div class="timeline-title">大學畢業生職位空缺高峰</div>
                <div class="timeline-desc">大學畢業生全職職位空缺約 8 萬個，達到近期高峰。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">職位空缺跌至 3.1 萬</div>
                <div class="timeline-desc">編程、行政等容易被 AI 取代的初級職位跌幅達 80%-90%。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 1 月</div>
                <div class="timeline-title">KPMG 調查發布</div>
                <div class="timeline-desc">訪問281名企業高管，67%表示企業正採用 AI，22%預期減人手。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 Q4</div>
                <div class="timeline-title">人力推算中期更新</div>
                <div class="timeline-desc">當局將公布 AI 對本港整體勞工市場影響的分析結果。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年趨勢</div>
                <div class="timeline-title">47% 視 AI 為核心技能</div>
                <div class="timeline-desc">受訪者認為掌握並應用 AI 是職場核心要素，比例較去年增逾倍。</div>
            </div>
        </div>

        <h3>💰 薪酬趨勢</h3>
        <ul>
            <li><strong>63%</strong> 受訪者在 2025 年獲加薪（與2024年的62%相約）</li>
            <li><strong>50%</strong> 受訪者加薪幅度為 5% 或以下</li>
            <li><strong>74%</strong> 預期 2026 年人工不變或增長最多 5%</li>
            <li><strong>24%</strong> 預計人工加幅超過 5%</li>
        </ul>

        <div class="highlight-box">
            <h4>✨ 關鍵洞察</h4>
            <p>AI 浪潮下，香港就業市場出現明顯分化：一邊是創新技術、專業服務、財務會計等「重災區」正面臨自動化替代，另一邊是銷售、項目經理等與營收和業務管理相關的職位反而更受青睞。掌握 AI 技能已成為職場必需品，但僅有技術不夠——能推動收入增長的管理職能更安全。</p>
        </div>

        <div class="alert-box">
            <h4>⚠️ 打工仔啟示</h4>
            <p>想避開 AI 衝擊？優先考慮銷售、項目管理等創收及業務營運崗位，同時提升 AI 應用能力。技術崗位中，AI、雲端、網絡安全等專業技術人才仍屬稀缺。</p>
        </div>
"""

metadata = {
    'title': 'AI搶飯碗？22%企業料減人手　創新技術都重災？銷售/PM工種最安全',
    'h1': 'AI 搶飯碗？<br>22% 企業料減人手',
    'subtitle': '畢馬威調查：創新技術、專業服務成重災區，銷售、PM 工種最安全',
    'source_url': 'https://www.hk01.com/%E7%A0%94%E6%95%B8%E6%89%80/60349936/ai%E6%90%B6%E9%A3%AF%E7%A2%97-22-%E4%BC%81%E6%A5%AD%E6%96%99%E6%B8%9B%E4%BA%BA%E6%89%8B-%E5%89%B5%E6%96%B0%E6%8A%80%E8%A1%93%E9%83%BD%E9%87%8D%E7%81%BD-%E9%8A%B7%E5%94%AE-pm%E5%B7%A8%E7%A8%AE%E6%9C%80%E5%AE%89%E5%85%A8',
    'source_name': '香港01',
    'pub_date': '2026-06-03',
    'img_alt': 'AI 取代人類工作與安全工種圖解',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260603_152800',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")
