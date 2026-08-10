#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://unwire.hk/2026/08/09/apple-qwen-mac-china/ai/" target="_blank">UNWIRE</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-09</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Apple 確認合資格中國大陸 Mac 用戶可將阿里巴巴千問 (Qwen) AI 服務連接至 Siri 及寫作工具，成為 Qwen 正式進駐 Apple 產品生態的第一步，歷時近 22 個月的規管審批終獲放行。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔧</div>
            <div class="tech-card-content">
                <h4>啟用需符合多重條件</h4>
                <p>用戶須運行 <strong>macOS 26.6+</strong>、Apple ID 地區設定為中國大陸、Mac 須為中國大陸版本，且用戶實際身處當地。啟用後仍需自行登入千問帳戶。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎙️</div>
            <div class="tech-card-content">
                <h4>Siri 與寫作工具整合</h4>
                <p>Siri 可將複雜提問交由千問處理（如撰寫詩詞、總結檔案），每次動用前會先徵詢用戶同意。寫作工具可利用千問生成文字或圖片內容。Apple 強調用戶資料不會用於模型訓練。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⏱️</div>
            <div class="tech-card-content">
                <h4>規管審批歷時近兩年</h4>
                <p>是次更新源於中國網信辦 (CAC) 7 月 15 日批准。Apple 早於 2024 年 iPhone 16 發布會預告 Apple Intelligence 將登陸中國，因規管要求外國 AI 須配合本地模型，延遲近 <strong>22 個月</strong>。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌏</div>
            <div class="tech-card-content">
                <h4>香港用戶不受影響</h4>
                <p>今次開放只限中國大陸合資格裝置，香港 Mac 用戶不會自動轉用千問，亦毋須更改任何設定。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>千問將全面整合至 iOS、iPadOS、macOS 及 visionOS，用戶可直接在 Apple 介面內使用文字及圖像理解與生成功能。百度亦證實有份參與當地 AI 開發工作。</p>
        </div>

        <div class="quote-box">
            <p>「同一部 Mac 或 iPhone，日後可能因應地區、帳戶及監管要求，使用不同人工智能引擎運作。」</p>
            <cite>— UNWIRE 分析</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>隨着千問正式接入 Apple 系統，全球 AI 平台之爭正式伸延至作業系統層面。Apple 正就不同市場採取「因地制宜」的 AI 模型策略，未來同一設備或因地區差異使用不同 AI 引擎。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2024 年</div>
                <div class="timeline-title">Apple Intelligence 預告登陸中國</div>
                <div class="timeline-desc">iPhone 16 發布會預告 AI 功能將登陸中國市場</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2024-2026</div>
                <div class="timeline-title">規管審批階段</div>
                <div class="timeline-desc">因中國法規要求外國 AI 須配合本地模型，審批延遲近 22 個月</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-15</div>
                <div class="timeline-title">網信辦批准</div>
                <div class="timeline-desc">中國網信辦 (CAC) 正式批准 Apple 與千問整合</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-08-08</div>
                <div class="timeline-title">Apple 發布支援指引</div>
                <div class="timeline-desc">Apple 官方支援網站發布千問擴充功能設定指南</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">全面整合至 Apple 系統</div>
                <div class="timeline-desc">千問將覆蓋 iOS、iPadOS、macOS、visionOS 全平台</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>中國大陸 Mac</th>
                    <th>香港/其他地區 Mac</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>macOS 版本要求</td>
                    <td class="highlight-col">macOS 26.6+</td>
                    <td>其他版本</td>
                </tr>
                <tr>
                    <td>Apple ID 地區</td>
                    <td class="highlight-col">中國大陸</td>
                    <td>當地設定</td>
                </tr>
                <tr>
                    <td>千問整合</td>
                    <td class="highlight-col">✅ 已獲批准</td>
                    <td>❌ 暫不適用</td>
                </tr>
                <tr>
                    <td>Siri + 千問</td>
                    <td class="highlight-col">可用</td>
                    <td>不可用</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '阿里 Qwen 正式駁入 Apple 生態 中國大陸 Mac 用戶率先使用',
    'h1':          '阿里 Qwen 正式駁入 Apple 生態<br>中國大陸 Mac 用戶率先使用',
    'subtitle':    '22 個月規管審批終獲放行，千問將全面整合至 Apple 全系統',
    'source_url':  'https://unwire.hk/2026/08/09/apple-qwen-mac-china/ai/',
    'source_name': 'UNWIRE',
    'pub_date':    '2026-08-09',
    'img_alt':     'Qwen 3.5 智能手機展示',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260810_113552',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print(f"❌ HTML 組裝失敗: {errors}")
    sys.exit(1)
