#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07" target="_blank">Reuters</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-07</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>北京當局過去一個月與阿里巴巴、字節跳動及 Z.ai 等主要科技公司舉行會議，討論限制海外用戶使用中國最先進 AI 模型的途徑。此舉反映中國跟美國一樣，將前沿人工智能視為需要管控的關鍵國家資產。中美兩國均在加強對前沿 AI 的管控，AI 已成為大國競爭的核心資產。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🇨🇳</div>
            <div class="tech-card-content">
                <h4>北京研擬 AI 模型出海限制</h4>
                <p>三名知情人士透露，中華人民共和國政府官員過去一個月與頂級科技公司舉行會議，討論限制海外取用中國最先進 AI 模型，包括尚未發布的模型。與會者包括阿里巴巴、字節跳動及 Z.ai，會議由商務部主導。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔒</div>
            <div class="tech-card-content">
                <h4>管制範圍：封閉及開源模型均涵蓋</h4>
                <p>官員討論的限制範圍涵蓋封閉原始碼（closed-source）和開源權重（open-weight）模型。官員還討論了將洩露或盜竊專有 AI 技術列為國家安全法犯罪的可能性，並探索限制哪些投資者可資助本土 AI 初創企業的措施。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🇺🇸</div>
            <div class="tech-card-content">
                <h4>美國的對應管制措施</h4>
                <p>美國總統特朗普政府也深度關注 AI 的國家安全風險，尤其是美國 AI 產品被中國、俄羅斯等國軍事情報機構濫用的可能性。此前美國下令外國國民不得取用 Anthropic 最先進的 Fable 和 Mythos 模型，迫使其在無法即時驗證國籍的情況下向所有用戶禁用這些模型。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💡</div>
            <div class="tech-card-content">
                <h4>Z.ai 崛起引發中美關注</h4>
                <p>Z.ai 最近因其 GLM-5.2 模型的能力接近美國頂級產品、但價格僅為一小部分而在矽谷引起轟動。阿里巴巴的 Qwen 和字節跳動的 Doubao 是中國最廣泛使用的 AI 模型。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 關鍵要點</h4>
            <ul>
                <li><strong>參與企業</strong>：阿里巴巴、字節跳動、Z.ai（由商務部主導）</li>
                <li><strong>管制範圍</strong>：封閉原始碼 + 開源權重模型</li>
                <li><strong>可能措施</strong>：國家安全法入罪、限制外國投資本土 AI 初創</li>
                <li><strong>背景</strong>：北京試圖將本土 AI 保留在國內，與美國將 AI 視為關鍵國家資產一致</li>
            </ul>
        </div>

        <div class="quote-box">
            <p>「北京已採取一系列措施試圖將本土 AI 保留在國內，顯示中國與美國一樣，將前沿人工智能視為需要控制流動的關鍵國家資產。」</p>
            <cite>— Reuters 獨家報道</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>中美兩國均在加強對前沿 AI 的管控，象徵 AI 已成為大國競爭的核心資產。北京此舉可能改變依賴低成本開源模型從業者的採購和成本假設，同時也可能促使更多中國 AI 創辦人選擇出走美國。這場 AI 主權之爭將深刻影響全球科技格局。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">北京下令 Meta 撤資 Manus</div>
                <div class="timeline-desc">北京命令 Meta 撤銷對 AI 初創公司 Manus 的 20 億美元收購</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">美國封禁 Anthropic 先進模型</div>
                <div class="timeline-desc">美國下令外國國民不得取用 Anthropic 的 Fable 和 Mythos 模型</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月</div>
                <div class="timeline-title">北京開始管制 AI 模型出海</div>
                <div class="timeline-desc">商務部主導與阿里巴巴、字節跳動、Z.ai 等討論限制海外取用中國 AI 模型</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月</div>
                <div class="timeline-title">Z.ai GLM-5.2 引起矚目</div>
                <div class="timeline-desc">Z.ai 的 GLM-5.2 模型能力接近美國頂級產品但成本極低，在矽谷引發轟動</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月 17 日</div>
                <div class="timeline-title">Moonshot 發布 Kimi K3</div>
                <div class="timeline-desc">Moonshot AI 發布 Kimi K3 模型，部分基準測試超越 GPT-5.6 和 Claude Fable 5</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>中國（北京管制）</th>
                    <th>美國（出口管制）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>管制對象</td>
                    <td class="highlight-col">限制本國 AI 模型出海</td>
                    <td>限制外國取用本國 AI 模型</td>
                </tr>
                <tr>
                    <td>涉及企業</td>
                    <td>阿里巴巴、字節跳動、Z.ai</td>
                    <td class="highlight-col">Anthropic、Meta、Google</td>
                </tr>
                <tr>
                    <td>法規依據</td>
                    <td>國家安全法、出口管制法規</td>
                    <td class="highlight-col">國家安全相關法規</td>
                </tr>
                <tr>
                    <td>覆蓋範圍</td>
                    <td>封閉 + 開源模型</td>
                    <td class="highlight-col">主要封閉模型（部分已放寬）</td>
                </tr>
                <tr>
                    <td>背後邏輯</td>
                    <td>保持本土 AI 領先優</td>
                    <td class="highlight-col">防止技術外流國家安全</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '北京研擬限制海外取用中國頂級 AI 模型',
    'h1': '北京研擬限制海外<br>取用中國頂級 AI 模型',
    'subtitle': '路透社獨家報道：北京與阿里巴巴、字節跳動、Z.ai 商討 AI 模型出海管制',
    'source_url': 'https://www.reuters.com/world/beijing-is-looking-curbing-overseas-access-chinas-top-ai-models-sources-say-2026-07-07',
    'source_name': 'Reuters',
    'pub_date': '2026-07-07',
    'img_alt': '北京限制 AI 模型出海',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260730_093633',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")
