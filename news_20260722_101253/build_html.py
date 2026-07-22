import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-21</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Google DeepMind 一口氣發布三款 Gemini 新模型，但市場最期待的旗艦級 Gemini 3.5 Pro 仍未現身，面對 OpenAI GPT-5 系列及 Anthropic Claude 系列的激烈競爭，Google 的旗艦模型開發似乎遭遇瓶頸。</p>

        <div class="tech-card">
            <div class="tech-card-icon">⚡</div>
            <div class="tech-card-content">
                <h4>Gemini 3.6 Flash：新一代主力工作模型</h4>
                <p>Gemini 3.6 Flash 是 Google 的「主力工作模型」，在編程、知識工作及多模態表現上均有提升，同時 Token 用量減少最多 17%，使用成本比 3.5 Flash 更低，專為大規模 AI Agent 建構而優化。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>Gemini 3.5 Flash-Lite：性價比之選</h4>
                <p>Gemini 3.5 Flash-Lite 是同系列中最具成本效益的型號，適合對成本敏感的應用場景，讓開發者能以更低成本使用 Gemini 系列能力。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔒</div>
            <div class="tech-card-content">
                <h4>Gemini 3.5 Flash Cyber：網絡安全專用模型</h4>
                <p>Gemini 3.5 Flash Cyber 是專為網絡安全漏洞偵測與修復微調的型號，以合理價格提供高效網安能力。該模型將僅向各國政府及可信合作夥伴提供，屬限量訪問試點計劃。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">❌</div>
            <div class="tech-card-content">
                <h4>Gemini 3.5 Pro：缺席的旗艦</h4>
                <p>此次發布最大遺憾是 Gemini 3.5 Pro 並未現身。Google 曾在 5 月預告 Pro 版本「已在內部使用，預計下月推出」，但 Bloomberg 報道指出 Google 在滿足內部性能目標方面遇到困難，導致發布延遲。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>這次發布的焦點不在旗艦模型，而是針對編程、網絡安全及成本優化的專用型號。3.5 Pro 的缺席顯示 Google 在旗艦模型開發上正面臨挑戰。</p>
        </div>

        <div class="quote-box">
            <p>「The focus on these releases is to deliver efficiency, latency, and reliability to customers that are building AI agents at scale.」</p>
            <cite>— Google DeepMind</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Google 此次聚焦於效率、延遲和可靠性三大核心需求，回應了開發者對低成本高效能模型的殷切需求。然而 3.5 Pro 的缺席顯示 Google 在旗艦模型開發上正面臨挑戰。隨著 OpenAI GPT-5 系列及 Anthropic Claude 系列的加速更新，Google 能否在 Gemini 4 實現突破，將是下半年 AI 領域的最大看點。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 2 月</div>
                <div class="timeline-title">Gemini 3.5 Pro 最後更新</div>
                <div class="timeline-desc">Google 發布 Gemini 3.5 Pro 上一次更新</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 5 月</div>
                <div class="timeline-title">Google 預告 3.5 Pro 即將推出</div>
                <div class="timeline-desc">Gemini 3.5 Flash 發布時，Google 表示 Pro 版本已內部使用中</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月 21 日</div>
                <div class="timeline-title">三款新模型發布</div>
                <div class="timeline-desc">Gemini 3.6 Flash、3.5 Flash-Lite、3.5 Flash Cyber 正式發布</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月（預計）</div>
                <div class="timeline-title">Gemini 3.5 Pro 持續延遲</div>
                <div class="timeline-desc">據 Bloomberg 報道，Google 內部仍在為 3.5 Pro 性能目標苦苦掙扎</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">Gemini 4 預訓練啟動</div>
                <div class="timeline-desc">Google DeepMind 宣佈已啟動有史以來最大規模的 Gemini 4 預訓練任務</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>Gemini 3.6 Flash</th>
                    <th>Gemini 3.5 Flash-Lite</th>
                    <th>Gemini 3.5 Flash Cyber</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>定位</td>
                    <td class="highlight-col">主力工作模型</td>
                    <td>性價比之選</td>
                    <td>網絡安全專用</td>
                </tr>
                <tr>
                    <td>Token 用量</td>
                    <td class="highlight-col">-17%（比 3.5 Flash）</td>
                    <td>—</td>
                    <td>—</td>
                </tr>
                <tr>
                    <td>成本</td>
                    <td class="highlight-col">比 3.5 Flash 低</td>
                    <td class="highlight-col">同系列最低</td>
                    <td>合理價格</td>
                </tr>
                <tr>
                    <td>適用場景</td>
                    <td>編程、知識工作、多模態</td>
                    <td>成本敏感應用</td>
                    <td>網絡安全漏洞偵測與修復</td>
                </tr>
                <tr>
                    <td>訪問權限</td>
                    <td>公開</td>
                    <td>公開</td>
                    <td>政府和可信合作夥伴限定</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Google 發布三款新 Gemini 型號　惟不見 3.5 Pro | TechCrunch',
    'h1':          'Google 發布三款新\nGemini 型號',
    'subtitle':    '3.6 Flash、3.5 Flash-Lite、3.5 Flash Cyber 三連發，3.5 Pro 仍缺席',
    'source_url':  'https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/',
    'source_name': 'TechCrunch',
    'pub_date':    '2026-07-21',
    'img_alt':     'Google 發布三款新 Gemini 型號，惟不見 3.5 Pro',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260722_101253',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print(f"❌ HTML 生成失敗：{errors}")
