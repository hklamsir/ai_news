import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://inews.hket.com/article/4155612/" target="_blank">香港經濟日報 iNews</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-03</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>成立僅3年的月之暗面以長文本與生產力定位突圍，Kimi大模型被馬斯克公開點名「令人印象深刻」，成為國產模型出海的新力量。公司不走聊天陪伴路綫，押注架構創新與長上下文能力，API收入已佔整體營收7成以上。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🏢</div>
            <div class="tech-card-content">
                <h4>差異化市場定位</h4>
                <p>月之暗面不走娛樂路綫，專注生產力應用。DeepSeek 主打工程師場景，百川智能強調通用性，Kimi 則深耕長上下文與企業工作流程，形成獨特競爭優勢。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📝</div>
            <div class="tech-card-content">
                <h4>長文本領域領先</h4>
                <p>Kimi 是早期突破百萬字上下文的中國模型之一，在 RULER、NeedleBench 等第三方測試中獲得不俗成績，深度調研與長任務流程能力成為企業採用關鍵。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌟</div>
            <div class="tech-card-content">
                <h4>馬斯克公開點名</h4>
                <p>月之暗面團隊提出的「主動殘差技術」提升了四分之一運算效率，馬斯克公開表示「令人印象深刻」，讓中國模型在海外市場獲得曝光。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>B端商業模式清晰</h4>
                <p>公司不走娛樂路綫，專注生產力應用。API 收入目前已佔 Kimi 整體營收 7 成以上，透過 API 服務推動業務增長。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Kimi 的核心策略：不追求最低價格，而是朝更高性能方向發展，同時透過 AWS 全球基建解決出海時的跨區速度、合規與服務穩定性問題。</p>
        </div>

        <div class="quote-box">
            <p>「相比娛樂或情緒價值場景，生產力應用可帶來更高商業回報，亦能讓模型能力真正服務企業工作流程，形成更可持續的商業閉環。」</p>
            <cite>— 黃震昕，月之暗面 B端負責人</cite>
        </div>

        <h3>🔧 技術策略：Scaling Law 的瓶頸與突破</h3>
        <p>月之暗面仍相信 Scaling Law（擴展定律），但坦言最大瓶頸是算力與成本。公司選擇主動向最難的問題挑戰，例如透過綫性注意力（Linear Attention）等技術，降低模型擴展成本，讓擴展定律持續往前走。</p>

        <h3>📋 下一代模型三大方向</h3>
        <ol>
            <li>以更少資料或算力達到相近效果，降低推理成本</li>
            <li>讓模型可記住更長任務流程，支援更長時間工作</li>
            <li>允許多個 Agent 協作處理複雜任務，提升企業級工作流程可落地性</li>
        </ol>

        <h3>🌍 借AWS全球基建出海</h3>
        <p>Kimi 已上架 AWS Marketplace，期望透過 AWS 的全球雲端基建、算力資源及合規能力，解決跨區訪問速度、服務穩定性等問題，拓展更大的國際市場。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2023 年</div>
                <div class="timeline-title">月之暗面成立</div>
                <div class="timeline-desc">公司成立，專注打造 Kimi 大模型，主打長文本處理與生產力應用。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">早期</div>
                <div class="timeline-title">突破百萬字上下文</div>
                <div class="timeline-desc">Kimi 是早期突破百萬字上下文的中國模型之一，建立技術壁壘。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026</div>
                <div class="timeline-title">馬斯克點名稱讚</div>
                <div class="timeline-desc">馬斯克公開表示月之暗面的「主動殘差技術」令他印象深刻，提升國際知名度。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026</div>
                <div class="timeline-title">AWS 峰會亮相</div>
                <div class="timeline-desc">月之暗面 B端負責人黃震昕出席 AWS 中國峰會，分享 Kimi 企業應用策略。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026</div>
                <div class="timeline-title">上架 AWS Marketplace</div>
                <div class="timeline-desc">Kimi 正式上架 AWS Marketplace，透過 AWS 全球基建拓展國際企業客戶。</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>模型</th>
                    <th>主要定位</th>
                    <th>核心優勢</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Kimi（月之暗面）</td>
                    <td>長上下文、企業工作流程</td>
                    <td class="highlight-col">百萬字上下文、深度調研、PPT/Excel 分析</td>
                </tr>
                <tr>
                    <td>DeepSeek</td>
                    <td>推理效率、工程師場景</td>
                    <td>成本優勢、推理效率高</td>
                </tr>
                <tr>
                    <td>百川智能</td>
                    <td>通用性、多模態</td>
                    <td>開放生態、多模態能力</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'AI狂潮｜月之暗面拆解Kimi模型突圍攻略　押注架構創新衝破大模型瓶頸',
    'h1':          '月之暗面拆解<br>Kimi模型突圍攻略',
    'subtitle':    '押注架構創新　馬斯克點名稱讚　API收入佔7成',
    'source_url':  'https://inews.hket.com/article/4155612/',
    'source_name': '香港經濟日報 iNews',
    'pub_date':    '2026-07-03',
    'img_alt':     '月之暗面 Kimi 模型突圍攻略',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260703_130047',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print(f"❌ HTML 生成失敗：{errors}")
