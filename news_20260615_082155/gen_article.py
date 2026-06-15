#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.engadget.com/2192907/gemini-can-now-adjust-your-picture-settings-on-google-tv/" target="_blank">ENGADGET</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-15</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Google TV 整合 Gemini AI，推出語音指令調整畫質和音頻設定功能，用家可以告別層層選單的遙控器操作，用自然語音控制亮度、對比、畫質模式、音量及 EQ。目前率先登陸美國部分 TCL 型號。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📺</div>
            <div class="tech-card-content">
                <h4>畫質調整指令</h4>
                <p>用戶可以直接說「設定畫質模式為運動模式」，Gemini 就會自動調整。正值世界盃期間，預計會非常受歡迎。若畫面太暗，說「屏幕太暗」，Gemini 會自動修正亮度。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔊</div>
            <div class="tech-card-content">
                <h4>音頻與 EQ 控制</h4>
                <p>除畫質外，亦支援音量調整、EQ 均衡器設定。若反映「對白聽不清」，Gemini 會自動增強人聲頻率，提升語音清晰度。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎯</div>
            <div class="tech-card-content">
                <h4>快速設定導航</h4>
                <p>若不完全信任 AI 的校準能力，用戶可以請 Gemini 直接打開特定設定選單，省去傳統遙控器層層點擊的麻煩，再自行接管微調。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>目前限制：僅支援部分 TCL 型號</h4>
                <p>功能目前獨家登陸美國部分 TCL 型號，包括 QM9K、X11L、QM9L、QM8L、RM9L，需進行系統更新才能使用。其他品牌或型號的支援時間尚未公佈。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 Google TV Gemini 功能時間線</h4>
            <ul>
                <li><strong>2025 年</strong>：新聞摘要功能 debut</li>
                <li><strong>2026 年 3 月</strong>：Richer Visual Help、體育簡報（Sports Briefs）、視覺 deep dives</li>
                <li><strong>2026 年 6 月</strong>：畫質及音頻語音控制功能正式推出</li>
            </ul>
        </div>

        <div class="quote-box">
            <p>「Gemini 會自動調整亮度或增強人聲，但各設備支援的畫質和音頻模式各有不同，建議用戶先了解自己的電視有哪些功能，再使用新的語音指令。」</p>
            <cite>— Google 官方建議</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這次更新顯示 Google 正在逐步將 Gemini AI 深層整合進 Google TV 的各個層面。從資訊查詢、體育摘要，到如今的畫質及音頻控制，語音助手正從被動查詢工具轉變為主動的客廳體驗管理者。隨著功能擴展，其他 Android TV 品牌有望在未來獲得支援。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年初</div>
                <div class="timeline-title">CES 發布</div>
                <div class="timeline-desc">Google 在 CES 2026 首次發布 Gemini 畫質/音頻控制功能</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 3 月</div>
                <div class="timeline-title">視覺功能擴展</div>
                <div class="timeline-desc">Richer Visual Help、體育簡報 Sports Briefs、視覺 deep dives 上線</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">畫質語音控制上線</div>
                <div class="timeline-desc">Gemini 正式可在 Google TV 上調整畫質和音頻設定</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">即將推出</div>
                <div class="timeline-title">TCL 型號支援</div>
                <div class="timeline-desc">QM9K、X11L、QM9L、QM8L、RM9L 陸續收到系統更新</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">待定</div>
                <div class="timeline-title">其他品牌支援</div>
                <div class="timeline-desc">尚未宣佈其他品牌或型號的支援時間表</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>功能</th>
                    <th>操作方式</th>
                    <th> Gemini 語音控制</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>亮度/對比調整</td>
                    <td>遙控器 → 設定 → 畫質 → 層層選單</td>
                    <td class="highlight-col">直接語音：「屏幕太暗」</td>
                </tr>
                <tr>
                    <td>畫質模式切換</td>
                    <td>手動在多個模式中選擇</td>
                    <td class="highlight-col">直接語音：「設為運動模式」</td>
                </tr>
                <tr>
                    <td>人聲增強</td>
                    <td>進入音頻設定 → 語音增強</td>
                    <td class="highlight-col">直接語音：「對白聽不清」</td>
                </tr>
                <tr>
                    <td>快速開啟設定</td>
                    <td>多次按鈕導航至目標選單</td>
                    <td class="highlight-col">語音要求 Gemini 直接打開特定選單</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Gemini Can Now Adjust Your Picture Settings On Google TV',
    'h1':          'Gemini Can Now Adjust Your<br>Picture Settings On Google TV',
    'subtitle':    'Google TV 整合 Gemini AI，用語音指令調整畫質和音頻設定',
    'source_url':  'https://www.engadget.com/2192907/gemini-can-now-adjust-your-picture-settings-on-google-tv/',
    'source_name': 'ENGADGET',
    'pub_date':    '2026-06-15',
    'img_alt':     'Gemini AI 調整 Google TV 畫質設定',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260615_082155',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")