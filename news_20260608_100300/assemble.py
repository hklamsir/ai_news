#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.zdnet.com/article/i-tried-google-drives-new-ai-cleanup-tool-storage-clutter/" target="_blank">ZDNET</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-04</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>ZDNET 記者親身測試 Google Drive 全新 AI 整理工具「Organize My Files」，嘗試清理 14 年累積的 340GB 混亂數據。工具能否幫助擺脫每月 $20 美元的 Google AI Pro 訂閱？</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>工具定位：有限的整理想法</h4>
                <p>這功能利用 Gemini AI 分析 Drive 中的散落文件，自動建議移至現有文件夾或創建新文件夾分類。用戶可在「Suggest File Moves」按鈕中查看所有建議，逐項審批後再執行移動。</p>
                <p><strong>實際測試結果：</strong>Gemini 只推薦了 19 項移動建議，大多是近期創建或上傳的文件，舊文件、大量垃圾文件幾乎完全被忽略。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">✅</div>
            <div class="tech-card-content">
                <h4>合理與荒謬並存</h4>
                <p><strong>合理的建議：</strong>將簡歷移入「resume」文件夾、創建「Family and Real Estate」收納房屋契約、創建「Travel Planning」整理旅遊行程。</p>
                <p><strong>荒謬的建議：</strong>把名為「Delete」的文件（記者本想刪除的）歸入「Travel Planning」——Gemini 完全無法識別明顯需要刪除的垃圾。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>感覺像半成品</h4>
                <p>記者跑了兩次工具，第二次在 30 秒內給出完全相同的建議。對一個有數千個文件夾、多年垃圾數據的用戶來說，這遠遠不夠。</p>
                <p>記者結論：「這不是我期望的 Drive 清理助手。也許 Google 以後會改善，但現在我仍被困在一個混亂的 Drive 和每月 $20 美元的 AI Pro 訂閱裡。」</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📊 記者實測數據</h4>
            <p>14 年累積數據：340GB | Gemini推薦整理：19 項 | 訂閱費用：每月 $20 美元 Google AI Pro</p>
        </div>

        <div class="quote-box">
            <p>這不是我期望的 Drive 清理助手。也許 Google 以後會改善，但現在我仍被困在一個混亂的 Drive 和每月 $20 美元的 AI Pro 訂閱裡。</p>
            <cite>— ZDNET 記者 Elyse Betters Picaro</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>「Organize My Files」反映 AI 助手在文件管理領域的潛力與局限——它能處理表面的、近期的文件整理，但無法理解更深層的個人文件價值觀。短期內，用戶仍需手動介入大量清理工作。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年初</div>
                <div class="timeline-title">Google 推出「Organize My Files」beta</div>
                <div class="timeline-desc">向一小部分用戶開放測試</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-06-02</div>
                <div class="timeline-title">正式脫離 beta 公開上線</div>
                <div class="timeline-desc">所有 Workspace 用戶和 AI訂閱者均可使用</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">實測過程</div>
                <div class="timeline-title">記者 запускает 工具兩次</div>
                <div class="timeline-desc">第二次在 30 秒內給出完全相同的建議，暴露工具深度分析能力不足</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">實測結果</div>
                <div class="timeline-title">19 項推薦 vs 340GB 垃圾</div>
                <div class="timeline-desc">Gemini 的建議僅覆蓋近期文件，舊垃圾完全被忽略</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">業界反應</div>
                <div class="timeline-title">工具被評為「半成品」</div>
                <div class="timeline-desc">用戶期望的功能與實際表現落差明顯</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>記者情況</th>
                    <th>Gemini 表現</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>數據量</td>
                    <td>340GB / 14 年</td>
                    <td class="highlight-col">覆蓋有限</td>
                </tr>
                <tr>
                    <td>整理建議</td>
                    <td>預期全面清理</td>
                    <td class="highlight-col">僅 19 項</td>
                </tr>
                <tr>
                    <td>垃圾識別</td>
                    <td>期望 AI 主動刪除</td>
                    <td class="highlight-col">完全無法識別</td>
                </tr>
                <tr>
                    <td>重複運行</td>
                    <td>期望更深度分析</td>
                    <td class="highlight-col">30 秒後給出完全相同建議</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '14 年 Google Drive 亂檔有救？AI 整理工具實測報告 | ZDNET',
    'h1': 'Google Drive AI 整理工具<br>實測結果出爐',
    'subtitle': '14 年累積 340GB 垃圾：Gemini 只推薦了 19 項整理建議',
    'source_url': 'https://www.zdnet.com/article/i-tried-google-drives-new-ai-cleanup-tool-storage-clutter/',
    'source_name': 'ZDNET',
    'pub_date': '2026-06-04',
    'img_alt': 'Google Drive AI 整理助手概念圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260608_100300',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ 文章組裝成功")
else:
    print(f"❌ 失敗：{errors}")
    sys.exit(1)