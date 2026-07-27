import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.scmp.com/tech/tech-war/article/3361711/chinas-kimi-k3-significantly-below-us-rivals-hacking-power-uk-us-study-shows" target="_blank">SCMP</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-27</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>英美聯合研究顯示，中国 Kimi K3 在網絡攻擊能力評估中總分僅 32.2%，遠低於美國頂尖模型平均 76.2%，且在 41 項任務中完全無法達成任意程式碼執行。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>Kimi K3 表現落後</h4>
                <p>Kimi K3 目前被視為中國最強大的大型語言模型，但在網絡攻擊能力評估中，表現「顯著低於最新前沿網絡能力模型」。研究機構透過 ExploitBench 公開基準測試來評估 AI 開發網絡安全漏洞利用程序的能力。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>詳細數據對比</h4>
                <p>Kimi K3 擊敗了中國對手智譜 AI 的 GLM-5.2（24.4%），但在國際比較中明顯落後於美國頂尖模型平均 76.2% 的成績。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>任意程式碼執行失敗</h4>
                <p>Kimi K3 在全部 41 項 ExploitBench 任務中，均未能達成任意程式碼執行（最高級別漏洞利用，可完全控制目標系統）。美國領先模型則在 20 項任務中達成此級別。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏛️</div>
            <div class="tech-card-content">
                <h4>研究機構背景</h4>
                <p>英國人工智能安全研究所（AISI）隸屬英國科學、創新和技術部；美國人工智能標準與創新中心（CAISI）隸屬美國商務部國家標準與技術研究院（NIST）。</p>
            </div>
        </div>


        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Kimi K3 總分 32.2% vs 美國頂尖模型平均 76.2%｜41 項任務中 0 次任意程式碼執行（美國模型 20 次）</p>
        </div>

        <div class="quote-box">
            <p>「Kimi K3 performs 'significantly below the most recent frontier cyber-capable models'」</p>
            <cite>— 英國 AISI 及美國 CAISI 聯合報告，2026-07-24</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>報告發布之際，正值華盛頓對中國開源人工智能迅速崛起感到日益焦慮。這項研究結果表明，儘管中國 AI 發展迅速，但在網絡安全領域的實際攻擊能力，與美國最先進模型仍有明顯差距。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026-07-17</div>
                <div class="timeline-title">WAIC 展示 Kimi K3</div>
                <div class="timeline-desc">Moonshot AI 在世界人工智能大會上展示 Kimi K3 模型</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-24</div>
                <div class="timeline-title">報告發布</div>
                <div class="timeline-desc">英國 AISI 及美國 CAISI 聯合發布 Kimi K3 網絡攻擊能力評估報告</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-27</div>
                <div class="timeline-title">SCMP 報導</div>
                <div class="timeline-desc">南華早報率先報導研究結果，引發業界關注</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來展望</div>
                <div class="timeline-title">持續追蹤</div>
                <div class="timeline-desc">研究機構將繼續監測中國 AI 模型的安全能力發展</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">長期影響</div>
                <div class="timeline-title">政策影響</div>
                <div class="timeline-desc">報告或影響各國對中國 AI 發展的政策制定</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>模型</th>
                    <th>總分</th>
                    <th>任意程式碼執行</th>
                    <th>來源</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Kimi K3</td>
                    <td class="highlight-col">32.2%</td>
                    <td>0/41 任務</td>
                    <td>中國 Moonshot AI</td>
                </tr>
                <tr>
                    <td>GLM-5.2</td>
                    <td>24.4%</td>
                    <td>—</td>
                    <td>中國智譜 AI</td>
                </tr>
                <tr>
                    <td>美國頂尖模型（平均）</td>
                    <td>76.2%</td>
                    <td>20/41 任務</td>
                    <td>美國（未具名）</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '中國 Kimi K3 網絡攻擊能力遠落後美國對手，研究顯示',
    'h1': '中國 Kimi K3 網絡攻擊能力<br>遠落後美國對手，研究顯示',
    'subtitle': 'Kimi K3 總分 32.2% 遠低於美國模型平均 76.2%',
    'source_url': 'https://www.scmp.com/tech/tech-war/article/3361711/chinas-kimi-k3-significantly-below-us-rivals-hacking-power-uk-us-study-shows',
    'source_name': 'SCMP',
    'pub_date': '2026-07-27',
    'img_alt': '中國 AI 模型 Kimi K3 網絡攻擊能力研究示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260727_084002',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
