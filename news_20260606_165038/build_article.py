import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.koc.com.tw/archives/645075" target="_blank">電腦王阿達</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-06</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>AI 圖像生成新創 <strong>Ideogram</strong> 正式發布 4.0 版本並開源，開放權重（Open Weight），成為首個達到設計專業水準的開源圖像生成模型。93 億參數、支援本地部署與微調，效果直逼 ChatGPT 等閉源模型，在排版和文字渲染維度上甚至超越所有競爭者。</p>

        <h3>📊 關鍵數據</h3>
        <ul>
            <li>🤖 <strong>參數量：</strong>93 億（9.3B）</li>
            <li>💾 <strong>量化版本：</strong>提供多種量化選項，消費級高階顯示卡即可運行</li>
            <li>🖥️ <strong>部署方式：</strong>完全本地運行，無需雲端</li>
            <li>🔧 <strong>微調支援：</strong>可根據品牌風格自訂微調</li>
            <li>🏆 <strong>Design Arena 排名：</strong>僅落後 OpenAI 和 Google 閉源模型</li>
            <li>✍️ <strong>文字渲染：</strong>超越所有競爭者，業界第一</li>
            <li>📜 <strong>授權：</strong>Non-Commercial 協議（企業需付費取得商業授權）</li>
        </ul>

        <h3>🔓 開源細節：權重、授權與部署門檻</h3>
        <p>Ideogram 4.0 的開放策略分為兩層：提供<strong>多種量化版本</strong>，讓擁有消費級高階顯示卡的創作者可以在本地完全掌控這款模型。不需要依賴雲端服務，不需要將資料傳到外部伺服器，還可以根據自己的品牌風格進行微調（fine-tuning）。</p>
        <p>對於重視隱私和資料主權的企業和個人創作者而言，這是一個相當有吸引力的選項。</p>

        <h3>🌐 平台整合：不只是模型，是一個生態系</h3>
        <p>Ideogram 4.0 並非只有一個孤零零的模型檔案。Ideogram 同步開放了多個平台的使用管道，包括：</p>
        <ul>
            <li>🖼️ <strong>ComfyUI 整合：</strong>社群已經建立了完整的工作流程，從模型下載、節點配置到生成範例都有詳細教學，大幅降低本地部署的技術門檻</li>
            <li>🖥️ <strong>本地部署成功：</strong>已有用戶成功在本地端完成部署並生成圖片，圖片大小可從 1024 起跳</li>
            <li>🔧 <strong>Hugging Face：</strong>模型同步上架 Hugging Face 平台</li>
        </ul>

        <h3>🖼️ 產品功能：設計工作流不只生成</h3>
        <p>除了模型本身，Ideogram 的產品端也同步更新了多項設計導向功能，包括可編輯文字和圖層功能即將推出。這個更新讓 Ideogram 從單純的圖像生成工具，轉型為完整的設計工作流解決方案。</p>

        <h3>🏆 對產業的意義：開源追上前線</h3>
        <p>Ideogram 4.0 的發布代表一個重要訊號：<strong>開放權重模型在設計級圖像生成領域，已經逼近閉源前線</strong>。在 Design Arena 上，Ideogram 4.0 僅落後 OpenAI 和 Google 的閉源模型，而在排版和文字渲染這兩個專業設計師最關心的維度上，它甚至超越了所有競爭者。</p>
        <p>這種策略讓人想起 Meta 在 LLM 領域的做法：用開放權重換取社群生態，用生態系鞏固技術地位。Ideogram 選擇在圖像生成領域走同樣的路，而且是在一個仍以閉源為主流的市場中。</p>

        <h3>⚠️ 商業授權的門檻</h3>
        <p>當然，商業授權仍然是門檻。模型權重的 <strong>Non-Commercial 協議</strong>意味著企業若要將其整合進產品或服務中，需要另外付費取得商業授權。這是開源與「免費使用」之間的界線，也是 Ideogram 的商業模式所在。</p>

        <h3>💡 誰適合使用 Ideogram 4.0 開源版本？</h3>
        <ul>
            <li>🔒 <strong>重視隱私的創作者：</strong>不希望自己的創意資料上傳到雲端</li>
            <li>🎨 <strong>品牌客製化需求：</strong>希望根據自家品牌風格微調模型</li>
            <li>💻 <strong>本地運算愛好者：</strong>擁有足夠強大的顯示卡，想要完全掌控自己的生成環境</li>
            <li>📚 <strong>研究人員：</strong>需要透明可審計的模型權重進行學術研究</li>
            <li>🏢 <strong>企業用戶：</strong>需要商業授權，但可獲得比閉源更低的總體擁有成本</li>
        </ul>

        <div class="tech-cards">
            <div class="tech-card">
                <div class="tech-card-icon">🤖</div>
                <h4>93 億參數</h4>
                <p>Ideogram 4.0 擁有 93 億參數，是目前最大的開源圖像生成模型之一</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🔓</div>
                <h4>開放權重</h4>
                <p>首個達到設計專業水準的開源圖像模型，權重完全開放</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">✍️</div>
                <h4>文字渲染第一</h4>
                <p>在排版和文字渲染維度上超越所有競爭者，業界領先</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🏠</div>
                <h4>本地部署</h4>
                <p>完全本地運行，無需雲端，保護隱私和資料主權</p>
            </div>
        </div>

        <h3>🔍 與封閉模型的比較</h3>
        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>Ideogram 4.0 開源</th>
                    <th>閉源前線模型</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>文字渲染</td>
                    <td class="highlight-col">第一</td>
                    <td>落後</td>
                </tr>
                <tr>
                    <td>Design Arena 總分</td>
                    <td>第三（落後 OpenAI/Google）</td>
                    <td>前二</td>
                </tr>
                <tr>
                    <td>部署方式</td>
                    <td class="highlight-col">本地 / 完全掌控</td>
                    <td>僅雲端</td>
                </tr>
                <tr>
                    <td>微調支援</td>
                    <td class="highlight-col">完整支援</td>
                    <td>通常不支援</td>
                </tr>
                <tr>
                    <td>隱私保護</td>
                    <td class="highlight-col">完全本地，資料不外流</td>
                    <td>需上傳雲端</td>
                </tr>
                <tr>
                    <td>商業授權</td>
                    <td>付費取得</td>
                    <td>已包含在 API 費用中</td>
                </tr>
            </tbody>
        </table>

        <div class="highlight-box">
            <p>💬 <strong>產業意義：</strong>Ideogram 4.0 開源的意義不僅是一個模型的發布，而是代表開放權重模型在設計級圖像生成領域已經能與閉源巨頭正面競爭。這與 Meta 在 LLM 領域的成功策略如出一轍：用開源換生態，用生態鞏固地位。</p>
        </div>
"""

metadata = {
    'title': '效果直逼 ChatGPT！Ideogram 4.0 正式開源：93 億參數圖像模型，支援本地部署與微調',
    'h1': '效果直逼 ChatGPT！Ideogram 4.0 正式開源<br>93 億參數圖像模型，支援本地部署與微調',
    'subtitle': '首個達到設計專業水準的開源圖像生成模型，文字渲染超越所有競爭者',
    'source_url': 'https://www.koc.com.tw/archives/645075',
    'source_name': '電腦王阿達',
    'pub_date': '2026-06-06',
    'img_alt': 'Ideogram 4.0 正式開源 93 億參數圖像模型',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260606_165038',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 重建成功")
else:
    print("❌ HTML 重建失敗")
    for e in errors:
        print(f"  - {e}")