import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.zdnet.com/article/microsoft-august-windows-update-421-bugs-zero-day-exploited/" target="_blank">ZDNET</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-11 至 2026-08-16</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Microsoft 發布 8 月 Patch Tuesday，修補 421 個漏洞，其中一個由北韓 Lazarus 組織利用的零日漏洞 CVE-2026-68820 已確認在野被主動利用，攻擊者透過 Windows 核心驅動程式 afd.sys 部署 FudModule 木馬。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🚨</div>
            <div class="tech-card-content">
                <h4>已確認被利用的零日漏洞（CVE-2026-68820）</h4>
                <p><strong>漏洞位置</strong>：Windows Ancillary Function Driver for WinSock（afd.sys）</p>
                <p><strong>漏洞類型</strong>：Use-after-free（釋放後使用）</p>
                <p><strong>CVSS 分數</strong>：7.0（高風險）</p>
                <p><strong>攻擊方式</strong>：本地已認證攻擊者透過特定應用程式觸發 race condition，即可 SYSTEM 層級執行代碼，無需用戶互動</p>
                <p><strong>攻擊者</strong>：北韓 Lazarus 組織，已利用此漏洞部署新版 FudModule 核心模式木馬</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>8 月漏洞統計</h4>
                <p>本次 Patch Tuesday 共修補 <strong>421 個漏洞</strong>，包括 <strong>62 個嚴重（Critical）等級</strong>漏洞，以及 <strong>3 個零日漏洞</strong>（1 個已確認被主動利用）</p>
                <p>自 2022 年起，afd.sys 已出現四個被實際利用的零日漏洞（含本次 CVE-2026-68820）</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💻</div>
            <div class="tech-card-content">
                <h4>各產品漏洞分布</h4>
                <p>Windows（236）、Office 與 Office 2016（196）、SharePoint Server（30）、開發者工具（26）、Azure（17）、Exchange Server（7）、Defender（1）及其他（6）</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>其他值得關注的漏洞</h4>
                <p><strong>CVE-2026-62832</strong>（Windows User Profile Service，權限提升，已公開披露）、<strong>CVE-2026-62893</strong>（Windows Deployment Services TFTP Server，遠端代碼執行）、<strong>CVE-2026-62878</strong>（Windows DNS Server，遠端代碼執行）、<strong>CVE-2026-62815</strong>（Microsoft QUIC，遠端代碼執行）、<strong>CVE-2026-62911</strong>（Exchange Server，權限提升）</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>這是連續第三個月微軟在例行 Patch Tuesday 中出現「已確認被主動利用」的零日漏洞，安全團隊應儘速修補 CVE-2026-68820 及 CVE-2026-62832。</p>
        </div>

        <div class="quote-box">
            <p>「自 2022 年起，afd.sys 已出現過三個被實際利用的零日漏洞，包括 CVE-2025-32709、CVE-2025-21418 和 CVE-2024-38193。」</p>
            <cite>— SecurityWeek，引用安全研究人員 Narang 的分析</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這次更新顯示攻擊者正加快利用公開披露漏洞的速度，連續三個月出現已被主動利用的零日漏洞，顯示網絡安全威脅形勢嚴峻。AI 輔助漏洞挖掘正發現更多以往隱藏的安全缺陷，大型軟體商的安全更新頻率及規模持續增加，安全團隊需建立更快速的修補機制。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2024 年</div>
                <div class="timeline-title">CVE-2024-38193</div>
                <div class="timeline-desc">afd.sys 零日漏洞，被 Lazarus 組織利用</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">CVE-2025-21418</div>
                <div class="timeline-desc">afd.sys 零日漏洞，被實際利用</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025 年</div>
                <div class="timeline-title">CVE-2025-32709</div>
                <div class="timeline-desc">afd.sys 零日漏洞，被實際利用</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">確認被利用的零日漏洞</div>
                <div class="timeline-desc">微軟連續第三個月在 Patch Tuesday 出現已被主動利用的零日</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 8 月 11 日</div>
                <div class="timeline-title">CVE-2026-68820</div>
                <div class="timeline-desc">afd.sys use-after-free 漏洞，被 Lazarus 組織利用部署 FudModule 木馬</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>月份</th>
                    <th>漏洞總數</th>
                    <th>零日（已確認被利用）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>2026 年 6 月</td>
                    <td>206</td>
                    <td class="highlight-col">1 個（已確認）</td>
                </tr>
                <tr>
                    <td>2026 年 7 月</td>
                    <td>570</td>
                    <td class="highlight-col">1 個（已確認）</td>
                </tr>
                <tr>
                    <td>2026 年 8 月</td>
                    <td>421</td>
                    <td class="highlight-col">1 個（已確認）+ 2 個公開披露</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Microsoft 8 月 Patch Tuesday 修補 421 漏洞：Lazarus 組織利用零日部署木馬',
    'h1':          'Microsoft 8 月修補 421 漏洞<br>確認 Lazarus 組織利用零日攻擊',
    'subtitle':    'CVE-2026-68820 零日漏洞被用於部署 FudModule 核心模式木馬，安全團隊應儘速更新',
    'source_url':  'https://www.zdnet.com/article/microsoft-august-windows-update-421-bugs-zero-day-exploited/',
    'source_name': 'ZDNET',
    'pub_date':    '2026-08-11',
    'img_alt':     'Microsoft 8 月 Patch Tuesday 修補 421 漏洞 Lazarus 零日攻擊',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260816_103841',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print("Errors:", errors)
