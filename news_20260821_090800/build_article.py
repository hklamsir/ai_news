#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.techbang.com/posts/131901-shieldfont-anti-ai-crawler-glyph-substitution" target="_blank">T客邦（cnBeta）</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-20</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>開源字型 ShieldFont 利用 OpenType 字形替換機制，讓人類看到正常文句、AI 爬蟲卻只能抓到無意義內容，為創作者對抗未授權 AI 數據採集提供全新武器。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔤</div>
            <div class="tech-card-content">
                <h4>「人機有別」的文字迷宮</h4>
                <p>ShieldFont 借用 OpenType 字型的「字形替換」功能，當人類透過瀏覽器造訪網頁時看到正常句子，但 AI 爬蟲抓取 HTML 原始碼時讀到的卻是截然不同的混亂內容。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📚</div>
            <div class="tech-card-content">
                <h4>嚴密語法對應精準污染AI訓練庫</h4>
                <p>ShieldFont 維持詞彙的語法屬性（名詞對名詞、過去式對過去式），使經處理的文本仍能通過 FineWeb-Edu 等品質過濾器，卻已扭曲超過半數事實陳述，讓 AI 訓練數據失去實用價值。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>限制與破解方式</h4>
                <p>目前 ShieldFont 僅支援英文。若攻擊者採用螢幕截圖加 OCR 技術仍可破解。此外，視障屏幕閱讀器也會讀出偽造文本，開發團隊已提供測試版無障礙功能作為應對。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🚀</div>
            <div class="tech-card-content">
                <h4>開源發布即取即用</h4>
                <p>ShieldFont 完整原始碼已於 GitHub 公開，可作為 React 組件輕鬆安裝至網頁中，為內容創作者提供主動出擊的全新選擇。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>約四分之一詞彙會被 ShieldFont 自動置換，但由於維持嚴謹語法結構，這些「毒化」文本仍能通過品質過濾器，從根本上破壞無授權抓取的商業效益。</p>
        </div>

        <div class="quote-box">
            <p>「ShieldFont 讓 AI 爬蟲只能蒐集到無效的錯誤資訊，從根本上破壞了無授權抓取的商業效益。」</p>
            <cite>— 開發團隊</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>ShieldFont 的出現標誌著內容創作者在面對 AI 時代數據採集浪潮時，終於擁有主動出擊的全新選擇。雖然並非完全無懈可擊，但這種結合字型技術與資訊安全的創新思維，已為網頁防禦開闢了新方向。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">AI 時代</div>
                <div class="timeline-title">大規模未授權抓取</div>
                <div class="timeline-desc">生成式 AI 崛起，網路文字數據成為各大公司爭相採集的資源</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">robots.txt</div>
                <div class="timeline-title">傳統防禦失效</div>
                <div class="timeline-desc">robots.txt 僅依賴爬蟲開發者自我約束，對刻意繞過的 AI 爬蟲缺乏約束力</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">ShieldFont 發布</div>
                <div class="timeline-title">OpenType 字形替換</div>
                <div class="timeline-desc">利用 OpenType 機制實現「人機有別」，人類看到正常文句、爬蟲看到亂碼</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">技術特點</div>
                <div class="timeline-title">語法維持機制</div>
                <div class="timeline-desc">約四分之一詞彙被替換，但仍能通過 FineWeb-Edu 品質過濾器</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">GitHub 開源</div>
                <div class="timeline-title">即取即用</div>
                <div class="timeline-desc">可作為 React 組件輕鬆安裝，為創作者提供主動防禦工具</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>對比項目</th>
                    <th>robots.txt</th>
                    <th>ShieldFont</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>約束力</td>
                    <td>依賴自我約束，無實質約束力</td>
                    <td class="highlight-col">技術層面强制實施</td>
                </tr>
                <tr>
                    <td>對AI爬蟲效果</td>
                    <td>可被刻意繞過</td>
                    <td class="highlight-col">使爬蟲只能抓到無意義內容</td>
                </tr>
                <tr>
                    <td>語法結構</td>
                    <td>不改變文字內容</td>
                    <td class="highlight-col">維持語法屬性對應，繞過品質過濾器</td>
                </tr>
                <tr>
                    <td>支援語言</td>
                    <td>所有語言</td>
                    <td class="highlight-col">目前僅支援英文</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '不想讓創作變AI飼料？全新開源字型「ShieldFont」登場，靠這招讓爬蟲抓到滿頭包',
    'h1':          '不想讓創作變AI飼料？<br>全新開源字型「ShieldFont」讓爬蟲抓到手足無措',
    'subtitle':    'ShieldFont 利用 OpenType 字形替換機制，讓人類看到正常文句、AI 爬蟲卻只能抓到無意義內容',
    'source_url':  'https://www.techbang.com/posts/131901-shieldfont-anti-ai-crawler-glyph-substitution',
    'source_name': 'T客邦',
    'pub_date':    '2026-08-20',
    'img_alt':     'ShieldFont 字型示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260821_090800',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print(f"❌ HTML 組裝失敗：{errors}")
    sys.exit(1)
