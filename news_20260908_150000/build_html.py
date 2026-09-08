import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://note.com/hal2400_ai/n/n80bb4382f518" target="_blank">note（HAL2400）</a></p>
            <p><strong>📅 發布日期</strong>：2026-09-07</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>日本 AI 創作者 HAL2400 展示如何結合 ChatGPT-6 Astra 與 Seedance 2.5，製作出逼真到難以與實拍區分的 AI 短片。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🎨</div>
            <div class="tech-card-content">
                <h4>第一步：ChatGPT-6 Astra 生成圖像</h4>
                <p>用簡單日文提示詞描述場景，ChatGPT-6 Astra 能生成相當逼真的圖像。可用簡單提示詞先試，再視需要加入更詳細的描述。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎬</div>
            <div class="tech-card-content">
                <h4>第二步：Seedance 2.5 圖像動畫化</h4>
                <p>將生成的圖像作為「第一剪」輸入 Seedance 2.5，轉換為影片。可加入提示詞描述鏡頭運動和氛圍，如「自然手持晃動、5秒、16:9」。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>讓 Astra 設計 Seedance 提示詞</h4>
                <p>將圖片傳給 ChatGPT-6 Astra，讓它根據每張圖量身設計 Seedance 2.5 的影片提示詞，自動避免 4 部影片之間的對話或反應重疊。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔧</div>
            <div class="tech-card-content">
                <h4>微調提示詞也很簡單</h4>
                <p>實際生成時難免需要微調，可直接與 ChatGPT 討論，一邊逐步修改提示詞，最終完成超真實的 AI 影片。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>作者 Hal2400 表示：「每天都在做 AI 影片，但做出來的成果讓我連自己都分不清真假。」ChatGPT-6 Astra + Seedance 2.5 的組合，已能製作出與實拍無異的 AI 短片。</p>
        </div>

        <div class="quote-box">
            <p>「ChatGPT-6 Astra 的圖像生成與 Seedance 2.5 的影片生成相結合，達到了令人驚嘆的水平。」</p>
            <cite>— HAL2400 | AI Visual Creator</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>隨著這類工具能力提升，AI 影片製作已變得相當簡單且親民。任何人只要掌握適當的提示詞技巧，就能製作出寫實、自然的 AI 短片。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026-09-07</div>
                <div class="timeline-title">Hal2400 發布 note 文章</div>
                <div class="timeline-desc">日本 AI 創作者展示 ChatGPT-6 Astra + Seedance 2.5 的 AI 影片工作流程</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-09-07</div>
                <div class="timeline-title">社群迴響</div>
                <div class="timeline-desc">Hal2400 在 X 分享用此方法生成的女子高中生日常影片，引發熱議</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-09-08</div>
                <div class="timeline-title">本文發布</div>
                <div class="timeline-desc">BNEXT 報導 Hal2400 的 AI 影片製作方法與「寫實、自然」的製作原則</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>傳統方式</th>
                    <th class="highlight-col">ChatGPT-6 Astra + Seedance 2.5</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>所需工具</td>
                    <td>多個專業軟體</td>
                    <td class="highlight-col">兩個 AI 工具即可</td>
                </tr>
                <tr>
                    <td>提示詞要求</td>
                    <td>需詳細描述每個細節</td>
                    <td class="highlight-col">簡單描述即可，Astra 自動延伸</td>
                </tr>
                <tr>
                    <td>影片風格</td>
                    <td>需手動指定鏡頭運動</td>
                    <td class="highlight-col">自然手持晃動，寫實感強</td>
                </tr>
                <tr>
                    <td>技術門檻</td>
                    <td>需要影片編輯經驗</td>
                    <td class="highlight-col">門檻大幅降低，業餘可上手</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '用ChatGPT-6 Astra和Seedance 2.5製作超真實AI影片的簡單方法',
    'h1': '用ChatGPT-6 Astra和Seedance 2.5<br>製作超真實AI影片的簡單方法',
    'subtitle': 'ChatGPT-6 Astra與Seedance 2.5的完美配合',
    'source_url': 'https://note.com/hal2400_ai/n/n80bb4382f518',
    'source_name': 'note HAL2400',
    'pub_date': '2026-09-07',
    'img_alt': 'ChatGPT-6 Astra 生成的女子高中生日常 AI 圖像',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260908_150000',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
