import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.engadget.com/2216473/google-notebooklm-is-now-gemini-notebook/" target="_blank">Engadget</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-22</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Google 將深度研究工具 NotebookLM 改名為「Gemini Notebook」，品牌正式與 Gemini 系列 AI 工具統一，並新增原生程式碼執行能力，用戶規模已超過 3,000 萬人。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔄</div>
            <div class="tech-card-content">
                <h4>品牌統一：NotebookLM → Gemini Notebook</h4>
                <p>Google 宣布將深耕研究工具 NotebookLM 更名為「Gemini Notebook」，目的與旗下其他 AI 工具（如 Gemini App、Gemini Advanced）保持品牌一致性。此舉並不意外，因為 Google 在今年四月已將 NotebookLM 完全整合至 Gemini App。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💻</div>
            <div class="tech-card-content">
                <h4>新功能：原生程式碼執行能力</h4>
                <p>配合更名，Gemini Notebook 新增程式碼編寫與執行功能，用戶可基於研究資料庫中的數據，直接在平台內進行複雜的數據分析，無需切換至外部環境，大幅提升研究效率。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>即將推出：整合 Google 搜尋 AI 模式</h4>
                <p>Google 表示將很快支援將 Gemini Notebook 內的筆記本無縫帶入一般 Google 搜尋的 AI 模式，進一步打通研究與搜尋的工作流程，讓研究資料與網路搜尋深度結合。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>用戶規模</h4>
                <p>Gemini Notebook 目前已擁有超過 <strong>3,000 萬</strong>名個人用戶，以及超過 <strong>60 萬</strong>個組織用戶，顯示其在研究與知識管理領域的高度採用率。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>NotebookLM 改名後仍是獨立產品，但品牌正式與 Gemini 生態系統統一。隨著原生程式碼能力與 Google 搜尋的深度整合，預計將吸引更多研究人員與知識工作者。</p>
        </div>

        <div class="quote-box">
            <p>「From today, the service will be known as Gemini Notebook, even if it remains a standalone product from the rest of Gemini — at least for now.」</p>
            <cite>— Engadget</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Gemini Notebook 的品牌統一與功能升級，顯示 Google 正積極將所有 AI 產品線整合至 Gemini 生態系統。隨著原生程式碼能力與 Google 搜尋的深度整合，預計將吸引更多研究人員與知識工作者使用此工具，進一步鞏固 Google 在 AI 領域的競爭優勢。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2025 年中</div>
                <div class="timeline-title">NotebookLM 獨立運行</div>
                <div class="timeline-desc">NotebookLM 作為 Google 旗下深度研究工具獨立運行，專注於 AI 輔助研究功能</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 4 月</div>
                <div class="timeline-title">整合至 Gemini App</div>
                <div class="timeline-desc">Google 將 NotebookLM 完全整合至 Gemini App，品牌開始統一</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月 22 日</div>
                <div class="timeline-title">正式改名 Gemini Notebook</div>
                <div class="timeline-desc">品牌統一為 Gemini Notebook，新增原生程式碼執行能力</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">即將推出</div>
                <div class="timeline-title">整合 Google 搜尋 AI 模式</div>
                <div class="timeline-desc">Gemini Notebook 筆記本將可無縫帶入 Google 搜尋 AI 模式</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來規劃</div>
                <div class="timeline-title">持續擴展 Gemini 生態</div>
                <div class="timeline-desc">Gemini Notebook 將作為 Gemini 生態核心成員，與其他 Gemini 工具深度整合</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>NotebookLM（舊）</th>
                    <th>Gemini Notebook（新）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>品牌名稱</td>
                    <td>NotebookLM</td>
                    <td class="highlight-col">Gemini Notebook</td>
                </tr>
                <tr>
                    <td>品牌定位</td>
                    <td>獨立產品</td>
                    <td class="highlight-col">Gemini 生態一員</td>
                </tr>
                <tr>
                    <td>程式碼執行</td>
                    <td>❌ 不支援</td>
                    <td class="highlight-col">✅ 原生支援</td>
                </tr>
                <tr>
                    <td>Google 搜尋整合</td>
                    <td>❌ 無</td>
                    <td class="highlight-col">✅ 規劃中</td>
                </tr>
                <tr>
                    <td>用戶規模</td>
                    <td>—</td>
                    <td class="highlight-col">3,000萬+ 個人 / 60萬+ 組織</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Google NotebookLM 改名為 Gemini Notebook | Engadget',
    'h1':          'Google NotebookLM 改名為<br>Gemini Notebook',
    'subtitle':    '品牌統一、功能升級，3000萬用戶的研究神器正式納入 Gemini 生態',
    'source_url':  'https://www.engadget.com/2216473/google-notebooklm-is-now-gemini-notebook/',
    'source_name': 'Engadget',
    'pub_date':    '2026-07-22',
    'img_alt':     'Google NotebookLM 改名為 Gemini Notebook',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260722_084827',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print(f"❌ HTML 生成失敗：{errors}")
