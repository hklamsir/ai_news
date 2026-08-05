import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.artificialintelligence-news.com/news/red-hat-nvidia-ibm-back-project-turning-ai-policy-into-code/" target="_blank">ArtificialIntelligence-News.com</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-04</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Red Hat 成立開源專案 asago，旨在將 AI 治理政策自動轉化為可部署的生產代碼，獲 NVIDIA、IBM、微軟、MIT、Alan Turing Institute 等重量級成員支持。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>asago 的使命</h4>
                <p>asago（AI Safety and Governance Orchestration）是一套自動化、可審計的工作流程，連接工程與合規團隊之間「碎片化的步驟、工具和需求」。在 EU AI Act 正式生效的背景下，解決了「要么拖慢 AI 創新、要么讓 AI 代理無監管運行」的兩難困境。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💡</div>
            <div class="tech-card-content">
                <h4>重量級參與陣容</h4>
                <p>Red Hat（主導）、IBM Research、NVIDIA Corp.、Microsoft、Brave Software、Alquimia AI、EvalEval 聯盟、MIT Lincoln Laboratory、North Carolina State University、Interdisciplinary Transformation University Austria、Alan Turing Institute。專案建基於 Red Hat 與 NVIDIA 在 Open Secure AI Alliance 中的前期工作，採用 Apache License 2.0 開源。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>業界痛點</h4>
                <p>現有做法依賴手動政策解讀和客製化腳本，在合規要求於不同團隊之間流轉時拖慢部署並引入錯誤。隨著企業從實驗性生成式 AI 走向長期運行生產的 AI 系統和自主代理，治理要求與工程師所需的測試、防護和基礎設施配置之間的鴻溝越來越大。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>四階段標準化流程</h4>
                <p>1️⃣ 政策解析：映射至 NIST AI Risk Management Framework、OWASP Top 10 for LLM Applications、EU AI Act（使用 IBM AI Risk Atlas）<br>2️⃣ 風險評估<br>3️⃣ 安全保障建議<br>4️⃣ 部署配置輸出。目標是讓審計人員能將生產控制措施追溯到具體政策條款。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>asago 目前處於 formation 階段，GitHub 倉庫已開放給開發者、學術研究人員和企業早期採用者參與。Stuart Battersby（Red Hat AI 安全與模型評估架構師）呼籲全球不同司法管轄區的成員加入，確保 AI 安全觀點獲得最大覆蓋。</p>
        </div>

        <div class="quote-box">
            <p>「asago 是真正的協作開源努力，匯集了科技業、學術界和政府的利害關係人。我們鼓勵更多 collaborator 加入這個社群驅動的計畫，特別是來自全球不同司法管轄區的成員，以確保 AI 安全的觀點能獲得最大覆蓋。」</p>
            <cite>— Stuart Battersby，Red Hat AI 安全與模型評估架構師</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>asago 的出現標誌著 AI 治理從手動時代走向自動化流程的關鍵轉折。隨著監管要求日益嚴格（如 EU AI Act 已正式生效），將政策直接轉化為可執行代碼的能力將成為企業 AI 部署的核心竞争力。此開源專案有機會為整個產業建立新的治理標準。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026-08-04</div>
                <div class="timeline-title">asago 專案宣佈</div>
                <div class="timeline-desc">Red Hat 宣佈成立 asago，獲得多家重量級機構支持</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">Formation 階段</div>
                <div class="timeline-title">開放協作</div>
                <div class="timeline-desc">GitHub 倉庫開放給開發者、學術研究人員和企業早期採用者</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">前期基礎</div>
                <div class="timeline-title">Open Secure AI Alliance</div>
                <div class="timeline-desc">asago 建基於 Red Hat 與 NVIDIA 在 Open Secure AI Alliance 中的前期工作</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">EU AI Act 生效</div>
                <div class="timeline-desc">歐盟 AI 法規正式生效，企業面臨更嚴格的合規要求</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未来</div>
                <div class="timeline-title">持續發展</div>
                <div class="timeline-desc">持續歡迎全球不同司法管轄區的 collaborator 加入</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>對比維度</th>
                    <th>傳統方式（手動）</th>
                    <th>asago（自動化）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>政策解讀</td>
                    <td>人工逐一解讀，速度慢</td>
                    <td class="highlight-col">自動映射至 NIST/EU AI Act 等框架</td>
                </tr>
                <tr>
                    <td>部署速度</td>
                    <td>合規與工程來回折騰，延遲數週</td>
                    <td class="highlight-col">直接輸出可部署配置</td>
                </tr>
                <tr>
                    <td>審計追蹤</td>
                    <td>難以追溯控制措施對應的政策條款</td>
                    <td class="highlight-col">完整審計軌跡，連結每個控制到具體條款</td>
                </tr>
                <tr>
                    <td>錯誤風險</td>
                    <td>手動腳本易引入人為錯誤</td>
                    <td class="highlight-col">自動化流程，減少人為錯誤</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'Red Hat, NVIDIA, IBM back project turning AI policy into code',
    'h1': 'Red Hat, NVIDIA, IBM back project<br>turning AI policy into code',
    'subtitle': 'asago 開源專案將 AI 治理政策自動轉化為生產代碼，獲多家科技巨頭與學術機構支持',
    'source_url': 'https://www.artificialintelligence-news.com/news/red-hat-nvidia-ibm-back-project-turning-ai-policy-into-code/',
    'source_name': 'ArtificialIntelligence-News.com',
    'pub_date': '2026-08-04',
    'img_alt': 'Red Hat, NVIDIA, IBM back project turning AI policy into code',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260805_110629',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
