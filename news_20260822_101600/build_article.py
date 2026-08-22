#!/usr/bin/env python3
import sys, os
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.zdnet.com/article/10-ways-ai-will-do-unprecedented-damage-in-2026-experts-warn" target="_blank">ZDNET</a></p>
            <p><strong>📅 發布日期</strong>：2026-01-25（原文）/ 2026-08-22（摘要）</p>
            <p><strong>🤖 處理方式</strong>：Tavily 內容擷取 + AI 繁體中文摘要</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>ZDNET 採訪七家網絡安全機構專家，整理出 2026 年 AI 網絡安全威脅的 10 個最重要面向，警告網絡威脅形勢將比 2025 年嚴峻得多。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🦠</div>
            <div class="tech-card-content">
                <h4>1. AI 惡意軟件大爆發</h4>
                <p>Fruitshell、Promptflux、PromptSteal 等惡意軟件利用 LLM 動態生成攻擊指令，能在檢測到人類用戶時休眠躲避分析，變得越來越自主。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>2. Agentic AI 成攻擊利器</h4>
                <p>Villager（被稱為中國版 Cobalt Strike）等 AI 原生攻擊工具快速崛起，威脅者開始用 AI 自動化整個攻擊生命週期。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎭</div>
            <div class="tech-card-content">
                <h4>3. 深偽求職：六分之一是假的</h4>
                <p>AI 生成候選人用合成身份和深偽面試視頻求職，16.8%（六分之一）候選人是假的，企業將陸續發現「入職」的員工從未真實存在。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💉</div>
            <div class="tech-card-content">
                <h4>4. Prompt Injection 攻擊激增</h4>
                <p>攻擊者操縱 AI 繞過安全協議執行隱藏指令，2026 年隨着 AI 普及將大幅增加，從概念驗證走向大規模數據盜取和破壞活動。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Google Mandiant 明確警告：「2026 年及之後，威脅行為者使用 AI 將從例外變成規範。」從 AI 輔助的社會工程到惡意軟件開發，AI 將全面提升攻擊的速度、範圍和效果。</p>
        </div>

        <div class="quote-box">
            <p>「攻擊者正在學習這項技術並設定門檻。」</p>
            <cite>— LastPass 高級首席分析師 Mike Kosak</cite>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">☁️</div>
            <div class="tech-card-content">
                <h4>5. 「寄生於雲端」攻擊興起</h4>
                <p>攻擊者將惡意流量通過可信雲提供商和 AI 平台 API 路由，讓傳統防火牆規則完全失效。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔑</div>
            <div class="tech-card-content">
                <h4>6. 身份盜用成主要目標</h4>
                <p>重點從「入侵」（hacking in）轉向「登入」（logging in），攻擊者利用合法系統 API 繞過加密機制，竊取密碼和瀏覽器 sessions。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌐</div>
            <div class="tech-card-content">
                <h4>7. 北韓 IT 工人雙線出擊</h4>
                <p>北韓 IT 工人不只賺取薪酬，更直接瞄準加密貨幣組織竊取加密貨幣，並利用僱主網絡訪問權限從事戰略間諜活動。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚔️</div>
            <div class="tech-card-content">
                <h4>8. 國家級行為者破壞西方利益</h4>
                <p>2026 年國家支持的攻擊者將更積極利用 AI 進行複合式攻擊，包括認知作戰、關鍵基礎設施破壞和混合戰。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">👔</div>
            <div class="tech-card-content">
                <h4>9. CISOs 問責制前所未有加重</h4>
                <p>隨着 AI 威脅加劇，CISO 個人法律和職業責任大幅增加，必須提升團隊技能應對 AI 相關威脅。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔐</div>
            <div class="tech-card-content">
                <h4>10. 憑證管理危機加劇</h4>
                <p>AI Agent 在企業網絡中擴展，每個 Agent 需要自己的憑證，令本已嚴峻的憑證管理問題火上加油。</p>
            </div>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Google Mandiant 明確表示：「2026 年及之後，威脅行為者使用 AI 將從例外變成規範。」從 AI 輔助的社會工程到惡意軟件開發，AI 將全面提升攻擊的速度、範圍和效果。LastPass 補充：「現在，攻擊者正在學習這項技術並設定門檻。」 defenders 正落後於威脅者。隨着 AI 加速發展，2026 年可能成為網絡安全形勢的轉折點——AI 攻擊將比 AI 防禦進步得更快。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">AI 輔助攻擊成為主流</div>
                <div class="timeline-desc">攻擊者開始利用 AI 提升生產力、進行社會工程和開發惡意軟件</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年 11 月</div>
                <div class="timeline-title">Google GTIG 發布 AI 惡意軟件觀測報告</div>
                <div class="timeline-desc">Fruitshell、Promptflux、PromptSteal 等命名，威脅從理論走向實際部署</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">Claude 被用於全球滲透攻擊</div>
                <div class="timeline-desc">標誌着 AI 原生攻擊工具時代來臨，NCC Group 稱這是首個大規模 AI 協調網絡間諜活動</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">AI 武器化進入規範化階段</div>
                <div class="timeline-desc">威脅者從「使用 AI」升級為「武器化 AI」，攻擊速度和規模大幅提升</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年（預測）</div>
                <div class="timeline-title">AI 防御落後於 AI 攻擊</div>
                <div class="timeline-desc">攻擊者設定技術門檻，defenders 持續落後，網絡安全形勢嚴峻</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>威脅類型</th>
                    <th>2025 年</th>
                    <th>2026 年（預測）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>AI 惡意軟件</td>
                    <td>概念驗證階段</td>
                    <td class="highlight-col">大規模實際部署，自主適應</td>
                </tr>
                <tr>
                    <td>深偽求職欺詐</td>
                    <td>已發現組織性騙局</td>
                    <td class="highlight-col">企業陸續發現「虛假員工」</td>
                </tr>
                <tr>
                    <td>Prompt Injection</td>
                    <td>新興威脅</td>
                    <td class="highlight-col">大幅增加，針對企業 AI 系統</td>
                </tr>
                <tr>
                    <td>Agentic AI 攻擊</td>
                    <td>工具出現（Villager）</td>
                    <td class="highlight-col">自動化整個攻擊生命週期</td>
                </tr>
                <tr>
                    <td>身份盜用方式</td>
                    <td>輔助入侵手段</td>
                    <td class="highlight-col">主要攻擊目標</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'AI 將在 2026 年造成前所未有的破壞：10 個專家警告的攻擊面向',
    'h1': 'AI 將在 2026 年造成<br>前所未有的破壞',
    'subtitle': '10 個專家警告的網絡安全威脅面向',
    'source_url': 'https://www.zdnet.com/article/10-ways-ai-will-do-unprecedented-damage-in-2026-experts-warn',
    'source_name': 'ZDNET',
    'pub_date': '2026-08-22',
    'img_alt': 'AI 網絡安全威脅視覺圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260822_101600',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print("❌ HTML 生成失敗:")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)
