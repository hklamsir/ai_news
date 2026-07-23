import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.ithome.com.tw/news/177477" target="_blank">iThome</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-21</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>資安業者 Pillar 披露 Cursor、OpenAI Codex CLI、Google Gemini CLI 等熱門 AI 程式代理存在沙箱繞過漏洞，AI 可透過工作區檔案與 Docker 間接取得主機操作能力，多數漏洞已陸續修補。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🐍</div>
            <div class="tech-card-content">
                <h4>Cursor：Python 執行檔置換漏洞</h4>
                <p>代理可更換專案內 Python 虛擬環境的執行檔，Cursor 內建的 Microsoft Python 擴充套件會在沙箱外執行該檔案，使攻擊指令取得使用者權限並修改專案外檔案。影響 3.1.2 以前版本，已修補。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚙️</div>
            <div class="tech-card-content">
                <h4>Cursor：CVE-2026-48124 自動執行漏洞</h4>
                <p>惡意設定檔可在代理作業結束時執行本機命令，過程不另行要求使用者核准。已影響 Cursor Desktop 2.4.37，於 3.0.0 修補。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🐳</div>
            <div class="tech-card-content">
                <h4>Docker：macOS 特權容器越界</h4>
                <p>在 Auto-Run Sandbox 模式下，代理可能啟動特權模式容器，透過 VirtioFS 機制取得使用者家目錄讀寫能力，並以使用者權限執行主機命令，全程無額外權限提示。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔓</div>
            <div class="tech-card-content">
                <h4>Codex CLI：安全命令豁免名單繞過</h4>
                <p>系統只依命令名稱判斷風險，未完整檢查附帶參數及實際作用，使看似只讀取的 Git 命令能改寫設定並在後續操作時執行外部程式。已於 Codex CLI 0.95.0 修補。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 受影響產品與修補狀態</h4>
            <ul>
                <li><strong>Cursor 3.1.2 以前</strong>：Python 執行檔置換漏洞 → 3.1.2 已修補</li>
                <li><strong>Cursor Desktop 2.4.37</strong>：CVE-2026-48124 自動執行漏洞 → 3.0.0 已修補</li>
                <li><strong>OpenAI Codex CLI</strong>：安全命令豁免繞過 → 0.95.0 已修補</li>
                <li><strong>Google Gemini CLI</strong>：Pillar 研究中，細節待公布</li>
            </ul>
        </div>

        <div class="quote-box">
            <p>「代理建立的設定檔應一律視為未受信任內容，相關指令也應套用與代理相同的權限檢查及使用者核准機制。」</p>
            <cite>— Pillar 研究團隊</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>此系列漏洞揭示了 AI 程式代理在安全架構上的根本性挑戰：沙箱隔離與開發工具便利性之間存在信任邊界模糊的問題。隨著 AI 代理被廣泛用於實際開發工作，如何確保代理產生的設定檔不會被濫用，將是業界必須面對的重要課題。Pillar 建議所有代理建立的設定檔應強制經過權限檢查與使用者核准機制。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">研究期間</div>
                <div class="timeline-title">Pillar 發現漏洞鏈</div>
                <div class="timeline-desc">Pillar 安全研究團隊發現 Cursor、Codex CLI 等工具的沙箱繞過途徑</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">漏洞披露</div>
                <div class="timeline-title">Pillar 公開研究</div>
                <div class="timeline-desc">Pillar 發布「The Week of Sandbox Escapes」安全研究報告</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-21</div>
                <div class="timeline-title">iThome 報導</div>
                <div class="timeline-desc">台灣資安專業媒體 iThome 率先跟進報導此安全事件</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">已修補</div>
                <div class="timeline-title">各廠商陸續修復</div>
                <div class="timeline-desc">Cursor 3.1.2、3.0.0 及 Codex CLI 0.95.0 相繼發布修補版本</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>工具</th>
                    <th>漏洞類型</th>
                    <th>修補版本</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Cursor</td>
                    <td>Python 執行檔置換</td>
                    <td class="highlight-col">3.1.2 已修補</td>
                </tr>
                <tr>
                    <td>Cursor</td>
                    <td>CVE-2026-48124 自動執行</td>
                    <td class="highlight-col">3.0.0 已修補</td>
                </tr>
                <tr>
                    <td>OpenAI Codex CLI</td>
                    <td>安全命令豁免繞過</td>
                    <td class="highlight-col">0.95.0 已修補</td>
                </tr>
                <tr>
                    <td>Google Gemini CLI</td>
                    <td>研究披露中</td>
                    <td>待修補</td>
                </tr>
                <tr>
                    <td>Antigravity</td>
                    <td>研究披露中</td>
                    <td>待修補</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Cursor等AI程式代理曝沙箱繞過風險，工作區檔案可透過開發工具與Docker越界執行',
    'h1':          'Cursor等AI程式代理<br>曝沙箱繞過風險',
    'subtitle':    '資安研究披露：AI代理可透過工作區檔案與Docker越界執行，Cursor、Codex CLI等已陸續修補',
    'source_url':  'https://www.ithome.com.tw/news/177477',
    'source_name': 'iThome',
    'pub_date':    '2026-07-21',
    'img_alt':     'AI 程式代理沙箱繞過漏洞示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260723_182359',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
