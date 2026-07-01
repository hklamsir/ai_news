#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.managertoday.com.tw/articles/view/72425" target="_blank">經理人（MANAGERTODAY）/ 未來商務</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-29</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>「未來兩年，一半的 PM 會被淘汰。」當 AI 把寫程式、做原型、整理文件全部接手，產品經理的核心價值已從「把事做對」轉向「做對的事」——也就是「場景想像力」。寓意科技執行長施政源表示，真正會被淘汰的，是不用 AI 的人。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📉</div>
            <div class="tech-card-content">
                <h4>PM 數量驟降三分之二</h4>
                <p>寓意科技自己的 PM 近兩年就少掉三分之二。執行長施政源表示，一方面是重新抓標準化，人太多反而不容易建立；另一方面，用 AI 的人跟不用 AI 的人，速度差至少兩到三倍（還是保守估計）。不用 AI，才是真正被淘汰的關鍵。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚡</div>
            <div class="tech-card-content">
                <h4>管理方式的根本改變</h4>
                <p>以前從客戶提出需求到交付，要經過 PM、系統分析師、架構師多個角色，規模稍大的專案至少要花一到一個半月才能跟客戶確認完。現在一個懂 AI 的人，可能一到兩天就能把底稿做出來，來回修改後不到一週就可以定稿。以前畫線稿要一到兩天，現在跟 AI 許願，一到兩個小時就能生出一個可以在瀏覽器上跑的雛形。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎯</div>
            <div class="tech-card-content">
                <h4>場景想像力比 PRD 更值錢</h4>
                <p>施政源指出，產品管理的核心能力是「掌舵、勾勒場景」。以前勾勒完場景，要花半年到一年才能讓客戶看到雛形；現在可能一個月到一個半月就能看到具體的東西。這讓「場景想像力」變得比以前更值錢，因為從想像到驗證的週期大幅縮短。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔄</div>
            <div class="tech-card-content">
                <h4>角色界線越來越模糊</h4>
                <p>界線模糊是百分之兩百確定的事，而且只會越來越模糊。2025 年 12 月他們成立了一個 vibe coding 部門，設了兩位 leader：一位 PM 出身、一位工程師出身。兩邊都在互相學、也一起跟 AI 學。不管工程師還是 PM，跟客戶使用者單位的距離越來越近。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>「Do the right thing, or do the thing right？」做對的事，還是把事做對。以前「把事做對」相對容易，但也費時；現在 AI 進來，把事做對這件事變得又快又便宜。真正難的，反而是「做對的事」——你要決定做什麼、為什麼做，這才是 PM 最核心的挑戰。</p>
        </div>

        <div class="quote-box">
            <p>「你今天這個服務，勾勒出的世界會長什麼樣？以前勾勒完場景，要花半年到一年才能讓客戶看到雛形；現在可能一個月到一個半月就能看到具體的東西。這讓『場景想像力』變得比以前更值錢。」</p>
            <cite>— 施政源，寓意科技創辦人兼執行長</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>施政源對工作者提出三個建議：第一，<strong>先學會用</strong> AI，唯有用了才知道哪些地方有用、哪些地方還得靠自己；第二，<strong>不要怕被取代</strong>，因為你能 cover 的範疇反而會變更大；第三，<strong>不要去管那條界線</strong>，不要被 R&R、頭銜和自尊綁住，讓角色的界線變模糊，你才會找到新的平衡點。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">訪談背景</div>
                <div class="timeline-title">《數位時代》黃亮崢專訪</div>
                <div class="timeline-desc">探討 AI 時代的 PM 到底要會什麼</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">過去做法</div>
                <div class="timeline-title">傳統專案流程</div>
                <div class="timeline-desc">PM 整理需求 → 系統分析師翻譯 → 架構師設計 → 排甘特圖，至少一到一個半月</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">現在做法</div>
                <div class="timeline-title">AI 加速流程</div>
                <div class="timeline-desc">懂 AI 的人一到兩天產底稿，一週內與客戶定稿，線稿由一到兩天縮短為一到兩小時</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年 12 月</div>
                <div class="timeline-title">成立 vibe coding 部門</div>
                <div class="timeline-desc">一位 PM 出身、一位工程師出身的 leader，互相學習並與 AI 協作</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來趨勢</div>
                <div class="timeline-title">PM 價值轉向</div>
                <div class="timeline-desc">從「把事做對」轉向「做對的事」，場景想像力比 PRD 更值錢</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>傳統 PM 模式</th>
                    <th>AI 時代 PM 模式</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>需求確認週期</td>
                    <td>1-1.5 個月</td>
                    <td class="highlight-col">不到 1 週</td>
                </tr>
                <tr>
                    <td>原型製作</td>
                    <td>1-2 天（線稿）</td>
                    <td class="highlight-col">1-2 小時（AI 生產）</td>
                </tr>
                <tr>
                    <td>核心能力</td>
                    <td>流程控制、甘特圖、PRD 撰寫</td>
                    <td class="highlight-col">場景想像力、判斷力、AI 運用</td>
                </tr>
                <tr>
                    <td>與客戶距離</td>
                    <td>每兩週交付一次、對焦一次</td>
                    <td class="highlight-col">日常混在一起、持續迭代</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '未來 2 年，一半的 PM 將被淘汰？寓意科技執行長：比寫 PRD 更值錢的是「場景想像力」',
    'h1': '未來 2 年，一半的 PM<br>將被淘汰？',
    'subtitle': '比寫 PRD 更值錢的是「場景想像力」',
    'source_url': 'https://www.managertoday.com.tw/articles/view/72425',
    'source_name': '經理人（MANAGERTODAY）/ 未來商務',
    'pub_date': '2026-06-29',
    'img_alt': 'AI 時代的 PM 需要場景想像力示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260701_192000',
    article_content=article_content,
    metadata=metadata
)

print(f"\n結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")