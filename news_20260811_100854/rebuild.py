#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://unwire.hk/2026/08/08/token-vs-ciyuan-ai-terms/ai/" target="_blank">UNWIRE</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-08</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>中國官媒人民網發表評論，批評英文 AI 術語 Token、Agent 氾濫，警告這將威脅國家科技話語權，呼籲推廣「詞元」、「智慧體」等標準中文譯名。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📢</div>
            <div class="tech-card-content">
                <h4>人民網發出警告</h4>
                <p>北京時間 8 月 5 日，人民網旗下「人民銳評」專欄發表《用"Token"還是"詞元"，事關科技話語權》文章，批評英文 AI 術語氾濫。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>三大危害</h4>
                <p>1. 大幅擠壓漢語表意空間<br>2. 擴大社會數位落差<br>3. 侵蝕漢語體系完整性</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔄</div>
            <div class="tech-card-content">
                <h4>歷史成功案例</h4>
                <p>過去 Computer→「電腦」、Internet→「網際網路」等譯名成功融入漢語體系，如今的問題是 Token、Agent、LLM 只以英文縮寫出現。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌏</div>
            <div class="tech-card-content">
                <h4>分層有序建議</h4>
                <p>國際學術交流保留英文；國內公共傳播、教育、政策普及則推廣「詞元」（Token）、「智慧體」（Agent）等標準中文譯名。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 核心呼籲</h4>
            <p>人民網呼籲相關部門優化術語審定機制，媒體與科技企業應主動踐行規範表達，引導青年樹立母語自覺。</p>
        </div>

        <div class="quote-box">
            <p>「術語是科技敘事的基礎單元。如果核心概念的定義權與闡釋權始終掌握在他人手中，具有中國特色的科技話語體系將無從建立。」</p>
            <cite>— 人民網《人民銳評》</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>在 AI 席捲全球之際，語言已成為國家科技戰略競爭的隱形戰場。中國此舉反映其在科技自主話語權方面的戰略考量，如何平衡本土化與國際接軌需求將是重要課題。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 8 月 5 日</div>
                <div class="timeline-title">人民網發表文章</div>
                <div class="timeline-desc">人民網旗下「人民銳評」發表《用"Token"還是"詞元"，事關科技話語權》</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">過去成功譯名</div>
                <div class="timeline-title">電腦、網際網路</div>
                <div class="timeline-desc">Computer→電腦、Internet→網際網路，成功融入漢語體系</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">現今問題</div>
                <div class="timeline-title">英文縮寫氾濫</div>
                <div class="timeline-desc">Token、Agent、LLM 等術語只以英文縮寫出現，缺乏本土化</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">建議方案</div>
                <div class="timeline-title">分層有序</div>
                <div class="timeline-desc">國際學術用英文，國內推廣「詞元」「智慧體」等中文譯名</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">長遠影響</div>
                <div class="timeline-title">科技話語權</div>
                <div class="timeline-desc">若不積極應對，恐喪失 AI 領域話語主動權</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>譯名對比</th>
                    <th>英文術語</th>
                    <th>建議中文譯名</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Token</td>
                    <td class="highlight-col">Token</td>
                    <td>詞元</td>
                </tr>
                <tr>
                    <td>Agent</td>
                    <td class="highlight-col">Agent</td>
                    <td>智慧體 / 智能體</td>
                </tr>
                <tr>
                    <td>LLM</td>
                    <td class="highlight-col">LLM</td>
                    <td>大型語言模型</td>
                </tr>
                <tr>
                    <td>Computer</td>
                    <td>Computer</td>
                    <td class="highlight-col">電腦（已成功）</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '中國官媒批評 AI 術語濫用英文　稱「Token」與「Agent」動搖科技話語權 | UNWIRE',
    'h1':          '中國官媒批評 AI 術語濫用英文<br>稱「Token」與「Agent」動搖科技話語權',
    'subtitle':    '人民網發表文章，批評英文 AI 術語氾濫，呼籲推廣「詞元」「智慧體」等標準中文譯名',
    'source_url':  'https://unwire.hk/2026/08/08/token-vs-ciyuan-ai-terms/ai/',
    'source_name': 'UNWIRE',
    'pub_date':    '2026-08-08',
    'img_alt':     '中國官媒批評 AI 術語英文濫用示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260811_100854',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 重建成功")
else:
    print(f"❌ HTML 重建失敗：{errors}")
    sys.exit(1)
