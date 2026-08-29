#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.blocktempo.com/tencent-hunyuan-hy4-preview-open-source-770b-moe-context-pricing/" target="_blank">BLOCKTEMPO</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-29</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>騰訊發布並開源旗艦模型「混元 Hy4 preview」，總參數 7,700 億、上下文 100 萬，規模是前代 2.6 倍，但 OpenRouter 輸入價格暴增 4.6 倍，備受市場關注。</p>

        <div class="tech-card">
            <div class="tech-card-icon">⚙️</div>
            <div class="tech-card-content">
                <h4>MoE 架構規格</h4>
                <p>總參數 7,700 億、每 token 啟用 490 億、上下文 100 萬。78 層主幹，每層 256 個路由專家 + 1 個共享專家，每個 token 挑 8 個路由專家上工。以 Apache 2.0 開源。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>價格暴增 4.6 倍</h4>
                <p>OpenRouter 輸入從 0.18 美元漲至 0.834 美元，輸出從 0.60 美元漲至 2.501 美元。騰訊雲標價為輸入每百萬 token 6 元人民幣、輸出 18 元。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>自家盲測只小贏</h4>
                <p>163 位內部專家盲測：Hy4 得 2.99 分、GLM 5.3 得 2.92 分、Kimi K3 得 2.94 分。對上 GLM 贏面僅差 6 個百分點。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🚀</div>
            <div class="tech-card-content">
                <h4>四大能力方向</h4>
                <p>軟體工程（長程開發除錯）、辦公分析（跨檔案協作）、遊戲開發（一句話生成原型）、科研（分子動力學模擬）。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點數據</h4>
            <p>總參數 7,700 億（Hy3 的 2.6 倍）| 上下文 100 萬（Hy3 的 4 倍）| 價格輸入漲 4.6 倍 | 盲測滿分 4 分得 2.99 分</p>
        </div>

        <div class="quote-box">
            <p>「Hy4 已經開始參與騰訊自身研發，協助優化訓練方法、資料策略、評測體系與底層運算子，自己提方案、自己跑實驗、再依結果調整。」</p>
            <cite>— 騰訊官方發布說明</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Hy4 的價格暴增考驗開發者接受度。其自我改進循環概念領先，但詳細成果尚待驗證。在 GLM 5.3 與 Kimi K3 夾擊下，能否突圍仍有待觀察。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">8月28日</div>
                <div class="timeline-title">Hy4 發布</div>
                <div class="timeline-desc">騰訊發布並開源混元 Hy4 preview</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">開源平台</div>
                <div class="timeline-title">多平台上架</div>
                <div class="timeline-desc">Hugging Face、ModelScope、GitCode、CNB</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">商業變現</div>
                <div class="timeline-title">價格暴增</div>
                <div class="timeline-desc">OpenRouter 輸入價格漲 4.6 倍</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">騰訊內部</div>
                <div class="timeline-title">自我研發</div>
                <div class="timeline-desc">Hy4 已參與騰訊自身研發流程</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">競爭態勢</div>
                <div class="timeline-title">三家激戰</div>
                <div class="timeline-desc">Hy4 小勝 GLM 5.3 與 Kimi K3，領先優勢微弱</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>Hy3 preview</th>
                    <th>Hy4 preview</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>總參數</td>
                    <td>2,950 億</td>
                    <td class="highlight-col">7,700 億（2.6 倍）</td>
                </tr>
                <tr>
                    <td>啟用參數</td>
                    <td>210 億</td>
                    <td class="highlight-col">490 億（2.3 倍）</td>
                </tr>
                <tr>
                    <td>上下文</td>
                    <td>256K</td>
                    <td class="highlight-col">100 萬（4 倍）</td>
                </tr>
                <tr>
                    <td>OpenRouter 輸入</td>
                    <td>0.18 美元</td>
                    <td class="highlight-col">0.834 美元（4.6 倍）</td>
                </tr>
                <tr>
                    <td>OpenRouter 輸出</td>
                    <td>0.60 美元</td>
                    <td class="highlight-col">2.501 美元（4.2 倍）</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '騰訊開源混元 Hy4 模型，7,700 億參數、價格漲超 4 倍',
    'h1': '騰訊開源混元 Hy4 模型<br>7,700 億參數、價格漲超 4 倍',
    'subtitle': '騰訊發布並開源新一代 MoE 旗艦模型，規模大增但價格同步暴增',
    'source_url': 'https://www.blocktempo.com/tencent-hunyuan-hy4-preview-open-source-770b-moe-context-pricing/',
    'source_name': 'BLOCKTEMPO',
    'pub_date': '2026-08-29',
    'img_alt': '騰訊混元 Hy4 模型示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260829_172430',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
    for e in errors:
        print(f"  注意: {e}")
else:
    print("❌ HTML 生成失敗")
    for e in errors:
        print(f"  錯誤: {e}")
    sys.exit(1)
