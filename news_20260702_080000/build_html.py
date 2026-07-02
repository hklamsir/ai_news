#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/06/30/google-introduces-a-faster-cheaper-image-generator-with-nano-banana-2-lite/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-30</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Google 推出全新 AI 圖像生成模型 Nano Banana 2 Lite，專為需要快速大量生成圖像的工作流程而優化，並支援 Gemini API 企業平台。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>Nano Banana 2 Lite 定位</h4>
                <p>Nano Banana 2 被定位為「通用主力馬」，而 Nano Banana 2 Lite 則專為需要高速、高吞吐量的大量圖像生成工作流程而設。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💡</div>
            <div class="tech-card-content">
                <h4>應用場景</h4>
                <p>Google 將其定位為廣告創作的輔助工具。儘管消費者對 AI 生成圖像（俗稱「AI 垃圾」）有所反彈，但企業仍持續大力投資 AI 圖像與影片工具。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎬</div>
            <div class="tech-card-content">
                <h4>Gemini Omni Flash 影片模型</h4>
                <p>Google 同時宣布擴大發布 Gemini Omni Flash，該模型於 Google I/O 大會首次亮相，影片輸出收費為每秒 $0.10 美元。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>Omni Product Studio</h4>
                <p>全新示範應用 Omni Product Studio 可將 Omni 生成的靜態圖像轉化為「電影級電子商務影片」，助力電子商務行銷。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Nano Banana 2 Lite 現已可在 Google AI Studio、Gemini API 及 Gemini Enterprise Agent Platform 使用，並作為 Nano Banana（傳統模型）的替代品。</p>
        </div>

        <div class="quote-box">
            <p>「Building with generative media is often about creative iteration. With these two models, developers can build comprehensive, end-to-end multimedia experiences that connect rapid image generation with video creation and editing.」</p>
            <cite>— Google 官方部落格</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>生成式媒體的建立在於創意迭代。Google 表示有了 Nano Banana 2 Lite 與 Gemini Omni Flash 這兩個模型，開發者可以建立完整、端對端的多媒體體驗，連接快速圖像生成與影片創作及編輯。同時，Google 與 A24 的 $7500 萬美元合作協議也顯示 AI 公司正積極與好萊塢建立更深的合作關係。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026-05</div>
                <div class="timeline-title">Google I/O 大會</div>
                <div class="timeline-desc">Gemini Omni Flash 首次亮相</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-06-30</div>
                <div class="timeline-title">Nano Banana 2 Lite 發布</div>
                <div class="timeline-desc">正式推出 Nano Banana 2 Lite 圖像生成模型</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-06-30</div>
                <div class="timeline-title">Gemini Omni Flash 擴大發布</div>
                <div class="timeline-desc">擴大發布 Gemini Omni Flash 影片模型</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-06-30</div>
                <div class="timeline-title">Omni Product Studio 展示</div>
                <div class="timeline-desc">展示全新 Omni Product Studio 應用</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">近期</div>
                <div class="timeline-title">Google 與 A24 合作</div>
                <div class="timeline-desc">簽署 $7500 萬美元合作協議，引發爭議</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>Nano Banana 2</th>
                    <th>Nano Banana 2 Lite</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>定位</td>
                    <td>通用主力馬（Generalist workhorse）</td>
                    <td class="highlight-col">高吞吐量快速工作流程</td>
                </tr>
                <tr>
                    <td>用途</td>
                    <td>進階應用場景</td>
                    <td class="highlight-col">大量快速圖像生成</td>
                </tr>
                <tr>
                    <td>狀態</td>
                    <td>旗艦模型</td>
                    <td class="highlight-col">Nano Banana 替代品</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Google 推出快速平價圖像生成器 Nano Banana 2 Lite | TechCrunch',
    'h1':          'Google 推出快速平價圖像生成器<br>Nano Banana 2 Lite',
    'subtitle':    '專為高速、高吞吐量工作流程優化的 AI 圖像生成模型',
    'source_url':  'https://techcrunch.com/2026/06/30/google-introduces-a-faster-cheaper-image-generator-with-nano-banana-2-lite/',
    'source_name': 'TechCrunch',
    'pub_date':    '2026-06-30',
    'img_alt':     'Google Nano Banana 2 Lite AI 圖像生成技術示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260702_080000',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print(f"❌ HTML 組裝失敗：{errors}")
    sys.exit(1)
