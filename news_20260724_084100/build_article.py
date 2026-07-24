import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/07/23/edtech-platform-raises-4-5m-to-help-teach-students-how-to-vibe-code/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-23</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>來自教師家族的 Dora Palfi 創辦 Imagi，專門幫助 K-12 學生和教師學習編程及 AI 技能，近日獲得 450 萬美元種子輪融資。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🎓</div>
            <div class="tech-card-content">
                <h4>創辦理念</h4>
                <p>Dora Palfi 來自教育世家，深信「教育能完全改變一個人的人生軌跡」。她於 2018 年與 Beatrice Ionascu 共同創立 Imagi，致力于為 K-12 學生和教師提供編程及 AI 學習工具。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>融資詳情</h4>
                <p>Imagi 宣布獲得 <strong>450 萬美元種子輪融資</strong>，投資者包括 Brighteye Ventures、Day One Capital 及藝術家 Wil.i.am。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤝</div>
            <div class="tech-card-content">
                <h4>與 Lovable 合作</h4>
                <p>去年 11 月，Imagi 宣布與 vibe coding 工具 <strong>Lovable</strong> 合作，老師可創建課程，讓學生在安全框架下學習 vibe coding。OpenAI 更提供 <strong>100 萬美元信用額度</strong>，讓學校免費使用 Imagi x Lovable 工具。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📱</div>
            <div class="tech-card-content">
                <h4>實際應用案例</h4>
                <p>一位老師運用此工具創建了可翻譯 <strong>15 種語言</strong>的課程翻譯 App；學員更開發了靈感來自電影《獨家腥聞》的 <strong>Alta 數碼衣櫃 App</strong>。</p>
            </div>
        </div>


        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Imagi 的合作模式顯示，AI 編程教育正走向「有保護的學習」方向——老師作為引導者，學生在安全範圍內探索 AI 工具。</p>
        </div>

        <div class="quote-box">
            <p>「教育能完全改變一個人的人生軌跡。」</p>
            <cite>— Dora Palfi，Imagi 創辦人</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>隨著 vibe coding 興起，這種「老師引導、學生安全探索」的教育模式有望在更多學校推廣。OpenAI 的百萬美元信用額度支援顯示科技巨頭對 AI 教育市場的重視。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2018 年</div>
                <div class="timeline-title">Imagi 創立</div>
                <div class="timeline-desc">Dora Palfi 與 Beatrice Ionascu 共同創辦 Imagi</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">新增 AI 素養課程</div>
                <div class="timeline-desc">Imagi 將 AI 素養納入 K-12 課程範疇</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年 11 月</div>
                <div class="timeline-title">與 Lovable 合作</div>
                <div class="timeline-desc">宣布與 vibe coding 工具 Lovable 建立合作夥伴關係</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年 11 月</div>
                <div class="timeline-title">OpenAI 資助</div>
                <div class="timeline-desc">OpenAI 提供 100 萬美元信用額度支援學校免費使用</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月</div>
                <div class="timeline-title">完成種子輪融資</div>
                <div class="timeline-desc">宣布獲得 450 萬美元種子輪融資，投資者包括 Brighteye Ventures、Day One Capital 及 Wil.i.am</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>Imagi 方案</th>
                    <th>傳統編程學習</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>學習方式</td>
                    <td class="highlight-col">Vibe Coding（AI 輔助）</td>
                    <td>純代碼編寫</td>
                </tr>
                <tr>
                    <td>師生互動</td>
                    <td class="highlight-col">老師創建課程，學生探索</td>
                    <td>老師授課為主</td>
                </tr>
                <tr>
                    <td>工具支援</td>
                    <td class="highlight-col">Lovable + OpenAI 信用額度</td>
                    <td>一般編程環境</td>
                </tr>
                <tr>
                    <td>應用場景</td>
                    <td class="highlight-col">15 種語言翻譯、數碼衣櫃 App 等</td>
                    <td>標準練習題目</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '教育科技平台 Imagi 獲投 450 萬美元　教學生如何「Vibe Coding」| TechCrunch',
    'h1':          '教育科技平台 Imagi 獲投 450 萬美元<br>教學生如何「Vibe Coding」',
    'subtitle':    'Dora Palfi 來自教育世家，深信教育能改變人生軌跡，2018 年創辦 Imagi 幫助 K-12 學生學習編程及 AI 技能',
    'source_url':  'https://techcrunch.com/2026/07/23/edtech-platform-raises-4-5m-to-help-teach-students-how-to-vibe-code/',
    'source_name': 'TechCrunch',
    'pub_date':    '2026-07-23',
    'img_alt':     'Imagi 是一款幫助 K-12 學生學習 vibe coding 的教育科技平台',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260724_084100',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print(f"❌ 組裝失敗：{errors}")
