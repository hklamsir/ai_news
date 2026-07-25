#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.bnext.com.tw/article/91555/military-ai-in-battlefield-tech-company" target="_blank">BNEXT</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-25</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>美國軍方與科技公司的合作藩籬正在瓦解。Palantir 的 Maven 智慧系統已將目標定位所需人力從2,000人降至20人，Anduril 獲得200億美元反無人機合約，OpenAI、Google、NVIDIA 等科技巨頭也正式向五角大廈解禁，軍事AI時代已經來臨。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🎯</div>
            <div class="tech-card-content">
                <h4>從2,000人到20人：AI顛覆目標定位</h4>
                <p>2003年美軍攻打伊拉克需2,000人負責的目標定位工作，如今透過 Palantir 的 Maven 智慧系統，僅需20名士兵即可完成。AI介入 OODA 循環（觀察、定向、決策、行動）各環節，在情報量爆炸的現代戰場扮演關鍵角色。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🚀</div>
            <div class="tech-card-content">
                <h4>史詩怒火行動：Maven系統全面上線</h4>
                <p>美國與以色列聯合對伊朗發動的「史詩怒火行動」全面依賴 Maven 智慧系統。能在瞬間分析衛星影像、無人機監控、雷達感測器乃至社群網路數據，自動生成數百個目標建議。開戰首兩週便轟炸多達6,000個目標。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💼</div>
            <div class="tech-card-content">
                <h4>Palantir：百億美元國防合約</h4>
                <p>Palantir 與美國陸軍簽署10年期企業服務協議，採購上限達100億美元。Maven 智慧系統及 Gotham 情報分析平台已被美軍廣泛用於情報分析與決策支援。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🛸</div>
            <div class="tech-card-content">
                <h4>Anduril：200億美元反無人機合約</h4>
                <p>Anduril 專注自主無人機、反無人機技術及戰場軟體平台。2026年與美國陸軍簽訂為期10年、採購上限200億美元的反無人機合約。台灣亦向 Anduril採購 ALTIUS 600M 攻擊型無人機，2026年3月前已全數交付。</p>
            </div>
        </div>


        <div class="highlight-box">
            <h4>📌 重點數據</h4>
            <ul>
                <li><strong>目標定位人力：</strong>從2,000人降至20人（Maven系統）</li>
                <li><strong>Maven系統戰果：</strong>史詩怒火行動首兩週轟炸6,000個目標</li>
                <li><strong>Palantir合約：</strong>100億美元（10年期）</li>
                <li><strong>Anduril合約：</strong>200億美元（10年期反無人機）</li>
                <li><strong>全球軍事AI市場：</strong>2024年達93.1億美元，年複合成長率13%</li>
                <li><strong>美國國防部AI投入：</strong>自2016年以來至少750億美元</li>
            </ul>
        </div>

        <div class="quote-box">
            <p>「AI已經徹底顛覆了傳統軍事上的識別目標、決策發動攻擊的殺傷鏈，在情報量已經大到人類難以單獨處理的現代戰場，扮演了過濾資訊及輔助決策的關鍵角色。」</p>
            <cite>— BNEXT 報導摘要</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>根據 Grand View Research 數據，全球軍事AI市場正以13%年複合成長率擴張。Palantir、Anduril 這類新一代國防科技公司正用矽谷方式快速將 AI 帶入軍事領域，傳統軍工巨頭洛克希德．馬丁、諾斯洛普．格魯曼、L3哈里斯等也不願錯過這股商機。2026年5月 OpenAI、Google、NVIDIA 等科技巨頭向五角大廈解禁，標誌著軍事AI時代的全面來臨。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2020 年</div>
                <div class="timeline-title">緋紅巨龍演習</div>
                <div class="timeline-desc">美軍在布拉格堡測試 AI 目標定位能力，開啟軍事AI時代</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">Palantir 100億合約</div>
                <div class="timeline-desc">Palantir 與美國陸軍簽署10年期企業服務協議，採購上限100億美元</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 1 月</div>
                <div class="timeline-title">委內瑞拉行動</div>
                <div class="timeline-desc">美國針對馬杜洛的突襲行動傳出使用 Palantir + Claude AI</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 3 月</div>
                <div class="timeline-title">台灣接收無人機</div>
                <div class="timeline-desc">台灣向 Anduril 採購的 ALTIUS 600M 攻擊型無人機全數交付</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 5 月</div>
                <div class="timeline-title">科技巨頭解禁</div>
                <div class="timeline-desc">OpenAI、Google、NVIDIA、微軟、亞馬遜、甲骨文與美國國防部達成協議，允許軍方使用其先進AI能力</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>公司/勢力</th>
                    <th>軍事AI布局</th>
                    <th>代表產品/合約</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Palantir</td>
                    <td>政府國防數據分析起家，AI融入軍方既有流程</td>
                    <td class="highlight-col">Maven智慧系統（100億美元合約）</td>
                </tr>
                <tr>
                    <td>Anduril</td>
                    <td>自主無人機、反無人機技術及戰場軟體平台</td>
                    <td class="highlight-col">反無人機合約（200億美元）</td>
                </tr>
                <tr>
                    <td>傳統軍工</td>
                    <td>洛克希德、諾斯洛普、L3哈里斯整合AI進既有產品</td>
                    <td>戰機、雷達、後勤維修AI化</td>
                </tr>
                <tr>
                    <td>科技巨頭</td>
                    <td>OpenAI、Google、NVIDIA 等正式向五角大廈解禁</td>
                    <td class="highlight-col">軍用AI部署協議（2026年5月）</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       '軍用AI加速進戰場！Palantir、Anduril搶進五角大廈，科技巨頭改寫下一代戰爭 | BNEXT',
    'h1':          '軍用AI<br>顛覆未來戰場',
    'subtitle':    '目標定位從2,000人降至20人：Palantir Maven系統與Anduril如何改寫戰爭形態',
    'source_url':  'https://www.bnext.com.tw/article/91555/military-ai-in-battlefield-tech-company',
    'source_name': 'BNEXT',
    'pub_date':    '2026-07-25',
    'img_alt':     '軍事AI指揮中心',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260725_125345',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print("❌ HTML 生成失敗")
    for err in errors:
        print(f"   - {err}")
