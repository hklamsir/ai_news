import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/07/29/google-is-rolling-out-its-age-assurance-tech-for-apps-worldwide-by-year-end/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-29</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Google 宣佈將其 Age Assurance 年齡驗證技術透過 Play Signal API 擴展至全球 Android 開發者，目標 2026 年底前覆蓋所有市場，目前已於巴西上線，澳洲、加拿大將於 8 月中率先採用。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📱</div>
            <div class="tech-card-content">
                <h4>運作方式</h4>
                <p>開發者可在<b>不取得用戶出生日期等個人資料</b>的情況下，獲取用戶的年齡範圍。家長透過 Family Link 分享子女年齡，成年人則可在 app 提示時自願分享年齡。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔒</div>
            <div class="tech-card-content">
                <h4>隱私保障</h4>
                <p>年齡範圍<b>不會自動分享</b>，需由家長主動 opt-in 選擇加入，且過程中無需暴露用戶真實生日等敏感個資。所有設定集中於 Family Link 管理。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🛡️</div>
            <div class="tech-card-content">
                <h4>配套安全工具</h4>
                <p>Google Play 提供多層保護：開發者可限制兒童探索特定 app；家長可管理螢幕使用時間、審批下載請求、設定 PIN 內容過濾。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌍</div>
            <div class="tech-card-content">
                <h4>全球推廣時間表</h4>
                <p>巴西已上線 → 澳洲、加拿大 2026 年 8 月中 → 全球市場 2026 年底前全面開放。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>此技術對標 Apple 已於 2026 年 2 月全球推出的 Age Verification 工具。隨著各地立法者持續施壓 app 商店加强未成年人保護，年齡驗證可能成為未來 app 開發的標準配備。</p>
        </div>

        <div class="quote-box">
            <p>「Google's technology allows developers to obtain a user's age range without needing to access personal information, like their date of birth.」</p>
            <cite>— TechCrunch 報導</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>在全球監管壓力下，Google 此舉可視為必要回應。隨著 Age Assurance 技術普及，開發者將能更輕易地提供符合法規要求且針對不同年齡層定制的安全體驗，形成業界新標準。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026-02</div>
                <div class="timeline-title">Apple Age Verification 全球上線</div>
                <div class="timeline-desc">Apple 率先在全球推出年齡驗證工具以符合各地法規</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-29</div>
                <div class="timeline-title">Google 宣佈 Play Signal API 擴展計劃</div>
                <div class="timeline-desc">Google 宣佈年內將 Age Assurance 技術推向全球開發者</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-08 中</div>
                <div class="timeline-title">澳洲、加拿大率先採用</div>
                <div class="timeline-desc">Play Signal API 登陸澳洲及加拿大市場</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-12</div>
                <div class="timeline-title">全球市場全面開放</div>
                <div class="timeline-desc">預計年底前覆蓋所有市場的 Android 開發者</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">進行中</div>
                <div class="timeline-title">各國監管持續加強</div>
                <div class="timeline-desc">立法者持續向 app 商店施壓，要求提供更好的未成年人保護</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>比較項目</th>
                    <th>Google Play Signal API</th>
                    <th>Apple Age Verification</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>推出時間</td>
                    <td>2026 年底全球</td>
                    <td class="highlight-col">2026 年 2 月全球</td>
                </tr>
                <tr>
                    <td>目前可用地區</td>
                    <td>巴西</td>
                    <td class="highlight-col">全球</td>
                </tr>
                <tr>
                    <td>需分享出生日期</td>
                    <td class="highlight-col">不需要</td>
                    <td>不需要</td>
                </tr>
                <tr>
                    <td>家長控制</td>
                    <td class="highlight-col">Family Link 集中管理</td>
                    <td>Screen Time 管理</td>
                </tr>
                <tr>
                    <td>默認分享</td>
                    <td>需 opt-in</td>
                    <td class="highlight-col">需 opt-in</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'Google 將其年齡驗證技術推向全球 Android 開發者',
    'h1': 'Google 將其年齡驗證技術<br>推向全球 Android 開發者',
    'subtitle': 'Play Signal API 年底前覆蓋所有市場，已在巴西上線，8 月中登陸澳洲、加拿大',
    'source_url': 'https://techcrunch.com/2026/07/29/google-is-rolling-out-its-age-assurance-tech-for-apps-worldwide-by-year-end/',
    'source_name': 'TechCrunch',
    'pub_date': '2026-07-29',
    'img_alt': '家長與青少年子女使用智能手機，Family Link 介面顯示年齡驗證控制選項',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260803_103556',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果: {'成功' if success else '失敗'}")
if errors:
    print(f"錯誤: {errors}")
