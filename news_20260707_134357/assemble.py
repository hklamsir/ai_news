#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.hkej.com/instantnews/hongkong/article/4451402/" target="_blank">信報 (HKEJ)</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-07</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>ManpowerGroup 香港調查顯示，57% 受訪僱主認為日常 AI 工具已成為提升生產力的首要槓桿，反映企業由傳統管理制度轉向以 AI 工具和相關技能為核心的結構性轉變。</p>

        <div class="tech-card">
            <div class="tech-card-icon">💼</div>
            <div class="tech-card-content">
                <h4>日常 AI 工具，生產力提升排名首位</h4>
                <p>57% 受訪僱主表示「用於日常工作的 AI 工具」帶來生產力提升，超越業務策略工具（53%）及自動化流程工具（53%）。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤝</div>
            <div class="tech-card-content">
                <h4>AI + HR 結合，重塑招聘體驗</h4>
                <p>44% 僱主視「人工智能輔助撰寫職位描述」為最有價值招聘創新，43% 看重「自動更新招聘流程狀態」，41% 注重「專業履歷表審閱服務」。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🧠</div>
            <div class="tech-card-content">
                <h4>軟技能無可取代，解難能力居首</h4>
                <p>71% 僱主願意為解難能力支付溢價，70% 重視溝通能力，66% 看重時間管理。AI 時代軟技能反而更受重視。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💻</div>
            <div class="tech-card-content">
                <h4>AI 技能成薪酬溢價關鍵</h4>
                <p>67% 僱主願為「人工智能模型及應用程式開發」人才支付溢價，62% 重視「AI 素養」，57% 看重「銷售及市場營銷技能」。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>AI 已由試驗性應用逐步走向核心業務流程，企業愈來愈着重把科技應用與人才發展結合，以提升整體生產力及競爭力。</p>
        </div>

        <div class="quote-box">
            <p>「過去僱主提升生產力主要倚重管理制度與人力資源政策，現在則明顯轉向以 AI 工具和相關技能為首要槓桿。」</p>
            <cite>— ManpowerGroup 香港調查</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>香港僱主在推動 AI 與數碼轉型的同時，需要多元職能共同配合，才能真正把技術能力轉化為業務增長。AI 工具已成為提升生產力的核心手段，但具備強大軟技能的人才仍是把 AI 效益轉化為業務成果的關鍵。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">57%</div>
                <div class="timeline-title">日常 AI 工具提升生產力</div>
                <div class="timeline-desc">排名第一的生產力提升來源</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">71%</div>
                <div class="timeline-title">解難能力最受重視</div>
                <div class="timeline-desc">軟技能薪酬溢價首位</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">67%</div>
                <div class="timeline-title">AI 開發技能最具價值</div>
                <div class="timeline-desc">技術技能薪酬溢價首位</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">44%</div>
                <div class="timeline-title">AI 輔助職位描述最具創新價值</div>
                <div class="timeline-desc">招聘創新應用首位</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">524</div>
                <div class="timeline-title">受訪僱主數目</div>
                <div class="timeline-desc">ManpowerGroup 香港調查樣本</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>AI 工具類型</th>
                    <th>提升生產力</th>
                    <th>應用場景</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>日常 AI 工具</td>
                    <td class="highlight-col">57%</td>
                    <td>日常工作流程優化</td>
                </tr>
                <tr>
                    <td>業務策略 AI 工具</td>
                    <td>53%</td>
                    <td>策略規劃與決策支持</td>
                </tr>
                <tr>
                    <td>自動化流程 AI 工具</td>
                    <td>53%</td>
                    <td>流程自動化與效率提升</td>
                </tr>
                <tr>
                    <td>AI 技能提升</td>
                    <td>50%</td>
                    <td>人才發展與培訓</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '調查丨57%受訪僱主指日常AI工具帶來生產力提升',
    'h1': '調查丨57%受訪僱主指<br>日常AI工具帶來生產力提升',
    'subtitle': 'ManpowerGroup 香港調查：AI 工具已成為提升生產力首要槓桿，軟技能依然無可取代',
    'source_url': 'https://www.hkej.com/instantnews/hongkong/article/4451402/',
    'source_name': '信報 (HKEJ)',
    'pub_date': '2026-07-07',
    'img_alt': '五成七僱主指AI提升生產力',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260707_134357',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 文章組裝成功")
else:
    print("❌ HTML 文章組裝失敗")
    for err in errors:
        print(f"   - {err}")
