import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://youtu.be/KaPpYLgZpxM" target="_blank">YouTube（科技頻道）</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-11</p>
            <p><strong>🤖 處理方式</strong>：根據影片逐字稿整理</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>一位科技 YouTuber 針對 AMD W7900/W7800 與 NVIDIA 5080/5070Ti Super 是否值得等待進行分析。觀點鮮明：AMD W7900 48G 純屬智商稅，5080/5070Ti Super 對純 AI 用戶意義不大，建議直接入手 RTX Pro 4000 24G 或使用在線 AI 服務。</p>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>AMD W7900 48G：智商稅，強烈不推薦</h4>
                <p>京東標價 <strong>2.9 萬</strong>，比 4090 48G 還貴。本質上就是 7900 XTX 的 48G 顯存版本，架構規格完全一致。實際 AI 運算速度比 4090 <strong>慢約 3 倍</strong>。唯一優點是帶專業認證，適合設計院等需要認證卡的場景。建議：等 1 年後買二手，1 萬出頭性價比更高。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔄</div>
            <div class="tech-card-content">
                <h4>AMD W7800 32G：架構過時</h4>
                <p>性能不如 7900 XTX，略強於 7900 GRE，屬 RDNA 3 架構。1.3 萬價位不如加錢買 RDNA 4 架構的 AI Pro R9700，後者在各方面都更強。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌅</div>
            <div class="tech-card-content">
                <h4>曙光：專業卡正在加速淘汰</h4>
                <p>未來將有大量 RTX 30 系列專業卡 + AMD RDNA 3 卡涌入市場。對本地部署 <strong>30B 級別大模型</strong>，這些卡堪稱神器。但對有 48G 顯存的用戶，FP8/FP4 加速聊勝於無。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎮</div>
            <div class="tech-card-content">
                <h4>5080 / 5070Ti Super：遊戲用值得等，純 AI 不建議</h4>
                <p>算力與 7900 XTX 差不多或略差，但得益於 N 卡生態實際表現更好。純為跑 AI：不如現在直接買 RTX Pro 4000 24G。Blackwell 架構的 FP4/FP8 加速對 24G 顯存用戶收益極低。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>對普通 AI 用戶：AMD W7900/W7800 完全不推薦，5080/5070Ti Super 等待價值有限。建議直接入手 <strong>RTX Pro 4000 24G</strong> 或使用 <strong>DeepSeek V4 在線服務</strong>（每月約 50-60 元）。</p>
        </div>

        <div class="quote-box">
            <p>「沒有本地部署 7B 的底氣，我是不敢全面擁抱 AI Agent 的。」</p>
            <cite>— 科技 YouTuber</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>專業計算卡正在加速淘汰，未來性價比更高的二手專業卡將大量流入個人市場。對普通用戶而言，24G 顯存已達 AI 甜點水位，在線 AI 服務成本極低，本地部署更多是「保險」而非剛需。技術只是工具，商業對接能力才是核心競爭力。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">當前</div>
                <div class="timeline-title">AMD W7900/W7800 上市</div>
                <div class="timeline-desc">AMD 推出專業卡，標價過高被質疑為智商稅</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">預期</div>
                <div class="timeline-title">5080/5070Ti Super 發布</div>
                <div class="timeline-desc">預計 8000-9000 元，遊戲用戶值得等待</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">1 年後</div>
                <div class="timeline-title">專業卡二手價格崩跌</div>
                <div class="timeline-desc">預計 1 萬出頭可買到二手 W7900 等專業卡</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">同時</div>
                <div class="timeline-title">大公司專業卡淘汰潮</div>
                <div class="timeline-desc">FP8/FP4 缺失導致專業卡性價比下降，大量流入市場</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">持續</div>
                <div class="timeline-title">在線 AI 服務普及</div>
                <div class="timeline-desc">DeepSeek V4 等在線服務成本低至每月 50-60 元</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>顯示卡</th>
                    <th>顯存</th>
                    <th>價格（人民幣）</th>
                    <th>AI 推薦度</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>RTX Pro 4000</td>
                    <td class="highlight-col">24G</td>
                    <td>待定</td>
                    <td>⭐⭐⭐⭐⭐ 現階段首選</td>
                </tr>
                <tr>
                    <td>5070Ti Super</td>
                    <td>24G</td>
                    <td>8000-9000</td>
                    <td>⭐⭐⭐⭐ 遊戲+AI 兼顧</td>
                </tr>
                <tr>
                    <td>AMD W7900</td>
                    <td class="highlight-col">48G</td>
                    <td>2.9 萬（不推薦）</td>
                    <td>⭐ 不推薦，性價比極差</td>
                </tr>
                <tr>
                    <td>AMD W7800</td>
                    <td>32G</td>
                    <td>1.3 萬（不推薦）</td>
                    <td>⭐ 架構過時</td>
                </tr>
                <tr>
                    <td>DeepSeek V4 在線</td>
                    <td>雲端</td>
                    <td class="highlight-col">50-60/月</td>
                    <td>⭐⭐⭐⭐⭐ 成本最低</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '5080 / 5070Ti Super vs AMD W7900 / W7800：24G 顯卡 AI 時代還值得折騰嗎？',
    'h1': '5080 / 5070Ti Super vs AMD W7900 / W7800：<br>24G 顯卡 AI 時代還值得折騰嗎？',
    'subtitle': '科技 YouTuber 現聲：專業卡性價比差、5080 遊戲為主、在線 AI 更划算',
    'source_url': 'https://youtu.be/KaPpYLgZpxM',
    'source_name': 'YouTube',
    'pub_date': '2026-07-11',
    'img_alt': 'NVIDIA 5080 / AMD W7900 顯示卡選購分析',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260711_151500',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
