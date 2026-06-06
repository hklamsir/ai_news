import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://unwire.hk/2026/06/03/hkgai-v3-launch-agent-workshop-2026/ai/" target="_blank">UNWIRE</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-06</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>香港生成式人工智能研發中心（HKGAI）於 6 月 3 日舉辦「<strong>HKGAI V3 大模型發布暨生態合作大會</strong>」，正式推出第三代本地化大型語言模型，並發布全新智能體平台 <strong>Agent Workshop</strong>。創新科技及工業局局長孫東親臨主禮，逾 <strong>20 家機構</strong>獲頒首批及第二批合作獎座，涵蓋電訊、金融、雲端及教育等範疇。</p>

        <h3>📊 關鍵數據</h3>
        <ul>
            <li>🤖 <strong>V3 模型：</strong>第三代本地化大型語言模型</li>
            <li>🏢 <strong>合作夥伴：</strong>逾 20 間機構（電訊、金融、雲端、教育）</li>
            <li>👤 <strong>港話通用戶：</strong>約 75 萬註冊用戶（香港人口約一成）</li>
            <li>👨‍💼 <strong>港文通用戶：</strong>逾 5 萬名公務員</li>
            <li>💰 <strong>香港 AI 市場：</strong>去年企業及政府支出突破 1,000 億港元</li>
            <li>🏗️ <strong>北部都會區：</strong>18 萬平方呎數碼基建正在興建</li>
            <li>💵 <strong>政府投入：</strong>今年 AI 相關開支逾 30 億港元</li>
            <li>⏱️ <strong>Agent Workshop：</strong>單次無干預穩定運作達 28 小時</li>
        </ul>

        <h3>🎯 四大目標：打造港式 Agentic AI 基座</h3>
        <p>香港科技大學首席副校長兼 HKGAI 主任 <strong>郭毅可教授</strong>將 V3 定位為「香港 Agentic 基座大模型」，以四大目標概括核心能力提升：</p>
        <ul>
            <li>🛠️ <strong>更成事：</strong>支援工具調用與多步工作流程</li>
            <li>⚡ <strong>更高效：</strong>大幅降低推理延遲</li>
            <li>🧠 <strong>更睿智：</strong>建立「精製知識組織制」，將香港本土法規直接嵌入模型訓練資料</li>
            <li>🇭🇰 <strong>更本地化：</strong>深化廣東話詞彙、港式書面語及兩文三語混用場景理解，自動將「打的」換成「搭的士」</li>
        </ul>
        <p>模型對<strong>廣東話詞彙、港式書面語及香港口音普通話</strong>均作全面升級，目標是建立香港智能體社會環境。</p>

        <h3>🤖 Agent Workshop：首個企業級 AI 智能體平台</h3>
        <p>Agent Workshop 定位為<strong>香港首個處理複雜任務的企業級 AI 智能體平台</strong>，突破現有智能體限制。在測試中可單次無干預穩定運作長達 <strong>28 小時</strong>，並一氣呵成完成資料整理、推理分析、報告撰寫及程式碼開發等多個環節。</p>
        <p>現場展示場景包括：</p>
        <ul>
            <li>📄 <strong>IPO 路演簡報：</strong>上傳公司年報後自動生成完整 IPO 路演簡報</li>
            <li>📋 <strong>環評法規核對：</strong>上傳環評報告後逐節核對法規要求並標記不符合項目</li>
            <li>🌐 <strong>自動建站：</strong>從單一描述出發自動建立完整可部署網站</li>
        </ul>
        <p>平台具備三大特點：</p>
        <ul>
            <li>🔧 <strong>自主拆解任務：</strong>無需人工逐步干預</li>
            <li>📦 <strong>生產力導向：</strong>直接輸出可交付成果而非簡單問答</li>
            <li>🇭🇰 <strong>超級人格：</strong>具備深度理解香港本地法規、習慣與語言的能力</li>
        </ul>

        <h3>🖥️ 三大旗艦產品同步升級</h3>
        <p>配合 V3 大模型推出，HKGAI 旗下三款旗艦產品同步升級：</p>
        <ul>
            <li>💬 <strong>港話通：</strong>現有註冊用戶約 75 萬（香港整體人口約一成），從單點問答進化為全情境規劃，成為香港市民個人 AI 生活助手</li>
            <li>📝 <strong>港文通：</strong>專為逾 5 萬名公務員用戶而設，涵蓋文書、文錄、文脈及文序四個政府文書工作場景</li>
            <li>📊 <strong>港會通：</strong>專攻會議智能，支援兩文三語即時翻譯，預備會議前背景資料及會後自動整理紀要，即將推出桌面電腦版及網上會議平台整合功能</li>
        </ul>

        <h3>💰 千億市場與對外發展潛力</h3>
        <p>HKGAI 以數據回應外界對香港 AI 市場潛力的疑慮：北部都會區 18 萬平方呎數碼基建已在興建，政府今年投入 AI 相關開支逾 <strong>30 億港元</strong>。非正式估算顯示去年香港企業及政府在 AI 相關 IT 項目支出已突破 <strong>1,000 億港元</strong>。</p>
        <p>HKGAI 認為憑藉香港<strong>超級聯繫人</strong>定位，本地化大模型技術同樣具備協助國產模型拓展外國市場的潛力。</p>

        <h3>💬 業界反應</h3>
        <div class="quote-box">
            <p>「HKGAI 推 HKGAI V3 及多項產品升級，與香港推進『人工智能+』及建構 AI 生態圈的政策完全吻合。相信 V3 將進一步提升日常使用體驗，期待相關產品持續發展，真正賦能香港千行百業。」</p>
            <cite>— 方保僑，香港資訊科技商會榮譽會長</cite>
        </div>

        <div class="tech-cards">
            <div class="tech-card">
                <div class="tech-card-icon">🤖</div>
                <h4>HKGAI V3 大模型</h4>
                <p>第三代本地化大型語言模型，定位為香港 Agentic AI 基座</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">⚡</div>
                <h4>28 小時無間斷運行</h4>
                <p>Agent Workshop 單次無干預穩定運作 28 小時，完成複雜多環節任務</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">💬</div>
                <h4>75 萬港話通用戶</h4>
                <p>約佔香港整體人口一成，從單點問答升級為全情境規劃 AI 助手</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">💰</div>
                <h4>千億港元市場</h4>
                <p>去年香港企業及政府 AI 相關IT支出突破 1,000 億港元</p>
            </div>
        </div>

        <div class="highlight-box">
            <p>💬 <strong>HKGAI V3 的意義：</strong>繼 Google、OpenAI 之後，香港也擁有了自己的本地化大模型生態。V3 不只是一個語言模型，更是一個以香港本地化為核心的 Agentic AI 基座——從廣東話、港式書面語到兩文三語，每個細節都為香港而設計。</p>
        </div>
"""

metadata = {
    'title': '香港生成式 AI 研發中心 推 HKGAI V3 大模型 搞 Agentic AI 逾 20 間合作夥伴',
    'h1': '香港生成式 AI 研發中心 推 HKGAI V3 大模型<br>搞 Agentic AI 逾 20 間合作夥伴',
    'subtitle': '第三代本地化大模型發布暨 Agent Workshop 平台登場，瞄準千億港元 AI 市場',
    'source_url': 'https://unwire.hk/2026/06/03/hkgai-v3-launch-agent-workshop-2026/ai/',
    'source_name': 'UNWIRE',
    'pub_date': '2026-06-06',
    'img_alt': 'HKGAI V3 大模型發布 逾 20 間合作夥伴',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260606_172039',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 重建成功")
else:
    print("❌ HTML 重建失敗")
    for e in errors:
        print(f"  - {e}")