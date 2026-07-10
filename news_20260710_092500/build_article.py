import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.zdnet.com/article/open-source-summit-linus-torvalds" target="_blank">ZDNET</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-10</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Linux 之父林納斯·托沃茲在印度開源峰會 2026 上語出驚人：自己已不再親自寫程式，而是專注於管理人與專案方向。他現在只靠 Git 和 Email 兩個工具工作，與 AI 工具保持距離，強調「在更高層次與人打交道」。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🐧</div>
            <div class="tech-card-content">
                <h4>Linux 7.1：緩慢而穩定前進</h4>
                <p>托沃茲強調 Linux 7.1 的發展方向是「緩慢而穩定，不搞大驚小怪」。他認為這是刻意為之——Linux 的成功正來自於這種務實的節奏，而非追求戲劇性的大改版。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>AI 工具：玩具專案用得上，核心還不行</h4>
                <p>托沃茲分享他對 AI 工具的看法：玩具專案可用 LLM 原型化想法，但對於核心級別的修復，「就我的經驗來說，LLM 還沒達到那個水平」，AI 輔助還無法勝任 Linux 核心開發。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚙️</div>
            <div class="tech-card-content">
                <h4>真正的工具只有兩個：Git 和 Email</h4>
                <p>當被問及日常工作方式，托沃茲的回答令人意外地簡潔：「Git 和 email，是我真正僅有的兩個工具。我用 Google 來查東西。」他補充自己是例外——大多數維護者其實使用更多工具。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔧</div>
            <div class="tech-card-content">
                <h4>清理歷史包袱：ISDN 和 ATM 支持被移除</h4>
                <p>開源社群正在加速移除過時的技術債務，例如 ISDN 和 ATM 網路標準的支持正在逐步停用。托沃茲坦言，即使仍有人在 386 上跑 Linux，也可以繼續用舊版核心，但向前看，社群不會永遠為老舊硬體提供支援。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>托沃茲的工作哲學：「我與人打交道，而非與工具打交道。」他選擇在更高層次工作，把精力放在管理人與專案方向上，而非親自寫程式碼。</p>
        </div>

        <div class="quote-box">
            <p>Git 和 email，是我真正僅有的兩個工具。我用 Google 來查東西。</p>
            <cite>— Linus Torvalds，Linux 之父</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>托沃茲的分享揭示開源社群正在經歷的兩個重要趨勢：</p>
        <p><strong>第一</strong>，AI 工具的定位問題——它適合原型設計和輔助工作，但核心程式碼的品質把關仍離不開資深開發者的判斷。</p>
        <p><strong>第二</strong>，技術債務的取捨——開源專案需要在向後兼容和向前發展之間找到平衡點，無法永遠支援每一代老舊硬體。</p>
        <p>他的「兩個工具」哲學，某程度上也代表了一種反樸歸真：在工具爆炸的年代，最核心的能力，其實是判斷力和人際協調。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">1991 年</div>
                <div class="timeline-title">Linux 誕生</div>
                <div class="timeline-desc">林納斯·托沃茲發布 Linux 核心首個版本</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2005 年</div>
                <div class="timeline-title">Git 誕生</div>
                <div class="timeline-desc">托沃茲為 Linux 核心開發創造 Git 版本控制系統</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月</div>
                <div class="timeline-title">Open Source Summit India</div>
                <div class="timeline-desc">托沃茲與 Dirk Hohndel 對談，披露現在只靠 Git 和 Email 工作</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維護者類型</th>
                    <th>托沃茲</th>
                    <th>其他維護者</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>主要工具</td>
                    <td class="highlight-col">Git + Email（僅兩個）</td>
                    <td>多個工具 + AI 輔助</td>
                </tr>
                <tr>
                    <td>工作層次</td>
                    <td class="highlight-col">與人打交道（高層次）</td>
                    <td>與工具打交道（較低層次）</td>
                </tr>
                <tr>
                    <td>AI 工具態度</td>
                    <td>玩具專案可用，核心不行</td>
                    <td class="highlight-col">用於補丁檢查</td>
                </tr>
                <tr>
                    <td>程式碼親自寫</td>
                    <td>否，已脫離一線</td>
                    <td class="highlight-col">是，仍在編碼</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': "'I'm not a programmer' anymore: Linus Torvalds on the only two tools he uses now",
    'h1': "'I'm not a programmer' anymore<br>Linus Torvalds 披露僅有的兩個工具",
    'subtitle': 'Linux 之父的務實哲學：Git + Email，專注管理人而非工具',
    'source_url': 'https://www.zdnet.com/article/open-source-summit-linus-torvalds',
    'source_name': 'ZDNET',
    'pub_date': '2026-07-10',
    'img_alt': 'Linux 核心開發者工作場景，Git 和 Email 工具',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260710_092500',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print("錯誤：")
    for e in errors:
        print(f"  - {e}")
