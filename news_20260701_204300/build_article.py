#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.stheadline.com/local-topics/3588582/%E5%8D%8A%E5%B0%8F%E6%99%82%E7%97%9B%E5%A4%B150%E8%90%AC%E6%96%B0%E5%9E%8B%E7%9C%9F%E4%BA%BAAI%E6%B4%97%E8%85%A6%E9%A8%99%E5%B1%80%E6%AE%BA%E5%88%B0-%E5%8C%96%E8%BA%AB%E5%81%87HKTVmall%E9%99%B7%E9%98%B1-%E7%B6%B2%E6%B0%91%E9%9C%87%E9%A9%9A%E5%94%94%E6%95%A2%E8%A9%B1%E5%94%94%E4%B8%AD%E6%8B%9BJuicy%E5%8F%AE" target="_blank">星島頭條（Juicy叮）</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-30</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>有打工仔誤墮新型「真人+AI」電話騙局，被騙徒化身「假HKTVmall」送保險，以精密的疲勞轟炸戰術，在短短兩日內騙走五十萬港元血汗錢。事件揭示AI技術已被騙徒利用來增加欺騙效果，引發網民熱議：「真唔敢話自己唔中招。」</p>

        <div class="tech-card">
            <div class="tech-card-icon">🎣</div>
            <div class="tech-card-content">
                <h4>陷阱起點：免費家居保險</h4>
                <p>騙徒自稱HKTVmall來電，聲稱事主「剔咗蘇黎世嘅一份家居保險」並已啟動自動轉帳。騙徒更付費將假保險產品放上平台讓用戶加入購物車，令事主對此事隱約有印象，加上對方表示保單即將由免費變為收費，事主便不虞有詐加了對方WhatsApp。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>「人類+AI」雙打騙局</h4>
                <p>騙徒傳送假蘇黎世網站連結，當中更有「AI客服」對話介面，版面幾可亂真。騙徒以「證明是戶口持有人」為由，要求事主截圖提供所有戶口結餘。更狡猾地表示「人類係睇唔到（AI對話）」，藉此博取信任，實情是騙徒正看著事主的戶口結餘來「砌」出騙款金額。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔢</div>
            <div class="tech-card-content">
                <h4>「驗證碼」竟是轉帳銀碼</h4>
                <p>騙徒發送一串所謂「驗證碼」（例如049308），指示事主在轉數快（FPS）的「銀碼」位置輸入。為求逼真，先給了一個無法過數的號碼讓事主「測試」，令事主信以為真只是「認證」。隨即要求在真實網上銀行輸入另一組「驗證碼」，第一筆近五萬元就此送出。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💔</div>
            <div class="tech-card-content">
                <h4>大腦Overload：疲勞轟炸至理智斷線</h4>
                <p>送出第一筆錢後，騙徒以「操作超時導致認證失敗」為由承諾退款，隨後不斷要求在多個銀行戶口之間轉帳，更教唆將過數額度加到最大。事主形容：「每一次AI嘅回覆都要等1分鐘以上，係超級消磨我嘅忍耐力同埋判斷力...個腦完全係Overload」。在心急想取回本金與判斷力盡失的情況下，再送出二十多萬。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>HKTVmall及蘇黎世保險（香港）已發布聲明指發現偽冒其公司的詐騙訊息，呼籲市民切勿點擊不明連結或提供個人資料。專家呼籲：收到任何可疑電話，應直接向相關機構官方渠道求證，切勿依從來電指示操作銀行戶口。</p>
        </div>

        <div class="quote-box">
            <p>「正所謂免費嘅嘢永遠係最貴！就係呢一份家居保險，令我損失咗500,000。」</p>
            <cite>— 受騙事主</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這宗騙局顯示，AI技術已被騙徒利用來增加欺騙效果。透過假網站、假AI客服、疲勞轟炸等手段，即使警覺性較高的市民也可能中招。網民表示：「佢哋手法日新月異......真唔敢話自己唔中招。」未來這類「真人+AI」混合騙案預計將持續增加。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">第一步</div>
                <div class="timeline-title">假冒HKTVmall來電</div>
                <div class="timeline-desc">騙徒聲稱事主參加了免費家居保險，即將自動扣費，要求聯絡「蘇黎世同事」取消</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第二步</div>
                <div class="timeline-title">引導加入WhatsApp</div>
                <div class="timeline-desc">騙徒以遷就收工時間為由，約定翌日下班後處理，令事主放下戒心</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第三步</div>
                <div class="timeline-title">假網站+AI客服洗腦</div>
                <div class="timeline-desc">傳送假蘇黎世網站連結，AI客服對話介面幾可亂真，套取戶口結餘</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第四步</div>
                <div class="timeline-title">驗證碼變轉帳銀碼</div>
                <div class="timeline-desc">以「測試」為由先給無法過數的號碼，建立信任後再誘騙轉帳近5萬</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第五步</div>
                <div class="timeline-title">疲勞轟炸再騙20多萬</div>
                <div class="timeline-desc">以「認證失敗」為由持續疲勞轟炸，迫事主在多戶口間轉帳，最終再失20多萬</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>傳統電話騙案</th>
                    <th>新型「真人+AI」騙案</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>技術含量</td>
                    <td>較低，依賴社交工程</td>
                    <td class="highlight-col">高，結合假網站+AI客服</td>
                </tr>
                <tr>
                    <td>騙徒角色</td>
                    <td>純人類操作</td>
                    <td class="highlight-col">人類+AI混合，AI負責應對</td>
                </tr>
                <tr>
                    <td>信任建立</td>
                    <td>傳統安打電話技巧</td>
                    <td class="highlight-col">假網站+AI即時回覆，更逼真</td>
                </tr>
                <tr>
                    <td>心理戰術</td>
                    <td>一次過要求大額轉帳</td>
                    <td class="highlight-col">疲勞轟炸，逐步蠶食理智</td>
                </tr>
                <tr>
                    <td>損失金額</td>
                    <td>相對較小或一次性</td>
                    <td class="highlight-col">分階段蠶食，累積可達數十萬</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '半小時痛失50萬！新型「真人+AI」洗腦騙局殺到 化身「假HKTVmall」陷阱 網民震驚：唔敢話唔中招',
    'h1': '半小時痛失50萬！<br>新型「真人+AI」洗腦騙局',
    'subtitle': '化身假HKTVmall陷阱 網民震驚',
    'source_url': 'https://www.stheadline.com/local-topics/3588582/',
    'source_name': '星島頭條（Juicy叮）',
    'pub_date': '2026-06-30',
    'img_alt': '新型AI+真人電話騙局警示圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260701_204300',
    article_content=article_content,
    metadata=metadata
)

print(f"\n結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")