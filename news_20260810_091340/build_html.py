#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.engadget.com/2232014/ai-is-now-making-new-viruses/" target="_blank">Engadget</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-10</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>AI 系統 Evo 成功生成約 70 萬種病毒候選，其中 16 種在實驗室培育成活病毒，部分繁殖速度甚至超越自然病毒。這項突破為基因療法帶來希望，卻也引發生物武器風險的嚴重擔憂。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🧬</div>
            <div class="tech-card-content">
                <h4>Evo 的驚人產能</h4>
                <p>研究團隊使用 Evo AI 系統，一次性生成約 <strong>70 萬種</strong>可能的全新病毒候選，並從中挑選 285 個最具潛力的候選者進行 DNA 合成與細菌植入實驗。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔬</div>
            <div class="tech-card-content">
                <h4>16 種活病毒誕生</h4>
                <p>最終，<strong>16 種</strong> Evo 的「創作」成功培育出可運作的病毒，活性媲美自然界的 Phi X-174 噬菌體，部分病毒繁殖速度甚至更快。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💊</div>
            <div class="tech-card-content">
                <h4>製藥與基因療法潛力</h4>
                <p>AI 設計病毒可改善基因療法、幫助研究基因組、開發對抗有害細菌的工具。嚴格監管下的突破有望造福人類健康。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">☢️</div>
            <div class="tech-card-content">
                <h4>生物武器風險隱憂</h4>
                <p>批評者將此技術比作核能——在正確的人手中可造福人類，在錯誤的人手中卻可造成毀滅性傷害。缺乏監管的 AI 生化研究可能打開潘朵拉的盒子。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Evo 生成 70 萬種病毒 → 篩選 285 種 → 成功培育 16 種活病毒，部分繁殖速度超越自然病毒。</p>
        </div>

        <div class="quote-box">
            <p>「這項技術如同核能——在正確的人手中可以造福人類，在錯誤的人手中卻可能造成毀滅性的生物武器威脅。」</p>
            <cite>— 業界分析師</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這項研究凸顯 AI 發展的雙面刃特性。業界呼籲建立嚴格的倫理規範和監管框架，確保 Evo 這類技術用於正道。監管機構和學術界需就 AI 設計生物分子的安全標準達成共識。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">實驗初期</div>
                <div class="timeline-title">Evo 生成 70 萬病毒候選</div>
                <div class="timeline-desc">AI 系統 Evo 一次性生成約 70 萬種可能的全新病毒</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">篩選階段</div>
                <div class="timeline-title">精選 285 個候選者</div>
                <div class="timeline-desc">研究團隊根據潛力從 70 萬候選中挑選 285 個最具發展性的樣本</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">DNA 合成</div>
                <div class="timeline-title">合成候選病毒 DNA</div>
                <div class="timeline-desc">對 285 個候選者進行 DNA 合成並植入細菌體內</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">培育結果</div>
                <div class="timeline-title">16 種活病毒成功培育</div>
                <div class="timeline-desc">部分病毒繁殖速度超越自然病毒，證明 AI 設計生物分子的可行性</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來展望</div>
                <div class="timeline-title">呼籲建立監管框架</div>
                <div class="timeline-desc">業界呼籲制定 AI 生物設計安全標準，防止技術被濫用</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>自然病毒（Phi X-174）</th>
                    <th>Evo 設計病毒</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>生成方式</td>
                    <td>自然演化</td>
                    <td class="highlight-col">AI 系統 Evo 設計</td>
                </tr>
                <tr>
                    <td>繁殖速度</td>
                    <td>標準參照</td>
                    <td class="highlight-col">部分超越自然病毒</td>
                </tr>
                <tr>
                    <td>候選數量</td>
                    <td>不適用</td>
                    <td class="highlight-col">70 萬種 → 285 種 → 16 種</td>
                </tr>
                <tr>
                    <td>應用潛力</td>
                    <td>自然存在</td>
                    <td class="highlight-col">基因療法、制藥</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'AI is now making new viruses',
    'h1':          'AI is now making new viruses',
    'subtitle':    'Evo AI 系統成功設計並培育出活病毒，製藥潛力與生物武器風險並存',
    'source_url':  'https://www.engadget.com/2232014/ai-is-now-making-new-viruses/',
    'source_name': 'Engadget',
    'pub_date':    '2026-08-10',
    'img_alt':     '顯微鏡下的病毒結構，實驗室場景',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260810_091340',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print(f"❌ HTML 組裝失敗: {errors}")
    sys.exit(1)
