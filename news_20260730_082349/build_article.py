#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://youtu.be/Fy6tKSHGEXQ" target="_blank">Best Partners TV</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-30</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成（字幕下載 + 整理）</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>DeepSeek 創辦人梁文鋒的內部講話被全網封殺，展現中國 AI 創辦人最坦誠的戰略思考：克制、開源、只盯 AGI 主線，用美國二十分之一的算力做出世界級成果。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🌟</div>
            <div class="tech-card-content">
                <h4>願景與克制哲學</h4>
                <p>DeepSeek 的出發點不是賺錢上市，而是「對人類有用、對世界懷著善意」。梁文鋒直言：「克制不是情懷，是戰略。」十個月收回設備成本的定價，只賺合理利潤，是克制的具體體現。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔓</div>
            <div class="tech-card-content">
                <h4>開源是戰略選擇</h4>
                <p>AI 最終可能佔 GDP 10%，這麼大的事情沒有人能獨佔。梁文鋒認為：「越想獨佔越做不成。」開源是讓利，定價低也是讓利，對外讓社會高興，對內讓員工有成就感。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🧠</div>
            <div class="tech-card-content">
                <h4>AGI 階梯式路線圖</h4>
                <p>DeepSeek 的 AGI 路線圖分為多個階梯：當前（超越人類）→ Agent（智能上限更高）→ 持續學習（關鍵突破）→ 奇點（模型自己開發自己）→ 具身智能（走進現實）。選擇這個順序是因為「這條路最輕鬆」。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>中美差距：落後一至兩年，算力差一個數量級</h4>
                <p>美國最大模型激活約 800B 參數，國內還在幾十 B 規模，落後一個數量級。但 DeepSeek 用美國二十分之一的算力把事情做出來了，目標是把時間差縮到六個月、三個月。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 核心數據</h4>
            <ul>
                <li><strong>中美算力差距</strong>：美國 800B 參數 vs 中國幾十 B，差一個數量級</li>
                <li><strong>DeepSeek 效率</strong>：用美國 1/20 算力做出同等成果</li>
                <li><strong>定價哲學</strong>：十個月收回設備成本，只賺合理利潤</li>
                <li><strong>訓練目標</strong>：150B 模型樂觀估計今年年底開始訓練</li>
            </ul>
        </div>

        <div class="quote-box">
            <p>「克制不是情懷，是戰略。捨棄一些東西可以換來更多其他的東西。」</p>
            <cite>— 梁文鋒，DeepSeek 創辦人</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這份被全網封殺的內部講話，展現了梁文鋒對中國 AI 發展的極致戰略清醒。他算的不是一兩年的賬，而是十年二十年的賬；爭的不是一城一池，而是誰能走到 AGI 終點的概率。在所有公司都在搶應用、搶商業化、搶入口的行業氛圍下，選擇慢、選擇克制、只盯著 AGI 主線的 DeepSeek，能否真的跑到終點，值得持續關注。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2022 年</div>
                <div class="timeline-title">DeepSeek 成立</div>
                <div class="timeline-desc">懷著對人類有用的善意，幾十個人開始做這件事</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2023 年</div>
                <div class="timeline-title">開源策略確立</div>
                <div class="timeline-desc">從一開始就想清楚開源是願景要求，也是客觀規律</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2024 年春節</div>
                <div class="timeline-title">DeepSeek 突然走紅</div>
                <div class="timeline-desc">沒有追求 C 端變現，堅持克制，維持低成本用戶</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">V3 訓練成功</div>
                <div class="timeline-desc">用 TileLang 完全繞過 CUDA，生態話語權提升</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">演講洩露風波</div>
                <div class="timeline-desc">四小時內部會議實錄被洩漏，全網遭封殺，融資暫停</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>DeepSeek（中國）</th>
                    <th>OpenAI（美國）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>最大模型規模</td>
                    <td>幾十 B 參數</td>
                    <td class="highlight-col">800B 參數</td>
                </tr>
                <tr>
                    <td>算力使用效率</td>
                    <td class="highlight-col">美國 1/20 算力</td>
                    <td>完整算力</td>
                </tr>
                <tr>
                    <td>商業策略</td>
                    <td class="highlight-col">克制、合理利潤</td>
                    <td>追求市場份額</td>
                </tr>
                <tr>
                    <td>開源策略</td>
                    <td class="highlight-col">完全開源</td>
                    <td>部分開源</td>
                </tr>
                <tr>
                    <td>與美國時間差</td>
                    <td>落後 1-2 年</td>
                    <td class="highlight-col">領先</td>
                </tr>
            </tbody>
        </table>

        <h3>💡 其他關鍵觀點</h3>
        <div class="tech-card">
            <div class="tech-card-icon">🇨🇳</div>
            <div class="tech-card-content">
                <h4>國產芯片機遇</h4>
                <p>CUDA 護城河正在瓦解：AI 幫助構建生態、TileLang 可快速重寫生態、專用芯片不再綁定 CUDA。華為 950 性能可平替 GB200，代價是四張華為卡頂一張英偉達卡。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">👥</div>
            <div class="tech-card-content">
                <h4>團隊穩定性是核心利益</h4>
                <p>只要團隊不散繼續做下去，就一定能做成 AGI。錢和資源都不是問題。DeepSeek 人才流動率一直比同行低，因為很多人「不是全奔著錢來的，是希望在能做成 AGI 的環境裡做事」。</p>
            </div>
        </div>
"""

metadata = {
    'title': '梁文鋒四小時講話為何被全網封殺',
    'h1': '梁文鋒四小時講話<br>為何被全網封殺',
    'subtitle': 'DeepSeek 創辦人內部會議實錄：AGI、開源、克制與終局思維',
    'source_url': 'https://youtu.be/Fy6tKSHGEXQ',
    'source_name': 'Best Partners TV',
    'pub_date': '2026-07-30',
    'img_alt': '梁文鋒 DeepSeek AGI 講話',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260730_082349',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")
