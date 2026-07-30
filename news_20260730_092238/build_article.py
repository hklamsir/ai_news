#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.scmp.com/week-asia/economics/article/3362166/ai-competition-heats-us-targets-southeast-asias-public-sector" target="_blank">SCMP</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-30</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>美國政府在東南亞推出「AI Spark」計劃，承諾提供財政及技術援助，支援東南亞各國部署美國 AI 系統用於公共服務，被視為抗衡中國 AI 模型在東南亞日益增長影響力的戰略之舉。這標誌着美中 AI 競賽正式延伸至東南亞公共部門。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🇺🇸</div>
            <div class="tech-card-content">
                <h4>AI Spark：美國的東南亞 AI 佈局</h4>
                <p>美國東盟大使 Kevin Kim 於 7 月 22 日宣布推出「美國—東盟 AI Spark」倡議（U.S.-ASEAN AI SPARK），隸屬特朗普政府「Pax Silica」計劃。該倡議將向有意採用美國 AI 系統的東南亞各國政府提供財政及技術援助，支援公共部門的 AI 應用。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>25 億美元一籃子援助計劃</h4>
                <p>美國同時宣佈向東南亞提供 25 億美元（約 196 億港元）的綜合援助計劃，包括：能源基礎設施 15 億美元（透過美國國際開發金融公司）、菲律宾通訊基建 1,000 萬美元、以及 AI Spark 專項資金（金額未公佈）。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🇨🇳</div>
            <div class="tech-card-content">
                <h4>抗衡中國 AI 影響力</h4>
                <p>分析師指出，美國推出 AI Spark 是為了抗衡中國 AI 模型及科技公司在東南亞的深入佈局。近年來中國 AI 企業在東南亞公共服務和數碼基礎設施的應用大幅增加，包括華為、騰訊、阿里巴巴等在多國都有 AI 項目落地。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌏</div>
            <div class="tech-card-content">
                <h4>東南亞不會選邊站</h4>
                <p>分析師普遍認為，AI Spark 不太可能迫使東南亞各國在美國與中國之間選邊站。該地區預計將繼續整合美國技術與中國及本地系統，避免依賴任何單一供應商。Kevin Kim 表示，投資涵蓋多個範疇，但鑑於東南亞對 AI、數據中心及其他領域的興趣，特別着重推進相關技術。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 關鍵數據</h4>
            <ul>
                <li><strong>25 億美元</strong>：美國向東南亞提供的綜合援助金額</li>
                <li><strong>15 億美元</strong>：能源基礎設施投資（透過 DFC）</li>
                <li><strong>1,000 萬美元</strong>：菲律宾通訊基建現代化</li>
                <li><strong>1 億美元</strong>：菲律宾外國軍事融資（較去年增加 6,000 萬）</li>
            </ul>
        </div>

        <div class="quote-box">
            <p>「AI Spark 將提供財政及技術支援，給有意部署美國 AI 系統用於公共部門應用的東南亞各國政府。」</p>
            <cite>— Kevin Kim，美國東盟大使</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>美中 AI 競賽延伸至東南亞公共部門，反映兩國在區域影響力的全面博弈。東南亞各國夾在兩大國之間，既要借力美國的資金和技術，又要避免過度依賴任何一方。隨着中國在該區的 AI 基礎設施持續擴展，美國的 AI Spark 能否有效抗衡，仍有待觀察。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月 22 日</div>
                <div class="timeline-title">美國宣佈 AI Spark</div>
                <div class="timeline-desc">美國東盟大使 Kevin Kim 正式宣佈 AI Spark 倡議</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月中</div>
                <div class="timeline-title"> Rubio 訪問馬尼拉</div>
                <div class="timeline-desc">美國國務卿 Rubio 出席東盟外長會議，推動 25 億美元援助計劃</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">近年</div>
                <div class="timeline-title">中國 AI 在東南亞擴張</div>
                <div class="timeline-desc">華為、騰訊、阿里巴巴等在東南亞廣泛部署 AI 公共服務</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2023 年</div>
                <div class="timeline-title">中國生成式 AI 法規</div>
                <div class="timeline-desc">中國推出《生成式人工智能服務管理暫行辦法》</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2024 年</div>
                <div class="timeline-title">「AI Plus」寫入政府工作報告</div>
                <div class="timeline-desc">中國將 AI Plus 納入政府工作報告，加強 AI 政策支持</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>美國 AI Spark</th>
                    <th>中國 AI 佈局</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>主要資金</td>
                    <td class="highlight-col">25 億美元綜合援助</td>
                    <td>無明確公佈金額</td>
                </tr>
                <tr>
                    <td>切入領域</td>
                    <td class="highlight-col">公共部門 AI 應用</td>
                    <td>公共服務、數碼基建</td>
                </tr>
                <tr>
                    <td>合作模式</td>
                    <td>政府對政府</td>
                    <td class="highlight-col">企業主導 + 政府支持</td>
                </tr>
                <tr>
                    <td>東南亞接受度</td>
                    <td>逐步擴展中</td>
                    <td class="highlight-col">已深入多國</td>
                </tr>
                <tr>
                    <td>政治色彩</td>
                    <td>Pax Silica 計劃一部分</td>
                    <td>「AI Plus」國家戰略</td>
                </tr>
            </tbody>
        </table>

        <h3>💡 其他投資重點</h3>
        <div class="tech-card">
            <div class="tech-card-icon">🛡️</div>
            <div class="tech-card-content">
                <h4>军事及執法合作</h4>
                <p>美国向菲律宾提供 1 億美元外國軍事融資，並提供 250 萬美元協助東盟各國打擊詐騙、網絡犯罪、毒品走私及洗錢。美军同时与 Meta、Google 等科技公司合作，制定公私合作打擊網絡詐騙的原則。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏥</div>
            <div class="tech-card-content">
                <h4>公共衛生</h4>
                <p>美国向菲律宾提供 6.85 億美元愛滋病防治援助，以及其他衛生安全合作項目，強化區域衛生安全網絡。</p>
            </div>
        </div>
"""

metadata = {
    'title': 'AI 競爭升溫 美國瞄準東南亞公共部門',
    'h1': 'AI 競爭升溫<br>美國瞄準東南亞公共部門',
    'subtitle': '美國推出 AI Spark 抗衡中國 AI 在東南亞的佈局',
    'source_url': 'https://www.scmp.com/week-asia/economics/article/3362166/ai-competition-heats-us-targets-southeast-asias-public-sector',
    'source_name': 'SCMP',
    'pub_date': '2026-07-30',
    'img_alt': '美國東南亞 AI 競爭',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260730_092238',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")
