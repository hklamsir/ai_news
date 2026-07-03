import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://unwire.hk/2026/07/03/unicef-children-ai-usage-speed/tech-secure/" target="_blank">UNWIRE</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-03</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>UNICEF 最新調查顯示，全球約 2,000 萬名兒童已使用 AI 工具，兒童接觸 AI 速度比成人快三倍。UNICEF 形容這代兒童正身處「一場全球實驗」當中，警告現行法規遠遠追不上 AI 使用速度，呼籲各國政府及科企正視。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>調查涵蓋十國、逾千名受訪者</h4>
                <p>「Disrupting Harm Phase 2」研究由 UNICEF 聯同 ECPAT International 及國際刑警組織合作進行，數據來自亞美尼亞、巴西、哥倫比亞等 10 個國家，每國訪問約 1,000 名 12-17 歲兒童及家長。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📝</div>
            <div class="tech-card-content">
                <h4>逾 200 萬兒童向 AI 求助　1,300 萬人靠 AI 做功課</h4>
                <p>約十分之一受訪兒童表示會向 AI 尋求關於困擾自己事情的意見，估計有 1,300 萬名兒童使用 AI 協助學習及做功課。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>兒童早已察覺風險</h4>
                <p>三分之一兒童擔心 AI 被用作詐騙或散播失實資訊，四分之一兒童擔心相片或影片被 AI 篡改成深偽（deepfake）內容。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚖️</div>
            <div class="tech-card-content">
                <h4>佛羅里達州控告 OpenAI</h4>
                <p>佛州入稟法院控告 OpenAI 及 Sam Altman，指控缺乏有效家長監控及年齡驗證機制保護未成年用戶，恐須承擔高達數十億美元（約港幣 78 億元）賠償。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>UNICEF 形容這一代兒童正身處「一場全球實驗」（a global experiment）當中，強調 AI 對認知發展、情緒依賴及潛在傷害的影響數據仍在浮現階段，實際上是一整代人在全球實驗中成長。</p>
        </div>

        <div class="quote-box">
            <p>「兒童較容易受到 AI 系統影響，包括其設計方式、背後的商業模式及個人資料被使用的情況。然而兒童本身卻缺乏能力去迴避或質疑這些系統，而且現時大部分 AI 治理都未有將兒童視為特定群體處理。」</p>
            <cite>— UNICEF 報告</cite>
        </div>

        <h3>💼 UNICEF 提出五大建議</h3>
        <ol>
            <li>加強研究 AI 對兒童發展的影響</li>
            <li>收緊針對 AI 性剝削的法例</li>
            <li>在 AI 系統設計階段內置安全及透明度機制</li>
            <li>擴展兒童及家長的 AI 素養教育</li>
            <li>投資改善網絡連接，避免數碼鴻溝擴大</li>
        </ol>

        <h3>🔮 業界展望</h3>
        <p>隨著愈來愈多兒童及青少年將 AI 工具融入日常學習與生活，各地政府及科企未來勢必加快制訂針對未成年用戶的規管框架。馬耳他等國家已率先推出全國性 AI 素養課程，在兒童接觸 AI 之前先做好教育配套。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026</div>
                <div class="timeline-title">UNICEF 發布調查報告</div>
                <div class="timeline-desc">調查涵蓋 10 個國家，指出全球約 2,000 萬名兒童已使用 AI 工具。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026</div>
                <div class="timeline-title">首屆全球 AI 治理對話</div>
                <div class="timeline-desc">報告在「全球 AI 治理對話」前夕發布，呼籲各國正視兒童使用 AI 的監管缺口。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026</div>
                <div class="timeline-title">佛州控告 OpenAI</div>
                <div class="timeline-desc">佛羅里達州入稟法院，指控 OpenAI 缺乏保護未成年用戶機制，恐須巨額賠償。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026</div>
                <div class="timeline-title">美國國會審議兒童網絡安全法案</div>
                <div class="timeline-desc">多項兒童網絡安全相關法案正在審議，科企監管壓力加劇。</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026</div>
                <div class="timeline-title">馬耳他推出 AI 素養課程</div>
                <div class="timeline-desc">馬耳他率先推出全國性 AI 素養課程，在兒童接觸 AI 前先做好教育配套。</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>調查數據</th>
                    <th>數字</th>
                    <th class="highlight-col">佔受訪者比例</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>全球使用 AI 的兒童</td>
                    <td>約 2,000 萬</td>
                    <td class="highlight-col">—</td>
                </tr>
                <tr>
                    <td>向 AI 求助解憂</td>
                    <td>逾 200 萬</td>
                    <td class="highlight-col">約 10%</td>
                </tr>
                <tr>
                    <td>用 AI 做功課</td>
                    <td>約 1,300 萬</td>
                    <td class="highlight-col">—</td>
                </tr>
                <tr>
                    <td>擔心 AI 詐騙/失實資訊</td>
                    <td>—</td>
                    <td class="highlight-col">33%</td>
                </tr>
                <tr>
                    <td>擔心深偽內容</td>
                    <td>—</td>
                    <td class="highlight-col">25%</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'UNICEF 調查：全球 2,000 萬兒童已用 AI　學習速度比成人快 3 倍',
    'h1':          'UNICEF 調查：全球<br>2,000 萬兒童已用 AI',
    'subtitle':    '學習速度比成人快三倍　 UNICEF 警告：兒童身處全球實驗',
    'source_url':  'https://unwire.hk/2026/07/03/unicef-children-ai-usage-speed/tech-secure/',
    'source_name': 'UNWIRE',
    'pub_date':    '2026-07-03',
    'img_alt':     'UNICEF 調查：全球 2,000 萬兒童已用 AI',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260703_131313',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print(f"❌ HTML 生成失敗：{errors}")
