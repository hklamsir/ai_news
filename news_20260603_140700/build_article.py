import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.zdnet.com/article/work-iq-is-microsofts-big-bet-on-agent-first-enterprise-software/" target="_blank">ZDNET</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-03</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要 + 深度優化</p>
        </div>

        <div class="alert-box">
            <h4>⚠️ 關鍵前提</h4>
            <p>Microsoft 形容 2026 年是企業軟件從「人類驅動」轉向「AI 代理驅動」的轉捩點。Work IQ 是這個新時代的核心基礎設施。</p>
        </div>

        <div class="quote-box">
            <p>「Work IQ 專為代理優先的世界而建，在這個世界中，AI 代理——而非人類開發者——能實時決定跨系統使用哪些工具。」</p>
            <cite>— Microsoft 官方描述</cite>
        </div>

        <h3>🎯 核心突破卡片</h3>
        <div class="tech-cards">
            <div class="tech-card">
                <div class="tech-card-icon">🔄</div>
                <h4>getSchema 動態發現</h4>
                <p>代理能在運行時動態發現數據結構，「詢問」數據「你是什麼」，數據會自我描述，無需預定義模型。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🛠️</div>
                <h4>10 個通用工具</h4>
                <p>Microsoft 將數千種企業操作「壓縮」成 10 個通用工具（fetch、create、update 等），代理可實時動態組合。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🔒</div>
                <h4>Entra 身份認證</h4>
                <p>所有調用均通過 Microsoft Entra 認證，包括新的 Entra Agent ID（非人類身份），數據留在租戶邊界內。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">💰</div>
                <h4>消耗式定價</h4>
                <p>按工具調用、編排和推理計費，支援在 Microsoft 365 管理中心設定成本控制和用量監控。</p>
            </div>
        </div>

        <h3>📊 Work IQ vs 傳統企業軟件</h3>
        <table class="comparison-table">
            <thead>
                <tr><th>維度</th><th>傳統企業軟件</th><th>Work IQ（代理優先）</th></tr>
            </thead>
            <tbody>
                <tr><td>數據發現</td><td>需預定義 API 和整合</td><td class="highlight-col">代理運行時動態查詢</td></tr>
                <tr><td>工具調用</td><td>人類開發者編碼連接</td><td class="highlight-col">代理實時自主選擇</td></tr>
                <tr><td>系統擴展</td><td>新增整合需大量會議協調</td><td class="highlight-col">代理自描述接口自動適配</td></tr>
                <tr><td>上下文窗口</td><td>需容納整個企業數據上下文</td><td class="highlight-col">getSchema 按需查詢，小記憶體佔用</td></tr>
                <tr><td>操作數量</td><td>數千種操作需要單獨集成</td><td class="highlight-col">10 個通用工具動態組合</td></tr>
            </tbody>
        </table>

        <h3>📅 Microsoft 企業 AI 佈局時間軸</h3>
        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">Work IQ 發布</div>
                <div class="timeline-desc">Microsoft 發布 Work IQ，作為企業代理優先軟件的核心基礎設施。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年同步</div>
                <div class="timeline-title">MDASH 公開</div>
                <div class="timeline-desc">Microsoft MDASH 結束預覽，發布 100+ 專業威脅獵殺 AI 代理。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年同步</div>
                <div class="timeline-title">Agent 365</div>
                <div class="timeline-desc">Microsoft 推出 Agent 365，企業 AI 代理數量快速增長。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年同步</div>
                <div class="timeline-title">Ask APIs</div>
                <div class="timeline-desc">為外部應用開放 M365 Copilot Chat 體驗，作為單一不透明服務。</div>
            </div>
        </div>

        <h3>🌟 服裝倉庫案例：代理如何解決問題</h3>
        <p>假設一家服裝製造商突然收到大量退貨。傳統 IT 系統難以發現問題，但代理可以：</p>
        <ul>
            <li>代理和子代理交叉引用 SKU 退貨率、物流路線圖、客戶服務投訴關鍵詞（如「癢」、「皮疹」、「打噴嚏」）</li>
            <li>代理發現一個共同因素：所有退貨商品在倉庫 A7 的 4 號區域停留至少 48 小時</li>
            <li>最終真相：5 號區域存放工業膠水，微量化學殘留物滲透到 4 號區域的服裝纖維中</li>
        </ul>

        <h3>🔍 記者尖銳提問與 Microsoft 回應</h3>
        <div class="alert-box">
            <h4>💰 Q：Work IQ 是否只是新一輪許可證、整合、監控和支援收費？</h4>
            <p>Microsoft：Work IQ API 為代理的工作方式優化，減少往返次數、降低延遲、提高令牌效率、擴大數據訪問吞吐量，且數據留在租戶邊界內。</p>
        </div>
        <div class="alert-box">
            <h4>🎯 Q：現有自動化、改進搜索、Microsoft 365 Copilot 已有的功能有何不同？</h4>
            <p>Microsoft：AI 代理訪問數據和使用工具的方式與人類完全不同，傳統 API 會導致代理結果質量更低、速度更慢、成本更高。</p>
        </div>
        <div class="alert-box">
            <h4>🛡️ Q：是否創建了新的集中智能層，讓攻擊者、內部威脅、配置錯誤的代理可以 exploit？</h4>
            <p>Microsoft：任何集中能力都是目標，但替代方案更糟——每個代理建立自己的數據存儲、数据移动、自己的身份驗證、自己的審計缺口。Work IQ 反而縮小了攻擊面。</p>
        </div>

        <div class="highlight-box">
            <h4>✨ 關鍵洞察</h4>
            <p>Microsoft 正押注 2026 年是企業軟件從人類驅動轉向 AI 代理驅動的轉捩點。Work IQ 將企業軟件從「應用程序 + 數據」模式徹底重構，讓代理能在運行時動態發現數據、自助組合工具、跨系統執行操作。這是企業 IT 數十年來最大的典範轉移。</p>
        </div>

        <div class="alert-box">
            <h4>⚠️ 潛在風險</h4>
            <p>文章作者警告：如果每個 IT 操作都需要巨額令牌消耗税，生產力提升可能不足以抵消成本。企業需要為代理優先的 AI 時代做好成本控制準備。</p>
        </div>
"""

metadata = {
    'title': 'Work IQ is Microsoft big bet on agent-first enterprise IT | ZDNET',
    'h1': '微軟 Work IQ<br>企業軟件大革命',
    'subtitle': 'AI 代理實時決定跨系統工具調用！Microsoft 押注 2026 為企業 AI 轉捩點',
    'source_url': 'https://www.zdnet.com/article/work-iq-is-microsofts-big-bet-on-agent-first-enterprise-software/',
    'source_name': 'ZDNET',
    'pub_date': '2026-06-03',
    'img_alt': 'Microsoft Work IQ 企業 AI 代理概念圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260603_140700',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")
