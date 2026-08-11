#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://newsletter.semianalysis.com/p/gemini-is-cooked-but-gcp-is-cooking" target="_blank">Semianalysis</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-07</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Semianalysis 報道指出 Google Gemini AI 模型已落後競爭對手，但 Google Cloud Platform（GCP）却強勢增長，季度營收增長達 82%，TPU 銷售成為新增長引擎。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📉</div>
            <div class="tech-card-content">
                <h4>Gemini 落後　3 Pro 成高峰</h4>
                <p>2025 年 11 月 Gemini 3 Pro 曾是全球最強模型，但 2026 年已明顯落後於 Anthropic 和 OpenAI。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📈</div>
            <div class="tech-card-content">
                <h4>GCP 強勢增長 82%</h4>
                <p>上季 GCP 增長率達 82%，部分來自 TPU 系統銷售，向 Anthropic 等客戶提供運算資源。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>TPU 銷售成新增長點</h4>
                <p>Q2 2026 TPU 銷售約 12 億美元，訂單儲備超過 1500 億美元，預計 2027 年驅動 GCP 增長至 100%+。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏆</div>
            <div class="tech-card-content">
                <h4>Thomas Kurian 勝出</h4>
                <p>雲端負責人 Thomas Kurian 在內部資源争夺中取得勝利，GCP 收入增長預計將顯著加速。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點數據</h4>
            <p>GCP 季度增長 <strong>82%</strong>，TPU 訂單儲備 <strong>$1500 億+</strong>，2027 年增長預計達 <strong>100%+</strong></p>
        </div>

        <div class="quote-box">
            <p>「短期金融化收益，值得犧牲前沿競爭力。」</p>
            <cite>— Semianalysis 批評 Google AI 策略</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Google 選擇將資源投入雲端 TPU 銷售業務而非提升 Gemini 實力，這種「金融化」策略或許能帶來短期收益，但長期而言可能削弱其在 AI 競賽中的地位。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2025 年 11 月</div>
                <div class="timeline-title">Gemini 3 Pro 高峰</div>
                <div class="timeline-desc">Gemini 3 Pro 曾是全球最強模型，令 OpenAI 發出紅色警報</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 Q1</div>
                <div class="timeline-title">DeepMind 成本飆升</div>
                <div class="timeline-desc">DeepMind/Gemini 培訓費用達每季 $54 億美元</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 Q2</div>
                <div class="timeline-title">GCP 增長 82%</div>
                <div class="timeline-desc">TPU 銷售約 $12 億美元成為新增長引擎</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">Gemini 明顯落後</div>
                <div class="timeline-desc">Anthropic 和 OpenAI 遙遙領先</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2027 年（預計）</div>
                <div class="timeline-title">GCP 增長 100%+</div>
                <div class="timeline-desc">TPU 銷售驅動，分析師共識僅 64%</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>Gemini</th>
                    <th>GCP</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>ARR（年度經常性收入）</td>
                    <td>$12 億</td>
                    <td class="highlight-col">$730 億+（預計 2027）</td>
                </tr>
                <tr>
                    <td>TPU 銷售</td>
                    <td>—</td>
                    <td class="highlight-col">$1200 億（預計 2027）</td>
                </tr>
                <tr>
                    <td>季度增長</td>
                    <td>落後</td>
                    <td class="highlight-col">82%</td>
                </tr>
                <tr>
                    <td>市場地位</td>
                    <td>明顯落後</td>
                    <td class="highlight-col">強勢增長</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Gemini 已無力回天　但 Google Cloud 強勢增長 | Semianalysis',
    'h1':          'Gemini 已無力回天<br>但 Google Cloud 強勢增長',
    'subtitle':    'Semianalysis 報道：GCP 季度增長 82%，TPU 銷售成新增長引擎',
    'source_url':  'https://newsletter.semianalysis.com/p/gemini-is-cooked-but-gcp-is-cooking',
    'source_name': 'Semianalysis',
    'pub_date':    '2026-08-07',
    'img_alt':     'Google Cloud GCP 資料中心生長圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260811_182455',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 重建成功")
else:
    print(f"❌ HTML 重建失敗：{errors}")
    sys.exit(1)
