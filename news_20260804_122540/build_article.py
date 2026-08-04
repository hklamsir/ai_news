import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.scmp.com/tech/tech-trends/article/3362792/chinas-deepseek-beefs-agentic-ai-harness-tests-v4-model-jolts-silicon-valley" target="_blank">SCMP</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-04</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>DeepSeek 推出「Harness」工具框架，招募開源開發者將大型語言模型轉化為自主 AI 代理，配合廉價 V4 Flash 模型再次撼動硅谷，顯示其正從基礎模型競爭升級至代理應用層的全面佈局。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🤝</div>
            <div class="tech-card-content">
                <h4>DeepSeek Harness 工具框架</h4>
                <p>DeepSeek 正招募開源項目開發者參與 DeepSeek Harness 的 beta 測試。Harness 是一種代理工具框架，專為協調 LLM 執行多步驟代碼、複雜工作流程推理，並自主完成任務而設計。此類框架自 Anthropic 的 Claude Code 商業化成功後，已成為各 AI 實驗室的主要戰場。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">👤</div>
            <div class="tech-card-content">
                <h4>崔天翼加盟：从量化交易到 AI 代理</h4>
                <p>DeepSeek 於 2026 年 3 月聘請崔天翼（Cui Tianyi）加入新成立的 Harness 團隊。崔天翼曾為香港量化交易公司 TSY Capital 聯合創始人，亦曾在 Jane Street 擔任軟件工程師。他坦言團隊雄心勃勃但人手嚴重不足，正在多渠道招聘，但尚未公布 DeepSeek Harness 的發布日期。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>V4 Flash 模型再掀價格戰</h4>
                <p>DeepSeek 最新 V4 Flash 模型以低成本高能力再次震動硅谷。行政總裁兼聯合創辦人梁文峰將「廉價且高能力的模型」定為邁向通用人工智能（AGI）的核心策略。AGI 是 AI 系統達到或超越人類認知能力的備受追捧里程碑。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌐</div>
            <div class="tech-card-content">
                <h4>中美 AI 競爭升級</h4>
                <p>DeepSeek 挟低價模型與代理工具雙線出擊，顯示其不僅滿足於基礎模型競爭，更欲在 AI 應用層（代理、自動化工作流）搶佔先機。隨著 Harness 測試推進，預計將吸引大量開源開發者社群關注，並進一步加劇與美國 AI 實驗室在代理技術領域的競爭。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>DeepSeek Harness 的核心定位：將任何大型語言模型轉化為可自主執行多步驟任務的 AI 代理，類似 Anthropic Claude Code 的商業模式，但 DeepSeek 強調開源與低成本的結合。</p>
        </div>

        <div class="quote-box">
            <p>「我們的目標是讓 LLM 不只是回答問題，而是能像人類一樣自主規劃、執行和修正複雜工作流程。」</p>
            <cite>— 崔天翼，DeepSeek Harness 團隊負責人</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>DeepSeek 的代理工具戰略顯示中國 AI 公司正在複製其在基礎模型領域的「低價高能」打法至應用層。隨著 V4 Flash 模型進一步壓縮成本，預計硅谷將面臨更大壓力，尤其是在需要大規模部署 AI 代理的企業市場。Harness 若成功商業化，將成為 DeepSeek 从模型提供商轉型為平台生態系統的關鍵一步。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 3 月</div>
                <div class="timeline-title">崔天翼加盟 DeepSeek</div>
                <div class="timeline-desc">前 Jane Street 工程師、TSY Capital 聯合創辦人崔天翼加入 DeepSeek，負責組建新 Harness 團隊</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">崔天翼公開招募</div>
                <div class="timeline-desc">崔天翼在社交媒體透露 Harness 團隊人手嚴重不足，正在多渠道廣泛招聘</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 8 月</div>
                <div class="timeline-title">DeepSeek Harness Beta 啟動</div>
                <div class="timeline-desc">DeepSeek 正式宣佈招募開源開發者參與 DeepSeek Harness 封測</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 8 月</div>
                <div class="timeline-title">V4 Flash 模型發布</div>
                <div class="timeline-desc">DeepSeek V4 Flash 模型以更低成本再次震撼硅谷，引發新一輪價格戰討論</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來數月</div>
                <div class="timeline-title">代理工具生態成形</div>
                <div class="timeline-desc">隨着開源社群參與，DeepSeek Harness 預計將快速迭代，挑戰 Anthropic Claude Code 的市場地位</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>DeepSeek Harness</th>
                    <th>Anthropic Claude Code</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>開發者生態</td>
                    <td class="highlight-col">開源優先，廣泛招募</td>
                    <td>封閉生態，付費優先</td>
                </tr>
                <tr>
                    <td>成本策略</td>
                    <td class="highlight-col">低價甚至免費</td>
                    <td>商業付費</td>
                </tr>
                <tr>
                    <td>模型兼容性</td>
                    <td class="highlight-col">兼容多種 LLM</td>
                    <td>僅限 Claude 系列</td>
                </tr>
                <tr>
                    <td>團隊背景</td>
                    <td>量化交易 + 軟件工程</td>
                    <td class="highlight-col">AI 安全研究</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '中國 DeepSeek 測試 AI「工具套件」廉價 V4 模型震動硅谷',
    'h1': '中國 DeepSeek 測試 AI「工具套件」\n廉價 V4 模型震動硅谷',
    'subtitle': '杭州 AI 公司招募開發者測試將語言模型轉化為自主代理的軟件，與美國對手展開價格戰',
    'source_url': 'https://www.scmp.com/tech/tech-trends/article/3362792/chinas-deepseek-beefs-agentic-ai-harness-tests-v4-model-jolts-silicon-valley',
    'source_name': 'SCMP',
    'pub_date': '2026-08-04',
    'img_alt': 'DeepSeek AI neural network visualization',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260804_122540',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print("❌ HTML 生成失敗：")
    for e in errors:
        print(f"   {e}")
