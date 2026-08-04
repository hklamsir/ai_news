import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://unwire.hk/2026/08/04/china-citizenship-restore/column/" target="_blank">UNWIRE</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-04</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>中國新版出境管理規定尚未生效，一名移居日本 13 年華商返國探親時已遭扣留審訊 7 天，傳被迫恢復中國國籍，並被限制未來 10 年不得出境，震動海外華人社群。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🛫</div>
            <div class="tech-card-content">
                <h4>探親後突遭扣留 審訊 7 天不眠不休</h4>
                <p>已移居日本 13 年、經營企業逾 20 年的華商，7 月 2 日攜全家返鄉探親，原定 7 月下旬返日。豈料登機前 5 分鐘突遭限制登機，一家隨後被分開扣留審訊長達 7 天，全程不眠不休。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">👨‍👩‍👧‍👦</div>
            <div class="tech-card-content">
                <h4>子女威脅送福利院 被迫「自願」放棄日本國籍</h4>
                <p>審訊期間執法人員威脅，若不配合恢復中國國籍，3 名子女將被送往邊遠地區福利院成為孤兒。華商為保子女，被迫在鏡頭前口述「自願放棄日本國籍、恢復中國國籍」，7 月 31 日收到官方《恢復中國國籍書》。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>8,000 萬人民幣資產全數癱瘓</h4>
                <p>取得《恢復中國國籍書》後，華商名下銀行戶口、支付寶及微信帳號全數無法登入，連機票、車票亦無法預訂。前往公安局備案，竟被告知一家五口 2036 年前禁止出境。其在日本苦心經營逾 20 年的企業聘用 40 多名員工，資產達 8,000 萬人民幣（約港幣 9,040 萬元），一夕之間陷入癱瘓。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚖️</div>
            <div class="tech-card-content">
                <h4>出境新規擴大管制 9 月 15 日施行</h4>
                <p>中國國務院 7 月 31 日公布《國務院關於出境入境管理的規定》共 19 條，新增以「國家產業安全、技術安全」為由限制出境條款，較 2013 年舊法範圍更廣。新規第四條訂明，在境外從事「危害國家安全和利益」行為者，回國後可被禁止出境 6 個月至 3 年。輿論憂慮限制出境權力下放至縣級機構，審查範圍由查證件擴大至查動機，恐進一步收緊公民出境自由。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>此案發生在新出境管理規定正式生效（9 月 15 日）之前，顯示當局已提前將出境管制付諸執法。截至目前中國官方尚未就上述個案作出公開回應或澄清。</p>
        </div>

        <div class="quote-box">
            <p>「若不配合恢復中國國籍，3 名子女可能被送往邊遠地區福利院，成為孤兒。」</p>
            <cite>— 陳情書內容，引述自羅翔教授公開文件</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>此案顯示中國對出境管制已從「法律條文」提前落實為「實際執法」。隨着 9 月 15 日新規施行，預料類似個案可能陸續浮現，尤其針對海外華人、留學生及跨境企業家。事件引發海外華人社群對人身安全及資產保障的深度憂慮，或將影響中國人才及資金回流意欲，涉及人權與出入境自由的國際關注亦可能升溫。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">7 月 2 日</div>
                <div class="timeline-title">華商一家返國</div>
                <div class="timeline-desc">移居日本 13 年華商攜全家返鄉探親，原定 7 月下旬返日</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">7 月中旬</div>
                <div class="timeline-title">突遭限制出境</div>
                <div class="timeline-desc">登機前 5 分鐘被限制登機，一家分開扣留審訊，長達 7 天不眠不休</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">7 月 31 日</div>
                <div class="timeline-title">被迫恢復中國國籍</div>
                <div class="timeline-desc">華商收到《恢復中國國籍書》，同日國務院正式公佈新規</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">8 月上旬</div>
                <div class="timeline-title">資產全數凍結</div>
                <div class="timeline-desc">銀行戶口、支付寶、微信全數癱瘓，被告知 2036 年前禁止出境</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">9 月 15 日</div>
                <div class="timeline-title">新規正式施行</div>
                <div class="timeline-desc">《國務院關於出境入境管理的規定》19 條文正式生效</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>2013 年舊法</th>
                    <th>2026 年新規</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>限制出境理由</td>
                    <td>證件問題、刑事嫌疑</td>
                    <td class="highlight-col">新增「國家產業安全、技術安全」</td>
                </tr>
                <tr>
                    <td>執行機構</td>
                    <td>省級以上政府</td>
                    <td class="highlight-col">縣級出入境管理機構</td>
                </tr>
                <tr>
                    <td>審查範圍</td>
                    <td>查驗證件</td>
                    <td class="highlight-col">查驗證件 + 查動機</td>
                </tr>
                <tr>
                    <td>最長限制期限</td>
                    <td>未明確</td>
                    <td class="highlight-col">6 個月至 3 年</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '科技人才出境新規公佈後 旅日華商返鄉探親被扣留 傳被恢復中國籍 10 年禁出境',
    'h1': '科技人才出境新規公佈後\n旅日華商返鄉探親被扣留 傳被恢復中國籍',
    'subtitle': '新規尚未生效已執法，旅日 13 年華商遭扣留審訊 7 天，傳被迫恢復中國籍並被禁出境 10 年',
    'source_url': 'https://unwire.hk/2026/08/04/china-citizenship-restore/column/',
    'source_name': 'UNWIRE',
    'pub_date': '2026-08-04',
    'img_alt': '旅客在機場排隊過安檢',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260804_131347',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print("❌ HTML 生成失敗：")
    for e in errors:
        print(f"   {e}")
