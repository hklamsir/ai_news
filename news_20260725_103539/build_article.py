#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/07/23/ai-chip-startup-etched-defies-skeptics-hits-10-3b-valuation-from-big-name-investors/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-23</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>由三位哈佛大學輟學生於 2022 年創立的 AI 晶片新創公司 Etched，成功完成 3 億美元 C 輪融資，估值一舉攀升至 103 億美元，投資陣容包括 Sequoia、Andreessen Horowitz、Peter Thiel、Andrej Karpathy 等大咖。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>公司由來與市場質疑</h4>
                <p>Etched 成立之際，專門為基於 Transformer 架構的 AI 模型設計晶片，被外界視為「瘋狂」之舉。當時多數人認為「只有 GPU 才能做 AI」，對專用晶片的前景存疑。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>投資陣容星光熠熠</h4>
                <p>本輪由傳奇創投 Sequoia 領投，另有 Andreessen Horowitz、SK Hynix、Jane Street、Diffusion Capital 參與。天使投資人包括 Peter Thiel、Andrej Karpathy（前特斯拉 AI 總監）、Dylan Field（Figma 創辦人）、Amjad Masad（Replit 創辦人）。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏭</div>
            <div class="tech-card-content">
                <h4>產品策略：整機銷售而非單晶片</h4>
                <p>Etched 的產品以整機系統形式銷售，而非單獨出售晶片。創辦人 Wachen 強調，核心專長是從零開始設計推論加速元件，顯著提升 AI 推論效率。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>技術差異化</h4>
                <p>與 NVIDIA 等通用 GPU 不同，Etched 專注於優化特定 AI 任務的運算效率，尤其針對 Transformer 架構模型，在特定場景下可實現比通用晶片更高的性價比。</p>
            </div>
        </div>


        <div class="highlight-box">
            <h4>📌 重點數據</h4>
            <ul>
                <li><strong>估值：</strong>103 億美元（約 10.3B USD）</li>
                <li><strong>融資金額：</strong>3 億美元（Series C）</li>
                <li><strong>創辦年份：</strong>2022 年</li>
                <li><strong>創辦人背景：</strong>三位哈佛大學輟學生</li>
            </ul>
        </div>

        <div class="quote-box">
            <p>「Etched 成立時，專門為 Transformer 架構設計 AI 晶片被視為瘋狂之舉，現在我們用成績回應質疑。」</p>
            <cite>— Robert Wachen，Etched 共同創辦人兼營運長</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Etched 的成功反映 AI 晶片市場正在走向多元化。隨著生成式 AI 應用場景持續細分，專用晶片的需求日益明確。從不被看好到估值破百億美元，Etched 用實際成果回應了質疑，也為整個 AI 硬體賽道注入更多想像空間。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2022 年</div>
                <div class="timeline-title">公司成立</div>
                <div class="timeline-desc">三位哈佛大學輟學生創立 Etched，專注 Transformer 架構 AI 晶片</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">創業初期</div>
                <div class="timeline-title">市場質疑</div>
                <div class="timeline-desc">外界普遍認為「只有 GPU 才能做 AI」，專用晶片路線不被看好</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年中</div>
                <div class="timeline-title">產品上市</div>
                <div class="timeline-desc">推出整機系統產品，強調推論加速效能優勢</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月</div>
                <div class="timeline-title">C 輪融資</div>
                <div class="timeline-desc">完成 3 億美元融資，由 Sequoia 領投，估值達 103 億美元</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來展望</div>
                <div class="timeline-title">持續擴張</div>
                <div class="timeline-desc">計畫擴大市場份額，挑戰 NVIDIA 在 AI 晶片領域的主導地位</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>對比項目</th>
                    <th>Etched（專用晶片）</th>
                    <th>NVIDIA GPU（通用晶片）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>設計目標</td>
                    <td>Transformer 架構 AI 模型</td>
                    <td class="highlight-col">各類型 AI 任務</td>
                </tr>
                <tr>
                    <td>推論效率</td>
                    <td class="highlight-col">特定場景效能更佳</td>
                    <td>通用性強</td>
                </tr>
                <tr>
                    <td>產品形態</td>
                    <td class="highlight-col">整機系統</td>
                    <td>晶片/顯卡</td>
                </tr>
                <tr>
                    <td>市場定位</td>
                    <td>細分市場專用</td>
                    <td class="highlight-col">主流市場領導者</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'AI 晶片新創 Etched 逆勢突圍，獲大咖投資人加持估值達 103 億美元 | TechCrunch',
    'h1':          'AI 晶片新創 Etched<br>逆勢突圍估值破百億',
    'subtitle':    '三位哈佛輟學生打造的 AI 專用晶片新創，獲 Sequoia、a16z 加持，估值達 103 億美元',
    'source_url':  'https://techcrunch.com/2026/07/23/ai-chip-startup-etched-defies-skeptics-hits-10-3b-valuation-from-big-name-investors/',
    'source_name': 'TechCrunch',
    'pub_date':    '2026-07-23',
    'img_alt':     'Etched AI 晶片示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260725_103539',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print("❌ HTML 生成失敗")
    for err in errors:
        print(f"   - {err}")
