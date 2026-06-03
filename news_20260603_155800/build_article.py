import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.artificialintelligence-news.com/news/ai-energy-grid-mapping-china/" target="_blank">Artificial Intelligence News</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-03</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要 + 深度優化</p>
        </div>

        <div class="alert-box">
            <h4>⚠️ 研究背景</h4>
            <p>研究由北京大學和阿里巴巴達摩院研究人员在《Nature》期刊發布，使用深度學習模型分析亞米級衛星影像，識別中國太陽能和風力設施。</p>
        </div>

        <div class="quote-box">
            <p>「這項庫存讓中國能夠以『上帝視角』俯瞰其新能源版圖。」</p>
            <cite>— 劉宇教授，北京大學地球與空間科學學院</cite>
        </div>

        <h3>🎯 核心突破卡片</h3>
        <div class="tech-cards">
            <div class="tech-card">
                <div class="tech-card-icon">☀️</div>
                <h4>319,972 太陽能設施</h4>
                <p>團隊識別了中國 31.9 萬個太陽能光伏設施，覆蓋全國 1,915 個縣級行政區。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🌬️</div>
                <h4>91,609 颱風機</h4>
                <p>同步測繪了超過 9.1 萬颱風力渦輪機，處理了 7.56 TB 的衛星影像數據。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🛰️</div>
                <h4>亞米級衛星影像</h4>
                <p>深度學習模型訓練於亞米級解析度衛星影像，從屋頂光電板到蒙古高原風電場都能識別。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">⚡</div>
                <h4>光風互補效果</h4>
                <p>研究證實：設施距離越遠，互補效果越強，甘肅的陰天不會影響內蒙古的風電廊道。</p>
            </div>
        </div>

        <h3>📊 中國 vs 全球 AI 電力需求對比</h3>
        <table class="comparison-table">
            <thead>
                <tr><th>地區/指標</th><th>數據</th><th>說明</th></tr>
            </thead>
            <tbody>
                <tr><td>中國 Q1 電力消耗</td><td class="highlight-col">+44% 按年</td><td>2026年首季達 229 億千瓦時</td></tr>
                <tr><td>全球數據中心預測</td><td class="highlight-col">~1,000 TWh</td><td>IEA 預測 2030 年前達標</td></tr>
                <tr><td>美國 PJM 容量價格</td><td class="highlight-col">10 年內升 10 倍</td><td>數據中心增長為主因</td></tr>
                <tr><td>中國清潔能源產值</td><td class="highlight-col">15.4 萬億元</td><td>相當於巴西全國 GDP</td></tr>
            </tbody>
        </table>

        <h3>📅 關鍵時間軸</h3>
        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 Q1</div>
                <div class="timeline-title">中國數據中心電力消耗飆升</div>
                <div class="timeline-desc">中國數據中心耗電量按年大增 44%，達 229 億千瓦時。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年（Nature 發布）</div>
                <div class="timeline-title">北京大學+達摩院研究發布</div>
                <div class="timeline-desc">完成中國首次全國級再生能源設施 AI 測繪，識別 41 萬設施。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2030 年（預測）</div>
                <div class="timeline-title">全球數據中心用電逼近 1,000 TWh</div>
                <div class="timeline-desc">IEA 預測數據中心用電量將接近千太瓦時，各國電網承壓。</div>
            </div>
        </div>

        <h3>🔍 研究主要發現</h3>
        <ul>
            <li><strong>光風互補大幅減少發電波動</strong>：太陽能和風力的互補特性在擴大地理範圍時效果越好</li>
            <li><strong>省級協調而非全國協調</strong>：中國當前電網管理是各省分別運作，未能發揮跨省互補優勢</li>
            <li><strong>棄風限光問題</strong>：長期困擾中國清潔能源的浪費問題，可透過全國統籌改善</li>
            <li><strong>數據和代碼已公開</strong>：研究數據集和代碼透過 Zenodo 向公眾開放</li>
        </ul>

        <div class="highlight-box">
            <h4>✨ 關鍵洞察</h4>
            <p>中國透過 AI 測繪全國再生能源設施，解決了「電網操作者無法優化他們不知道的東西」的根本問題。當前各國正處於 AI 用電爆炸式增長的臨界點，這項測繪能力讓中國在整合再生能源方面領先全球。清潔能源已成為中國經濟支柱（15.4 萬億元，巴西 GDP 規模），這個「上帝視角」將進一步提升其能源安全和電網效率。</p>
        </div>

        <div class="alert-box">
            <h4>⚠️ 全球啟示</h4>
            <p>這項研究不僅是中國的成就，也為其他國家提供了模板。通過大範圍地理 AI 測繪基礎設施，各國可以更有效地協調再生能源，穩定電網並減少棄風棄光。中國的清潔能源經濟產值已相當於巴西全國 GDP，這種規模的管理需要同樣規模的技術工具。</p>
        </div>
"""

metadata = {
    'title': "China's AI just mapped its entire renewable energy grid | Artificial Intelligence News",
    'h1': '中國 AI 測繪<br>全國再生能源電網',
    'subtitle': 'Nature 研究：北京大學+達摩院識別 41 萬設施，各國應該關注',
    'source_url': 'https://www.artificialintelligence-news.com/news/ai-energy-grid-mapping-china/',
    'source_name': 'Artificial Intelligence News',
    'pub_date': '2026-06-03',
    'img_alt': '中國 AI 測繪再生能源電網概念圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260603_155800',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")
