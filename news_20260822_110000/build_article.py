#!/usr/bin/env python3
import sys, os
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://techcrunch.com/2026/08/20/chatgpt-can-now-send-texts-for-you-with-new-apple-messages-plugin/" target="_blank">TechCrunch</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-20</p>
            <p><strong>🤖 處理方式</strong>：Tavily 內容擷取 + AI 繁體中文摘要</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>OpenAI 推出 ChatGPT Apple Messages 插件，讓 iMessage 用戶可以將訊息收件箱連接至 ChatGPT，讓 AI 代為排序、分析、編輯訊息，甚至直接代發訊息，標誌着 AI 從「建議」走向「代執行」的關鍵轉變。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📱</div>
            <div class="tech-card-content">
                <h4>直接代發訊息</h4>
                <p>用戶可要求 ChatGPT 根據收到的訊息，建議後續回覆內容並代為發送給聯絡人。OpenAI 官方宣傳影片展示：用戶請 ChatGPT 根據前一天收到的訊息，建議要發給聯絡人的跟進訊息。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>深度搜尋訊息歷史</h4>
                <p>用戶可透過 ChatGPT 搜尋埋在訊息歷史深處的過往對話，快速找到曾經分享的資料、預訂記錄或其他重要資訊。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">✏️</div>
            <div class="tech-card-content">
                <h4>排序、分析、編輯</h4>
                <p>用戶可直接在 ChatGPT 介面內對 iMessage 對話進行排序、分析或編輯，大幅提升訊息管理效率。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💼</div>
            <div class="tech-card-content">
                <h4>支援專業場景</h4>
                <p>插件同時支援 Codex 和 ChatGPT Work，個人和企業用戶均可使用，不僅是個人日常應用，也可融入專業工作流程。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>OpenAI 明確警告用戶：不要開啟「持續批准」（persistent approval）模式。這會移除你在 ChatGPT 代發訊息前的最後審查機會，訊息將在無需你確認的情況下直接發送。</p>
        </div>

        <div class="quote-box">
            <p>「這項功能運行在用戶本機，且不會為所有訊息建立索引。」</p>
            <cite>— OpenAI 向 Bloomberg 表示</cite>
        </div>

        <h3>🔐 隱私疑慮</h3>
        <p>與多數 AI 相關功能一樣，這項新插件引發隱私問題。OpenAI 向 Bloomberg 表示插件在用戶本機運行且「不會為所有訊息建立索引」，但 TechCrunch 指出這些說明的具體意涵尚不明確。TechCrunch 已向 OpenAI 進一步查詢詳情，目前尚未獲得回覆。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026-08-20</div>
                <div class="timeline-title">OpenAI 推出 Apple Messages 插件</div>
                <div class="timeline-desc">插件正式上線，用戶可將 iMessage 收件箱連接 ChatGPT</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-08-20</div>
                <div class="timeline-title">OpenAI 向 Bloomberg 強調隱私立場</div>
                <div class="timeline-desc">強調插件本地運行、不建立訊息索引，但具體細節未明</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-08-20</div>
                <div class="timeline-title">TechCrunch 向 OpenAI 查詢更多資訊</div>
                <div class="timeline-desc">TechCrunch 就隱私疑慮進一步採訪，OpenAI 尚未回覆</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來（預測）</div>
                <div class="timeline-title">隱私監管機構或介入</div>
                <div class="timeline-desc">随着 AI 插件接觸用戶敏感個人訊息，隱私合規問題可能受到監管機構關注</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來（預測）</div>
                <div class="timeline-title">AI 代執行功能普及</div>
                <div class="timeline-desc">從建議到代執行，AI 個人助理功能持續進化，便利性與安全性平衡成關鍵議題</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>功能</th>
                    <th>說明</th>
                    <th>風險等級</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>代發訊息</td>
                    <td>ChatGPT 直接以用戶身份發送 iMessage</td>
                    <td class="highlight-col">⚠️ 高（建議保持審查）</td>
                </tr>
                <tr>
                    <td>持續批准模式</td>
                    <td>ChatGPT 無需確認直接發送</td>
                    <td class="highlight-col">❌ 危險（官方建議停用）</td>
                </tr>
                <tr>
                    <td>訊息排序分析</td>
                    <td>AI 讀取並整理訊息內容</td>
                    <td>⚠️ 中（涉及敏感對話）</td>
                </tr>
                <tr>
                    <td>深度搜尋歷史</td>
                    <td>ChatGPT 可存取全部訊息歷史</td>
                    <td>⚠️ 中（數據留在本機）</td>
                </tr>
                <tr>
                    <td>刪除訊息</td>
                    <td>AI 協助刪除指定訊息</td>
                    <td>⚠️ 中（需確認目標正確）</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'ChatGPT 新增 Apple Messages 插件：可代你發送 iMessage 文字訊息',
    'h1': 'ChatGPT 新增<br>Apple Messages 插件',
    'subtitle': 'AI 從建議走向代執行：iMessage 隱私疑慮隨之而來',
    'source_url': 'https://techcrunch.com/2026/08/20/chatgpt-can-now-send-texts-for-you-with-new-apple-messages-plugin/',
    'source_name': 'TechCrunch',
    'pub_date': '2026-08-20',
    'img_alt': 'ChatGPT Apple Messages 插件示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260822_110000',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print("❌ HTML 生成失敗:")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)
