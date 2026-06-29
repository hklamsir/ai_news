import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://vocus.cc/article/6a3f7049fd897800010f3ffa" target="_blank">VOCUS (@learn4c)</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-27</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Google 推出 Gemini Study Notebooks，把 Gemini 變成一位真正有系統的「學習夥伴」，具備形成性評量 + 個人化學習路徑的能力，不再只是回答問題，而是能持續記錄學習歷程、分析弱點、安排下一步學習。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📚</div>
            <div class="tech-card-content">
                <h4>學習與研究筆記本</h4>
                <p>教師或學生可上傳講義、PDF、投影片、閱讀資料等課程素材，Gemini 會進行診斷測驗，找出學生的能力與知識缺口，再依照結果規劃個人化的學習內容與練習。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>學習儀表板（Learning Dashboard）</h4>
                <p>每個單元區分為三種狀態：🔵 優點/強項（Strengths）、🩷 需要加強的地方（Focus areas）、⚪ 尚未開始（Not started），讓學生清楚看見學習進度，不再盲目刷題。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>AI 學習助理教練</h4>
                <p>過去 AI 大多在學生卡住時回答一個問題；現在，Gemini 能持續記錄學習歷程、分析弱點、安排下一步學習，逐漸扮演起「學習助理教練」的角色。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔗</div>
            <div class="tech-card-content">
                <h4>與 NotebookLM 雙向連動</h4>
                <p>除了在 Gemini 使用，也能接續在 NotebookLM 產生 Podcast（語音摘要）、教學影片（影片摘要），打造完整的 AI 學習生態系。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Study Notebooks 將<strong>免費提供使用</strong>，陸續在全球所有支援 Gemini 的地區推出，學校帳號與 18 歲以下學生也預計在今年夏天開始提供。</p>
        </div>

        <div class="quote-box">
            <p>「AI 不只是幫助學生找到答案，而是開始幫助學生找到自己的學習定位，也找到自己下一步最值得學習的地方。」</p>
            <cite>— learn4c @ VOCUS</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>如果 Gemini Study Notebooks 的能力持續成熟，AI 將不只是知識販賣機，而會成為每位學生專屬的學習助教，教師則能將更多心力放在引導思考、設計學習體驗，以及陪伴學生面對困難，共同成長。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">輸入教材</div>
                <div class="timeline-title">上傳課程素材</div>
                <div class="timeline-desc">上傳講義、PDF、投影片、閱讀資料</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">診斷測驗</div>
                <div class="timeline-title">Diagnostic Quiz</div>
                <div class="timeline-desc">Gemini 進行測驗，找出能力與知識缺口</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">個人化路徑</div>
                <div class="timeline-title">建立學習路徑</div>
                <div class="timeline-desc">Gemini 規劃個人化學習內容與練習</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">學習儀表板</div>
                <div class="timeline-title">追蹤進度</div>
                <div class="timeline-desc">查看強項、需要加強、尚未開始的項目</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">持續循環</div>
                <div class="timeline-title">下一輪學習</div>
                <div class="timeline-desc">依進度調整學習內容，循環改進</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>功能</th>
                    <th>傳統 AI 助教</th>
                    <th>Gemini Study Notebooks</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>互動方式</td>
                    <td>被動回答問題</td>
                    <td class="highlight-col">主動診斷學習缺口</td>
                </tr>
                <tr>
                    <td>學習追蹤</td>
                    <td>無</td>
                    <td class="highlight-col">儀表板完整呈現</td>
                </tr>
                <tr>
                    <td>個人化</td>
                    <td>統一的答案</td>
                    <td class="highlight-col">依診斷結果客製化</td>
                </tr>
                <tr>
                    <td>學習路徑</td>
                    <td>無</td>
                    <td class="highlight-col">AI 規劃個人化路徑</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Gemini 學習筆記本：打造個人化學習體驗，重新定位專屬學習系統',
    'h1':          'Gemini 學習筆記本<br>打造個人化學習體驗',
    'subtitle':    'Google 把 Gemini 變成學習夥伴，不只是問答而是系統性追蹤學習進度',
    'source_url':  'https://vocus.cc/article/6a3f7049fd897800010f3ffa',
    'source_name': 'VOCUS',
    'pub_date':    '2026-06-27',
    'img_alt':     'Gemini 個人化學習介面，學生在教室使用 AI 學習工具',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260629_083845',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print("❌ HTML 組裝失敗")
    for e in errors:
        print(f"   {e}")