import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.ctee.com.tw/news/20260816700307-430804" target="_blank">CTEE 工商時報</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-14 至 2026-08-16</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>阿里巴巴旗下 AI 模型「千問」（Qwen）過去半年全球累計下載量突破 30 億次，超越 Meta（2.27 億次）及 Google（4.18 億次），成為全球最受歡迎的开源 AI 模型之一。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📈</div>
            <div class="tech-card-content">
                <h4>Qwen 下載量碾壓美國巨頭</h4>
                <p>根據 Hugging Face 8 月 14 日報告：Qwen 前 7 個月累計下載約 <strong>20.61 億次</strong>，大幅領先 Google（約 4.18 億次）及 Meta（約 2.27 億次）。阿里巴巴已開放超過 <strong>460 款模型</strong>，衍生模型突破 <strong>30 萬個</strong>。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>開源生態席捲全球</h4>
                <p>Qwen 在 Hugging Face 上已有逾 <strong>15.1 萬個衍生模型</strong>，規模約為 Meta 整體的 <strong>2.6 倍</strong>。除阿里巴巴外，月之暗面（Moonshot AI）、DeepSeek 等中國 AI 業者也透過低成本、開放權重策略擴大使用族群。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔧</div>
            <div class="tech-card-content">
                <h4>Qwen3.8 系列正式開源</h4>
                <p>阿里巴巴於 2026 年 8 月 14 日開源 Qwen3.8 系列，其中 Qwen3.8-27B 為原生多模態稠密模型，僅 270 億參數，整體水平超越 Qwen3.7-Plus，在編程及辦公場景中表現出色。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌏</div>
            <div class="tech-card-content">
                <h4>全球布局：東南亞、非洲企業客戶</h4>
                <p>阿里巴巴透過雲端服務將 Qwen 推向東南亞、非洲等地企業客戶，同時《時代》雜誌將阿里巴巴列為「2026 年最具影響力十大人工智能公司」之一，與字節跳動、智譜 AI 並列三家上榜中國企業。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Qwen 的爆發顯示中國 AI 業者在开源生態的布局已見成效。開放權重允許開發者下載、修改並依需求開發，使下載量與衍生模型數量形成正向循環。</p>
        </div>

        <div class="quote-box">
            <p>「Qwen 已在 Hugging Face 成為開放模型生態系統最大的基礎之一。」</p>
            <cite>— Hugging Face 報告，2026 年 8 月 14 日</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>隨著越來越多開發者以 Qwen 為基礎打造新產品，阿里巴巴有望在企業 AI 服務市場進一步挑戰美國科技巨頭。開源生態的規模效應正在重塑全球 AI 競爭格局。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2023 年</div>
                <div class="timeline-title">Qwen 全面開源</div>
                <div class="timeline-desc">阿里巴巴宣布 Qwen 系列全面開源，開啟开源 AI 之路</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年初</div>
                <div class="timeline-title">Qwen 下載量破 10 億</div>
                <div class="timeline-desc">《時代》雜誌報道 Qwen 系列累計下載突破 10 億次</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 2 月</div>
                <div class="timeline-title">春節 AI 大戰</div>
                <div class="timeline-desc">Qwen 春節期間用戶發出 50 億次「千問幫我」指令，1.3 億人首次體驗 AI 購物</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 8 月 14 日</div>
                <div class="timeline-title">Qwen3.8 開源</div>
                <div class="timeline-desc">正式開源 Qwen3.8 系列，Qwen-27B 多模態模型發布</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 8 月 15 日</div>
                <div class="timeline-title">半年下載破 30 億</div>
                <div class="timeline-desc">阿里巴巴宣布 Qwen 系列半年累計下載突破 30 億次，超越 Meta 和 Google</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>公司</th>
                    <th>Hugging Face 下載量（2026 年前 7 月）</th>
                    <th>衍生模型數量</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>阿里巴巴（Qwen）</strong></td>
                    <td class="highlight-col">約 20.61 億次</td>
                    <td class="highlight-col">逾 15.1 萬個</td>
                </tr>
                <tr>
                    <td>Google</td>
                    <td>約 4.18 億次</td>
                    <td>—</td>
                </tr>
                <tr>
                    <td>Meta</td>
                    <td>約 2.27 億次</td>
                    <td>約 5.8 萬個（參考值）</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '中國AI又突圍！阿里千問半年下載破30億 超車Meta、Alphabet成全球第一',
    'h1':          '中國AI又突圍！<br>阿里千問半年下載破30億',
    'subtitle':    'Qwen 系列 Hugging Face 下載量碾壓 Google 與 Meta，衍生模型突破 30 萬個',
    'source_url':  'https://www.ctee.com.tw/news/20260816700307-430804',
    'source_name': 'CTEE 工商時報',
    'pub_date':    '2026-08-16',
    'img_alt':     '阿里巴巴千問 Qwen AI 模型下載量突破 30 億次',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260816_213029',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print("Errors:", errors)
