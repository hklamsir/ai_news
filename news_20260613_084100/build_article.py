import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/06/11/cheaper-faster-and-culturally-aware-avataars-video-ai-is-built-for-indias-scale/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-11</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🚀 技術突破：10 倍提速、成本大幅下降</h3>
        <p>Avataar AI 採用蒸餾技術（distillation）將阿里巴巴 Wan 2.2 壓縮為更精簡快速的版本，結果驚人：</p>
        <ul>
            <li><strong>步驟</strong>：Varya 只需 4 步，Wan 2.2 需要 50 步</li>
            <li><strong>速度</strong>：5 秒 720p 影片生成僅需 <strong>45 秒</strong>（Wan 2.2 需 1,230 秒）</li>
            <li><strong>成本</strong>：每秒僅 ₹0.48（$0.005），比 Veo、Kling、Luma、Runway 便宜約 <strong>20 倍</strong></li>
        </ul>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>價格比較</h4>
                <p>Varya 每秒 $0.005，競爭對手（Veo、Kling、Luma、Runway）每定價 $0.10 或以上，性價比差距達 20 倍。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎯</div>
            <div class="tech-card-content">
                <h4>瞄準印度市場</h4>
                <p>Peak XV 董事總經理 Rajan Anandan 表示：「印度是影片優先市場，當前 AI 影片模型對印度來說太貴。如果 AI 影片要觸及學生、教師、微中小型企業、創作者和公共服務，成本必須大幅下降。」</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏛️</div>
            <div class="tech-card-content">
                <h4>呼應 India AI Mission</h4>
                <p>Avataar AI 是印度政府 <strong>India AI Mission</strong>（約 12 億美元）入選的 12 家新創之一。印度目標在 2028 年前吸引 <strong>2,000 億美元</strong> AI 投資，並在六個月內將 GPU 容量翻倍。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎨</div>
            <div class="tech-card-content">
                <h4>文化敏感度訓練</h4>
                <p>Avataar AI 使用精選數據訓練 Varya，識別印度文化特徵：節日（排日（排燈節、灑紅節等）、食物（印度香飯、咖喱等）、服飾（紗麗、旁遮普服等）及建築風格。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Varya 的推出反映印度 AI 發展的路線選擇：不做基礎模型競爭，專注應用開發及建立開發者生態，以性價比和文化親和力取勝。</p>
        </div>

        <div class="quote-box">
            <p>「印度是影片優先市場。當前 AI 影片模型對印度來說太貴。如果 AI 影片要觸及學生、教師、微中小型企業、創作者和公共服務，成本必須大幅下降。成本是印度 AI 普及的最大突破口。」</p>
            <cite>— Rajan Anandan，Peak XV 董事總經理</cite>
        </div>

        <h3>🌐 開源策略</h3>
        <p>Varya 將作為開源模型發布於 <strong>India AIKosh 入口網站</strong>，連同訓練數據一併公開，讓開發者能自行托管或修改。Avataar 亦計劃與 Higgsfield、Adobe Firefly 等影片工具合作。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">印度 AI 任務啟動</div>
                <div class="timeline-title">India AI Mission</div>
                <div class="timeline-desc">印度政府推出約 12 億美元 AI 發展計劃</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">新創入選</div>
                <div class="timeline-title">Avataar AI 獲選</div>
                <div class="timeline-desc">成為 12 家入選新創之一，獲得補貼 GPU 計算資源</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">近期發布</div>
                <div class="timeline-title">Varya 模型發布</div>
                <div class="timeline-desc">基於 Wan 2.2 蒸餾優化，10 倍速、20 倍便宜</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">開源發布</div>
                <div class="timeline-title">登陸 AIKosh</div>
                <div class="timeline-desc">開源模型及訓練數據將發布於印度政府 AI 入口網站</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來目標</div>
                <div class="timeline-title">2,000 億美元投資</div>
                <div class="timeline-desc">印度目標在 2028 年前吸引 2,000 億美元 AI 投資</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>Varya</th>
                    <th>Wan 2.2 / 競爭對手</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>生成步驟</td>
                    <td class="highlight-col">4 步</td>
                    <td>50 步（ Wan 2.2）</td>
                </tr>
                <tr>
                    <td>5 秒 720p 所需時間</td>
                    <td class="highlight-col">45 秒</td>
                    <td>1,230 秒</td>
                </tr>
                <tr>
                    <td>每秒成本</td>
                    <td class="highlight-col">$0.005（₹0.48）</td>
                    <td>$0.10 或以上</td>
                </tr>
                <tr>
                    <td>文化識別</td>
                    <td class="highlight-col">印度特色（節日、食物、服飾）</td>
                    <td>通用模型，缺乏文化敏感度</td>
                </tr>
                <tr>
                    <td>開源策略</td>
                    <td class="highlight-col">開源 + 訓練數據公開</td>
                    <td>封閉或部分開放</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Cheaper, faster, and culturally aware, Avataar\'s video AI is built for India\'s scale | TechCrunch',
    'h1':          '印度製影片 AI<br>Varya 十倍速・二十倍平',
    'subtitle':    'Avataar AI 基於阿里巴巴 Wan 2.2 蒸餾優化，成本大幅下降 20 倍，瞄準印度影片優先市場',
    'source_url':  'https://techcrunch.com/2026/06/11/cheaper-faster-and-culturally-aware-avataars-video-ai-is-built-for-indias-scale/',
    'source_name': 'TechCrunch',
    'pub_date':    '2026-06-11',
    'img_alt':     '印度影片 AI 平民價',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260613_084100',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")