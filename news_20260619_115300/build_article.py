import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.bnext.com.tw/article/91177/ahrefs-ai-search-seo-rules" target="_blank">BNEXT 數位時代</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-10</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Ahrefs 分析超過 10 億筆數據，發現傳統 SEO 規則多數不再適用 AI 搜尋：Schema 結構化標記對 AI 引用幾乎無效，而 YouTube 提及次數才是提升 AI 品牌能見度的關鍵。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📝</div>
            <div class="tech-card-content">
                <h4>列表文章稱霸 AI 引用</h4>
                <p>「最佳 X」部落格列表文（Listicle）佔 ChatGPT 所有引用頁面類型的 43.8%，是最受 AI 青睐的內容形式。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔒</div>
            <div class="tech-card-content">
                <h4>七成引用行銷人無法控制</h4>
                <p>ChatGPT 引用來源中，有 67% 是行銷人員無法影響的。維基百科佔 29.7%、網站首頁佔 23.8%、應用程式商店佔 6.6%。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>Google 掛零不等於 AI 引用掛零</h4>
                <p>ChatGPT 引用最多的頁面中，有 28.3% 在 Google 自然搜尋排名完全掛零。這是一個完全獨立的內容發現管道。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>Schema 結構化標記幾乎無效</h4>
                <p>加入結構化標記對 AI 引用幾乎沒有影響。AI Overviews 引用率甚至下滑 −4.6%，其餘變化幅度均在誤差範圍內。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>YouTube 提及次數與 AI 品牌能見度的相關係數高達 0.737，是所有研究因子中最高的——超越反向連結、頁面數量、網域評分等傳統 SEO 指標。</p>
        </div>

        <div class="quote-box">
            <p>「我不確定 SEO 還有沒有用。當 AI 爬取網頁的邏輯不同於 SEO，這意味著行銷人過去積累的直覺與經驗也需調整了。」</p>
            <cite>— 行銷從業者的心聲</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>AI 搜尋的遊戲規則與傳統 SEO 截然不同。行銷人需要重新思考內容策略：過去被認為重要的技術優化（如 Schema 標記）的重要性大幅下降，而視頻內容（YouTube）的重要性則顯著提升。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">過去十年</div>
                <div class="timeline-title">SEO 時代</div>
                <div class="timeline-desc">關鍵詞優化、反向連結、Schema 標記是主要工作</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">現在</div>
                <div class="timeline-title">AI 搜尋崛起</div>
                <div class="timeline-desc">用戶直接問 ChatGPT 而非搜尋引擎，行為模式根本改變</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">研究發現</div>
                <div class="timeline-title">傳統 SEO 失效</div>
                <div class="timeline-desc">Schema 標記對 AI 引用無效，YouTube 成為關鍵</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">研究發現</div>
                <div class="timeline-title">獨立管道</div>
                <div class="timeline-desc">28.3% AI 高引用頁面在 Google 排名掛零</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">內容策略調整</div>
                <div class="timeline-desc">列表文章、YouTube 內容優先，技術優化退居次要</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>傳統 SEO</th>
                    <th>AI 搜尋時代</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Schema 結構化標記</td>
                    <td>重要</td>
                    <td class="highlight-col">幾乎無效</td>
                </tr>
                <tr>
                    <td>YouTube 提及</td>
                    <td>普通指標</td>
                    <td class="highlight-col">相關係數最高（0.737）</td>
                </tr>
                <tr>
                    <td>列表文章（Listicle）</td>
                    <td>一般內容</td>
                    <td class="highlight-col">43.8% 是 AI 引用最多類型</td>
                </tr>
                <tr>
                    <td>Google 排名</td>
                    <td>決定性因素</td>
                    <td class="highlight-col">28.3% 高引用頁面排名掛零</td>
                </tr>
                <tr>
                    <td>內容發現管道</td>
                    <td>主要靠 Google</td>
                    <td class="highlight-col">AI 聊天機器人是獨立管道</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'AI搜尋優化怎麼做？Ahrefs數據揭潛規則：schema標記沒用、YouTube最關鍵',
    'h1':          'AI搜尋優化怎麼做？<br>Ahrefs 數據揭潛規則',
    'subtitle':    'Schema 結構化標記幾乎無效，YouTube 提及次數相關係數 0.737 奪冠',
    'source_url':  'https://www.bnext.com.tw/article/91177/ahrefs-ai-search-seo-rules',
    'source_name': 'BNEXT 數位時代',
    'pub_date':    '2026-06-10',
    'img_alt':     'AI搜尋優化概念圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260619_115300',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print(f"❌ 錯誤：{errors}")