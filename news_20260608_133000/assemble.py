#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://unwire.pro/2026/06/08/ai-hk-labour/news/" target="_blank">UNWIRE</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-08</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>香港最新失業率維持3.7% 相對低位，但總就業人數只有約 364.8 萬，較 2018 年大幅減少 23.4 萬人。在 750 萬人口中，受僱人口不足一半。當 AI 以指數級速度發展，香港將面對怎樣的化學反應？</p>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>階段一：AI 作為勞動缺口「完美替補」</h4>
                <p>香港企業正面對請人難、人力成本高昂困境，AI 成為維持城市運作的關鍵幫手：餐飲業送餐機械人、金融業 AI 審批系統、行政文書 GenAI 輔助。</p>
                <p>日本「社會 5.0」經驗：將 AI、物聯網、機械人深度融入社會，填補數百萬勞動力缺口。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>階段二：「白領結構性擠出」危機</h4>
                <p>當 AI 具備自主推理及生成能力後，危機浮現。Goldman Sachs 報告指出生成式 AI 可能令全球 3 億個全職工作自動化。華爾街與矽谷正以少數「AI 協調者」取代大量中層白領。</p>
                <p>香港將新增一批「因 AI 而被迫退出勞動市場的中產階級」。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💀</div>
            <div class="tech-card-content">
                <h4>階段三：「無用階級」與消費黑洞</h4>
                <p>致命宏觀經濟悖論：企業大量採用 AI，薪金支出減少，社會上超過一半人不工作、缺乏穩定收入——誰來消費？</p>
                <p>歷史學家 Yuval Noah Harari 警告 AI 時代可能催生龐大「無用階級」。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏛️</div>
            <div class="tech-card-content">
                <h4>階段四：重塑社會契約</h4>
                <p>香港傳統「低稅率、積極不干預」模式將受嚴峻挑戰。政府依賴薪俸稅收入基礎勢必動搖。</p>
                <p><strong>海外探索：</strong>韓國「機械人稅」、Sam Altman 推動 UBI、芬蘭 UBI 實驗——均在探索 AI 時代的財富重分配機制。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📊 香港勞動市場關鍵數據</h4>
            <p>就業人數：364.8 萬（較 2018 年減少 23.4 萬）| 失業率：3.7% | 受僱人口不足總人口一半 | 全球3 億個全職工作可能被 AI 自動化</p>
        </div>

        <div class="quote-box">
            <p>「未來教育不能再訓練學生像機器一樣執行任務，因為 AI 永遠比人類做得更好。我們必須尋找『人類溢價』——同理心、複雜人際談判與衝突調解、對市場痛點深刻洞察，以及倫理道德戰略判斷。」</p>
            <cite>— 梁偉峯博士</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>當 AI 處理世界上大部分繁文縟節，香港社會未來繁榮，不再取決於「有多少人每天擠港鐵返工」，而是取決於我們能否善用這場科技變革，創造一個即使許多人「唔使做」，也能公平分享科技紅利、活得有尊嚴的新社會契約。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2018 年</div>
                <div class="timeline-title">香港就業人數高峰</div>
                <div class="timeline-desc">總就業人數約 388 萬人</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">就業人數跌至 364.8 萬</div>
                <div class="timeline-desc">6 年間減少 23.4 萬人，跌幅6%</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">AI 爆發性發展</div>
                <div class="timeline-desc">生成式 AI 能力跨越「輔助」門檻，開始具備自主推理及生成能力</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">進行中</div>
                <div class="timeline-title">餐飲、金融、行政 AI 化</div>
                <div class="timeline-desc">送餐機械人、AI 審批系統、GenAI 輔助文書興起</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">「人類溢價」成關鍵</div>
                <div class="timeline-desc">同理心、談判、倫理判斷——AI 難以複製的能力</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>對比維度</th>
                    <th>當前香港</th>
                    <th>AI 全面普及後</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>就業人數</td>
                    <td>364.8 萬</td>
                    <td class="highlight-col">預計持續減少</td>
                </tr>
                <tr>
                    <td>勞動性質</td>
                    <td>大量人力執行</td>
                    <td class="highlight-col">AI 處理繁文縟節</td>
                </tr>
                <tr>
                    <td>主要威脅</td>
                    <td>人口老化、移民潮</td>
                    <td class="highlight-col">白領結構性擠出</td>
                </tr>
                <tr>
                    <td>社會契約</td>
                    <td>低稅率、不干預</td>
                    <td class="highlight-col">需重新探討財富分配</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '告別全民就業時代：AI 普及與香港勞動參與率觸底雙重夾擊 | UNWIRE',
    'h1': '告別全民就業時代<br>AI 與香港勞動市場雙重夾擊',
    'subtitle': '750萬人口中受僱人口不足一半，AI時代將如何重塑香港未來？',
    'source_url': 'https://unwire.pro/2026/06/08/ai-hk-labour/news/',
    'source_name': 'UNWIRE',
    'pub_date': '2026-06-08',
    'img_alt': '香港勞動市場AI雙重夾擊概念圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260608_133000',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ 文章組裝成功")
else:
    print(f"❌ 失敗：{errors}")
    sys.exit(1)