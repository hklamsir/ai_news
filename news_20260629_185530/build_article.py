import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://technews.tw/2026/06/29/deepseek-launches-dspark-with-up-to-85-faster-inference/" target="_blank">TechNews 科技新報</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-29</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>DeepSeek 聯合北京大學發布開源推理加速框架 DSpark，採用半自回歸生成架構與置信度調度驗證機制，在高併發場景下將用戶端生成速度提升 60%-85%，有效吞吐量翻 4 倍。</p>

        <div class="tech-card">
            <div class="tech-card-icon">⚡</div>
            <div class="tech-card-content">
                <h4>半自回歸生成架構</h4>
                <p>融合高吞吐並行生成與輕量級串行校驗，結合置信度調度驗證機制，根據系統負載動態調整驗證長度，解決大語言模型在高併發場景下的推理效率瓶頸。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🚀</div>
            <div class="tech-card-content">
                <h4>效能大幅提升</h4>
                <p>基於 DeepSeek-V4 真實用戶流量評估，相較 MTP-1 基線：用戶端生成速度提升 60%-85%，高併發場景下有效吞吐量翻 4 倍。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤝</div>
            <div class="tech-card-content">
                <h4>跨模型通用性</h4>
                <p>在阿里 Qwen3-4B/8B/14B 上測試，相較自回歸草稿模型接受 Token 長度提升 26.7%-30.9%，相較並行草稿模型提升 16.3%-18.4%。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📦</div>
            <div class="tech-card-content">
                <h4>完全開源</h4>
                <p>開源 DSpark 模型權重及 DeepSpec 訓練代碼倉庫。DeepSeek 創始人梁文鋒位列論文作者，這是 6 月中旬完成 500 億人民幣融資後首次開源新成果。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>DSpark 適合需要高併發推理的生產環境，包括 AI 客服、內容生成、程式碼助手等應用場景。</p>
        </div>

        <div class="quote-box">
            <p>「DSpark 將用戶端生成速度提升了 60%-85%，高併發場景下有效吞吐量翻 4 倍。」</p>
            <cite>— DeepSeek 與北京大學論文</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這是 DeepSeek 在完成 500 億人民幣融資後首次開源新成果。DSpark 的出現為大語言模型的推理效率優化提供了新方向，特別適合高併發生產環境。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月中旬</div>
                <div class="timeline-title">500 億融資完成</div>
                <div class="timeline-desc">DeepSeek 完成 500 億人民幣融資</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月 27 日</div>
                <div class="timeline-title">DSpark 發布</div>
                <div class="timeline-desc">DeepSeek 聯合北京大學發布論文及開源成果</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月 27 日</div>
                <div class="timeline-title">部署上線</div>
                <div class="timeline-desc">DSpark 已部署到 DeepSeek-V4 線上服務系統</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">進行中</div>
                <div class="timeline-title">效能驗證</div>
                <div class="timeline-desc">基於真實用戶流量持續評估</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">技術演進</div>
                <div class="timeline-desc">持續優化框架，推動開源生態發展</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>測試模型</th>
                    <th>相較自回歸草稿（Token 長度提升）</th>
                    <th>相較並行草稿（Token 長度提升）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Qwen3-4B</td>
                    <td class="highlight-col">+30.9%</td>
                    <td>+16.3%</td>
                </tr>
                <tr>
                    <td>Qwen3-8B</td>
                    <td class="highlight-col">+26.7%</td>
                    <td>+18.4%</td>
                </tr>
                <tr>
                    <td>Qwen3-14B</td>
                    <td class="highlight-col">+30.0%</td>
                    <td>+18.3%</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'DS 開源推理加速框架 DSpark，推理速度最高提升 85%',
    'h1':          'DeepSeek 發布 DSpark<br>推理速度最高提升 85%',
    'subtitle':    'DeepSeek 聯合北京大學開源半自回歸推理加速框架，高併發吞吐量翻 4 倍',
    'source_url':  'https://technews.tw/2026/06/29/deepseek-launches-dspark-with-up-to-85-faster-inference/',
    'source_name': 'TechNews 科技新報',
    'pub_date':    '2026-06-29',
    'img_alt':     'DSpark 推理加速示意圖，AI 資料中心光纖網路與效能提升數據',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260629_185530',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print("❌ HTML 組裝失敗")
    for e in errors:
        print(f"   {e}")