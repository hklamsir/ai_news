#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.engadget.com/2207936/midjourney-wants-studios-that-sued-show-court-ai-use/" target="_blank">Engadget</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-06</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>AI 圖像生成器 Midjourney 正在反擊好萊塢工作室的版權侵權訴訟，要求原告披露其 AI 訓練方式，試圖以「原告同樣在做他們指控的事情」來削弱訴訟立場。</p>

        <div class="tech-card">
            <div class="tech-card-icon">⚖️</div>
            <div class="tech-card-content">
                <h4>訴訟背景</h4>
                <p>去年，多家好萊塢工作室對 Midjourney 提起訴訟，指控其 AI 圖像生成器能夠生成超人、蝙蝠俠和其他版權角色的圖像，涉嫌版權侵權。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎨</div>
            <div class="tech-card-content">
                <h4>Midjourney 的反制策略</h4>
                <p>Midjourney 認為用公開可用的圖像訓練 AI 屬於合理使用（fair use），更重要的是指出這些工作室本身也在用同樣方式訓練自己的 AI 模型。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📋</div>
            <div class="tech-card-content">
                <h4>要求披露的資訊</h4>
                <p>Midjourney 要求工作室提供 AI 業務計劃、研究報告、訓練數據集、模型權重及董事會 AI 簡報資料。不過法官已裁定工作室只需披露「面向消費者」的 AI 應用資訊。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚖️</div>
            <div class="tech-card-content">
                <h4>法律依據</h4>
                <p>Midjourney 律師 Bobby Ghajar 表示：「如果原告正在做他們試圖懲罰的同樣事情，那麼這些證據將直擊 Midjourney 的合理使用和不正當防衛的核心。」</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>此案的聯邦法官裁決可能為「什麼樣的資訊可以在法庭上被採納」樹立先例，影響未來 AI 與版權相關的訴訟。</p>
        </div>

        <div class="quote-box">
            <p>「如果原告正在做他們試圖懲罰的同樣事情，那麼這些證據將直擊 Midjourney 的合理使用和不正當防衛的核心。」</p>
            <cite>— Bobby Ghajar，Midjourney 律師</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這場法律戰的結果將決定 AI 訓練與版權之間的界限。隨著 AI 技術在各產業的廣泛應用，如何在保護版權與促進技術創新之間取得平衡，將是司法機構和立法者面臨的重大挑戰。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">去年</div>
                <div class="timeline-title">工作室提起訴訟</div>
                <div class="timeline-desc">Warner Bros. Discovery、Disney、Universal Studios 等指控 Midjourney 版權侵權</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">Midjourney 回應</div>
                <div class="timeline-title">合理使用抗辯</div>
                <div class="timeline-desc">主張用公開圖像訓練 AI 屬於合理使用，且工作室本身也這樣做</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">6 月中旬</div>
                <div class="timeline-title">法官初步裁決</div>
                <div class="timeline-desc">法官裁定工作室只需披露「面向消費者」的 AI 應用資訊</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">Midjourney 上訴</div>
                <div class="timeline-title">請求推翻裁決</div>
                <div class="timeline-desc">要求聯邦法院推翻法官裁決，強制工作室全面披露 AI 訓練資料</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">待裁決</div>
                <div class="timeline-title">將樹立先例</div>
                <div class="timeline-desc">此案結果將影響未來 AI 與版權相關訴訟的證據採納標準</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>對比項目</th>
                    <th>工作室立場</th>
                    <th>Midjourney 立場</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>AI 訓練方式</td>
                    <td>指責 Midjourney 用版權圖像訓練</td>
                    <td class="highlight-col">聲稱自己也用同樣方式訓練</td>
                </tr>
                <tr>
                    <td>合理使用主張</td>
                    <td>反對</td>
                    <td class="highlight-col">支援，認為公開圖像可用於訓練</td>
                </tr>
                <tr>
                    <td>資訊披露</td>
                    <td class="highlight-col">已獲準只披露消費級 AI 應用</td>
                    <td>要求全面披露</td>
                </tr>
                <tr>
                    <td>法律依據</td>
                    <td>版權侵權</td>
                    <td class="highlight-col">公平使用 + 不正當防衛</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Midjourney 要求好萊塢工作室在法庭上披露 AI 使用方式',
    'h1':          'Midjourney 要求好萊塢工作室<br>在法庭上披露 AI 使用方式',
    'subtitle':    'AI 圖像生成器反擊版權訴訟，要求原告披露自身 AI 訓練方式',
    'source_url':  'https://www.engadget.com/2207936/midjourney-wants-studios-that-sued-show-court-ai-use/',
    'source_name': 'Engadget',
    'pub_date':    '2026-07-06',
    'img_alt':     'Midjourney 對好萊塢工作室訴訟示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260706_082829',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
