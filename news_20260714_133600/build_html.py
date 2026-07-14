import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/07/13/waze-adds-new-ai-powered-features-and-customization-updates/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-13</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Google 旗下的 Waze 推出全新 AI 功能，包括 Gemini 驅動的個人化導航、對話式路況回報和摩托車專用模式，提升與 Apple Maps 等競爭對手的競爭力。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>Gemini AI 個人化導航</h4>
                <p>Waze 根據用戶出行歷史和城市交通模式提供個人化路線建議。例如，若用戶偏好高速公路而非當地道路，系統會優先顯示此類路線。用戶可在設定中關閉個人化功能或選擇替代路線。現已全球推送至 Android 和 iOS。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>Gemini 目的地搜尋</h4>
                <p>用戶可透過 Gemini 快速聊天功能找到目的地。點擊搜尋語音圖標即可提問，例如「找一家現在營業的咖啡店」、「找 Grand Mall 附近的停車場」或「找附近油價最低的加油站」。Waze 會回覆選項列表。現已向 beta 用戶全球推送。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏍️</div>
            <div class="tech-card-content">
                <h4>摩托車專用模式</h4>
                <p>AI 驅動的摩托車模式考慮兩輪車的特殊捷徑和道路限制，幫助騎士找到最佳路線並獲得更準確的預計到達時間。系統會顯示對騎士有風險的路況，如坑洞、減速帶、凸起人行橫道、肩膀盡頭和窄橋。現已在阿根廷、巴西、哥倫比亞、馬來西亞、墨西哥、秘魯和菲律賓推出。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🗣️</div>
            <div class="tech-card-content">
                <h4>對話式路況回報</h4>
                <p>Waze 已支援用自然語音回報交通狀況，現在更允許用戶以對話方式建議地圖更新，包括報告道路封閉或過時地址。用戶可說「這裡道路封閉」，Waze 會將詳細信息發送給當地地圖編輯者。現已全球推送。</p>
            </div>
        </div>


        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>部分新功能由 Google Gemini AI 驅動，反映 Google 將 Gemini 整合至旗下產品的策略。「少說話」模式可減少駕駛期間的語音提示，方便用戶專注聆聽音樂或播客。</p>
        </div>

        <div class="quote-box">
            <p>「Some of the new features are powered by Google's Gemini AI assistant, which reflects the tech giant's broader push to integrate Gemini across its products while also better positioning Waze to compete with rival services such as Apple Maps.」</p>
            <cite>— TechCrunch</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Google 透過在 Waze 中整合 Gemini AI，加強其在導航市場的競爭力。個人化路線和 AI 驅動的功能將成為導航應用程式的標準配備，提升用戶體驗和忠誠度。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">功能推出</div>
                <div class="timeline-title">個人化導航</div>
                <div class="timeline-desc">根據用戶偏好和交通模式提供個人化路線建議</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">功能推出</div>
                <div class="timeline-title">Gemini 目的地搜尋</div>
                <div class="timeline-desc">透過對話找到目的地，如咖啡店、停車場、加油站</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">功能推出</div>
                <div class="timeline-title">摩托車模式</div>
                <div class="timeline-desc">AI 考慮兩輪車特殊路況和限制</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">功能推出</div>
                <div class="timeline-title">對話式路況回報</div>
                <div class="timeline-desc">以自然語音報告道路封閉或過時地址</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">功能推出</div>
                <div class="timeline-title">靜音模式</div>
                <div class="timeline-desc">減少語音提示，方便專注聆聽音樂或播客</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>功能</th>
                    <th>說明</th>
                    <th>推出狀況</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>個人化導航</td>
                    <td>根據用戶偏好和歷史記錄提供路線建議</td>
                    <td class="highlight-col">全球推送中</td>
                </tr>
                <tr>
                    <td>Gemini 目的地搜尋</td>
                    <td>對話式目的地查詢</td>
                    <td class="highlight-col">Beta 用戶可用</td>
                </tr>
                <tr>
                    <td>摩托車模式</td>
                    <td>兩輪車專用導航和路況提示</td>
                    <td>部分國家</td>
                </tr>
                <tr>
                    <td>對話式路況回報</td>
                    <td>自然語音報告道路狀況</td>
                    <td class="highlight-col">全球推送中</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Waze 推出全新 AI 功能與個人化設定更新',
    'h1':          'Waze 推出全新<br>AI 功能更新',
    'subtitle':    'Gemini 驅動個人化導航、摩托車模式、對話式路況回報',
    'source_url':  'https://techcrunch.com/2026/07/13/waze-adds-new-ai-powered-features-and-customization-updates/',
    'source_name': 'TechCrunch',
    'pub_date':    '2026-07-13',
    'img_alt':     'Waze 導航應用程式介面，顯示 AI 驅動的路線建議',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260714_133600',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 建立成功")
else:
    print(f"❌ HTML 建立失敗：{errors}")
