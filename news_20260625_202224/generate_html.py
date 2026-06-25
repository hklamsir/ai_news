#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate HTML for AI news article"""

import sys
import os

script_dir = '/home/lamsir/.openclaw/workspace/skills/ai-news/script'
sys.path.insert(0, script_dir)

from html_utils import assemble_article

article_dir = '/home/lamsir/ai_news/news_20260625_202224'

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://github.com/QwenLM/Qwen-AgentWorld" target="_blank">GitHub QwenLM/Qwen-AgentWorld</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-24</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>阿里雲 Qwen 團隊開源 Qwen-AgentWorld，這是首個覆蓋七個統一領域的原生語言世界模型，訓練數據超過 1000 萬條真實互補軌跡。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔬</div>
            <div class="tech-card-content">
                <h4>什麼是語言世界模型？</h4>
                <p>與過往將世界建模作為事後附加元件的做法不同，Qwen-AgentWorld 是「原生語言世界模型」——環境建模從 CPT 階段就已成為訓練目標，而非事後添加。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔄</div>
            <div class="tech-card-content">
                <h4>三階段訓練流程</h4>
                <p><strong>CPT</strong>（持續預訓練）：注入環境知識<br><strong>SFT</strong>（監督微調）：激活下一狀態預測推理<br><strong>RL</strong>（強化學習）：提升模擬保真度</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌐</div>
            <div class="tech-card-content">
                <h4>七個統一領域</h4>
                <p>首個單一模型覆蓋七個代理交互領域：MCP、Search、Terminal、SWE、Android、Web、OS</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>AgentWorldBench 評測</h4>
                <p>從五個維度評估：格式、事實性、一致性、真實性、質量。加入 LWM RL 後，多項指標提升超過 10 個百分點。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Qwen-AgentWorld-35B-A3B（MoE，35B 總參數 / 3B 活躍參數，256K 上下文）已開源，AgentWorldBench 評測基準亦已開源（Apache 2.0）。</p>
        </div>

        <div class="quote-box">
            <p>「與過往將世界建模作為事後附加元件的做法不同，Qwen-AgentWorld 是原生語言世界模型：環境建模從 CPT 階段就已成為訓練目標。」</p>
            <cite>— Qwen-AgentWorld GitHub README</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Qwen-AgentWorld 的開源標誌著語言世界模型進入新階段。這種「原生」方法在多個代理任務領域展現顯著優勢，為研究者和開發者提供了強大的工具。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026-06-24</div>
                <div class="timeline-title">正式開源發布</div>
                <div class="timeline-desc">Qwen-AgentWorld-35B-A3B 及 AgentWorldBench 開源</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">訓練階段 1</div>
                <div class="timeline-title">CPT 注入環境知識</div>
                <div class="timeline-desc">持續預訓練階段注入環境知識</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">訓練階段 2</div>
                <div class="timeline-title">SFT 激活推理</div>
                <div class="timeline-desc">監督微調激活下一狀態預測推理</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">訓練階段 3</div>
                <div class="timeline-title">RL 提升保真度</div>
                <div class="timeline-desc">強化學習階段提升模擬保真度</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">擴展更多領域</div>
                <div class="timeline-desc">持續擴展語言世界模型覆蓋的領域</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>模型</th>
                    <th>Terminal-Bench 2.0</th>
                    <th>SWE-Bench Verified</th>
                    <th>SWE-Bench Pro</th>
                    <th>WideSearch F1</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Qwen3.5-35B-A3B-SFT</td>
                    <td>33.25</td>
                    <td>64.47</td>
                    <td>42.18</td>
                    <td>33.38</td>
                </tr>
                <tr>
                    <td>+ LWM RL</td>
                    <td class="highlight-col">39.55 (+6.30)</td>
                    <td class="highlight-col">67.86 (+3.39)</td>
                    <td class="highlight-col">47.42 (+5.24)</td>
                    <td class="highlight-col">46.17 (+12.79)</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'Qwen-AgentWorld：通用代理的語言世界模型',
    'h1': 'Qwen-AgentWorld：通用代理的語言世界模型',
    'subtitle': '阿里雲 Qwen 團隊開源首個覆蓋七個統一領域的原生語言世界模型',
    'source_url': 'https://github.com/QwenLM/Qwen-AgentWorld',
    'source_name': 'GitHub QwenLM',
    'pub_date': '2026-06-24',
    'img_alt': 'Qwen-AgentWorld：首個原生語言世界模型',
}

success, errors = assemble_article(
    article_dir=article_dir,
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print("❌ HTML 生成失敗")
    for e in errors:
        print(f"  {e}")
