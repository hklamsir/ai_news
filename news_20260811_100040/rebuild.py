#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.reuters.com/business/microsoft-plans-unveil-its-new-maia-300-ai-chip-this-fall-information-reports-2026-08-10/" target="_blank">Reuters</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-10</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>微軟計劃於 2026 年秋季發布 Maia 300 AI 晶片，正與台積電協商在 2027 年量產超過 30 萬顆晶片，目標減少對 Nvidia 晶片的依賴，追趕 Google 和 Amazon 在自研 AI 晶片方面的領先地位。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📅</div>
            <div class="tech-card-content">
                <h4>秋季發布計劃</h4>
                <p>Maia 300 預計於 2026 年秋季發布，最快可能 9 月亮相。這是微軟在自研 AI 晶片領域的重要一步。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏭</div>
            <div class="tech-card-content">
                <h4>與台積電車量產談判</h4>
                <p>微軟正與台積電協商，爭取 2027 年交付超過 30 萬顆晶片的產能，長期目標是確保超過 100 萬顆晶片的製造產能。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚔️</div>
            <div class="tech-card-content">
                <h4>追趕 Google 和 Amazon</h4>
                <p>微軟在自研 AI 晶片方面落後於對手。Google 已從 TPU 銷售確認營收，Amazon 的 Trainium 晶片亦獲得越來越多客戶採用。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤝</div>
            <div class="tech-card-content">
                <h4>Anthropic 合作談判</h4>
                <p>微軟希望說服 Anthropic 等主要客戶採用 Maia 晶片。Anthropic 已與 Amazon 達成 10 年 Trainium 合作協議，並計劃使用 Google TPU。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點數據</h4>
            <p>微軟目標 2027 年交付 <strong>30 萬+</strong> 顆 Maia 300 晶片，長期產能目標超過 <strong>100 萬顆</strong>。</p>
        </div>

        <div class="quote-box">
            <p>「微軟持續投資自訂矽晶片，作為長期 AI 基礎設施策略的一部分。生產數據並未反映我們項目的規模。」</p>
            <cite>— Andrew Wall，Azure Maia 總經理</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>微軟的 Maia 300 計劃顯示，其正積極追趕 Google 和 Amazon 在自研 AI 晶片方面的領先地位。降低對 Nvidia 的依賴已成為各大雲端服務商的當務之急。不過，組件供應和台積電生產線分配可能為此目標帶來挑戰。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2023 年 11 月</div>
                <div class="timeline-title">首款 Maia 晶片發布</div>
                <div class="timeline-desc">微軟發布首款自研 AI 晶片 Maia</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 1 月</div>
                <div class="timeline-title">Maia 200 亮相</div>
                <div class="timeline-desc">第二代 Maia 200 發布，採用台積電 3 奈米製程</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 8 月</div>
                <div class="timeline-title">Maia 300 計劃曝光</div>
                <div class="timeline-desc">The Information 報道微軟秋季發布計劃</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 9 月（預計）</div>
                <div class="timeline-title">Maia 300 發布</div>
                <div class="timeline-desc">最快可能 9 月正式發布</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2027 年（預計）</div>
                <div class="timeline-title">量產交付</div>
                <div class="timeline-desc">目標交付 30 萬+ 顆晶片</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>公司</th>
                    <th>自研 AI 晶片</th>
                    <th>現況</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Google</td>
                    <td>Tensor Processing Unit (TPU)</td>
                    <td class="highlight-col">已開始確認營收</td>
                </tr>
                <tr>
                    <td>Amazon</td>
                    <td>Trainium</td>
                    <td class="highlight-col">獲得越來越多客戶採用</td>
                </tr>
                <tr>
                    <td>Microsoft</td>
                    <td>Maia 系列</td>
                    <td>追趕中，Maia 300 秋季發布</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '微軟秋季發布 Maia 300 AI 晶片　與台積電協商量產 30 萬顆 | Reuters',
    'h1':          '微軟秋季發布 Maia 300 AI 晶片<br>與台積電協商量產 30 萬顆',
    'subtitle':    '微軟正與台積電車量產談判，目標 2027 年交付，落後 Google Amazon 自研晶片步伐',
    'source_url':  'https://www.reuters.com/business/microsoft-plans-unveil-its-new-maia-300-ai-chip-this-fall-information-reports-2026-08-10/',
    'source_name': 'Reuters',
    'pub_date':    '2026-08-10',
    'img_alt':     '微軟 Maia 300 AI 晶片示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260811_100040',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 重建成功")
else:
    print(f"❌ HTML 重建失敗：{errors}")
    sys.exit(1)
