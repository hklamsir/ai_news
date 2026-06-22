import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://mp.weixin.qq.com/s/nq4EnNvnVNoX45r8d6rM5Q" target="_blank">AI信息Gap（微信公眾號）</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-22</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Agnes AI 自 6 月 1 日將文字、圖片、視頻三個模型 API 同時免費開放後，第二週 Token 總量飆升至 3.12 萬億，同時文本模型升級支援百萬 Token 上下文，圖片模型支援 4K 生成，三週建立龐大開源生態系。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔥</div>
            <div class="tech-card-content">
                <h4>免費效應：3.12 萬億 Token</h4>
                <p>Agnes 免費開放第二週，Token 總量達 3.12 萬億，其中文字模型貢獻約 1.9 萬億，圖片和視頻模型合計 1.2 萬億。成本歸零後，用戶真正在大量創作，而非僅僅試用。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📈</div>
            <div class="tech-card-content">
                <h4>百萬上下文 + 4K 生圖升級</h4>
                <p><strong>Agnes-2.0-Flash</strong>：正式上線百萬 Token 上下文窗口，可將一整本長篇小說、數十份企業年報、或大型代碼項目直接全文投喂給 AI。<br>
                <strong>Agnes-Image-2.1-Flash</strong>：支援 4K 生圖（最高 4096×4096），支援多步編輯、局部修改、主體一致性保持等進階功能。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🛠️</div>
            <div class="tech-card-content">
                <h4>開源生態系快速成型</h4>
                <p>免費三週，GitHub 已出現大量開源項目：將三個模型封裝為 Agent Skill（一鍵接入 Codex、Claude Code、OpenClaw、Hermes）、ComfyUI 節點支援、完整創作平台（一條鏈路全部使用 Agnes API）。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎬</div>
            <div class="tech-card-content">
                <h4>網友創作完整短片</h4>
                <p>有網友已用 Agnes 視頻模型創作完整短片《最後的守燈人》，3 分 18 秒、20 個鏡頭、11 段對白，全程使用 Agnes API 生成。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 關鍵數據</h4>
            <p>第二週 Token 總量：<strong>3.12 萬億</strong>｜文本模型：<strong>1.9 萬億</strong>｜圖片+視頻：<strong>1.2 萬億</strong>｜上下文窗口：<strong>100 萬 Token</strong>｜圖片解像度：<strong>4K（4096×4096）</strong></p>
        </div>

        <div class="quote-box">
            <p>「三個模型，全免費，沒有限期，還在持續升級中。」</p>
            <cite>— AI信息Gap</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Agnes AI 以全模態 + 完全免費 + 持續升級的策略，快速建立了開發者生態系。百萬 Token 上下文打破了長文處理瓶頸，4K 生圖滿足了專業創作需求。當成本壁壘消失，創作邊界正在重新定義。語音生成 TTS 即將上線，全模態链路最後一塊拼圖即將完成。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">6 月 1 日</div>
                <div class="timeline-title">Agnes 全模態 API 免費開放</div>
                <div class="timeline-desc">文字、圖片、視頻三個模型 API 同時免費，無限期</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第二週</div>
                <div class="timeline-title">Token 總量達 3.12 萬億</div>
                <div class="timeline-desc">文字模型 1.9 萬億，圖片+視頻模型 1.2 萬億</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第三週前</div>
                <div class="timeline-title">Agnes-2.0-Flash 百萬上下文</div>
                <div class="timeline-desc">百萬 Token 上下文窗口上線，長文處理無壓力</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第三週前</div>
                <div class="timeline-title">Agnes-Image-2.1-Flash 4K 生圖</div>
                <div class="timeline-desc">支援 4K（4096×4096）生圖及多步編輯</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">即將上線</div>
                <div class="timeline-title">語音生成 TTS</div>
                <div class="timeline-desc">全模態链路最後一塊拼圖即將完成</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>模型</th>
                    <th>升級內容</th>
                    <th>規格</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Agnes-2.0-Flash</td>
                    <td class="highlight-col">百萬 Token 上下文</td>
                    <td>100 萬 Token 窗口</td>
                </tr>
                <tr>
                    <td>Agnes-Image-2.1-Flash</td>
                    <td class="highlight-col">4K 生圖</td>
                    <td>最高 4096×4096</td>
                </tr>
                <tr>
                    <td>Agnes 視頻模型</td>
                    <td class="highlight-col">短片創作</td>
                    <td>已有人製作出完整短片</td>
                </tr>
                <tr>
                    <td>Agnes TTS</td>
                    <td>即將上線</td>
                    <td>語音生成能力</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Agnes AI 免費三週：3.12 萬億 Token、百萬上下文 + 4K 生圖',
    'h1':          'Agnes AI 再升級<br>百萬上下文 + 4K 生圖',
    'subtitle':    '免費開放三週 Token 量達 3.12 萬億，文本模型支援百萬 Token 上下文，圖片模型支援 4K 生圖',
    'source_url':  'https://mp.weixin.qq.com/s/nq4EnNvnVNoX45r8d6rM5Q',
    'source_name': 'AI信息Gap',
    'pub_date':    '2026-06-22',
    'img_alt':     'Agnes AI 全模態API免費開放，多模態文字圖片視頻語音處理核心示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260622_204026',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
