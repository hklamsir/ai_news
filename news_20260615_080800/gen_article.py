#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techtrenches.dev/p/the-west-forgot-how-to-make-things" target="_blank">TECHTRENCHES</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-15</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>作者是烏克蘭工程團隊負責人，以國防工業衰退的教訓為切入點，揭示軟體業正在犯同一個錯誤：過度優化導致關鍵人才與技術知識流失，最終連「製造」能力本身都不復存在。</p>

        <div class="tech-card">
            <div class="tech-card-icon">💣</div>
            <div class="tech-card-content">
                <h4>國防業的教訓：Stinger 導彈</h4>
                <p>停產 20 年後重啟，需要 70 歲退休工程師回來教年輕人看 40 年前的紙本圖紙。測試設備在倉庫裡積灰， nose cone 仍需手工組裝——和四十年前完全一樣。四年才能交付，不是因為缺錢，是因為知道怎麼做的人在十年前就退休了。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💣</div>
            <div class="tech-card-content">
                <h4>歐洲砲彈危機</h4>
                <p>承諾一年交付 100 萬發，結果只做到一半。法國 2007 年停產推進劑，德國只有兩天庫存。 Nammo 工廠 2020 年關閉，需從零重啟。歐洲花了五年、數十億美元，仍未達到產能目標。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">☢️</div>
            <div class="tech-card-content">
                <h4>Fogbank：知識蒸發的終極案例</h4>
                <p>一種核彈頭材料，1975-1989 年生產，之後停產。重新研發時花了 $6900 萬、數年時間，結果發現當年的製造工藝依賴一個「連工人自己都不知道」的無意雜質才能運作。美國核武器計劃無法複製自己發明的材料——知識在沒有被真正理解的情況下就消失了。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📉</div>
            <div class="tech-card-content">
                <h4>軟體業正在犯同樣的錯</h4>
                <p>Salesforce 宣佈 2025 年不再招聘工程師；54% 的工程主管認為 AI 會減少 Junior Hiring；62% 的計算機系入學人數下降。作者親歷：2,253 求職人，只錄取 4 人（0.18%）——同時具備技術能力和判斷 AI 錯在哪的人才幾乎不存在。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 核心數據</h4>
            <ul>
                <li>METR 研究：資深開發者用 AI 工具反而慢了 19%，預期卻是快 24%——Reality Gap 高達 43 個百分點</li>
                <li>1993 年五角大樓併購潮：51 家國防承包商整合成 5 家，裁員 65%</li>
                <li>人才培養周期：Junior → Mid-level 需 3-5 年；Senior → Principal/Architect 需 10+ 年</li>
                <li>重建產能：簡單系統 3-5 年，複雜系統 5-10 年</li>
            </ul>
        </div>

        <div class="quote-box">
            <p>「五年後我們需要 Senior 工程師——那些能凌晨 2 點 Debug 分散式故障、帶著不存在於代碼庫中的制度知識的人。這些工程師還不存在，因為我們現在沒有在培養他們。」</p>
            <cite>— TECHTRENCHES</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>當 Junior 跳過 Debug 和犯錯學習，他們無法建立隱性專業知識（Tacit Expertise）。等這代工程師退休時，那些知識不會轉移到 AI——它就這樣消失了。這是軟體業的 Fogbank。國防業已經付出代價，現在輪到軟體業。」</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">1993</div>
                <div class="timeline-title">五角大樓併購潮</div>
                <div class="timeline-desc">51 家國防承包商整合成 5 家，裁員 65%，整個供應鏈被「優化」</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2007</div>
                <div class="timeline-title">法國停產推進劑</div>
                <div class="timeline-desc">法國停止國內推進劑生產，歐洲 Defence Industrial Base 進一步空洞化</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2022</div>
                <div class="timeline-title">俄烏戰爭爆發</div>
                <div class="timeline-desc">歐洲急需砲彈，發現所有供應鏈都已斷裂；Stinger 需要四年才能重啟生產</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2023</div>
                <div class="timeline-title">歐洲百萬砲彈承諾跳票</div>
                <div class="timeline-desc">承諾一年交付 100 萬發，實際只交付約一半，直到 2024 年 12 月才達標</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025</div>
                <div class="timeline-title">軟體業人才危機</div>
                <div class="timeline-desc">Salesforce 停招工程師，大學 CS 入學人數下滑，AI 導致 Junior Hiring 減少</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>領域</th>
                    <th>國防業（已知）</th>
                    <th>軟體業（正在發生）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>優化策略</td>
                    <td>併購整合、裁員、供應鏈精簡</td>
                    <td class="highlight-col">用 AI 取代 Junior Hiring</td>
                </tr>
                <tr>
                    <td>知識流失</td>
                    <td>工程師退休、文件不完整</td>
                    <td class="highlight-col">Junior 跳過 Debug/犯錯，無法建立隱性知識</td>
                </tr>
                <tr>
                    <td>重建週期</td>
                    <td>3-10 年</td>
                    <td class="highlight-col">人才培養 3-10+ 年，無法靠錢壓縮</td>
                </tr>
                <tr>
                    <td>危機代價</td>
                    <td>四年才重啟導彈生產、砲彈交付延遲 9 個月</td>
                    <td class="highlight-col">待觀察，但模式完全相同</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'The West Forgot How to Build. Now It\'s Forgetting Code',
    'h1':          'The West Forgot How to Build.<br>Now It\'s Forgetting Code',
    'subtitle':    '從國防工業的教訓看軟體業正在犯的同一個錯誤',
    'source_url':  'https://techtrenches.dev/p/the-west-forgot-how-to-make-things',
    'source_name': 'TECHTRENCHES',
    'pub_date':    '2026-06-15',
    'img_alt':     '西方忘記如何建造，現在正在忘記如何寫代碼',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260615_080800',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")