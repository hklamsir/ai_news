import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://news.cnyes.com/news/id/6506944" target="_blank">鉅亨網</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-28</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>美國半導體新創 xLight 以自由電子雷射（FEL）挑戰艾司摩爾 EUV 光源壟斷，獲得美國商務部 1.5 億美元注資，前英特爾執行長基辛格出任董事長，為這場「寄生式創新」增添重量級產業背書。</p>

        <div class="tech-card">
            <div class="tech-card-icon">💡</div>
            <div class="tech-card-content">
                <h4>自由電子雷射（FEL）技術</h4>
                <p>xLight 鎖定 2 至 7 奈米波長的「Blue-X」波段，理論平均輸出功率可達約 5 千瓦，為現有 LPP 系統功率的四倍以上，光譜頻寬更窄、亮度更高，且無需消耗錫或氫氣等耗材。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏭</div>
            <div class="tech-card-content">
                <h4>解耦式架構</h4>
                <p>FEL 為集中式光源，一台裝置理論上可同時為 10 至 20 台光刻掃描器供光，使晶圓廠從「一機一帶光源」變為「光源中心加掃描器集群」的解耦架構，宣稱可將生產效率提高 50%（新建廠可翻倍）。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤝</div>
            <div class="tech-card-content">
                <h4>「寄生式創新」策略</h4>
                <p>xLight 定位為艾司摩爾的二級供應商，以 FEL 光源模組取代 Cymer LPP 光源系統，繞開整機光學與精密機械壁壘。但其命運與 ASML 接納程度深度綁定。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>5.5 億美元資金實力</h4>
                <p>美國商務部《晶片與科學法案》提供 1.5 億美元股权投资，聯邦政府成為最大股東之一；正洽談新一輪 3.5 億美元融資，擬邀艾司摩爾、台積電、英特爾及美光跟隨投資。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>目前全球唯一能製造 EUV 微影設備的廠商是艾司摩爾，市佔率約 94%。艾司摩爾執行長 Christophe Fouquet 公開承認雙方有技術演示合作，但強調這是一段「漫長的旅程」。</p>
        </div>

        <div class="quote-box">
            <p>「這種『寄生式創新』策略讓公司可聚焦光源研發、繞開整機光學與精密機械壁壘，但也使其命運與 ASML 的接納程度深度綁定。」</p>
            <cite>— 鉅亨網，2026-06-28</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>xLight 的出現為半導體供應鏈「去單點故障化」提供了新的可能性。但艾司摩爾本身仍押注 LPP 路線，2026 年初宣布在實驗室展示 1000 瓦 EUV 光源，目標 2030 年單台設備產能提升至每小時 330 片晶圓。這場顛覆之旅，仍然漫長。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2021 年</div>
                <div class="timeline-title">xLight 成立</div>
                <div class="timeline-desc">加州新創公司成立，專注 FEL 光源研發</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年 3 月</div>
                <div class="timeline-title">基辛格加入</div>
                <div class="timeline-desc">前英特爾執行長基辛格出任 xLight 執行董事長</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">美國政府入股</div>
                <div class="timeline-desc">商務部依據《晶片與科學法案》提供 1.5 億美元股权投资</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">新一輪融資</div>
                <div class="timeline-desc">正洽談 3.5 億美元新融資，擬邀 ASML、台積電等跟隨投資</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2028 年</div>
                <div class="timeline-title">原型機目標</div>
                <div class="timeline-desc">計劃 2028 年前造出可接入量產環境的原型機</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>艾司摩爾 LPP 方案</th>
                    <th>xLight FEL 方案</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>光源技術</td>
                    <td>雷射等離子體（LPP）錫滴</td>
                    <td class="highlight-col">自由電子雷射（FEL）</td>
                </tr>
                <tr>
                    <td>輸出功率</td>
                    <td>約 600 瓦（量產）</td>
                    <td class="highlight-col">約 5 千瓦（理論）</td>
                </tr>
                <tr>
                    <td>波長</td>
                    <td>13.5 奈米（EUV）</td>
                    <td class="highlight-col">2-7 奈米（Blue-X）</td>
                </tr>
                <tr>
                    <td>供光方式</td>
                    <td>一機一帶光源</td>
                    <td class="highlight-col">集中光源供 10-20 掃描器</td>
                </tr>
                <tr>
                    <td>發展階段</td>
                    <td>已商業化量產</td>
                    <td class="highlight-col">原型機研發中（2028 目標）</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '英特爾前執行長坐鎮！美AI新創公司想分食艾司摩爾獨佔已久的光刻機蛋糕 | 鉅亨網 - 美股雷達',
    'h1':          'xLight 挑戰艾司摩爾<br>自由電子雷射掀半導體光源革命',
    'subtitle':    '前英特爾執行長基辛格出任董事長！美國新創以 FEL 光源分食 EUV 市場大餅',
    'source_url':  'https://news.cnyes.com/news/id/6506944',
    'source_name': '鉅亨網',
    'pub_date':    '2026-06-28',
    'img_alt':     '半導體晶圓廠內安裝新一代高功率 Blue-X 雷射光源的意象圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260629_105506',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print("❌ HTML 組裝失敗")
    for e in errors:
        print(f"   {e}")