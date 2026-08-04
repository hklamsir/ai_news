import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://unwire.hk/2026/08/02/suno-gema-copyright-ruling/ai/" target="_blank">UNWIRE</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-02</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>德國慕尼黑地方法院裁定 AI 音樂平台 Suno 未經授權訓練及重現受保護音樂作品侵犯著作權，成為歐洲首例確認「AI 音樂訓練須先獲授權」的法院裁決。法院跨境裁決，即使訓練在美國進行，只要模型伺服器設於德國且面向德國市場，德國法院即具管轄權。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🎵</div>
            <div class="tech-card-content">
                <h4>測試歌曲一覽</h4>
                <p>訴訟聚焦 6 首知名歌曲：〈Atemlos durch die Nacht〉、〈Rasputin〉、〈Big in Japan〉、〈Forever Young〉、〈Mambo No. 5〉及〈Daddy Cool〉。GEMA 在庭上展示，僅輸入簡單提示（歌詞、音樂風格、歌曲名稱），Suno 即可生成幾乎與原曲一致的旋律、和聲及節奏。法院認定 Suno 透過 stream-ripping 技術從 YouTube 繞過版權保護取得訓練素材。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚖️</div>
            <div class="tech-card-content">
                <h4>跨境裁決：訓練在美國也不行</h4>
                <p>法院裁定 2 項侵權行為：(1) Suno 在美國訓練時複製受保護作品；(2) 模型本身及在德國生成輸出時同樣構成複製及公開傳播侵權。即使訓練活動在美國進行，只要模型伺服器設於德國且面向德國市場提供服務，德國法院仍具管轄權。Suno 主張的美國「合理使用」（fair use）原則不成立。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>Suno 估值 54 億美元面臨裁決</h4>
                <p>Suno 今年 6 月完成 4 億美元（約港幣 31.2 億元）新一輪融資，由 Bond Capital 領投，估值倍升至 54 億美元（約港幣 421.2 億元）。惟裁決令 Suno 面對更龐大法律及財務壓力，公司回應指「不同意裁決」，正評估包括上訴在內各種選項。法院命令 Suno 停止侵權行為、交代侵權所得收入及承擔待計算損害賠償。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📜</div>
            <div class="tech-card-content">
                <h4>唱片公司授權新版圖</h4>
                <p>GEMA 推出 PLAI by GEMA 授權音樂資料庫，涵蓋約 178,000 個聲音檔案，橫跨逾 60 個音樂類型，為 AI 音樂公司提供合法訓練數據。Suno 早前已與 Warner Music Group 達成和解並成立合資企業，計劃 2026 年推出全新獲授權模型，惟與 Universal Music Group 及 Sony 談判仍陷僵局。競爭對手 Udio 已與 Universal 達成和解。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>此案確立重要原則：AI 訓練並非「合理使用」豁免範圍，模型提供方而非用戶須承擔侵權責任。《歐盟人工智能法》不能作為著作權侵權辯解。</p>
        </div>

        <div class="quote-box">
            <p>「法院認定 Suno 透過 stream-ripping 技術從 YouTube 繞過平台版權保護措施取得訓練素材，構成未經授權複製。」</p>
            <cite>— 德國慕尼黑地方法院裁決要點</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>此案為歐洲 AI 音樂版權確立重要先例，預料更多唱片公司將循此模式於歐洲提告 AI 音樂平台，同時合規授權方案需求將急速增長。GEMA 的 PLAI by GEMA 或成為行業授權標準，填補目前 AI 音樂訓練的合法性缺口。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2025 年 11 月</div>
                <div class="timeline-title">Suno 估值 24.5 億美元</div>
                <div class="timeline-desc">Suno 估值達 24.5 億美元（約港幣 191.1 億元）</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">Suno 完成 4 億美元融資</div>
                <div class="timeline-desc">Suno 完成 4 億美元新一輪融資，估值倍升至 54 億美元（約港幣 421.2 億元）</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月 31 日</div>
                <div class="timeline-title">GEMA 案裁決出爐</div>
                <div class="timeline-desc">慕尼黑地方法院裁定 Suno 侵權，命令停止侵權、交代侵權所得並承擔賠償</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 8 月 2 日</div>
                <div class="timeline-title">UNWIRE 報導裁決</div>
                <div class="timeline-desc">案件成為歐洲首例確認 AI 音樂訓練須先獲授權的法院裁決</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年內（預計）</div>
                <div class="timeline-title">Suno 與 Warner 合資模型推出</div>
                <div class="timeline-desc">Suno 與 Warner Music Group 合資的獲授權模型計劃推出</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>Suno</th>
                    <th>Udio（競爭對手）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>歐洲版權裁決</td>
                    <td class="highlight-col">慕尼黑法院裁定侵權</td>
                    <td>尚未被歐洲法院裁決</td>
                </tr>
                <tr>
                    <td>與大型唱片公司關係</td>
                    <td>Warner 和解，Universal/Sony 談判僵局</td>
                    <td class="highlight-col">已與 Universal 達成和解</td>
                </tr>
                <tr>
                    <td>授權策略</td>
                    <td>合資 + 訴訟雙軌</td>
                    <td class="highlight-col">全面授權路線</td>
                </tr>
                <tr>
                    <td>最新估值</td>
                    <td>54 億美元</td>
                    <td>未披露</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'Suno 遭德國法院裁定侵權　歐洲首例 AI 音樂訓練須先獲授權',
    'h1': 'Suno 遭德國法院裁定侵權\n歐洲首例 AI 音樂訓練須先獲授權',
    'subtitle': '德國慕尼黑法院裁定 Suno 未經授權訓練侵犯著作權，命令停侵權並承擔賠償，成為歐洲首例 AI 音樂版權先例',
    'source_url': 'https://unwire.hk/2026/08/02/suno-gema-copyright-ruling/ai/',
    'source_name': 'UNWIRE',
    'pub_date': '2026-08-02',
    'img_alt': 'Suno 應用程式界面展示多個音樂選項',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260804_134441',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print("❌ HTML 生成失敗：")
    for e in errors:
        print(f"   {e}")
