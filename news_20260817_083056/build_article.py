import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.bnext.com.tw/article/91851/gemini-canva-magic-layers-edit" target="_blank">BNEXT 數位時代</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-17</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Google Gemini 整合 Canva Magic Layers 功能，讓用戶可將 AI 生成的圖片一鍵轉為可編輯的 Canva 設計稿，輕鬆修改文字、換色、調整版面。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🖼️</div>
            <div class="tech-card-content">
                <h4>步驟 1：Gemini 生成圖片</h4>
                <p>在 Gemini 對話框輸入英文提示詞，例如：「A vibrant poster design for a Taipei summer market, modern illustration style, plain flat color background behind headline text area, minimal focal points.」</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📨</div>
            <div class="tech-card-content">
                <h4>步驟 2-3：呼叫 @Canva 指令</h4>
                <p>圖片生成完畢後，於同一對話框輸入：<br><code>@Canva, turn this image into an editable Canva design.</code><br><strong>注意：</strong>系統目前僅支援英文指令，中文指令（如「轉成 Canva」）無法觸發功能。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔗</div>
            <div class="tech-card-content">
                <h4>步驟 4：完成授權綁定</h4>
                <p>首次使用時，Gemini 會跳出授權確認卡片，點擊後引導至帳號綁定頁面。若未跳出提示，可前往「設定>連結的應用程式」手動開啟授權。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">✏️</div>
            <div class="tech-card-content">
                <h4>步驟 5：進入 Canva 編輯</h4>
                <p>轉換完成後點擊專屬連結，即可跳轉至 Canva 網頁版。圖片已轉為可分層調整的設計稿，支援文字、物件、背景色的修改。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 Magic Layers 限制</h4>
            <p><strong>可修改：</strong>獨立文字框（改字/換字型）、獨立物件（移動/刪除）、單純背景色<br>
            <strong>無法修改：</strong>複雜交疊的圖像、半透明陰影與背景融合的區域（會維持合併圖層）</p>
        </div>

        <div class="quote-box">
            <p>「系統是透過辨識原有圖像的文字內容，並套用 Canva 字庫中相近的字型進行重建，因此無法保證與 AI 隨機生成的原圖字體 100% 相同。」</p>
            <cite>— BNEXT 報導</cite>
        </div>

        <h3>💰 免費 vs 付費版差異</h3>
        <p>Magic Layers 屬於 Canva Premium AI 功能，每次執行都會扣除帳號內的 AI 額度。免費帳號額度較少，Pro 或團隊版帳號擁有較充裕次數。</p>

        <h3>❓ 常見問題</h3>
        <p><strong>中文指令能用嗎？</strong> 目前僅支援英文，系統無法解析中文指令。<br>
        <strong>可一次處理多張圖嗎？</strong> 不行，採用「一圖一專案」運作。<br>
        <strong>拆出來字型不同？</strong> 正常現象，系統套用 Canva 字庫中相近字型重建。<br>
        <strong>手機也能用嗎？</strong> 可以，但建議用電腦網頁版編輯效果較好。</p>

        <h3>🔮 業界展望</h3>
        <p>隨著代理式 AI（Agentic AI）快速發展，AI 的角色從被動問答轉變為能主動代為執行任務。Gemini 與 Canva 的整合展現了 AI 工具之間的互聯趨勢，讓用戶無需手動下載上傳，即可在不同平台間無縫銜接工作流程。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">輸入提示詞</div>
                <div class="timeline-title">步驟 1</div>
                <div class="timeline-desc">在 Gemini 輸入英文提示詞生成圖片</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">@Canva 指令</div>
                <div class="timeline-title">步驟 2-3</div>
                <div class="timeline-desc">輸入 @Canva, turn this image into an editable Canva design.</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">帳號授權</div>
                <div class="timeline-title">步驟 4</div>
                <div class="timeline-desc">首次使用需完成 Canva 帳號授權綁定</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">跳轉編輯</div>
                <div class="timeline-title">步驟 5</div>
                <div class="timeline-desc">點擊連結進入 Canva 網頁版編輯</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">修改調整</div>
                <div class="timeline-title">後續編輯</div>
                <div class="timeline-desc">在 Canva 中修改文字、換色、調整版面</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>功能</th>
                    <th>免費版</th>
                    <th>Pro/團隊版</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Magic Layers 額度</td>
                    <td class="highlight-col">較少</td>
                    <td class="highlight-col">較充裕</td>
                </tr>
                <tr>
                    <td>圖層編輯</td>
                    <td>基本功能</td>
                    <td class="highlight-col">完整功能</td>
                </tr>
                <tr>
                    <td>團隊協作</td>
                    <td>無法使用</td>
                    <td class="highlight-col">支援</td>
                </tr>
                <tr>
                    <td>品牌工具組</td>
                    <td>無法使用</td>
                    <td class="highlight-col">支援</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Gemini圖片怎麼轉Canva編輯？5步驟教學：呼叫@Canva、好用提示詞範例，免費付費版差在哪？',
    'h1':          'Gemini 圖片轉 Canva<br>5 步驟教學',
    'subtitle':    'Gemini 生成圖片如何一鍵轉為可編輯的 Canva 設計稿？',
    'source_url':  'https://www.bnext.com.tw/article/91851/gemini-canva-magic-layers-edit',
    'source_name': 'BNEXT 數位時代',
    'pub_date':    '2026-08-17',
    'img_alt':     'Gemini 與 Canva Magic Layers 整合介面',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260817_083056',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
