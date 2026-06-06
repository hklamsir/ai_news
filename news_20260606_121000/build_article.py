import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/06/05/supabase-doubles-valuation-to-10b-in-8-months/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-06</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>開源資料庫新創 <strong>Supabase</strong> 宣布完成 5 億美元 F 輪融资，估值達到 <strong>100 億美元</strong>（投前估值），較 8 個月前的 50 億美元翻倍。這也是近期 AI 驅動開發熱潮中的最大規模融资之一。</p>

        <h3>📊 關鍵數據</h3>
        <ul>
            <li>📈 <strong>估值：</strong>100 億美元（投前）→ 約 105 億美元（投後）</li>
            <li>💰 <strong>融資額：</strong>5 億美元 F 輪</li>
            <li>📅 <strong>估值成長：</strong>8 個月內從 50 億美元翻至 100 億美元</li>
            <li>👨‍💻 <strong>開發者數量：</strong>近 1,000 萬用戶（8 個月內翻倍）</li>
            <li>🚀 <strong>資料庫增長：</strong>過去一年超過 600%</li>
            <li>🤖 <strong>AI 工具占比：</strong>超過 60% 的資料庫由 AI 工具創建</li>
        </ul>

        <h3>🔥 為何 Supabase 成長這麼快？</h3>
        <p>CEO Paul Copplestone 在博客中特別點名感謝 <strong>Claude Code</strong> 和 <strong>Codex</strong> 這兩款 AI 程式工具，認為它們「擴大了能夠構建產品的人數」。Supabase 同時也是 <strong>Bolt、Figma、Lovable、Replit</strong> 等平台的資料庫首選。</p>

        <h3>🛠 技術亮點：Multigres</h3>
        <p>本週 Supabase 推出了名為 <strong>Multigres</strong> 的工具，定位為 Postgres 的「操作系統」。它旨在簡化 Postgres 大規模運行的複雜性，讓開發者能夠集中管理讀副本、自動故障轉移、連接限制、備份等任務。</p>

        <h3>💡 另類的商業策略</h3>
        <p>Copplestone 曾在节目中透露，他拒絕了許多大型企業的百萬美元合約，因為這些合約會帶來產品決策上的壓力。他堅持自己的產品願景不走企業定制路線——這種「反向策略」在創業圈相當罕見，但顯然對 Supabase 非常有效。</p>

        <h3>🏦 投資方</h3>
        <p>本輪由 <strong>GIC</strong> 領投，现有投资方包括 <strong>Stripe</strong>，新投資方包括 <strong>Georgian</strong> 和 <strong>Salesforce Ventures</strong>。</p>

        <h3>📈 估值軌跡回顧</h3>
        <ul>
            <li>2025 年中：20 億美元（約 2 億美元融资）</li>
            <li>2025 年 10 月：50 億美元（1 億美元融资）</li>
            <li>2026 年 6 月：100 億美元（5 億美元融资）</li>
        </ul>

        <div class="tech-cards">
            <div class="tech-card">
                <div class="tech-card-icon">🚀</div>
                <h4>600% 資料庫增長</h4>
                <p>過去一年內，Supabase 上的資料庫啟動數量增長超過 600%，展現出爆發式成長態勢。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🤖</div>
                <h4>AI 工具佔比 60%+</h4>
                <p>超過六成的資料庫是由 AI 工具創建，顯示 AI 輔助開發已成為主流趨勢。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">👨‍💻</div>
                <h4>1,000 萬開發者</h4>
                <p>短短 8 個月內，Supabase 的開發者用戶數量從 500 萬翻倍至近 1,000 萬。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">💎</div>
                <h4>100 億美元獨角獸</h4>
                <p>最新估值 100 億美元（約 105 億美元投後），較 8 個月前翻倍，躋身全球最大新創之列。</p>
            </div>
        </div>

        <h3>🔍 為什麼開發者選擇 Supabase？</h3>
        <p>Supabase 基於開源的 <strong>PostgreSQL</strong> 資料庫，提供即時 API、身份認證、儲存等功能，讓開發者可以快速構建應用。相比傳統資料庫，Supabase 大幅降低了開發複雜度，特別適合：</p>
        <ul>
            <li>🔧 <strong>需要即時功能的行動/Web 應用</strong></li>
            <li>🤖 <strong>AI 輔助編碼流程中的快速原型開發</strong></li>
            <li>📱 <strong>需要無縫擴展的規模化新創產品</strong></li>
            <li>🌐 <strong>希望避免供應商鎖定的開源愛好者</strong></li>
        </ul>

        <h3>🌟 Multigres：Postgres 的作業系統</h3>
        <p>本週發布的 <strong>Multigres</strong> 是 Supabase 最新的重量級工具，被形容為 Postgres 的「操作系統」。它為開發者提供了一個中央管理介面，來處理以下繁瑣任務：</p>
        <ul>
            <li>📖 <strong>讀副本管理</strong> — 自動負載均衡</li>
            <li>🔄 <strong>自動故障轉移</strong> — 確保高可用性</li>
            <li>🔗 <strong>連接限制控制</strong> — 優化資源使用</li>
            <li>💾 <strong>備份管理</strong> — 自動化備份策略</li>
            <li>📊 <strong>效能監控</strong> — 即時效能儀表板</li>
        </ul>
        <p>這意味著即使是非專業 DBA 的普通開發者，也能輕鬆管理大規模 Postgres 部署。</p>

        <h3>💬 Paul Copplestone 的反向策略</h3>
        <div class="quote-box">
            <p>「我拒絕參與那些『爛化』開發者工具的趨勢，因為那些百萬美元合約會讓產品變得不再以開發者為中心。」</p>
            <cite>— Paul Copplestone，Supabase CEO & Co-founder</cite>
        </div>
        <p>大多數新創公司在成長過程中都會走向企業化服務，但 Copplestone 選擇了一條截然不同的路：<strong>堅持產品願景，不被大型客戶的需求牵着鼻子走</strong>。這種策略在商業世界看似冒險，卻讓 Supabase 保持了快速的產品迭代和開發者優先的文化。</p>

        <h3>📈 與其他新創的估值比較</h3>
        <table class="comparison-table">
            <thead>
                <tr>
                    <th>新創公司</th>
                    <th>最新估值</th>
                    <th>領域</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Supabase</td>
                    <td class="highlight-col">100 億美元</td>
                    <td>開源資料庫</td>
                </tr>
                <tr>
                    <td>FirebirdSQL</td>
                    <td>非營利</td>
                    <td>開源資料庫</td>
                </tr>
                <tr>
                    <td>MongoDB</td>
                    <td>~140 億美元</td>
                    <td>NoSQL 資料庫</td>
                </tr>
                <tr>
                    <td>PlanetScale</td>
                    <td>~10 億美元</td>
                    <td>MySQL 分支</td>
                </tr>
            </tbody>
        </table>

        <h3>🏆 AI 驅動開發時代的最大贏家</h3>
        <p>Supabase 的爆發式成長，是 AI 輔助編碼工具興起最大的受益者之一。當 <strong>Claude Code</strong>、<strong>Codex</strong>、<strong>Bolt</strong>、<strong>Lovable</strong> 等工具讓「人人都能開發」成為可能時，作為這些工具首選資料庫的 Supabase 自然水漲船高。</p>
        <p>這輪 5 億美元的资金將主要用於：</p>
        <ul>
            <li>📡 <strong>擴展全球基礎設施</strong> — 加快資料庫部署速度</li>
            <li>🔬 <strong>深化 AI 整合</strong> — 讓 AI 輔助開發更無縫</li>
            <li>👥 <strong>擴大團隊規模</strong> — 招聘更多工程師</li>
            <li>🌏 <strong>拓展企業市場</strong> — 在保持開發者優先的同時進軍企業</li>
        </ul>

        <div class="highlight-box">
            <p>💬 <strong>Paul Copplestone（原話）：</strong>「AI 模型擴大了能夠構建產品的人數，而 Supabase 的使命是讓這個過程變得盡可能簡單。」</p>
        </div>
"""

metadata = {
    'title': 'Supabase 估值翻倍至 100 億美元：8 個月內從 50 億躍升至獨角獸巨頭',
    'h1': 'Supabase 估值翻倍至 100 億美元<br>8 個月內從 50 億躍升至獨角獸巨頭',
    'subtitle': '開源資料庫新創完成 5 億美元 F 輪融资，AI 驅動開發熱潮下的最大贏家之一',
    'source_url': 'https://techcrunch.com/2026/06/05/supabase-doubles-valuation-to-10b-in-8-months/',
    'source_name': 'TechCrunch',
    'pub_date': '2026-06-06',
    'img_alt': 'Supabase 估值翻倍至 100 億美元',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260606_121000',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 重建成功")
else:
    print("❌ HTML 重建失敗")
    for e in errors:
        print(f"  - {e}")
