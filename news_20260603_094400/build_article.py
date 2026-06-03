import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.stheadline.com/realtime-world/3578920/AI%E6%90%B6%E9%A3%AF%E7%A2%97%E7%B4%90%E7%B4%84%E8%81%AF%E5%84%B2%E9%8A%80%E8%A1%8C%E9%81%A0%E7%A8%8B%E5%B7%A5%E4%BD%9C%E6%89%8D%E6%98%AF%E5%A4%A7%E5%AD%B8%E7%94%9F%E5%A4%B1%E6%A5%AD%E9%97%9C%E9%8D%B5" target="_blank">星島頭條</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-03</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要 + 深度優化</p>
        </div>

        <div class="alert-box">
            <h4>⚠️ 研究背景</h4>
            <p>這項研究由紐約聯邦儲備銀行經濟學家伊曼紐爾（Natalia Emanuel）領導發布，研究比較了2017-2019年與2022-2024年的就業數據。</p>
        </div>

        <div class="quote-box">
            <p>「企業不願僱用應屆大學畢業生從事遠程工作，因為如果他們不回辦公室，令培訓和指導變得更困難。」</p>
            <cite>— 紐約聯邦儲備銀行研究報告</cite>
        </div>

        <h3>🎯 核心突破卡片</h3>
        <div class="tech-cards">
            <div class="tech-card">
                <div class="tech-card-icon">📊</div>
                <h4>失業率升 1%</h4>
                <p>從事「可遠程」工作的年輕大學畢業生失業率上升約 1 個百分點，年長員工反而下降。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🔬</div>
                <h4>三分之二貢獻</h4>
                <p>研究計算得出：遠程工作對年輕大學畢業生失業率上升的「貢獻」接近三分之二。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">🤖</div>
                <h4>AI 影響甚微</h4>
                <p>研究不同職業對 AI 的暴露程度，發現 AI 對年輕人失業的影響甚微，遠程工作才是元兇。</p>
            </div>
            <div class="tech-card">
                <div class="tech-card-icon">👔</div>
                <h4>偏愛資深員工</h4>
                <p>企業偏愛需要較少指導就能工作的經驗員工，對於包含遠程工作的團隊，這種偏好更明顯。</p>
            </div>
        </div>

        <h3>📊 數據對比：年輕 vs 年長員工</h3>
        <table class="comparison-table">
            <thead>
                <tr><th>群體</th><th>可遠程工作失業率變化</th><th>需到場工作失業率變化</th><th>AI 影響程度</th></tr>
            </thead>
            <tbody>
                <tr><td>29歲以下年輕大學畢業生</td><td class="highlight-col">+1%</td><td>變化不大</td><td>甚微</td></tr>
                <tr><td>29歲及以上年長員工</td><td>-些微下降</td><td>變化不大</td><td>甚微</td></tr>
                <tr><td>無大學學位人群</td><td>存在類似模式</td><td>差距很小</td><td>甚微</td></tr>
            </tbody>
        </table>

        <h3>📅 關鍵時間軸</h3>
        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2017-2019 年</div>
                <div class="timeline-title">疫情前基準</div>
                <div class="timeline-desc">研究比較的基準期，年輕大學畢業生就業狀況正常。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2020 年</div>
                <div class="timeline-title">新冠疫情爆發</div>
                <div class="timeline-desc">疫情後遠程工作模式廣泛流行，成為常態。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2022-2024 年</div>
                <div class="timeline-title">疫情後數據</div>
                <div class="timeline-desc">研究比較的時期，可遠程工作年輕人失業率明顯上升。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2022-2025 年</div>
                <div class="timeline-title">失業率達 3.7%</div>
                <div class="timeline-desc">29歲以下大學畢業生失業率從疫情前平均水平上升了 20%。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">失業率達 5.8%</div>
                <div class="timeline-desc">22至27歲大學畢業生失業率達到自2012年以來最高水平。</div>
            </div>
        </div>

        <h3>🌟 企業案例印證</h3>
        <p>研究引用了一間財富 500 強科技公司的數據：</p>
        <ul>
            <li><strong>辦公室關閉時</strong>（遠程工作）：公司僱用了更少經驗不足的年輕工人，更多經驗豐富的工人。</li>
            <li><strong>辦公室重新開放後</strong>：公司又轉回僱用更多年輕工人。</li>
            <li><strong>含遠程工作的團隊</strong>：即使已恢復辦公，公司仍然偏愛經驗更豐富的員工。</li>
        </ul>

        <div class="highlight-box">
            <h4>✨ 關鍵洞察</h4>
            <p>這項研究顛覆了大眾對「AI 搶飯碗」的擔憂。數據顯示，年輕大學畢業生就業狀況惡化早於 ChatGPT 出現，真正的元兇是疫情後流行的遠程工作模式——企業難以對遠程員工進行培訓指導，因此更傾向聘請有經驗、較少指導需求的資深員工。</p>
        </div>

        <div class="alert-box">
            <h4>⚠️ 對畢業生的建議</h4>
            <p>研究顯示，親身到場工作可能更有利於應屆畢業生獲得培訓機會。若想在疫情後的求職市場脫穎而出，或許需要優先考慮需要到場的崗位，而非遠程工作機會。</p>
        </div>
"""

metadata = {
    'title': 'AI搶飯碗？｜紐約聯儲銀行：遠程工作才是大學生失業關鍵',
    'h1': 'AI 搶飯碗？<br>聯儲銀行：遠程工作才是元兇',
    'subtitle': '研究指應屆畢業生失業率上升三元兇是遠程工作，AI 影響甚微',
    'source_url': 'https://www.stheadline.com/realtime-world/3578920/AI%E6%90%B6%E9%A3%AF%E7%A2%97%E7%B4%90%E7%B4%84%E8%81%AF%E5%84%B2%E9%8A%80%E8%A1%8C%E9%81%A0%E7%A8%8B%E5%B7%A5%E4%BD%9C%E6%89%8D%E6%98%AF%E5%A4%A7%E5%AD%B8%E7%94%9F%E5%A4%B1%E6%A5%AD%E9%97%9C%E9%8D%B5',
    'source_name': '星島頭條',
    'pub_date': '2026-06-03',
    'img_alt': '遠程工作 vs 辦公室工作對比圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260603_094400',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")
