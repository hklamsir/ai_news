import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://mp.weixin.qq.com/s/Tl9g3li56NaK2vwSM4V1jA" target="_blank">微信公眾號「老李流放美利堅」</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-09</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>日本一名15歲初中生利用ChatGPT協助編寫攻擊程式，在3至4小時內將46,812個動畫平台會員帳號集體退會，服務被迫停擺一個半月。這起案件暴露了AI工具正在拉低網路攻擊門檻的嚴峻趨勢。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🔍</div>
            <div class="tech-card-content">
                <h4>發現漏洞與初步攻擊</h4>
                <p>被告從小學四年級開始自學程式設計，擅長通信解析（抓包分析）。在研究萬代頻道網站時，他發現了一個不需要正常會員ID和密碼就能登錄的漏洞，並自己寫了一套訪問退會處理頁面的程式。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>ChatGPT充當結對程式員</h4>
                <p>自己寫的程式因為跑得太慢，於是請ChatGPT幫忙優化，最終用另一種程式語言重寫完成了攻擊程式。ChatGPT的角色更像是一個「幫忙優化慢代碼、幫忙換語言重寫」的結對程式員，沒有主動策劃攻擊。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>3至4小時清空4.68萬帳號</h4>
                <p>整個攻擊在3至4小時內完成，46,812個帳號在用戶完全不知情的情況下被集體退會。運營公司緊急停止服務，11月6日宣布全面關停，直到12月19日才恢復，足足停擺一個半月。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💀</div>
            <div class="tech-card-content">
                <h4>「因為能登錄的帳號很多，所以就做了」</h4>
                <p>警方披露的供述令人不寒而慄：被告對被害企業「沒有恨意」，既無勒索信，也無政治訴求，純粹是「發現自己可以做得到」的念頭驅使。這種無明確動機的濫用，比任何勒索信都更難提前防範。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>2026年6月13日首次逮捕，7月4日再次被捕，7月6日東京都警正式公布案情。被告更換IP約30次繞開企業封鎖，但警方最終仍透過通信日誌追查到其身份。</p>
        </div>

        <div class="quote-box">
            <p>「我只是发现自己做得到」，这大概是我们今年读到过最可怕的攻击者动机。</p>
            <cite>— 安全從業者 @Securedotcom</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>這起案件暴露了一個值得警惕的趨勢：<strong>生成式AI把「半成品腳本」和「能在真實系統上穩定跑完四萬次的程式」之間的距離，縮短到了一個自學幾年的中學生就能跨過去的程度</strong>。</p>
        <p>對於企業而言，退會、改密、改支付方式這類敏感業務操作，本身就應該有更嚴格的身份校驗和頻率控制。對於家長和學校而言，一個孩子展現出的技術天賦，如果沒人告訴他「未授權訪問就是違法」，這份天賦隨時可能滑向他自己都始料未及的方向。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2025年11月4日</div>
                <div class="timeline-title">攻擊發生</div>
                <div class="timeline-desc">下午5點起，46,812個萬代頻道會員帳號開始被集體退會</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025年11月6日</div>
                <div class="timeline-title">服務關停</div>
                <div class="timeline-desc">萬代頻道緊急停止全部服務，最多約136萬帳戶資訊可能已被觸及</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2025年12月19日</div>
                <div class="timeline-title">服務恢復</div>
                <div class="timeline-desc">萬代頻道恢復運營，服務停擺約一個半月</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026年6月13日</div>
                <div class="timeline-title">首次逮捕</div>
                <div class="timeline-desc">埼玉縣所澤市高一男生（15歲）因涉嫌違反《禁止不正當訪問法》被首次逮捕</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026年7月4日</div>
                <div class="timeline-title">再次逮捕</div>
                <div class="timeline-desc">因涉嫌偽計業務妨害被再次逮捕</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026年7月6日</div>
                <div class="timeline-title">案情公布</div>
                <div class="timeline-desc">東京都警對外正式公布案情，震驚全社會</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>傳統網路攻擊</th>
                    <th>AI輔助攻擊（本案）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>技術門檻</td>
                    <td>需要精英駭客技能</td>
                    <td class="highlight-col">自學幾年的中學生即可</td>
                </tr>
                <tr>
                    <td>攻擊準備時間</td>
                    <td>數週至數月</td>
                    <td class="highlight-col">利用AI快速優化，數天內完成</td>
                </tr>
                <tr>
                    <td>動機</td>
                    <td>金錢、政治、復仇</td>
                    <td class="highlight-col">「因為我能做到」——無明確動機</td>
                </tr>
                <tr>
                    <td>防範難度</td>
                    <td>可通過威脅情報預警</td>
                    <td class="highlight-col">純技術問題無法提前預警</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '「因為能登錄的帳號很多，就做了」：日本15歲高中生借ChatGPT一夜清空4.68萬個動畫帳號',
    'h1': '「因為能登錄的帳號很多，就做了」<br>日本15歲高中生借ChatGPT一夜清空4.68萬個動畫帳號',
    'subtitle': 'AI工具降低攻擊門檻：一名中學生的「技術好奇心」如何變成一場大規模網路攻擊',
    'source_url': 'https://mp.weixin.qq.com/s/Tl9g3li56NaK2vwSM4V1jA',
    'source_name': '老李流放美利堅',
    'pub_date': '2026-07-09',
    'img_alt': '日本15歲高中生用ChatGPT清空動畫帳號示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260710_090000',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print("錯誤：")
    for e in errors:
        print(f"  - {e}")
