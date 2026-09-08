import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.bnext.com.tw/article/92145/gpt-6-astra-skill-cleanup-less-is-more" target="_blank">數位時代 BNEXT</a></p>
            <p><strong>📅 發布日期</strong>：2026-09-07</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>GPT-6 Astra 上線後，Codex 工程師建議趁機幫 skill 檔和 AGENTS.md 做大掃除，刪除過時、冗長或互相衝突的指令，否則只會拖慢模型效率。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>Skill 裝太多為何變笨？</h4>
                <p>初始 skill 清單最多占 context 的 2%（或 8,000 字元），超出会被截短甚至省略。描述互相矛盾時，模型更難判斷該用哪個。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">✂️</div>
            <div class="tech-card-content">
                <h4>五步驟大掃除</h4>
                <p>① 描述縮短到一句話　② 結構拆成路由器加附件　③ 刪食譜式流程　④ 禁令改授權並定義完成　⑤ 叫 Astra 自己稽核</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>兩種人不急著刪</h4>
                <p>若 repo 裡的 skill 會被同事的 agent（可能用 Sol、Luna 等其他模型）讀到，對 Astra 剛好的指令對它們可能不夠，仍需保留過渡規則。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💡</div>
            <div class="tech-card-content">
                <h4>核心原則：寫準而非寫少</h4>
                <p>Skill 描述要精準、結構成合、授權要明確。先刪描述、再拆結構，把完成條件寫清楚後交給模型判斷。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>GPT-6 Astra 的 context 管理上限為 2%（或 8,000 字元），Skill 描述太長或互相衝突，會讓模型直接省略部分指令，效率反而變差。</p>
        </div>

        <div class="quote-box">
            <p>「假設 Codex 已經很有能力，只寫會改變它決策的資訊。」</p>
            <cite>— OpenAI Codex skill-creator 更新原則（2026-08-13）</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>專家建議「先刪描述、再拆結構」，把完成條件寫清楚後，剩下的交給模型自己判斷。重點是「寫準」不只是「寫少」。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026-08-13</div>
                <div class="timeline-title">Skill-creator 大砍 45%</div>
                <div class="timeline-desc">OpenAI 將 Codex 內建的 skill-creator 從 416 行砍到 229 行，第一條原則改為「假設模型已經很有能力」</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-09-06</div>
                <div class="timeline-title">GPT-6 Astra 發布</div>
                <div class="timeline-desc">OpenAI 發布 GPT-6 Astra 模型，具備更強的理解模糊指令與自我判斷能力</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-09-07</div>
                <div class="timeline-title">Provencher 發文建議</div>
                <div class="timeline-desc">Codex 工程師 Eric Provencher 在 X 發表長文，建議趁新模型上線做一次 skill 大掃除</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-09-08</div>
                <div class="timeline-title">本文發布</div>
                <div class="timeline-desc">BNEXT 報導 Provencher 的五步驟建議及「寫準而非寫少」的核心原則</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">Skill 架構重構趨勢</div>
                <div class="timeline-desc">隨著 Astra 普及，預計更多開發者會重新檢視並簡化自己的 skill 檔和 AGENTS.md</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>舊模式（Sol 時代）</th>
                    <th class="highlight-col">新模式（Astra 時代）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Skill 描述</td>
                    <td>詳細說明書，越長越好</td>
                    <td class="highlight-col">一句話，只說做什麼和何時用</td>
                </tr>
                <tr>
                    <td>流程指令</td>
                    <td>一步步食譜，規定先讀什麼再做什麼</td>
                    <td class="highlight-col">刪掉，讓模型自己判斷該讀什麼</td>
                </tr>
                <tr>
                    <td>約束方式</td>
                    <td>禁令式「先問再做」</td>
                    <td class="highlight-col">明確授權，定義完成標準</td>
                </tr>
                <tr>
                    <td>結構</td>
                    <td>肥大單一 SKILL.md 檔</td>
                    <td class="highlight-col">路由器加附件，按需讀取</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'GPT-6 Astra變強後，Skill檔反而該大掃除！Codex工程師點名5種舊指令拖累效率',
    'h1': 'GPT-6 Astra變強後<br>Skill檔反而該大掃除！',
    'subtitle': 'Codex工程師點名5種舊指令拖累效率',
    'source_url': 'https://www.bnext.com.tw/article/92145/gpt-6-astra-skill-cleanup-less-is-more',
    'source_name': '數位時代 BNEXT',
    'pub_date': '2026-09-07',
    'img_alt': 'GPT-6 Astra 示意圖，AI 編程代理示意',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260908_141300',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
