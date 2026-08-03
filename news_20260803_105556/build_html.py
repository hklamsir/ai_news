import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.zdnet.com/article/windows-installation-files-getting-bigger-blame-ai/" target="_blank">ZDNET</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-30</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Windows 安裝檔案過去 10 年容量翻倍，罪魁禍首並非傳統因素，而是 Microsoft 為 Copilot+ PC 預載的 AI 模型——即使電腦沒有 NPU 也需下載這些約 3 GB 的代碼。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📀</div>
            <div class="tech-card-content">
                <h4>安裝檔案有多大？</h4>
                <p>Windows 10 原版約 4 GB，最新 ISO 已超過 8 GB（10 年翻倍）；使用 Media Creation Tool 下載仍需 6.8 GB。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>AI 模型成罪魁禍首</h4>
                <p>Copilot+ PC 包含約 <b>3 GB 共享 AI 模型</b>用於本地 AI 功能。即使電腦沒有 NPU、沒有 Copilot，仍需下載這些檔案，只是安裝程式會忽略它們。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>更新機制的問題</h4>
                <p>Microsoft 將這些大型 AI 代碼隨<b>每月累積更新</b>發布，而非透過 Microsoft Store 分發，導致 Windows Update 負擔過重且需重啟。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💡</div>
            <div class="tech-card-content">
                <h4>解決方案：Microsoft Store 分發</h4>
                <p>Windows 11 已開始將部分元件透過 Store 分發，只在使用該應用時才更新，且<b>不需要重啟</b>即可完成安裝。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>專家 Michael Niehaus（16 年 Microsoft 部署經驗）指出：「Windows 變大了嗎？是的。更新變大了嗎？是的。Copilot+ 讓情況更糟嗎？是的，而且糟糕很多。」</p>
        </div>

        <div class="quote-box">
            <p>「If you have a plain-vanilla, no-NPU, Copilot-minus PC, you still have to download these bits, which the Windows installer will then ignore.」</p>
            <cite>— Michael Niehaus，2Pint Software（前 Microsoft 16 年員工）</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>隨著 Copilot+ PC 普及，這些 AI 模型只會繼續增加。若 Microsoft 不改善分發機制，硬碟空間有限的用戶將持續受到影響。Store 分發模式可能是未來關鍵。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2016</div>
                <div class="timeline-title">Windows 10 原版 ISO</div>
                <div class="timeline-desc">約 4 GB，是當時標準安裝大小</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2024</div>
                <div class="timeline-title">Copilot+ PC 推出</div>
                <div class="timeline-desc">Microsoft 開始預載約 3 GB AI 模型</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026-07</div>
                <div class="timeline-title">Michael Niehaus 分析出爐</div>
                <div class="timeline-desc">曝光 AI 模型導致 Windows 安裝檔案膨脹的問題</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">現已</div>
                <div class="timeline-title">Windows ISO 超過 8 GB</div>
                <div class="timeline-desc">10 年內翻倍，Media Creation Tool 仍需 6.8 GB</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">Microsoft Store 分發模式</div>
                <div class="timeline-desc">有望減少 Windows Update 負擔，無需重啟安裝</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>比較項目</th>
                    <th>傳統 Windows Update</th>
                    <th>Microsoft Store 分發</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>下載大小</td>
                    <td class="highlight-col">含所有 AI 模型（~3 GB）</td>
                    <td>僅下載使用中的元件</td>
                </tr>
                <tr>
                    <td>需要重啟</td>
                    <td class="highlight-col">是</td>
                    <td>否</td>
                </tr>
                <tr>
                    <td>NPU 需求</td>
                    <td>無 NPU 電腦也需下載</td>
                    <td class="highlight-col">只下載相關內容</td>
                </tr>
                <tr>
                    <td>更新時機</td>
                    <td>每月累積更新統一推送</td>
                    <td class="highlight-col">按需更新</td>
                </tr>
                <tr>
                    <td>硬碟空間佔用</td>
                    <td>較多閒置檔案</td>
                    <td class="highlight-col">按使用需求</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'Windows 安裝檔案愈來愈大？AI 模型成罪魁禍首',
    'h1': 'Windows 安裝檔案愈來愈大？<br>AI 模型成罪魁禍首',
    'subtitle': 'Copilot+ PC 預載 3 GB AI 模型，無 NPU 電腦也需下載，10 年 ISO 容量翻倍至 8 GB',
    'source_url': 'https://www.zdnet.com/article/windows-installation-files-getting-bigger-blame-ai/',
    'source_name': 'ZDNET',
    'pub_date': '2026-07-30',
    'img_alt': 'Windows 筆記型電腦顯示過大的安裝檔案下載視窗，內含 AI 模型相關內容',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260803_105556',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果: {'成功' if success else '失敗'}")
if errors:
    print(f"錯誤: {errors}")
