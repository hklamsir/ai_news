import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/07/06/if-you-use-google-youre-training-its-ai-heres-how-to-opt-out/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-06</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Google 於 2026 年 6 月低調更新隱私設定，將用戶上傳至搜尋服務的媒體檔案（圖片、檔案、音訊、影片）自動納入 AI 模型訓練資料庫。用戶需主動關閉「Save Media」選項才能退出訓練。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>設定變更背景</h4>
                <p>Google 將原本的「Web & App Activity」設定拆分為兩個獨立選項：Web & App Activity 和新的 Search Services 設定（預設開啟）。用戶以為改了舊設定就能控制資料儲存，但新設定會獨立運作。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>哪些資料被用於 AI 訓練</h4>
                <p>媒體檔案（圖片、檔案、音訊、影片）、搜尋歷史、位置資料，以及來自造訪網站的個人化廣告資訊。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>用戶隱私受影響</h4>
                <p>此次更新顯示大型科技公司如何利用隱私政策更新，在用戶不知情下擴大 AI 訓練資料的收集範圍。用戶需要主動了解並調整隱私設定。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🛡️</div>
            <div class="tech-card-content">
                <h4>如何退出 AI 訓練</h4>
                <p>前往「Search Services History」頁面，取消勾選「Save Media」（可單獨取消，不影響其他記錄）；並設定自動刪除期限（3 個月、18 個月或 36 個月）。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>即使你修改了「Web & App Activity」設定，新聞 Search Services（尤其是「Save Media」）仍會獨立運作，不受影響。如不希望媒體被用於 AI 訓練，必須另外關閉「Save Media」選項。</p>
        </div>

        <div class="quote-box">
            <p>「Like your Search Services History, your saved media is also used to develop and improve Google services and technologies, including AI models and safety measures.」</p>
            <cite>— Google 官方聲明</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>專家建議定期檢視各平台的隱私設定，尤其是這類「預設同意」的更新。用戶應主動管理數位足跡，才能保護個人隱私不被過度收集用於 AI 訓練。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">Google 低調發布隱私更新</div>
                <div class="timeline-desc">透過客戶 email 通知用戶，悄悄將媒體檔案納入 AI 訓練資料範圍</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">更新前</div>
                <div class="timeline-title">用戶可透過 Web & App Activity 控制</div>
                <div class="timeline-desc">用戶以為調整資料保留期限就能控制 Google 儲存哪些資料</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">更新後</div>
                <div class="timeline-title">設定拆分为兩個獨立選項</div>
                <div class="timeline-desc">Web & App Activity 與新的 Search Services 設定分離，兩者獨立運作</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月</div>
                <div class="timeline-title">媒體曝光引發關注</div>
                <div class="timeline-desc">TechCrunch 等媒體報導此變更，用戶開始關注如何保護隱私</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">日後</div>
                <div class="timeline-title">用戶需主動管理隱私設定</div>
                <div class="timeline-desc">專家建議定期檢視各平台隱私設定，尤其是預設同意的更新</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>更新前</th>
                    <th>更新後</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>設定控制</td>
                    <td>透過 Web & App Activity 統一控制</td>
                    <td class="highlight-col">拆分為兩個獨立設定，需分別管理</td>
                </tr>
                <tr>
                    <td>媒體儲存</td>
                    <td>不涉及 AI 訓練</td>
                    <td class="highlight-col">預設開啟，用於 AI 模型訓練</td>
                </tr>
                <tr>
                    <td>退出方式</td>
                    <td>修改一處設定即可</td>
                    <td class="highlight-col">需另外取消「Save Media」選項</td>
                </tr>
                <tr>
                    <td>自動刪除選項</td>
                    <td>僅 Web & App Activity 有</td>
                    <td class="highlight-col">兩處設定都有（3/18/36 個月）</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'If you use Google, you\'re training its AI. Here\'s how to opt out. | TechCrunch',
    'h1': 'If you use Google, you\'re training its AI.<br>Here\'s how to opt out.',
    'subtitle': 'Google 悄悄將用戶媒體檔案納入 AI 訓練，隱私設定拆分後需分開管理',
    'source_url': 'https://techcrunch.com/2026/07/06/if-you-use-google-youre-training-its-ai-heres-how-to-opt-out/',
    'source_name': 'TechCrunch',
    'pub_date': '2026-07-06',
    'img_alt': 'Google 隱私設定頁面與 AI 訓練說明',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260707_083700',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
