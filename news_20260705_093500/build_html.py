#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://gigazine.net/gsc_news/en/20260704-alibaba-bans-claude-code/" target="_blank">GIGAZINE</a>、<a href="https://www.reuters.com/world/china/alibaba-ban-claude-code-workplace-over-alleged-backdoor-risks-source-says-2026-07-03/" target="_blank">Reuters</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-04 至 2026-07-05</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>中國科技巨頭阿里巴巴宣布禁用員工使用 Anthropic 的 AI 編程工具 Claude Code，主因是該工具被發現內含可識別中國用戶的隱藏代碼，禁令將於 2026 年 7 月 10 日生效。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>事件起因</h4>
                <p>阿里巴巴禁止員工在工作場所使用 Claude Code，原因涉及安全風險。Anthropic 工程師 Tariq Sihipar 解釋，團隊在 2026 年 3 月推出了一項實驗性功能，旨在防止未經授權的轉售商濫用帳戶，並保護系統免受「蒸餾」（distillation）攻擊——即用其他模型的輸出訓練自家 AI 的做法。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💡</div>
            <div class="tech-card-content">
                <h4>技術爭議</h4>
                <p>Claude Code 被發現內含可追蹤中國用戶的隱藏代碼，引發安全疑慮。Anthropic 此前曾指責阿里巴巴的 AI 研究機構 Qwen Lab 對 Claude 發動蒸餾攻擊，涉及超過 2,880 萬次非法存取。Anthropic 表示相關緩解措施已於後續版本中加強，原本就計劃下線這項實驗功能。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>商業衝擊</h4>
                <p>阿里巴巴將 Claude Code 列為「高風險軟體」，並建議員工改用公司內部開發的 Qoder 工具。這項禁令也反映了中美 AI 領域的激烈競爭態勢。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>風波背景</h4>
                <p>此前 Anthropic 已公開指責阿里巴巴的 Qwen Lab 發動「蒸餾攻擊」，非法存取 Claude 模型超過 2,880 萬次。雙方關係持續緊張，這次禁令可視為科技冷戰的又一表現。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>禁令將於 <strong>2026 年 7 月 10 日</strong>正式生效。阿里巴巴建議員工改用公司內部工具 <strong>Qoder</strong>。</p>
        </div>

        <div class="quote-box">
            <p>「Since March 2026, we have been conducting experiments aimed at preventing account abuse by unlicensed resellers and protecting against distillation.」</p>
            <cite>— Tariq Sihipar, Anthropic 工程師</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>此次風波顯示跨國科技公司在數據安全與 AI 倫理上面臨的挑戰。隨著各國加強對 AI 工具的監管，企業需在技術創新與風險管控間取得平衡。中美 AI 競爭將持續升溫，各類工具的合規性將成為企業決策的關鍵因素。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026-03</div>
                <div class="timeline-title">Anthropic 啟動實驗功能</div>
                <div class="timeline-desc">Anthropic 推出可識別中國用戶的實驗性代碼</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-06-25</div>
                <div class="timeline-title">蒸餾攻擊指控</div>
                <div class="timeline-desc">Anthropic 指責阿里巴巴 Qwen Lab 非法存取 Claude 超過 2,880 萬次</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-01</div>
                <div class="timeline-title">功能下線</div>
                <div class="timeline-desc">Anthropic 表示已全面回滾爭議性實驗功能</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-03</div>
                <div class="timeline-title">Reuters 率先報導</div>
                <div class="timeline-desc">消息人士透露阿里巴巴即將實施禁令</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07-10</div>
                <div class="timeline-title">禁令生效</div>
                <div class="timeline-desc">阿里巴巴員工正式禁止使用 Claude Code</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>Anthropic 立場</th>
                    <th>阿里巴巴立場</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>用戶追蹤爭議</td>
                    <td>防止帳戶濫用與蒸餾攻擊</td>
                    <td class="highlight-col">列為高風險軟體</td>
                </tr>
                <tr>
                    <td>蒸餾攻擊指控</td>
                    <td>Qwen Lab 非法存取 2,880 萬次</td>
                    <td class="highlight-col">未公開回應</td>
                </tr>
                <tr>
                    <td>替代方案</td>
                    <td>持續改進 Claude Code</td>
                    <td class="highlight-col">推員工使用 Qoder</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'Alibaba bans employees from using Claude Code due to security risk concerns.',
    'h1': '阿里巴巴禁用 Claude Code<br>AI 工具安全爭議升級',
    'subtitle': '中國科技巨頭宣布禁用 Anthropic 編程工具，憂安全風險與用戶追蹤爭議',
    'source_url': 'https://gigazine.net/gsc_news/en/20260704-alibaba-bans-claude-code/',
    'source_name': 'GIGAZINE / Reuters',
    'pub_date': '2026-07-05',
    'img_alt': '阿里巴巴辦公室大螢幕顯示 Claude Code 被標記為禁止存取的示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260705_093500',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
