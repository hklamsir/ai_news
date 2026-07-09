import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.bnext.com.tw/article/91455/anthropic-engineer-claude-harness" target="_blank">BNEXT</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-08</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Anthropic 工程師 Thariq Shihipar 在 AI Engineer World's Fair 分享與 Claude Fable 5 協作的經驗，核心觀點是：模型表現好不好，往往不只看模型本身，改善工具環境與提示更能釋放潛力。他透露 Claude Code 團隊把系統提示砍掉八成，少下禁令、多給脈絡，模型反而表現更好。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📝</div>
            <div class="tech-card-content">
                <h4>系統提示的演變</h4>
                <p>Claude 3.5 Sonnet 時代最佳做法是「提示寫短、工具給少」；中期流行「提示寫長、工具給多」；但到了最新一代，又倒回去——模型反而想要更短提示，因為範例會綁住它的想像力。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">✂️</div>
            <div class="tech-card-content">
                <h4>砍掉八成系統提示</h4>
                <p>Claude Code 團隊把系統提示砍掉約八成，原則從「規定它不能做什麼」改成「給它足夠的背景」，少下禁令、多給脈絡，模型才真正發揮實力。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🛠️</div>
            <div class="tech-card-content">
                <h4>工具讓模型更強</h4>
                <p>一般聊天模型無法回答「名字以『aw』結尾的寶可夢」；但 Claude Code 能自己跑程式、抓清單再篩選，展現工具賦予模型的能力差距。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤔</div>
            <div class="tech-card-content">
                <h4>讓模型反過來問你問題</h4>
                <p>從 Opus 4 的「勉強叫得動」，到 Opus 4.5 的「一口氣完成訪談」，再到 Fable 5 的「直接生出嵌問題的 HTML 報告」，同一功能跨越多版本持續改進。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Shihipar 最值得記住的一句話：「東西變好做了，但做出價值還是難（building is easier, but generating value is still hard）。」別太沉迷於把流程弄得漂亮，真正難的，是找到那件值得做的事。</p>
        </div>

        <div class="quote-box">
            <p>「模型表現好不好，往往不只看模型本身。改善工具環境與提示，更能釋放其潛藏實力。」</p>
            <cite>— Thariq Shihipar，Anthropic Claude Code 團隊工程師</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>當模型被「解開束縛」後，瓶頸轉移到人身上。Shihipar 指出「地圖不等於實地」——你腦中的計畫、提示是地圖；真正的程式庫、現實限制才是實地。Claude Fable 5 會一口氣跑很大一片範圍，撞上很多你地圖上沒畫的決策點。「對齊地圖和實地、把未知找出來」，已成為 AI 工程師新的核心挑戰。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">Claude 3.5 Sonnet</div>
                <div class="timeline-title">提示寫短、工具給少</div>
                <div class="timeline-desc">最佳做法是提示寫短、工具給少、多塞範例</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">中期</div>
                <div class="timeline-title">提示寫長、工具給多</div>
                <div class="timeline-desc">業界流行反過來，提示寫長、工具給多、範例塞好塞滿</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">最新一代</div>
                <div class="timeline-title">又倒回去</div>
                <div class="timeline-desc">模型反而想要更短提示，範例會綁住它的想像力</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-01</div>
                <div class="timeline-title">Fable 5 恢復全球存取</div>
                <div class="timeline-desc">Claude Fable 5 於當天恢復全球存取，Shihipar 發表演講</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-08</div>
                <div class="timeline-title">BNEXT 報導</div>
                <div class="timeline-desc">BNEXT 發布中文報導，分析 Anthropic 工程師的 prompt 演變觀點</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>階段</th>
                    <th>提示策略</th>
                    <th>效果</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Claude 3.5 Sonnet</td>
                    <td>提示寫短、工具給少、多塞範例</td>
                    <td class="highlight-col">效果良好</td>
                </tr>
                <tr>
                    <td>中期趨勢</td>
                    <td>提示寫長、工具給多、範例塞滿</td>
                    <td>過度約束模型</td>
                </tr>
                <tr>
                    <td>最新一代</td>
                    <td>砍掉八成系統提示，少禁令多給脈絡</td>
                    <td class="highlight-col">模型真正發揮實力</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '提示詞越寫越長反而害了你！Anthropic工程師：Claude Code團隊砍掉8成系統提示，模型才真正發揮',
    'h1': '提示詞越寫越長反而害了你！<br>Anthropic工程師：Claude Code團隊砍掉8成系統提示，模型才真正發揮',
    'subtitle': 'Anthropic 工程師 Shihipar 分享：少下禁令、多給脈絡，模型才能真正發揮實力',
    'source_url': 'https://www.bnext.com.tw/article/91455/anthropic-engineer-claude-harness',
    'source_name': 'BNEXT',
    'pub_date': '2026-07-08',
    'img_alt': 'Claude Code 提示詞演變示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260709_085100',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print("❌ 錯誤：")
    for e in errors:
        print(f"   {e}")
