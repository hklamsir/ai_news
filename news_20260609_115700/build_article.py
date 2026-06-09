import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.engadget.com/big-tech/what-to-expect-from-wwdc-2026-110000086.html" target="_blank">Engadget</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-09</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>WWDC 2026 是 Tim Cook 最後一次以 CEO 身份主持的 WWDC，主軸是 Siri AI 革新和 iOS 27，Apple 終於準備好展示與 ChatGPT 和 Gemini 競爭的新版 Siri。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>Siri 大革新：AI 助手時代來臨</h4>
                <p>經過兩年多的承諾與延遲，Apple 終於在 WWDC 2026 展示真正 AI 化的 Siri。Apple 承認在 AI 時代用戶對 Siri 的期望已大幅提高，這次革新包含：</p>
                <ul>
                    <li><strong>Google Gemini 加持</strong>：Apple 與 Google 合作，採用 Gemini 模型系列為 Apple Foundation Models 提供動力</li>
                    <li><strong>獨立 Siri App</strong>：新版 Siri 不只嵌入系統，還會以獨立 App 形式運行</li>
                    <li><strong>更強對話能力</strong>：能理解上下文、處理多步驟任務、跨 App 互動</li>
                    <li><strong>視覺智能整合</strong>：支援 Visual Intelligence 功能</li>
                </ul>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📱</div>
            <div class="tech-card-content">
                <h4>iOS 27 其他重點更新</h4>
                <p>除了 Siri 革新，iOS 27 還帶來多項實用更新：</p>
                <ul>
                    <li><strong>相機 App 重新設計</strong>：可自訂相機控制、新增自訂 widgets</li>
                    <li><strong>Safari 分頁管理</strong>：加入 Apple Intelligence 驅動的 Tab 管理功能</li>
                    <li><strong>一鍵密碼更新</strong>：快速更新密碼</li>
                    <li><strong>跨 App 上下文感知</strong>：能在不同 App 之間共享上下文</li>
                    <li><strong>Messages AI 回覆建議</strong>：AI 生成的快速回覆</li>
                    <li><strong>電話 App 進化</strong>：通話中可從 Mail、Messages 等 App 提取相關資訊</li>
                    <li><strong>第三方 AI 模型選擇</strong>：用戶可選擇用哪家 AI 模型驅動 Apple Intelligence 功能</li>
                </ul>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💡</div>
            <div class="tech-card-content">
                <h4>設計與其他更新</h4>
                <p>Liquid Glass 設計語言持續沿用，但用戶可選擇淡化或凸顯其元素。此外還有 Apple Wallet 分帳功能、Weather App 新增「條件」面板、Image Playground 和 Genmoji 更新等。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">👔</div>
            <div class="tech-card-content">
                <h4>Tim Cook 最後一屆 WWDC</h4>
                <p>這是 Tim Cook 作為 Apple CEO 的最後一屆 WWDC，他將於 9 月 1 日將 CEO 職位交棒給硬件工程高級副總裁 John Ternus。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Apple 兩年前就承諾 AI 版的 Siri，但多次延遲交付，還因此面臨 2.5 億美元的集體訴訟（Apple 未承認任何過錯）。這次與 Google Gemini 的合作，顯示 Apple 在 AI 競賽中選擇借力而非硬拚。</p>
        </div>

        <div class="quote-box">
            <p>「Apple 承認在 AI 時代用戶對 Siri 的期望已大幅提高，這次終於準備好展示與 ChatGPT 和 Gemini 競爭的新版 Siri。」</p>
            <cite>— Engadget</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>WWDC 2026 被視為近年來最重要的 Apple 開發者大會。Siri 能否真正與 ChatGPT 和 Gemini 競爭，將是業界關注的焦點。Tim Cook 的告別加上 AI  Siri 的正式亮相，讓這屆 WWDC 別具意義。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2024 年</div>
                <div class="timeline-title">Apple 首次承諾 AI Siri</div>
                <div class="timeline-desc">Apple 在 WWDC 2024 首次承諾推出 AI 版 Siri，但未能如期交付</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">延遲交付 + 集體訴訟</div>
                <div class="timeline-desc">Siri 升級再次延遲，Apple 達成 2.5 億美元集體訴訟和解</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月 8 日</div>
                <div class="timeline-title">WWDC 2026 正式揭幕</div>
                <div class="timeline-desc">Tim Cook 最後一次以 CEO 身份主持，公布真正的 AI Siri</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月 8-12 日</div>
                <div class="timeline-title">WWDC 2026 開發者大會</div>
                <div class="timeline-desc">為期一週的開發者活動，展示 iOS 27、macOS 27 等新系統</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 9 月 1 日</div>
                <div class="timeline-title">Tim Cook 交棒</div>
                <div class="timeline-desc">John Ternus 正式接任 Apple CEO</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>比較項目</th>
                    <th>舊版 Siri</th>
                    <th>新版 AI Siri</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>對話能力</td>
                    <td>指令式互動</td>
                    <td class="highlight-col">理解上下文、多步驟任務</td>
                </tr>
                <tr>
                    <td>App 整合</td>
                    <td>系統嵌入</td>
                    <td class="highlight-col">獨立 App + 跨 App 互動</td>
                </tr>
                <tr>
                    <td>AI 模型</td>
                    <td>Apple 自家模型</td>
                    <td class="highlight-col">Google Gemini 加持</td>
                </tr>
                <tr>
                    <td>視覺智能</td>
                    <td>無</td>
                    <td class="highlight-col">支援 Visual Intelligence</td>
                </tr>
                <tr>
                    <td>用戶選擇</td>
                    <td>無</td>
                    <td class="highlight-col">可選第三方 AI 模型</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'WWDC 2026 懶人包：Siri 終於 AI 化！Tim Cook 告別之作',
    'h1':          'WWDC 2026 懶人包<br>Siri 終於 AI 化！',
    'subtitle':    'Tim Cook 告別之作：Google Gemini 加持、新版 Siri 獨立 App、iOS 27 全面更新',
    'source_url':  'https://www.engadget.com/big-tech/what-to-expect-from-wwdc-2026-110000086.html',
    'source_name': 'Engadget',
    'pub_date':    '2026-06-09',
    'img_alt':     'WWDC 2026 Siri AI 革新示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260609_115700',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print("錯誤：")
    for e in errors:
        print(f"  - {e}")