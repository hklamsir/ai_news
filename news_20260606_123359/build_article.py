import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://fc.bnext.com.tw/articles/view/4654" target="_blank">未來商務</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-06</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>2026 年 6 月 1 日，NVIDIA 執行長黃仁勳在台北流行音樂中心發表 <strong>GTC Taipei 2026</strong> 主題演講，主題為「Useful AI Has Arrived（有用的 AI 終於來臨）」。這是 GTC 大會首度在台北舉行。專家解讀：NVIDIA 正式宣告從 GPU 晶片公司轉型為<strong>AI 基礎設施公司（Infrastructure Company）</strong>，目標是提供端到端的 AI 實現平台。</p>

        <h3>📊 關鍵數據</h3>
        <ul>
            <li>📅 <strong>活動：</strong>GTC Taipei 2026（台北首屆）</li>
            <li>🎤 <strong>講者：</strong>黃仁勳（NVIDIA CEO）</li>
            <li>🔧 <strong>新品：</strong>Vera Rubin 全新 AI 架構</li>
            <li>🏭 <strong>台灣供應鏈：</strong>超過 150 家台廠共同設計</li>
            <li>🔢 <strong>電晶體：</strong>Vera Rubin 平台整合 6 兆個電晶體</li>
            <li>⏱️ <strong>演講時長：</strong>2 小時（準時開始、準時結束）</li>
            <li>🎂 <strong>里程碑：</strong>CUDA 滿 20 週年</li>
            <li>📍 <strong>地點：</strong>台北流行音樂中心</li>
        </ul>

        <h3>🔑 黃仁勳的核心訊息：NVIDIA 不只是 GPU 公司</h3>
        <p>智源智庫創辦人王智立（Jeremy Wang）分析：「這場演講最重要的訊息，是 NVIDIA 公開宣示自己不再只是 GPU 晶片公司，也不只是系統公司，而是一家 AI 基礎設施公司。」過去市場也許認為 NVIDIA 是晶片公司或系統整合商，但黃仁勳這次大膽呈現了完整雄心：不管是網路互連技術還是 CPU，NVIDIA 的能力現在都已達到世界頂尖。</p>
        <p>這個基礎設施野心最具體的體現，就是這次發布的 <strong>Vera Rubin</strong>。黃仁勳已將其定位為未來雲端 AI 基礎設施的完整解決方案，不只是一顆晶片或一套系統，而是整個 AI 實現所需的端到端平台。</p>

        <h3>🖥️ Vera Rubin 機櫃：無外部電線的秘密</h3>
        <p>今年 Vera Rubin 機櫃最讓人印象深刻的細節，是跟去年相比，<strong>外部電線全部消失了</strong>。這代表從晶片換代到整個機械設計的整合，在一年之內就把所有外部走線都內化進去。這需要 NVIDIA 內部與台灣供應商之間極度緊密的協同設計（Codesign）能力。</p>

        <h3>🇹🇼 150 家台廠共同設計：台灣供應鏈的不可複製性</h3>
        <p>Vera Rubin 平台整合了 <strong>6 兆個電晶體</strong>，動用了超過 <strong>150 家台灣供應鏈夥伴</strong>。從台積電的 3 奈米先進製程與 CoWoS 封裝、鴻海與廣達的系統組裝，到散熱、電源、連接器各環節，全部都是從最早的設計階段就一起進來的 Codesign 模式。</p>
        <p>這就是為什麼台灣的供應鏈競爭優勢很難被複製。黃仁勳現場說：「<strong>台灣從一開始就和我們在一起</strong>。」台灣創造了 NVIDIA，NVIDIA 也成就了台灣現在的 AI 光景。</p>

        <h3>🤖 AI Agent 熱潮：NVIDIA 的佈局</h3>
        <p>黃仁勳在 Agent（代理）這個議題上著墨最深。他給出了一個很清楚的定義：<strong>Agent 等於 LLM（大型語言模型）加上 Harness（駕馭工程）</strong>。LLM 是大腦，負責思考、推理；Harness 是身體，涵蓋工具、安全機制以及所有對外互動的介面。</p>
        <p>他以 NVIDIA 與 EDA 軟體龍頭 Cadence 的合作為例：過去需要幾週時間、大量工程師反覆驗證的晶片設計流程，透過 NVIDIA 打造的 Super Agent，現在幾個小時就能搞定。這說明 Agent 已不是概念，而是真正落地在工作流程中。</p>

        <h3>🖥️ 其他亮點：CUDA 20 週年、AI PC、Physical AI</h3>
        <ul>
            <li>🎂 <strong>CUDA 20 週年：</strong>黃仁勳在 GTC Taipei 慶祝 CUDA 問世 20 週年，這個平台讓 NVIDIA 從遊戲顯卡公司轉型為 AI 運算霸主</li>
            <li>💻 <strong>AI PC：</strong>展示了新一代 AI PC 架構，強調本地端 AI 運算能力</li>
            <li>🤖 <strong>Physical AI（實體 AI）：</strong>探討 AI 與實體世界結合的下一個戰場</li>
        </ul>

        <h3>🛠️ 台灣在半導體供應鏈的角色分析</h3>
        <p>在半導體產業待了三十幾年的王智立指出，台灣的供應鏈優勢建立在多個層面的累積：</p>
        <ul>
            <li>🔬 <strong>晶圓製造：</strong>台積電的先進製程領先全球，為 NVIDIA 提供最尖端晶片製造能力</li>
            <li>📦 <strong>先進封裝：</strong>CoWoS 封裝技術讓 HBM 記憶體與邏輯晶片高效整合</li>
            <li>🔧 <strong>系統組裝：</strong>鴻海、廣達等代工巨頭具備大規模、高品質的組裝能力</li>
            <li>❄️ <strong>散熱與電源：</strong>台灣供應商在高密度運算的熱管理領域技術領先</li>
            <li>🔌 <strong>連接器：</strong>精密連接器是高速資料傳輸的關鍵零組件</li>
        </ul>
        <p>這些環節都需要時間累積，也需要在整個生態系中彼此默契配合的執行力。這也是為什麼其他國家難以在短期內複製這個供應鏈模式。</p>

        <div class="tech-cards">
            <div class="tech-card">
                <div class="tech-card-icon">🏭</div>
                <h4>150 家台廠供應鏈</h4>
                <p>超過 150 家台灣供應鏈夥伴參與 Vera Rubin 的 Codesign，從晶圓廠到系統組裝全部協作</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🔢</div>
                <h4>6 兆個電晶體</h4>
                <p>Vera Rubin 平台整合了 6 兆個電晶體，是目前世界上最大的 AI 運算平台之一</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🤖</div>
                <h4>AI Agent 實際落地</h4>
                <p>與 Cadence 合作，晶片設計時間從數週縮短至數小時，AI Agent 已非概念</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🎂</div>
                <h4>CUDA 20 週年</h4>
                <p>從 2006 年問世至今，CUDA 將 NVIDIA 從遊戲顯卡公司推向 AI 運算霸主地位</p>
            </div>
        </div>

        <h3>🌍 從遊戲顯卡到 AI 帝國：NVIDIA 的 20 年轉型</h3>
        <p>CUDA 問世的 20 年，也是 NVIDIA 從遊戲顯卡公司轉型為 AI 運算霸主的故事。2006 年 NVIDIA 推出 CUDA，讓開發者能用 GPU 進行通用運算，當時大多數人並不理解這個決定的重要性。如今 CUDA 已成為 AI 深度學習事實上的標準平台，幾乎所有大型語言模型訓練背後都有 CUDA 的身影。</p>
        <p>黃仁勳在 GTC Taipei 2026 宣示 NVIDIA 的新定位，某种程度上也是在向整個產業宣告：AI 基礎設施的遊戲才剛開始，而 NVIDIA 已經搶佔了最有利的位置。</p>

        <h3>💬 專家點評</h3>
        <div class="quote-box">
            <p>「一家原本專做 GPU 的公司，現在要做端到端（End-to-End）的解決方案。這感覺像是一統江湖。」</p>
            <cite>— 王智立（Jeremy Wang），智源智庫創辦人，GSA 前亞太區創始執行長</cite>
        </div>

        <div class="highlight-box">
            <p>💬 <strong>黃仁勳（原話）：</strong>「有用的 AI 終於來臨（Useful AI Has Arrived）。」</p>
        </div>
"""

metadata = {
    'title': 'NVIDIA 轉型 AI 基礎設施公司！黃仁勳 GTC Taipei 2026 說了什麼？專家解析輝達佈局策略',
    'h1': 'NVIDIA 轉型 AI 基礎設施公司！<br>黃仁勳 GTC Taipei 2026 專家解析',
    'subtitle': 'Vera Rubin 由 150 家台廠共同設計，黃仁勳宣告 NVIDIA 不再只是 GPU 公司的完整戰略',
    'source_url': 'https://fc.bnext.com.tw/articles/view/4654',
    'source_name': '未來商務',
    'pub_date': '2026-06-06',
    'img_alt': 'NVIDIA 轉型 AI 基礎設施公司',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260606_123359',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 重建成功")
else:
    print("❌ HTML 重建失敗")
    for e in errors:
        print(f"  - {e}")