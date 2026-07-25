#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.zdnet.com/article/light-flip-news/" target="_blank">ZDNET</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-25</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
            <p><strong>📝 作者</strong>：Kyle Kucharski（資深編輯）</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>總部位於布魯克林的公司 Light 推出全新折疊手機 Light Flip，售價 299 美元，主打極簡主義——無電子郵件、無 App、功能極度精簡，配合 T9 數字鍵盤輸入法，讓用戶重新專注於通話的本質。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📱</div>
            <div class="tech-card-content">
                <h4>極簡硬體設計</h4>
                <p>折疊後尺寸僅 110mm × 58mm × 19mm，重量 160 克。配備 MediaTek MT8873 處理器、6GB RAM、128GB 儲存空間，支援 5G/4G LTE、e-SIM、藍牙 5.0，另有 3.5mm 耳機孔。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⌨️</div>
            <div class="tech-card-content">
                <h4>T9 輸入法再現</h4>
                <p>T9（Text on 9 keys）輸入法透過數字鍵多次點擊選擇字母。Light 刻意保留這種「費時」的輸入方式，作為減少發短訊干擾的「軟性門檻」——你可以用它發訊息，但過程並不愉快。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>親民定價與月費</h4>
                <p>Light Flip 售價 299 美元，比 Light Phone 3 更優惠。月費僅 39 美元，降低了「數位排毒」的門檻。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌱</div>
            <div class="tech-card-content">
                <h4>「翻轉生活」九個月計畫</h4>
                <p>購買 Light Flip 的用戶可參加為期九個月的「Flip Your Life」計畫，逐步協助用戶擺脫智慧手機依賴，培養更健康的手機使用習慣。</p>
            </div>
        </div>


        <div class="highlight-box">
            <h4>📌 重點規格</h4>
            <ul>
                <li><strong>售價：</strong>299 美元</li>
                <li><strong>月費：</strong>39 美元</li>
                <li><strong>尺寸：</strong>110mm × 58mm × 19mm（折疊）</li>
                <li><strong>重量：</strong>160 克</li>
                <li><strong>記憶體：</strong>6GB RAM + 128GB</li>
                <li><strong>網絡：</strong>5G / 4G LTE</li>
                <li><strong>輸入法：</strong>T9 數字鍵盤</li>
            </ul>
        </div>

        <div class="quote-box">
            <p>「這款手機刻意保留 T9 輸入法——你可以用它發訊息，但過程並不愉快。這正是設計的一部分。」</p>
            <cite>— Light 公司設計理念</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>在智慧手機功能日益膨脹的時代，Light 的極簡路線持續吸引特定用戶群——他們渴望斷開網路的牽絆，重新掌控自己的注意力。Light Flip 以更親民的價格和更入門的硬體，降低了「數位排毒」的門檻。這種「反技術」設計在歐美市場已形成獨特的文化現象。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2017 年</div>
                <div class="timeline-title">Light 成立</div>
                <div class="timeline-desc">總部位於布魯克林，專注極簡手機設計</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">過去</div>
                <div class="timeline-title">Light Phone 系列</div>
                <div class="timeline-desc">陸續推出 Light Phone、Light Phone 2、Light Phone 3，主打無 App 極簡體驗</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月</div>
                <div class="timeline-title">Light Flip 發布</div>
                <div class="timeline-desc">全新折疊手機，299 美元，結合 T9 輸入法與極簡美學</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">上市時</div>
                <div class="timeline-title">「翻轉生活」計畫</div>
                <div class="timeline-desc">九個月計畫協助用戶逐步脫離智慧手機依賴</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">市場持續擴展</div>
                <div class="timeline-desc">以更親民價格吸引追求數位健康的消費者</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>對比項目</th>
                    <th>Light Flip</th>
                    <th>Light Phone 3</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>售價</td>
                    <td class="highlight-col">299 美元</td>
                    <td>較高</td>
                </tr>
                <tr>
                    <td>月費</td>
                    <td class="highlight-col">39 美元</td>
                    <td>較高</td>
                </tr>
                <tr>
                    <td>重量</td>
                    <td>160 克</td>
                    <td class="highlight-col">124 克</td>
                </tr>
                <tr>
                    <td>機身</td>
                    <td class="highlight-col">折疊式</td>
                    <td>直板式</td>
                </tr>
                <tr>
                    <td>輸入法</td>
                    <td class="highlight-col">T9 數字鍵</td>
                    <td>觸控螢幕</td>
                </tr>
                <tr>
                    <td>極簡程度</td>
                    <td class="highlight-col">更極簡</td>
                    <td>相對豐富</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'Light 推出 299 美元折疊手機：無 App、主打 T9 輸入法，目標是讓人重新連接 | ZDNET',
    'h1':          'Light Flip<br>極簡折疊手機回歸',
    'subtitle':    '無 App、無電子郵件、只有 T9 輸入法——Light 推出 299 美元折疊手機，讓你重新專注於通話',
    'source_url':  'https://www.zdnet.com/article/light-flip-news/',
    'source_name': 'ZDNET',
    'pub_date':    '2026-07-25',
    'img_alt':     'Light Flip 折疊手機',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260725_112716',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print("❌ HTML 生成失敗")
    for err in errors:
        print(f"   - {err}")
