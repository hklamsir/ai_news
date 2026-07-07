import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.hk01.com/深度報道/60336466/" target="_blank">HK01</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-07</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>科大副校郭毅可主張香港應建立「主權AI」，以本地數據為基礎，避免數字殖民與文化偏見，並將香港打造成為世界第一個以 AI 支撐的城市。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>什麼是「主權AI」？</h4>
                <p>「主權AI」是指對 AI 基礎設施（資料、算力、模型、治理規則）擁有完整的控制權與自主決策能力。最早由 NVIDIA 總裁黃仁勛於 2023 年提出，將 AI 定位為「數字主權」的演進和延伸。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💡</div>
            <div class="tech-card-content">
                <h4>為何香港需要「主權AI」？</h4>
                <p>外國 AI（如 ChatGPT、Gemini）無法準確回答香港本地問題（如巴士路線、法律條文）；過度依賴外部技術存在「斷供」風險；本地數據可規避數字殖民與文化偏見。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>安全與主權考量</h4>
                <p>當 AI 深度融入城市運作，技術主導權等同社會安全。在地緣政治局勢波動下，過度依賴外部技術存在被隨時「斷供」的風險。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🧠</div>
            <div class="tech-card-content">
                <h4>香港的「主權AI」實踐：HKGAI</h4>
                <p>科大主導的香港生成式人工智能研發中心（HKGAI）推出「港話通」聊天機械人，支援廣東話、普通話及英文，使用本地數據及價值觀，截至今年 6 月已有近 75 萬名註冊用戶。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>「一國兩制」是香港發展「主權AI」的最大優勢——能直接享受國家領先的人才與技術資源，同時擁有普通法法治體系和中西合璧的文化環境，可成為國家建設「主權AI」的「試驗場」。</p>
        </div>

        <div class="quote-box">
            <p>「AI 應該拉近社會貧富差距、能力差距的槓桿，而不是擴大差距的高牆。」</p>
            <cite>— 郭毅可，科大副校長兼 HKGAI 主任</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>新加坡投入超過 61 億港元發展 AI，香港的 AI 發展正從「實驗室研發階段」邁向「實體產業賦能階段」。郭毅可相信，只要妥善利用技術並與監管配合，定能克服傳統治理瓶頸，讓城市運轉更為科學與高效。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2023 年</div>
                <div class="timeline-title">「主權AI」概念提出</div>
                <div class="timeline-desc">NVIDIA 總裁黃仁勛提出「主權AI」概念</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2019 年</div>
                <div class="timeline-title">新加坡發布國家人工智慧戰略</div>
                <div class="timeline-desc">新加坡政府發布首份《國家人工智慧戰略》</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2023 年</div>
                <div class="timeline-title">新加坡 SEA-LION 模型</div>
                <div class="timeline-desc">新加坡國家人工智慧中心開發以東南亞 11 種語言為基礎的大語言模型</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">新加坡大力投資 AI</div>
                <div class="timeline-desc">新加坡宣佈未來 5 年投入超過 10 億新加坡元發展 AI</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">「港話通」近 75 萬用戶</div>
                <div class="timeline-desc">HKGAI 推出的「港話通」已有近 75 萬名註冊用戶</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>比較項目</th>
                    <th>香港</th>
                    <th>新加坡</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>AI 戰略</td>
                    <td class="highlight-col">HKGAI 主導，建立「主權AI」</td>
                    <td>《國家人工智慧戰略》</td>
                </tr>
                <tr>
                    <td>本地模型</td>
                    <td class="highlight-col">港話通、港文通、港法通、港金通</td>
                    <td>SEA-LION（東南亞 11 種語言）</td>
                </tr>
                <tr>
                    <td>投資規模</td>
                    <td>AI+ 與產業發展策略委員會</td>
                    <td class="highlight-col">5 年逾 10 億新加坡元（約 61.3 億港元）</td>
                </tr>
                <tr>
                    <td>獨特優勢</td>
                    <td class="highlight-col">一國兩制 + 普通法 + 中西文化</td>
                    <td>政府強勢補貼 + 全民總動員</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '與AI共存．四｜專訪科大副校郭毅可——建立「主權AI」拒絕數字殖民 | HK01',
    'h1': '專訪科大副校郭毅可<br>建立「主權AI」拒絕數字殖民',
    'subtitle': '香港需要建立「主權AI」，以本地數據為基礎，避免數字殖民',
    'source_url': 'https://www.hk01.com/深度報道/60336466/',
    'source_name': 'HK01',
    'pub_date': '2026-07-07',
    'img_alt': '香港科技大學與 AI 城市願景',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260707_130800',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
