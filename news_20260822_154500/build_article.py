#!/usr/bin/env python3
import sys, os
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.youtube.com/watch?v=eG4MLdFetrE" target="_blank">Best Partners TV</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-22（本摘要）</p>
            <p><strong>🤖 處理方式</strong>：YouTube 字幕下載 + AI 繁體中文摘要</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Cursor 推出自家代碼託管平台 Origin，除具備 Repo、PR、Code Review、Merge 等完整功能，更將 AI Agent 直接嵌入代碼托管與協作流程。Cursor 的目標並非要取代 GitHub，而是把「代碼存放」本身變成 AI Agent 工作的一部分。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🚀</div>
            <div class="tech-card-content">
                <h4>完整代碼協作功能</h4>
                <p>開發者可在 Origin 直接創建代碼倉庫、推送本地項目，支援 Pull Request、代碼瀏覽、Diff 查看、評論、Code Review 以至 Merge，基本覆蓋完整代碼協作流程。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>AI Agent 嵌入協作流程</h4>
                <p>開發者可針對屏幕上打開的文件直接向 AI 提問，也可讓 Agent 修改代碼、創建或更新 PR、直接推送代碼。過去由人類負責的 Commit、PR、Review 工作，越來越多可交給 Agent 完成。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔗</div>
            <div class="tech-card-content">
                <h4>GitHub 實時同步</h4>
                <p>Origin 支援把 GitHub 倉庫實時鏡像到平台，同時保持 GitHub 作為主要數據源，用戶無需放棄現有 GitHub 流程。外媒評價這是 Origin 最巧妙的设计之一。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌐</div>
            <div class="tech-card-content">
                <h4>接入 Vercel、Buildkite、Depot</h4>
                <p>Cursor 持續擴展 Origin 周邊生態，令代碼從編寫、提交、Review 到測試和部署，整個流程逐漸被納入同一個工作流。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Cursor 官方明確表示：「你的代碼、PR 與 Agent 現在全部都集中在一處。」開發者角色正從「親力親為」轉向「提出需求、檢查結果、最终决策」，這一趨勢正在加速。</p>
        </div>

        <div class="quote-box">
            <p>「過去由人類開發者負責的 Commit、PR、Review 工作，越來越多可交給 Agent 完成，人類更多負責提出需求、檢查結果和最終决策。」</p>
            <cite>— Best Partners TV《大飛》</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Cursor Origin 的出現，代表 AI 編程工具正從「輔助人類寫代碼」進化到「接管整個開發協作流程」。未來開發者的角色將持續轉變——從親力親為轉向提出需求與把關結果。但在大型團隊中如何在 AI 便利性與代碼安全審核之間取得平衡，仍是需慎重考慮的議題。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">過去</div>
                <div class="timeline-title">Cursor = AI 編程工具</div>
                <div class="timeline-desc">代碼生成、重構、糾錯和優化，建基於 GitHub 之上的 AI 工具</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">GitHub 大面積異常</div>
                <div class="timeline-title">Cursor Origin 宣佈</div>
                <div class="timeline-desc">Cursor 向付費用戶推出代碼托管平台，打破傳統工具邊界</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">Origin 上線</div>
                <div class="timeline-title">完整代碼協作流程</div>
                <div class="timeline-desc">支援 Repo、PR、Code Review、Merge，覆蓋完整開發生命週期</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">核心差異</div>
                <div class="timeline-title">AI Agent 直接嵌入</div>
                <div class="timeline-desc">代碼托管本身成為 AI Agent 工作流程的一部分，非單純存放位置</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">開發者角色轉變</div>
                <div class="timeline-desc">人類更多負責提出需求與最終把關，Agent 承擔執行層面工作</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>功能</th>
                    <th>傳統 GitHub</th>
                    <th>Cursor Origin</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>代碼倉庫</td>
                    <td>✅ 完整支援</td>
                    <td class="highlight-col">✅ 完整支援</td>
                </tr>
                <tr>
                    <td>PR 與 Code Review</td>
                    <td>✅ 完整支援</td>
                    <td class="highlight-col">✅ 完整支援</td>
                </tr>
                <tr>
                    <td>AI Agent 嵌入</td>
                    <td>❌ 無</td>
                    <td class="highlight-col">✅ 直接在流程中使用 Agent</td>
                </tr>
                <tr>
                    <td>代碼即時 AI 提問</td>
                    <td>❌ 無</td>
                    <td class="highlight-col">✅ 針對打開的文件直接提問</td>
                </tr>
                <tr>
                    <td>GitHub 同步</td>
                    <td>—</td>
                    <td class="highlight-col">✅ 實時鏡像，保持 GitHub 為主數據源</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'Cursor 推出代碼託管平台 Origin：AI Agent 融入程式開發協作流程',
    'h1': 'Cursor 推出代碼託管平台<br>Origin',
    'subtitle': 'AI Agent 融入代碼托管與協作流程的下一個時代',
    'source_url': 'https://www.youtube.com/watch?v=eG4MLdFetrE',
    'source_name': 'Best Partners TV',
    'pub_date': '2026-08-22',
    'img_alt': 'Cursor Origin 代碼托管平台 AI 視覺圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260822_154500',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print("❌ HTML 生成失敗:")
    for e in errors:
        print(f"  {e}")
    sys.exit(1)
