import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.mirrordaily.news/story/72148" target="_blank">鏡報（Mirror Daily）</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-09</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Google DeepMind 副總裁紀懷新表示，過去 20 年由搜尋推薦系統撐起的兆美元網路經濟，即將被具備「思維鏈」推理能力的 AI 打破。AI 將從預測下一個 token 升級至預測下一個 idea，催生能自動操控軟體工具的代理式 AI，整個網路生態系統將出現重大改變。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>搜尋推薦系統撐起兆美元產業</h4>
                <p>過去 20 年來，智慧型手機每一個 App 都是搜尋、推薦系統的變體。Google 搜尋引擎、YouTube、Instagram、抖音的短影音推薦，全都基於搜尋推薦系統。這個模式每年為全球網際網路產業帶來 1 兆美元的收入。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🧠</div>
            <div class="tech-card-content">
                <h4>思維鏈打破瓶頸：從預測 token 到預測 idea</h4>
                <p>過往大語言模型依賴機器學習預測下一個 token，但很快就遭遇瓶頸——因為它沒有辦法做多步驟推理。突破點在於「思維鏈」：訓練 AI 像教小孩子一樣——給小孩看數學題怎麼解，讓小孩從中學習解決問題的步驟，就能舉一反三。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>推理能力讓 AI 自動操控軟體工具</h4>
                <p>AI 發展出推理能力後，終於從預測下一個 token 升級至可以預測下一個 idea，能自動規劃步驟並操控軟體工具。以 Google 與加拿大電信業者 Bell 的合作案例：用户拿新網路設備不知道怎麼設定時，用 Google App 掃一掃就會自動引導。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚙️</div>
            <div class="tech-card-content">
                <h4>Agent Harness：讓 AI 代理不再「放飛自我」</h4>
                <p>矽谷正在發展「Agent Harness」（駕馭代理人），用來解決 AI 記憶力差、代理式 AI 不受控、資安風險等挑戰。不再依賴更新、更厲害的模型，而是把 AI 模型變成一個無需持續監督也能完成真實工作的可靠工人。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>紀懷新建議：「Agent Harness 台灣一定要跟上，它非常、非常重要。」不同產業需要的 LLM 也會不同，AI 不只能依照不同需求而「可程式化」（programmable），還將打破過去 20 年由搜尋推薦系統主導的網路經濟模式。</p>
        </div>

        <div class="quote-box">
            <p>你還覺得以後的手機還是長得一模一樣嗎？</p>
            <cite>— 紀懷新，Google DeepMind 副總裁</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>紀懷新認為，AI 推理能力將擴展至跨手機、電腦、智慧眼鏡等各種不同裝置。只要在同一個帳號裡，這些裝置就擁有同樣的記憶，換裝置也不影響 AI 使用，能即時反應並高度客製化。過去 20 年由搜尋推薦系統主導的網路經濟模式，即將被具備推理能力的 AI 打破。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">1990 年代末</div>
                <div class="timeline-title">搜尋引擎興起</div>
                <div class="timeline-desc">Google 等搜尋引擎開始改變網路使用方式</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2007 年</div>
                <div class="timeline-title">智慧型手機時代</div>
                <div class="timeline-desc">iPhone 發布，App 生態引爆搜尋推薦系統應用</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2022 年</div>
                <div class="timeline-title">ChatGPT 橫空出世</div>
                <div class="timeline-desc">大語言模型開始普及，但仍是預測 token 階段</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025-2026 年</div>
                <div class="timeline-title">思維鏈突破</div>
                <div class="timeline-desc">Chain of Thought 導入大語言模型，AI 推理能力大幅提升</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月</div>
                <div class="timeline-title">Agent Harness 興起</div>
                <div class="timeline-desc">矽谷全面建立 AI 駕馭系統，網路生態即將大洗牌</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>舊時代：搜尋推薦 AI</th>
                    <th>新時代：推理 AI</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>核心能力</td>
                    <td>預測下一個 token</td>
                    <td class="highlight-col">預測下一個 idea</td>
                </tr>
                <tr>
                    <td>任務類型</td>
                    <td>搜尋、推薦、分類</td>
                    <td class="highlight-col">自動規劃、多步驟執行</td>
                </tr>
                <tr>
                    <td>工具操控</td>
                    <td>無法主動操控軟體</td>
                    <td class="highlight-col">自動操控軟體工具</td>
                </tr>
                <tr>
                    <td>輸出形式</td>
                    <td>文字為主</td>
                    <td class="highlight-col">文字、聲音、影像多模態</td>
                </tr>
                <tr>
                    <td>產業年收入</td>
                    <td>1 兆美元（搜尋推薦）</td>
                    <td class="highlight-col">即將重塑</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'AI代理還不夠　Google大將紀懷新曝AI科技下一步　網路生態將大洗牌',
    'h1': 'AI代理還不夠<br>Google大將紀懷新曝AI科技下一步　網路生態將大洗牌',
    'subtitle': '思維鏈讓 AI 從預測 token 升級至預測 idea，搜尋推薦系統兆美元經濟模式即將被打破',
    'source_url': 'https://www.mirrordaily.news/story/72148',
    'source_name': '鏡報',
    'pub_date': '2026-07-09',
    'img_alt': 'AI 神經網路跨裝置概念圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260710_123000',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print("錯誤：")
    for e in errors:
        print(f"  - {e}")
