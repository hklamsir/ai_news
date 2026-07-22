import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://bun.com/blog/bun-in-rust" target="_blank">Bun Blog</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-22</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Bun 宣佈將 53.5 萬行核心程式碼從 Zig 全面遷移至 Rust。一位工程師借助 Fable 與 Claude Code，在 11 天內完成這項龐大工程，並確保所有測試通過，展示了 AI 輔助程式設計的重大突破。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🦀</div>
            <div class="tech-card-content">
                <h4>為何選擇 Rust？</h4>
                <p>Bun 團隊表示，過去大量的 bug 來自記憶體錯誤，包括使用後釋放（use-after-free）、雙重釋放（double-free）以及錯誤路徑中忘記釋放記憶體。在 Safe Rust 中，這些都是<strong>編譯器錯誤</strong>，而非執行期問題，能從源頭消滅整類錯誤。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>最小風險重寫策略</h4>
                <p>歷史上重寫往往是災難的開始。Bun 採用「機械式移植」：將每個 <code>.zig</code> 檔案對應至 Rust 的 <code>.rs</code> 檔案，採用最少的行為變更，並使用 Bun 既有的完整測試套件驗證正確性，確保新舊版本行為一致。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>AI 輔助：50 個動態工作流 × 11 天</h4>
                <p>整個遷移使用約 50 個動態工作流，每個工作流循環執行：生成移植指南、機械式移植程式碼、修補編譯器錯誤、確保子命令正常運作、執行完整測試套件、大規模重構清理，全部由一位工程師主導完成。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🚀</div>
            <div class="tech-card-content">
                <h4>Bun v1.4 新武器</h4>
                <p>Rust 重寫為 Bun v1.4 帶來更快速、更小、更低記憶體消耗的表現。工具鏈包括：<strong>Rust Borrow Checker</strong>（編譯期記憶體安全）、<strong>Miri</strong>（CI 執行動期檢測）、<strong>LeakSanitizer</strong>（記憶體洩漏檢測）、<strong>24/7 覆蓋導向模糊測試</strong>（專門針對 Parser）。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Bun 此次重寫規模達 535,496 行程式碼，傳統上需要一支工程師團隊花費約一年時間。藉助 AI 工具，一位工程師在 11 天內完成，展示了 AI 輔助程式設計的巨大潛力。</p>
        </div>

        <div class="quote-box">
            <p>「One engineer can do a lot more today than a year ago. [...] With 1 engineer using Fable & closely monitoring Claude Code, we went from start to 100% of the test suite passing on all platforms in 11 days.」</p>
            <cite>— Bun Blog</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Bun 的 Rust 重寫展示了 AI 輔助程式設計在大型重構專案中的驚人潛力。一個工程師在 11 天內完成了過去需要團隊一年的工作，這預示著「單兵作戰」的大型軟體重構將會越來越常見，也可能徹底改變軟體工程的協作模式與工期估算方式。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">起點</div>
                <div class="timeline-title">Bun 現存規模確認</div>
                <div class="timeline-desc">Bun 含註釋共 535,496 行 Zig 程式碼</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第 1-2 天</div>
                <div class="timeline-title">生成移植指南</div>
                <div class="timeline-desc">建立 Zig → Rust 的 PORTING.md 與 LIFETIMES.tsv 映射文件</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第 3-8 天</div>
                <div class="timeline-title">機械式移植與編譯器錯誤修補</div>
                <div class="timeline-desc">每個 .zig 檔案移植至 .rs，修補所有編譯器錯誤，讓子命令正常運作</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第 9-10 天</div>
                <div class="timeline-title">完整測試套件通過</div>
                <div class="timeline-desc">Bun 完整測試套件在所有平台（macOS、Windows、Linux）全部通過</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第 11 天</div>
                <div class="timeline-title">大規模重構清理</div>
                <div class="timeline-desc">進行大規模重構與清理，達到團隊代碼品質標準</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>傳統重寫模式</th>
                    <th>Bun Rust 重寫（AI 輔助）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>所需工程師</td>
                    <td>團隊（數人）</td>
                    <td class="highlight-col">1 人</td>
                </tr>
                <tr>
                    <td>預計工期</td>
                    <td>約 1 年</td>
                    <td class="highlight-col">11 天</td>
                </tr>
                <tr>
                    <td>程式碼規模</td>
                    <td colspan="2" class="highlight-col">535,496 行</td>
                </tr>
                <tr>
                    <td>測試策略</td>
                    <td>重新編寫測試</td>
                    <td class="highlight-col">沿用原有測試套件</td>
                </tr>
                <tr>
                    <td>記憶體安全保障</td>
                    <td>依賴規範與測試</td>
                    <td class="highlight-col">Rust 編譯器強制保證</td>
                </tr>
                <tr>
                    <td>主要工具</td>
                    <td>手動編程</td>
                    <td class="highlight-col">Fable + Claude Code</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Bun 宣佈使用 Rust 重寫　1工程師11天完成53萬行遷移 | Bun Blog',
    'h1':          'Bun 宣佈使用\nRust 重寫核心',
    'subtitle':    '53萬行 Zig 程式碼全面遷移至 Rust，一位工程師借助 AI 工具僅用 11 天完成',
    'source_url':  'https://bun.com/blog/bun-in-rust',
    'source_name': 'Bun Blog',
    'pub_date':    '2026-07-22',
    'img_alt':     'Bun 宣佈使用 Rust 重寫核心，1工程師11天完成53萬行遷移',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260722_210656',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print(f"❌ HTML 生成失敗：{errors}")
