#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate HTML for AI news article"""

import sys
import os

# Add script dir to path
script_dir = '/home/lamsir/.openclaw/workspace/skills/ai-news/script'
sys.path.insert(0, script_dir)

from html_utils import assemble_article

article_dir = '/home/lamsir/ai_news/news_20260625_155948'

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://hk.finance.yahoo.com/news/ai%E6%9C%80%E7%B5%82%E8%B4%8F%E5%AE%B6%E4%B8%8D%E6%98%AFopenai%E6%88%96anthropic-%E5%B0%88%E5%AE%B6%E9%BB%9E%E5%90%8D-%E9%80%99%E5%85%A9%E5%AE%B6%E5%85%AC%E5%8F%B8-%E6%89%8D%E6%98%AF%E6%9C%80%E5%A4%A7%E5%8F%97%E7%9B%8A%E8%80%85-050011084.html" target="_blank">鉅亨網</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-25</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>科技投資專家 Igor Pejic 認為，AI 競賽的真正贏家既非 OpenAI 也非 Anthropic，而是採用「混合戰略」的 Alphabet 與微軟。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔀</div>
            <div class="tech-card-content">
                <h4>兩條通往 AI 經濟的道路</h4>
                <p>投資人只要了解通往 AI 經濟的兩條道路，就能贏得這場競賽的大部分勝利：<strong>技術優先</strong>（追求技術上的絕對領先）與<strong>規模化部署</strong>（著眼於大規模商業化普及）。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>「幻覺」問題制約 AI 發展</h4>
                <p>AI 模型的「幻覺」問題——在缺乏明顯破綻的情況下捏造資訊——仍是挥之不去的隱患。這使得 AI 操作可靠性大打折扣，目前的 AI 仍只能扮演輔助角色。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🚀</div>
            <div class="tech-card-content">
                <h4>AGI 優先陣營：Anthropic、OpenAI、xAI</h4>
                <p>準備上市的 Anthropic、OpenAI，以及隨 SpaceX 一併計畫掛牌的 xAI 被歸類為「AGI 優先」陣營，追求通用人工智慧為核心目標。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏢</div>
            <div class="tech-card-content">
                <h4>Alphabet 與微軟：混合戰略的贏家</h4>
                <p><strong>Alphabet</strong>：DeepMind 演算法實力不亞於對手，但若 AGI 遲遲未能實現，承受的風險遠低於「孤注一擲」的對手。<br><br><strong>微軟</strong>：Copilot 與 Azure 提供穩固基礎，同時持有 OpenAI 重要股權並持續投入自家尖端 AI 模型研發。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>科技投資的分散投資，不只是配置不同地區或商業模式的企業。無論是聚焦於混合型玩家，或同時配置技術先驅與規模化推動者，都需要將多種可能的未來情境納入考量。</p>
        </div>

        <div class="quote-box">
            <p>「美國多數科技公司目前仍將資源優先投入訓練更強大的尖端模型，而非擴大現有模型的使用規模。」</p>
            <cite>— Igor Pejic，《Tech Money》作者</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Pejic 提醒投資人：對於認為 AI 競賽最終將由「快速、大規模部署」決定勝負的投資人，美國市場本身就已提供多元選擇，不必轉向中國業者。蘋果選擇不直接與通用型 AI 正面競爭，而是待 AI 使用量爆發後從中獲利。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2024-2025</div>
                <div class="timeline-title">AI 上市潮醞釀</div>
                <div class="timeline-desc">OpenAI、Anthropic 籌備 IPO，市場對 AI 贏家討論升溫</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025-2026</div>
                <div class="timeline-title">AGI 追求者集結</div>
                <div class="timeline-desc">Anthropic、OpenAI、xAI 被歸類為「AGI 優先」陣營</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026</div>
                <div class="timeline-title">混合戰略受青睞</div>
                <div class="timeline-desc">Alphabet 與微軟被視為最穩健的 AI 投資選擇</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">多元布局成主流</div>
                <div class="timeline-desc">投資人需同時配置技術先驅與規模化推動者</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">長期</div>
                <div class="timeline-title">AGI 實現與否？</div>
                <div class="timeline-desc">市場充斥各種預測時間表，但都只是「瞎猜」</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>公司</th>
                    <th>AI 策略</th>
                    <th>優勢</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Alphabet</td>
                    <td>混合戰略</td>
                    <td class="highlight-col">DeepMind 演算法實力 + 雲端 + 搜尋引擎主導地位</td>
                </tr>
                <tr>
                    <td>微軟</td>
                    <td>多線押注</td>
                    <td class="highlight-col">Copilot + Azure + OpenAI 股權</td>
                </tr>
                <tr>
                    <td>OpenAI / Anthropic / xAI</td>
                    <td>AGI 優先</td>
                    <td>追求技術絕對領先，但風險較高</td>
                </tr>
                <tr>
                    <td>亞馬遜</td>
                    <td>規模化部署</td>
                    <td>AWS 商業化 + Rufus 購物助理</td>
                </tr>
                <tr>
                    <td>Meta</td>
                    <td>規模化部署</td>
                    <td>Llama 模型優化廣告投放</td>
                </tr>
                <tr>
                    <td>蘋果</td>
                    <td>平台策略</td>
                    <td>待 AI 使用量爆發後從中獲利</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'AI最終贏家不是OpenAI或Anthropic？專家點名「這兩家公司」才是最大受益者',
    'h1': 'AI最終贏家不是OpenAI或Anthropic？<br>專家點名「這兩家公司」才是最大受益者',
    'subtitle': '科技投資專家：Alphabet 與微軟的混合戰略才是 AI 競賽中最穩健的選擇',
    'source_url': 'https://hk.finance.yahoo.com/news/ai%E6%9C%80%E7%B5%82%E8%B4%8F%E5%AE%B6%E4%B8%8D%E6%98%AFopenai%E6%88%96anthropic-%E5%B0%88%E5%AE%B6%E9%BB%9E%E5%90%8D-%E9%80%99%E5%85%A9%E5%AE%B6%E5%85%AC%E5%8F%B8-%E6%89%8D%E6%98%AF%E6%9C%80%E5%A4%A7%E5%8F%97%E7%9B%8A%E8%80%85-050011084.html',
    'source_name': '鉅亨網',
    'pub_date': '2026-06-25',
    'img_alt': 'AI最終贏家：混合戰略公司才是最大受益者',
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
