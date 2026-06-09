import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.techbang.com/posts/129757-openclaw-skill-cleaner-ai-trim" target="_blank">T客邦</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-09</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>OpenClaw 開發者「龍蝦之父」Peter Steinberger 無法忍受開發者將 AI 技能描述寫得像書本一樣冗長，因而開源了「skill-cleaner」技能體檢工具，呼籲開發者：「別再塞垃圾進上下文了！」</p>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>技能冗長推高運行成本與雜訊干擾</h4>
                <p>AI 技能提示詞的冗長問題不只是文字描述的長短，而是直接反映在每一次 API 呼叫的 Token 帳單上。多寫一句廢話，每次調用就得支付額外的運行成本。</p>
                <ul>
                    <li><strong>額外計費</strong>：每個無效 Token 都增加 API 成本</li>
                    <li><strong>決策混亂</strong>：Agent 接收無效資訊越多，決策品質越差</li>
                    <li><strong>延遲增加</strong>：上下文越長，處理時間越長</li>
                    <li><strong>注意力分散</strong>：模型被無效內容干擾</li>
                </ul>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🧹</div>
            <div class="tech-card-content">
                <h4>skill-cleaner 五大核心功能</h4>
                <ul>
                    <li><strong>技能提示詞預算審計</strong>：計算技能佔用的上下文令牌空間，分析預算比例，給出優化方案</li>
                    <li><strong>重複技能檢測</strong>：跨越 Codex 內置庫、快取與個人根目錄，掃描並標記高度相似或同名的冗餘技能</li>
                    <li><strong>未使用技能篩查</strong>：基於歷史日誌，找出長期未被呼叫的閒置技能以供清理</li>
                    <li><strong>技能根目錄審計</strong>：統計所有技能來源並整理載入鏈路</li>
                    <li><strong>描述精簡優化</strong>：主動篩選出冗長的技能描述，推薦簡化語法以節省預算</li>
                </ul>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📝</div>
            <div class="tech-card-content">
                <h4>極簡設計哲學：技能應該像路標</h4>
                <p>Peter 主張 AI 技能的設計應該要像「路標」一樣精簡：路標的唯一任務是為 Agent 指明道路，不該把整本說明書掛在路標上。</p>
                <p>他自己開源的 <code>skill-cleaner</code> 就是最佳示範——核心技能檔案 <code>Skill.md</code> <strong>僅有 56 行提示詞</strong>。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">😂</div>
            <div class="tech-card-content">
                <h4>穴居人風格省 Token</h4>
                <p>Peter 甚至在社群用極簡的「穴居人風格」（caveman style）示範省 Token：</p>
                <blockquote><code>install skill, agent smart, user happy</code></blockquote>
                <p>堪稱將省錢刻入骨子裡。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>skill-cleaner 的核心技能檔案 Skill.md 僅有 56 行提示詞，而背後支撐運作的調用腳本則足足有近千行程式碼。這充分體現了「技能描述是路標，核心程式碼才是說明書」的極簡設計美學。</p>
        </div>

        <div class="quote-box">
            <p>「別再塞垃圾進上下文了！」</p>
            <cite>— Peter Steinberger（龍蝦之父）</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>隨著大型語言模型被應用在更複雜的工作流中，高雜訊的上下文不僅產生額外計費，還會讓 Agent 出現決策混亂。將冗餘文字精簡、將複雜邏輯封裝在底層程式碼中，才是打造高效、省錢且高可靠性 AI 系統的正確方向。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">過去</div>
                <div class="timeline-title">技能描述越寫越長</div>
                <div class="timeline-desc">開發者陷入「提示詞寫得越詳細，AI 就表現越好」的迷思</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">問題累積</div>
                <div class="timeline-title">上下文窗口被無效雜訊塞滿</div>
                <div class="timeline-desc">每次 API 呼叫都要為無效 Token 付費，Agent 決策品質下降</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">龍蝦之父開源 skill-cleaner</div>
                <div class="timeline-desc">Peter Steinberger 親自撰寫技能體檢工具並開源</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">現在</div>
                <div class="timeline-title">極簡設計風格崛起</div>
                <div class="timeline-desc">技能描述應像路標，核心邏輯封裝在程式碼中</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">高效、省錢、高可靠性的 AI 系統</div>
                <div class="timeline-desc">精簡冗餘文字成為 AI 開發的新方向</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>對比項目</th>
                    <th>傳統方式（冗長技能）</th>
                    <th>極簡方式（skill-cleaner）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>技能描述</td>
                    <td>像說明書，冗長詳細</td>
                    <td class="highlight-col">像路標，精簡直接</td>
                </tr>
                <tr>
                    <td>Skill.md 行數</td>
                    <td>數百甚至上千行</td>
                    <td class="highlight-col">56 行（skill-cleaner 示範）</td>
                </tr>
                <tr>
                    <td>Token 消耗</td>
                    <td>每次呼叫支付額外成本</td>
                    <td class="highlight-col">最小化，節省 API 費用</td>
                </tr>
                <tr>
                    <td>Agent 決策</td>
                    <td>受無效資訊干擾</td>
                    <td class="highlight-col">清晰無噪音</td>
                </tr>
                <tr>
                    <td>維護性</td>
                    <td>難以追蹤和清理</td>
                    <td class="highlight-col">方便審計和優化</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'OpenClaw 龍蝦之父教你省錢！開源工具「skill-cleaner」幫你的 AI 技能大減肥',
    'h1':          'OpenClaw 龍蝦之父教你省錢！<br>開源工具「skill-cleaner」幫你的 AI 技能大減肥',
    'subtitle':    '別再塞垃圾進上下文了！Peter Steinberger 開源技能體檢工具，省 Token 就等於省錢',
    'source_url':  'https://www.techbang.com/posts/129757-openclaw-skill-cleaner-ai-trim',
    'source_name': 'T客邦',
    'pub_date':    '2026-06-09',
    'img_alt':     'skill-cleaner 技能減肥工具概念圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260609_135348',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print("錯誤：")
    for e in errors:
        print(f"  - {e}")