import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://udn.com/news/story/6811/9548568" target="_blank">聯合新聞網</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-06</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>美國多家企業主管驚覺，用 AI 取代員工的代價竟然如此高昂！某公司最近 Claude 月費帳單竟高達 <strong>5 億美元</strong>。問題出在「詞元」（token）消耗——企業鼓勵員工多多使用 AI，但每一次提問都需要消耗大量詞元，帳單迅速失控。</p>

        <h3>📊 關鍵數據</h3>
        <ul>
            <li>💰 <strong>企業 Claude 月費：</strong>某公司帳單高達 5 億美元</li>
            <li>📝 <strong>單次提問成本：</strong>750 字文字提問消耗逾 1,000 個詞元</li>
            <li>📉 <strong>Uber：</strong>還沒到 4 月就燒光 2026 全年 AI 預算</li>
            <li>📉 <strong>裁員潮：</strong>今年來 167 家科技公司累計裁員 11.7 萬人</li>
            <li>🏢 <strong>微軟：</strong>取消內部 Claude Code 授權，要求員工改用 GitHub Copilot CLI</li>
            <li>📊 <strong>輝達內部分析：</strong>AI 成本比人力還貴</li>
            <li>🚫 <strong>亞馬遜：</strong>關閉內部 AI 使用排行榜「KiroRank」，呼籲員工「不要為 AI 而 AI」</li>
        </ul>

        <h3>💸 問題根源：詞元消耗失控</h3>
        <p>企業為提升生產力，紛紛鼓勵員工「詞元最大化」（Tokenmaxxing）——多多向 AI 聊天機器人提問。這種行為甚至變成員工在同事間炫耀的資本，彰顯自己在關鍵績效指標中的表現。</p>
        <p>然而代價驚人：</p>
        <ul>
            <li>📝 <strong>文字提問：</strong>750 字就需要消耗逾 1,000 個詞元</li>
            <li>🎬 <strong>影片/圖像生成：</strong>詞元消耗更高</li>
            <li>💻 <strong>代碼生成：</strong>同樣消耗大量詞元</li>
            <li>⚠️ <strong>最重要：</strong>任務還沒執行完畢，帳單就得支付</li>
        </ul>

        <h3>🏢 企業的警覺與調整</h3>
        <p>這些 AI 費用多得讓企業主管直呼意外，尤其是代理 AI（Agentic AI）使用日增，耗費的詞元數量隨之暴增。讓主管開始納悶：使用 AI 真的比聘用人員便宜嗎？</p>
        <p>多家科技巨頭已開始行動：</p>
        <ul>
            <li>🚗 <strong>Uber</strong>：營運長表示關切，因為還沒到 4 月就燒光 2026 全年 AI 預算</li>
            <li>💻 <strong>微軟</strong>：取消對內部授權使用 Anthropic 的 Claude Code，要求員工改用 GitHub Copilot CLI</li>
            <li>🔴 <strong>輝達</strong>：內部分析顯示 AI 成本比人力還貴</li>
            <li>🛒 <strong>亞馬遜</strong>：關閉內部 AI 使用排行榜「KiroRank」，呼籲員工「不要為 AI 而 AI」</li>
        </ul>

        <h3>📉 對勞動市場的影響</h3>
        <p>企業採用 AI 的初衷是讓團隊更精簡、任務更快速有效率達成。然而根據 Layoff.fyi 統計，<strong>今年來 167 家科技公司累計已裁員 11.7 萬人</strong>，快要追平 275 家公司 2025 全年合計裁掉的 12.5 萬人。</p>
        <p>美企如今逆轉「詞元最大化」政策，顯示美國勞動市場或許已度過最糟情況。AI 成本高漲反而成為支撐就業的意外因素。</p>

        <h3>🔄 企業的理性回歸</h3>
        <p>企業紛紛開始節制使用 AI，顯示對 AI 投資報酬不滿意。大型科技公司近幾年來投入數十億美元布建 AI 基礎設施。儘管大型科技股目前仍盤旋在高檔價位，許多企業已警覺到這種詞元支出水準難以為繼。</p>
        <p>這波 AI 成本覺醒可能會讓企業重新思考：AI 的價值在於提升效率，而非無節制地使用。</p>

        <div class="tech-cards">
            <div class="tech-card">
                <div class="tech-card-icon">💰</div>
                <h4>5 億美元月費</h4>
                <p>某公司 Claude 月費帳單高達 5 億美元，遠超預期</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">📝</div>
                <h4>詞元消耗失控</h4>
                <p>750 字提問消耗逾 1,000 個詞元，影片/圖像生成消耗更高</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">📉</div>
                <h4>裁員 11.7 萬人</h4>
                <p>今年來 167 家科技公司裁員，逼近去年全年總和</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🚫</div>
                <h4>不要為 AI 而 AI</h4>
                <p>亞馬遜關閉使用排行榜，微軟取消 Claude Code 內部授權</p>
            </div>
        </div>

        <h3>💬 業界觀點</h3>
        <div class="quote-box">
            <p>「詞元最大化」所費不貲，而且任務還沒執行完畢，帳單就得支付。</p>
            <cite>— 企業主管對 AI 成本覺醒的感慨</cite>
        </div>

        <div class="highlight-box">
            <p>💡 <strong>逆轉訊號：</strong>美企逆轉「詞元最大化」政策，反而可能成為美國勞動市場的利好——當 AI 成本高於人力，企業選擇僱用真人的誘因反而增加。</p>
        </div>
"""

metadata = {
    'title': '人力更便宜？AI成本爆表痛醒美企主管 月費帳單竟飆5億美元',
    'h1': '人力更便宜？AI成本爆表痛醒美企主管<br>月費帳單竟飆 5 億美元',
    'subtitle': '詞元消耗失控！企業發現 AI 成本比人力還貴，開始逆轉「詞元最大化」政策',
    'source_url': 'https://udn.com/news/story/6811/9548568',
    'source_name': '聯合新聞網',
    'pub_date': '2026-06-06',
    'img_alt': 'AI 月費飆至 5 億美元 企業痛醒',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260606_205540',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 重建成功")
else:
    print("❌ HTML 重建失敗")
    for e in errors:
        print(f"  - {e}")