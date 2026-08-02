import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.reuters.com/technology/artificial-intelligence/artificial-intelligencer-openai-explores-ai-devices-with-small-models-new-chip-2025-12-11/" target="_blank">Reuters</a></p>
            <p><strong>📅 發布日期</strong>：2025-12-11</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>OpenAI 正積極開發自家 AI 硬體裝置，瞄準「環境式 AI 運算」市場，計劃推出配備定制晶片的永遠開機式個人 AI 助理，與 Google、Meta 等科技巨頭正面交鋒。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>OpenAI 進軍硬體領域</h4>
                <p>OpenAI 正在開發 AI 硬體裝置，核心願景是打造一款「了解你一切」的個人助理。與傳統手機「開機或關機、在口袋或桌面」的被動模式不同，OpenAI 的目標是創造一種始終在場、主動感知環境的裝置，但同時提供明確、可見的指示，告知用戶裝置何時正在留意。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💻</div>
            <div class="tech-card-content">
                <h4>定制晶片：關鍵突破</h4>
                <p>要實現上述願景，OpenAI 需要一種全新晶片。現有的伺服器晶片（如 Nvidia 或其他廠商）是為平行運算工作負載優化，服務數百萬用戶。但個人 AI 裝置需要的是完全相反的處理器——專為單一用戶設計，嚴格的功率限制，並能即時運行精簡模型。OpenAI 正探索開發專為設備端推論優化的定制晶片。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚔️</div>
            <div class="tech-card-content">
                <h4>競爭態勢升溫</h4>
                <p>AI 硬體戰場日漸火熱：Google 宣布與 Warby Parker 合作 2026 年推出 AI 智能眼鏡；Meta 收購了 Limitless，開發可記錄和摘要你一天生活的「AI 記憶」穿戴裝置。整個業界都在猜測 OpenAI 是否能重現當年 ChatGPT 的奇蹟，這次是在硬體領域。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📅</div>
            <div class="tech-card-content">
                <h4>分階段推出策略</h4>
                <p>這類裝置將分階段推出：第一階段是更輕巧、針對特定任務且基於雲端的裝置；第二階段是對隱私更敏感、永遠開機的裝置，但業內人士警告強大的設備端電腦可能需要數年時間才能成熟。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>永遠開機、被動感知環境的 AI 裝置將重新定義人機互動方式——從「用戶主動呼叫」轉變為「AI 主動理解情境」。誰能率先推出，誰就能定義下一個 AI 時代。</p>
        </div>

        <div class="quote-box">
            <p>「Which tech giant pulls this off first, and whether consumers are actually ready for an always-on AI device, will define the next era of AI.」</p>
            <cite>— Reuters</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>原型機已在內部流傳，整個產業都在屏息以待。專家指出，消費者是否真的准备好接受無時無刻不在的 AI 裝置，將是成敗的關鍵考驗。晶片定製化、功耗控制、隱私保障將是三大技術攻堅方向。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2025 年中</div>
                <div class="timeline-title">OpenAI 硬體計畫曝光</div>
                <div class="timeline-desc">OpenAI 開始探索自家 AI 晶片與硬體裝置</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年 12 月</div>
                <div class="timeline-title">Google x Warby Parker 合作</div>
                <div class="timeline-desc">Google 宣布與 Warby Parker 合作 2026 年推出 AI 智能眼鏡</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年 12 月</div>
                <div class="timeline-title">Meta 收購 Limitless</div>
                <div class="timeline-desc">Meta 收購 Limitless，佈局「AI 記憶」穿戴裝置市場</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年（預計）</div>
                <div class="timeline-title">輕量雲端 AI 裝置問世</div>
                <div class="timeline-desc">第一階段輕量、任務導向的雲端 AI 裝置有望率先推出</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年後（預計）</div>
                <div class="timeline-title">永遠開機裝置成熟</div>
                <div class="timeline-desc">強大設備端 AI 電腦預計需要數年時間才能完全成熟</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>比較維度</th>
                    <th>傳統伺服器晶片</th>
                    <th>OpenAI 定制晶片目標</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>設計目標</td>
                    <td>平行運算，服務數百萬用戶</td>
                    <td class="highlight-col">單一用戶，設備端即時推論</td>
                </tr>
                <tr>
                    <td>功率限制</td>
                    <td>高功率伺服器環境</td>
                    <td class="highlight-col">嚴格功率約束，行動裝置</td>
                </tr>
                <tr>
                    <td>模型大小</td>
                    <td>大型雲端模型</td>
                    <td class="highlight-col">精簡模型，本地運行</td>
                </tr>
                <tr>
                    <td>延遲要求</td>
                    <td>可接受網路延遲</td>
                    <td class="highlight-col">即時回應，離線可用</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Artificial Intelligencer: OpenAI explores AI devices with small models and new chip',
    'h1':          'OpenAI 進軍 AI 硬體<br>永遠開機式助理夢',
    'subtitle':    'Reuters 獨家：OpenAI 開發定制晶片，分階段推出環境式 AI 裝置',
    'source_url':  'https://www.reuters.com/technology/artificial-intelligence/artificial-intelligencer-openai-explores-ai-devices-with-small-models-new-chip-2025-12-11/',
    'source_name': 'Reuters',
    'pub_date':    '2025-12-11',
    'img_alt':     'OpenAI AI 硬體裝置概念圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260802_113800',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
