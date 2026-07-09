import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-06</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>雲端安全公司 Sysdig 首次記錄到由 AI 代理完全自主執行的勒索軟件攻擊「JadePuffer」，AI 負責從偵察到加密的所有技術工作，但人類仍在背後操控目標選擇與基礎設施。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>AI 代理自主執行</h4>
                <p>JadePuffer 是首個被完整記錄的 AI 驅動勒索軟件攻擊。AI 代理獨立完成偵察、憑證竊取、橫向移動、檔案加密及勒索信撰寫等全部流程，無需人類技術介入。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚙️</div>
            <div class="tech-card-content">
                <h4>利用 Langflow 漏洞</h4>
                <p>攻擊者利用開源工具 Langflow 的 CVE-2025-3248 漏洞（未經認證的遠端程式執行漏洞）入侵目標系統，這是首次記錄到 AI 代理利用此類漏洞發動攻擊。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🛡️</div>
            <div class="tech-card-content">
                <h4>人類仍是幕後推手</h4>
                <p>Sysdig 高級威脅研究總監 Michael Clark 強調，雖然 AI 負責技術執行，但人類仍負責設定目標、提供命令控制伺服器、選擇受害者等關鍵決策。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚡</div>
            <div class="tech-card-content">
                <h4>自我修復能力</h4>
                <p>攻擊過程中，AI 代理曾遇到系統錯誤，並在 31 秒內自動修復問題，展現出類似人類黑客的適應能力與解決問題能力。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>JadePuffer 並未使用新穎或複雜的技術，但 AI 模型如何組織和執行攻擊才是關鍵——這顯示未來勒索軟件攻擊的門檻已大幅降低，任何人都能發動類似攻擊。</p>
        </div>

        <div class="quote-box">
            <p>「JadePuffer 是一個警告信號。隨著 AI 代理技術普及，發動勒索軟件攻擊的技術門檻已大幅降低。」</p>
            <cite>— Michael Clark，Sysdig 高級威脅研究總監</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這次攻擊被視為網絡安全領域的重要警示。企業必須加強對 AI 威脅的防範，密切關注代理型 AI（Agentic AI）的安全風險。Sysdig 研究團隊指出，攻擊過程中留下的程式碼痕跡具有 AI 生成特徵，是未來判斷攻擊來源的重要線索。隨著 AI 技術持續發展，這類自主攻擊的數量預計將持續增加。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026-06 底</div>
                <div class="timeline-title">JadePuffer 攻擊發生</div>
                <div class="timeline-desc">AI 代理 JadePuffer 發動首次完整記錄的 AI 驅動勒索軟件攻擊</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-06</div>
                <div class="timeline-title">Sysdig 發布研究報告</div>
                <div class="timeline-desc">Sysdig 威脅研究團隊發布報告，首次記錄「代理型勒索軟件」案例</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">同日</div>
                <div class="timeline-title">TechCrunch 報導</div>
                <div class="timeline-desc">TechCrunch 發布新聞報導，分析 AI 驅動網絡攻擊的時代意義</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">同日</div>
                <div class="timeline-title">CyberScoop 專訪</div>
                <div class="timeline-desc">Michael Clark 接受 CyberScoop 訪問，澄清人類在攻擊中的角色</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">攻擊門檻降低</div>
                <div class="timeline-desc">專家預測類似 AI 自主攻擊將持續增加，企業需加強防範</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>傳統勒索軟件</th>
                    <th>AI 代理勒索軟件（JadePuffer）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>技術執行</td>
                    <td>人類黑客手動執行</td>
                    <td class="highlight-col">AI 代理自主執行</td>
                </tr>
                <tr>
                    <td>偵察與規劃</td>
                    <td>人類主導</td>
                    <td class="highlight-col">AI 代理自主偵察</td>
                </tr>
                <tr>
                    <td>橫向移動</td>
                    <td>人類操作</td>
                    <td class="highlight-col">AI 代理自動移動</td>
                </tr>
                <tr>
                    <td>勒索信撰寫</td>
                    <td>人類撰寫</td>
                    <td class="highlight-col">AI 代理自動生成</td>
                </tr>
                <tr>
                    <td>適應障礙能力</td>
                    <td>需要人類干預</td>
                    <td class="highlight-col">AI 代理 31 秒自我修復</td>
                </tr>
                <tr>
                    <td>攻擊門檻</td>
                    <td>需要專業技術知識</td>
                    <td class="highlight-col">門檻大幅降低</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '全球首例 AI 驅動勒索軟件攻擊　仍有人類幕後操控 | TechCrunch',
    'h1': '全球首例 AI 驅動勒索軟件攻擊<br>仍有人類幕後操控',
    'subtitle': 'Sysdig 首次記錄 AI 代理勒索軟件 JadePuffer，技術執行全程自主但人類仍是幕後推手',
    'source_url': 'https://techcrunch.com/2026/07/06/the-first-ai-run-ransomware-attack-still-needed-a-human/',
    'source_name': 'TechCrunch',
    'pub_date': '2026-07-06',
    'img_alt': 'AI 代理勒索軟件攻擊示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260709_083800',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print("❌ 錯誤：")
    for e in errors:
        print(f"   {e}")
