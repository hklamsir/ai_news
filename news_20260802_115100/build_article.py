import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.engadget.com/2227710/a-dollar2-sticker-let-me-bypass-the-meta-glasses-anti-creep-feature/" target="_blank">Engadget</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-31</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Meta 智能眼鏡的 LED 錄影指示燈本意是保障旁觀者隱私，但市面上出現一款不到 2 美元的「防窺貼紙」，聲稱能繞過此安全功能。實測證明這些便宜配件意外地有效，令 Meta 的防偷拍機制形同虛設。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔴</div>
            <div class="tech-card-content">
                <h4>LED 指示燈的貓鼠遊戲</h4>
                <p>Ray-Ban Meta 智能眼鏡配備明亮的 LED 指示燈，錄影時會亮起提醒旁觀者。然而這項安全設計催生了一系列「繞過攻略」——用戶不斷尋找漏洞，而 Meta 則不斷堵塞。今次最新的漏洞，只是一張薄薄的隔光貼紙。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏷️</div>
            <div class="tech-card-content">
                <h4>2 美元貼紙如何運作</h4>
                <p>這種所謂的「隱私配件」由兩層組成：帶有缺口的小型透明塑料片 + 覆蓋在上的黑色貼紙。缺口設計讓部分光線仍能觸及感測器，使 Meta 的安全機制認為一切正常，同時黑色貼紙有效遮蓋 LED 燈。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚖️</div>
            <div class="tech-card-content">
                <h4>Meta 的回應</h4>
                <p>Meta 表示：「發現繞過此內建隱私保護的產品和用戶已違反我們的政策，我們正在探索加強檢測這種篡改行為的能力，並停用相關功能。此外，我們會移除推廣篡改服務的廣告、帖子和 Marketplace 列表，並對違規者採取行動——包括永久停權。」</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>繁榮的地下市場</h4>
                <p>這類產品在 TikTok Shop 等平台有旺盛需求，某款套裝售價 16.99 美元，包含十二張貼紙和一對輔助定位的鑷子。這個現象凸顯 Meta 目前在智能眼鏡隱私問題上正面臨的重大挑戰。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>這些「隱私配件」之所以有效，關鍵在於不完全遮擋 LED，而是精確控制光線量讓感測器仍能感知光線，既騙過了 Meta 的安全機制，又不會觸發「LED 被遮擋」的警告。</p>
        </div>

        <div class="quote-box">
            <p>「Products and people that have found ways around this built-in privacy protection violate our policies.」</p>
            <cite>— Meta 發言人聲明</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這場貓鼠遊戲短期內不會結束。Meta 若要真正解決問題，可能需要從硬體層面著手——例如要求每次開機時強制驗證 LED 功能正常，否則直接停用相機。但這將為普通用戶帶來不便，如何平衡隱私保障與使用便利性，將是 Meta 持續面對的難題。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2023 年</div>
                <div class="timeline-title">Ray-Ban Meta 眼鏡上市</div>
                <div class="timeline-desc">配備 LED 錄影指示燈作為隱私保障</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2024-2025 年</div>
                <div class="timeline-title">Meta 持續更新防篡改機制</div>
                <div class="timeline-desc">軟件更新逐步堵塞繞過漏洞</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年底</div>
                <div class="timeline-title">Meta 推出更嚴格措施</div>
                <div class="timeline-desc">若 LED 被物理損壞，永久停用相機功能</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年中</div>
                <div class="timeline-title">隔光貼紙繞過方案流出</div>
                <div class="timeline-desc">利用光線控制而非物理遮擋的新方法</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月</div>
                <div class="timeline-title">Meta 警告將永久停權</div>
                <div class="timeline-desc">明確表示將打擊篡改行為</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>方案</th>
                    <th>原理</th>
                    <th>效果</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>物理遮擋 LED</td>
                    <td>完全覆蓋 LED</td>
                    <td class="highlight-col">Meta 偵測到，永久停用相機</td>
                </tr>
                <tr>
                    <td>隔光貼紙（最新）</td>
                    <td>精確控制光線量，騙過感測器</td>
                    <td class="highlight-col">安全機制被成功繞過</td>
                </tr>
                <tr>
                    <td>膠帶直接遮擋</td>
                    <td>完全遮光</td>
                    <td>立即觸發警告，相機被鎖</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'A dollar2 sticker let me bypass the Meta Glasses anti-creep feature',
    'h1':          '2 美元貼紙<br>繞過 Meta 眼鏡防偷拍',
    'subtitle':    'Engadget 實測：隔光貼紙令 LED 指示燈失效，Meta 警告將永久停權',
    'source_url':  'https://www.engadget.com/2227710/a-dollar2-sticker-let-me-bypass-the-meta-glasses-anti-creep-feature/',
    'source_name': 'Engadget',
    'pub_date':    '2026-07-31',
    'img_alt':     '2 美元貼紙繞過 Meta 智能眼鏡防偷拍功能',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260802_115100',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
