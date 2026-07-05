#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techtrenches.dev/p/ai-finds-the-holes-only-your-engineers" target="_blank">Tech Trenches</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-05</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>AI 安全掃描工具發現了海量漏洞，但這些「發現」只是數量，不等於風險消除。根據 VulnCheck 數據，2025 年所有 CVE 中僅約 1% 曾被實際用於攻擊。在工程師被建議裁減的同時，修復速度遠遠落後於發現速度，這正是這篇文章要探討的核心矛盾。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>發現 ≠ 修復 ≠ 風險消除</h4>
                <p>VulnCheck 追蹤了 2025 年所有 CVE 的利用情況：約 1% 曾被實際攻擊。發現漏洞本身並不能改變任何事，直到有人真正修補它。在零閒餘产能下，一個已記錄但無法修補的漏洞，與從未發現它的暴露程度几乎相同，只是多了一條待辦事項。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>機器填補的是隊列，不是排出隊列</h4>
                <p>AI 工具正在加速發現漏洞，但修復速度遠跟不上發現速度。AI 生成代碼比任何人審查都快，工具標記漏洞比任何人確認都快。這種「生成超越審查」的速度差，正是資料外洩的根源。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🛡️</div>
            <div class="tech-card-content">
                <h4>攻擊者與防禦者的不對稱</h4>
                <p>攻擊者運行同樣的掃描器和模型，面對同樣的漏洞清單。發現從來不是防禦優勢，因為雙方發現能力相同。真正的差異在於位置：攻擊者專注一件事並控制時間軸——反覆打磨漏洞、確認可觸發。防禦者則什麼都無法控制。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>諷刺的對比</h4>
                <p>賣 AI 安全工具說找到了 23,000 個漏洞，同時卻建議你裁掉負責修補的工程師。Sam Altman 早在 2025 年就公開表示：「也許我們確實需要更少軟體工程師。」但自動化可以發現 bug，卻無法判斷它是否重要——而真正懂得判斷的工程師正在被裁員。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>根據 VulnCheck 數據，2025 年所有 CVE 中僅 <strong>1%</strong> 曾被實際用於攻擊。發現不等於修復，工程師的判斷與修復能力仍然不可替代。</p>
        </div>

        <div class="quote-box">
            <p>「You could read the whole surge as good news. The code did not get more broken, the tools just got better at seeing what was already there. It is a comforting story, and it falls apart the moment you remember who else owns the tools.」</p>
            <cite>— Tech Trenches</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>AI 安全掃描工具的普及提高了漏洞發現效率，但也製造了大量待處理項目。真正的挑戰在於：如何在 AI 輔助發現與人類工程師修復之間建立平衡。沒有工程師確認和修補，發現本身毫無意義。企業在採用 AI 安全工具的同時，必須確保有足夠的人力資源進行漏洞確認與修復。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2025</div>
                <div class="timeline-title">Sam Altman 發言</div>
                <div class="timeline-desc">OpenAI CEO 表示「也許我們確實需要更少軟體工程師」</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025</div>
                <div class="timeline-title">CVE 利用統計</div>
                <div class="timeline-desc">VulnCheck 數據顯示僅 1% CVE 曾被實際用於攻擊</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026</div>
                <div class="timeline-title">AI 工具爆發</div>
                <div class="timeline-desc">AI 安全掃描工具發現漏洞數量飆升，企業庫存積壓</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026</div>
                <div class="timeline-title">裁員潮持續</div>
                <div class="timeline-desc">同時企業持續裁減工程師團隊</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">現況</div>
                <div class="timeline-title">生成超越審查</div>
                <div class="timeline-desc">AI 生成代碼速度 > 審查速度，成為安全漏洞源頭</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>對比項目</th>
                    <th>攻擊者</th>
                    <th>防禦者</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>工具能力</td>
                    <td>使用同樣 AI 掃描器</td>
                    <td class="highlight-col">依賴同樣 AI 掃描器</td>
                </tr>
                <tr>
                    <td>工作模式</td>
                    <td>專注一件事，控制時間軸</td>
                    <td class="highlight-col">需應對所有漏洞，無法控制節奏</td>
                </tr>
                <tr>
                    <td>漏洞態度</td>
                    <td>確認可觸發後才行動</td>
                    <td class="highlight-col">必須處理所有發現</td>
                </tr>
                <tr>
                    <td>效率瓶頸</td>
                    <td>無</td>
                    <td class="highlight-col">人類工程師產能受限</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'Why AI Security Tools Still Need Your Engineers',
    'h1': 'AI 安全工具找到了漏洞<br>卻找不到修補的人',
    'subtitle': '發現不等於修復：VulnCheck 數據顯示僅 1% CVE 曾被實際攻擊',
    'source_url': 'https://techtrenches.dev/p/ai-finds-the-holes-only-your-engineers',
    'source_name': 'Tech Trenches',
    'pub_date': '2026-07-05',
    'img_alt': '工程師面對大量安全警告，抱頭苦惱的場景',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260705_104500',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
