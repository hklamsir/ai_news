import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.bnext.com.tw/article/91213/ai-agent-qa" target="_blank">BNEXT</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-13</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>📈 【問趨勢】AI掌權後，會出賣人類嗎？（馮勃翰・台大經濟系副教授）</h3>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>Q1：免費的最貴？</h4>
                <p>這一波 AI 工具的免費，更像是早期軟體公司的補貼策略——先用低價搶市占率。短期消費者確實得利，但算力成本仍高，補貼隨時可能收手，現在的免費優惠是有時效的。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎯</div>
            <div class="tech-card-content">
                <h4>Q2-Q3：AI會壟斷我們的選擇嗎？</h4>
                <p>AI 代理做的事，只是把演算法推薦從線上延伸到線下實體行為。關鍵籌碼是「不要只使用單一 AI」——若大眾最後習慣性依賴特定平台，該平台就有了壟斷性議價能力。建議交叉比對不同 AI 的推薦結果。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📉</div>
            <div class="tech-card-content">
                <h4>Q4：AI熱是泡沫嗎？</h4>
                <p>諾貝爾經濟學獎得主阿克洛夫提出：每次重要技術革新後都會出現騙局、形成泡沫、然後帶來一段蕭條。這不是悲觀，是歷史規律。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>🤖 【問模型】下一輪比什麼？（蕭上農・iCook愛料理共同創辦人）</h4>
                <p>「哪一家最強」短期內還會不斷變動。頂尖通用模型最後可能剩 3-4 家，但頂端收斂、邊緣分眾才是更可能的格局。現在比的是「<strong>駕馭工程（Harness Engineering）</strong>」——誰能把模型包得好用。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>品牌印象固化後，技術追上也沒用。就像你知道某個新品牌球鞋已追上 Nike，但買運動鞋時還是直覺去看 Nike。誰先在「生產力工具」這個心智位置插旗，誰就有更長的緩衝時間。</p>
        </div>

        <div class="quote-box">
            <p>「馬有再強的力氣，沒有馬具就只是一匹野馬，駕馭工程就是那套韁繩和馬鞍。」</p>
            <cite>— 李宏毅，台大電機系教授（引用者：蕭上農）</cite>
        </div>

        <h3>💳 【問消費】AI變買手，銀行如何確保人授意？（陳懿文・萬事達卡台灣區董事總經理）</h3>
        <p>萬事達卡設計了 <strong>Agent Pay</strong> 兩個機制：</p>
        <ul>
            <li><strong>Consent（授權）</strong>：清楚設定哪個 AI 可在什麼條件與範圍內替你行動</li>
            <li><strong>Intent（意圖）</strong>：把你最初的需求（想买什麼、預算多少、什麼規格）以文字記錄下來作為比對基準</li>
        </ul>
        <p>此外，真實卡號不會進入 AI 系統，採用代碼化（Tokenization）技術已近 10 年，每筆 AI 代理的交易都必須搭配消費者的生物辨識才能完成授權。</p>

        <h3>⚖️ 【問權責】AI代理闖禍，被告是我？（黃沛聲・立勤國際律师事务所主持律師）</h3>

        <div class="tech-card">
            <div class="tech-card-icon">⚖️</div>
            <div class="tech-card-content">
                <h4>Q13：AI出錯，我能撇清嗎？</h4>
                <p>核心邏輯：<strong>誰授權、誰負責</strong>。只要外觀上 AI 看起來是代表你而行動，最終還是你要承擔並負責。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏢</div>
            <div class="tech-card-content">
                <h4>Q14：企業用AI客服，公司要賠嗎？</h4>
                <p>2024 年加拿大航空案例：旅客問 AI 客服是否有親屬優惠，AI 承諾可先買票、事後申請退費。加航最後仲裁敗訴。企業用 AI 當客服，AI 講的話統統算企業講的話。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📝</div>
            <div class="tech-card-content">
                <h4>Q15-Q16：用AI工作最常踩什麼法律紅線？</h4>
                <p>用 AI 生成圖文侵權，算你的。所有 AI 系統服務條款已寫明：AI 可能存在幻覺，請自行負責。最危險的是<strong>記憶共用問題</strong>——共用 AI 帳號，公司機密、客戶個資可能在沒意識到的情況下被外部人員問出來。</p>
            </div>
        </div>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">Q1-Q4</div>
                <div class="timeline-title">問趨勢</div>
                <div class="timeline-desc">免費有時效、AI會影響偏好、勿依賴單一AI、泡沫是歷史規律</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">Q5-Q8</div>
                <div class="timeline-title">問模型</div>
                <div class="timeline-desc">最強AI一直在變、百家爭鳴→頂端收斂、下一輪比駕馭工程、品牌印象比技術重要</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">Q9-Q12</div>
                <div class="timeline-title">問消費</div>
                <div class="timeline-desc">Agent Pay雙機制（Consent+Intent）、代碼化+生物辨識、AI推薦標準待建立</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">Q13-Q14</div>
                <div class="timeline-title">問權責</div>
                <div class="timeline-desc">誰授權誰負責、企業用AI客服AI承諾=企業承諾</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">Q15-Q16</div>
                <div class="timeline-title">問法律紅線</div>
                <div class="timeline-desc">AI生成侵權算你的、AI幻覺開發商不負責、共用帳號是最危險陷阱</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>問題面向</th>
                    <th>核心焦點</th>
                    <th>專家觀點</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>問趨勢</td>
                    <td class="highlight-col">免費優惠有時效</td>
                    <td>補貼隨時可能收手</td>
                </tr>
                <tr>
                    <td>問模型</td>
                    <td class="highlight-col">駕馭工程比能力更重要</td>
                    <td>把模型包得好用才是關鍵</td>
                </tr>
                <tr>
                    <td>問消費</td>
                    <td class="highlight-col">Agent Pay：Consent + Intent</td>
                    <td>代碼化+生物辨識保護交易</td>
                </tr>
                <tr>
                    <td>問權責</td>
                    <td class="highlight-col">誰授權、誰負責</td>
                    <td>AI犯錯等於你犯錯</td>
                </tr>
                <tr>
                    <td>法律紅線</td>
                    <td class="highlight-col">共用AI帳號最危險</td>
                    <td>公司機密可能被外洩</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '信用卡交給AI前的16個關鍵思考：免費的最貴？出包算誰？',
    'h1':          '信用卡交給AI前<br>先停・看・問',
    'subtitle':    '經濟學、新創、金融、法律4位專家解答AI代理時代的關鍵問題',
    'source_url':  'https://www.bnext.com.tw/article/91213/ai-agent-qa',
    'source_name': 'BNEXT',
    'pub_date':    '2026-06-13',
    'img_alt':     '信用卡交給 AI 前先停看問',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260613_094200',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")