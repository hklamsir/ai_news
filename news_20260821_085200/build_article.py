#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.bnext.com.tw/article/91774/nvidia-hut8-ai-power-deal" target="_blank">BNEXT（商業周刊）</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-07</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>輝達與比特幣礦商 Hut 8 簽下 15 年巨額租約，揭示 AI 資料中心的最大瓶頸已從 GPU 轉向電力，輝達更從硬體銷售商轉型為基礎設施整合者。</p>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>500億美元世紀合作</h4>
                <p>輝達向 Hut 8 簽署德州「Beacon Point」AI 資料中心 15 年租約，30 年合約總價上看 500 億美元（約新台幣 1.6 兆元），標誌著輝達戰略的重大轉變。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚡</div>
            <div class="tech-card-content">
                <h4>電力成新焦點</h4>
                <p>AI 資料中心的最大瓶頸已從 GPU 晶片轉向穩定、充足的電力供應。Hut 8 是極少數能在單一地點提供 1GW 併聯電網的業者，電量約等於半個台北市每日所需。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔗</div>
            <div class="tech-card-content">
                <h4>Hut 8 的華麗轉身</h4>
                <p>從比特幣挖礦起家的 Hut 8，在新執行長帶領下以「能源第一」策略轉型 AI 基礎設施，更與川普家族合作成立「American Bitcoin」合資公司，持股八成負責實際營運。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏢</div>
            <div class="tech-card-content">
                <h4>輝達的戰略轉型</h4>
                <p>輝達從單純賣 AI 硬體，到直接下場承租基礎設施，象徵 AI 競賽新規則：擁有電力資源者擁有更多話語權，而非僅僅是擁有 GPU 晶片。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Hut 8 目前持有的 AI 基礎設施合約總價值達 266 億美元（約新台幣 8,000 億元），顯示能源基礎設施供應商正在 AI 價值鏈中快速崛起。</p>
        </div>

        <div class="quote-box">
            <p>「我們真正的核心資產，是『能源』！」</p>
            <cite>— 艾許·吉努特（Hut 8 執行長）</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>輝達與 Hut 8 的「強強聯手」雖矚目，但背後暗藏風險：若未來 AI 需求降溫，重金打造的資料中心將面臨算力過剩與成本回收壓力。然而，短期內電力將持續成為 AI 擴張的關鍵資源，能源供應商的話語權正急速上升。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2017年</div>
                <div class="timeline-title">Hut 8 成立</div>
                <div class="timeline-desc">由加拿大機構投資人與 Bitfury Group 聯合籌組成立</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2024年</div>
                <div class="timeline-title">策略轉型</div>
                <div class="timeline-desc">新執行長吉努特將公司核心定調為「能源第一」</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2024年</div>
                <div class="timeline-title">川普家族合作</div>
                <div class="timeline-desc">與川普兩子成立「American Bitcoin」合資公司</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026年</div>
                <div class="timeline-title">輝達巨額合作</div>
                <div class="timeline-desc">輝達簽下 15 年租約，30 年合約總價上看 500 億美元</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">風險與機會</div>
                <div class="timeline-desc">AI 需求若降溫將面臨算力過剩壓力，但電力供應商話語權持續上升</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>對比項目</th>
                    <th>傳統 AI 競賽</th>
                    <th>新型 AI 競賽</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>核心資源</td>
                    <td class="highlight-col">GPU 晶片</td>
                    <td>電力供應</td>
                </tr>
                <tr>
                    <td>關鍵廠商</td>
                    <td>輝達、AMD 等晶片商</td>
                    <td class="highlight-col">Hut 8 等基礎設施商</td>
                </tr>
                <tr>
                    <td>輝達角色</td>
                    <td>純硬體銷售商</td>
                    <td class="highlight-col">基礎設施整合者</td>
                </tr>
                <tr>
                    <td>30年合約總價</td>
                    <td>—</td>
                    <td class="highlight-col">500 億美元</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '輝達砸最高1.6兆結盟神秘挖礦商！AI下一戰搶的不是GPU，是電',
    'h1':          '輝達砸最高1.6兆結盟神秘挖礦商！<br>AI下一戰搶的不是GPU，是電',
    'subtitle':    '輝達與 Hut 8 簽下 15 年租約，30 年合約總價上看 500 億美元，揭露 AI 資料中心的瓶頸已從 GPU 轉向電力',
    'source_url':  'https://www.bnext.com.tw/article/91774/nvidia-hut8-ai-power-deal',
    'source_name': 'BNEXT',
    'pub_date':    '2026-08-07',
    'img_alt':     '輝達與 Hut 8 合作示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260821_085200',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print(f"❌ HTML 組裝失敗：{errors}")
    sys.exit(1)
