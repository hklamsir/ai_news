import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://unwire.hk/2026/07/10/higher-education-ai-challenges/learning/" target="_blank">UNWIRE.HK</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-10</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>當答案不再稀缺，高等教育還應教甚麼？悉尼大學教育科技學教授 Danny Liu 指出，AI 世代全球大學最急切需要作出的改變，是不再將「學術研究產出」視為大學排名的核心基準。教學質素、學生能力發展、課程創新，同樣需要納入真正有分量的評核機制。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🎓</div>
            <div class="tech-card-content">
                <h4>被扭曲的教育價值觀</h4>
                <p>「著名大學的畢業生，就是最頂尖的人才」——這種將教育簡化為單一、單向攀升路徑的觀念，導致以分數為中心的高壓競賽，從學童的精神健康危機、青少年集體迷失，到家庭關係緊繃，引發嚴重的結構性下行連鎖效應。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔬</div>
            <div class="tech-card-content">
                <h4>被 research metrics 绑架的體制</h4>
                <p>全球高等教育最不合時宜的慣性，就是高度重視教授的研究產出。當制度主要獎勵研究表現，教師自然優先投入研究。即使認同 AI 教育改革重要，也未必有足夠時間、誘因和支援重新設計課程。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>AI 時代大學的真正命題</h4>
                <p>當答案不再稀缺，大學需要回答根本問題：AI 夥伴會成為學生的益友還是損友？會令人類被完美取代，還是能成就人工智能加持的卓越人才？關鍵在於教育如何啟發學生的問題意識、應變能力、抗逆力、邏輯及批判性思考，以至最核心的創造力。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🇭🇰</div>
            <div class="tech-card-content">
                <h4>香港大學的回應</h4>
                <p>面對 AI 浪潮，香港多間大學已迅速行動：將 AI 應用於教學法，使學習更個人化及以學生為主導；部分大學更為中小學校長開辦培訓課程，共同探討在 AI 時代「教甚麼」與「如何教」。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>三年內，將不會再有人談論「要當心 AI 幻覺」或「如何正確運用 AI」，AI 將成為學生學習與成長中最貼身的夥伴。高等教育及業界必須合力建立新視點，重新定義「好大學」和「好教授」的評核標準。</p>
        </div>

        <div class="quote-box">
            <p>AI 世代全球大學最急切需要作出的改變，是不再將「學術研究產出」視為大學排名的核心基準。</p>
            <cite>— Danny Liu，悉尼大學教育科技學教授</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>AI 的威力逼使社會觀念不得不迅速改變——整條人才供應鏈必須重新構建，「人才」的定義必須重寫，培育人才的過程也必須重新審視。</p>
        <p>未來，AI 將成為學生最貼身的學習夥伴。大學需要回答的不只是「教甚麼」，更是如何啟發學生的光問題意識、創造力與批判性思考，證明高等教育仍有不可取代的價值。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">工業革命前</div>
                <div class="timeline-title">學徒制教育</div>
                <div class="timeline-desc">師徒傳授實務技能為主</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">19 世紀</div>
                <div class="timeline-title">現代大學制度興起</div>
                <div class="timeline-desc">以研究與學術產出為核心評核標準</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">AI 進入教育討論</div>
                <div class="timeline-desc">教育局公布《中小學數字教育發展藍圖》</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月</div>
                <div class="timeline-title">學與教博覽 2026</div>
                <div class="timeline-desc">Danny Liu 呼籲重新定義大學評核標準</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">三年內（預測）</div>
                <div class="timeline-title">AI 成為學習標配</div>
                <div class="timeline-desc">不再有人談論 AI 應用，AI 將成為學生最貼身的夥伴</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>傳統高等教育</th>
                    <th>AI 時代高等教育</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>核心價值</td>
                    <td>學術研究產出</td>
                    <td class="highlight-col">教學質素 + 學生能力發展</td>
                </tr>
                <tr>
                    <td>評核重點</td>
                    <td>公開試分數、論文數量</td>
                    <td class="highlight-col">批判思考、創造力、應變能力</td>
                </tr>
                <tr>
                    <td>知識獲取</td>
                    <td>教師傳授為主</td>
                    <td class="highlight-col">AI 輔助個人化學習</td>
                </tr>
                <tr>
                    <td>大學功能</td>
                    <td>知識儲存與傳遞</td>
                    <td class="highlight-col">啟發思考、培育品格</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '傳統大學若放於 AI 時代，錯在哪裡？',
    'h1': '傳統大學若放於 AI 時代<br>錯在哪裡？',
    'subtitle': '當答案不再稀缺，高等教育必須重新回答最根本的問題',
    'source_url': 'https://unwire.hk/2026/07/10/higher-education-ai-challenges/learning/',
    'source_name': 'UNWIRE.HK',
    'pub_date': '2026-07-10',
    'img_alt': '大學生在公園中學習，全息投影 AI 助手輔助學習場景',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260710_172000',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print("錯誤：")
    for e in errors:
        print(f"  - {e}")
