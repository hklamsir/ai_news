#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://businessfocus.io/article/358641/" target="_blank">BusinessFocus</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-01</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>優必選旗下消費級品牌優世界（UWORLD）於6月30日正式發布U1系列人形機械人，男版高階機售價99萬元人民幣（約108萬港元），女版高階機售價88萬元人民幣（約96萬港元），主打「情感陪伴」而非傳統家務功能。消息一出優必選股價一度抽升近兩成，收市仍升逾7%，訂單已突破1.1萬台。</p>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>價格與定位</h4>
                <p>U1 Lite（輕量化半身版）11.98萬元人民幣（約13.1萬港元）；U1 Pro（全尺寸）16.98萬元人民幣（約18.5萬港元）；旗艦款U1 Ultra男版售價99萬元人民幣（約108萬港元），女版售價88萬元人民幣（約96萬港元）。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">❤️</div>
            <div class="tech-card-content">
                <h4>賣的是情緒支配權</h4>
                <p>產品賣點並非傳統家電式「做多少工作」，而是模仿人類親密關係中的回應、記憶、注視和依附感。名錶賣身份，豪車賣階層，AI伴侶賣的可能是「永不離開、永不頂嘴、永遠在線」的幻想。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📈</div>
            <div class="tech-card-content">
                <h4>資本市場反應熱烈</h4>
                <p>優必選股價在發布會當日下午一度抽升近兩成，收市仍升逾7%。訂單已突破1.1萬台，以最低售價計算銷售額已具備十億元級想像空間。對於2025年仍錄得約7.9億元人民幣虧損的優必選而言，消費級機械人若能跑出規模，估值框架或會被重新改寫。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>創辦人願景</h4>
                <p>優必選創始人周劍在發布會上表示：「機械人將替代手機，成為AI最核心的交互終端。」他更稱這一變化「將是劃時代的」。U1系列為全球唯一具備規模化量產能力的全尺寸超仿生產品。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>從理性角度看，近百萬港元的AI伴侶或許不值；但從消費心理看，優必選真正測試的是現代人願意用多少錢購買「可控親密感」——「永不離開、永不頂嘴、永遠在線」的幻想。</p>
        </div>

        <div class="quote-box">
            <p>「機械人將替代手機，成為AI最核心的交互終端，這一變化將是劃時代的。」</p>
            <cite>— 周劍，優必選創始人兼CEO</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>優必選U1系列力爭於今年內完成全部1.1萬台交付。男版身高約1.83米，女版身高約1.68米，配備88個自由度，支援眼神注視、對話互動、專屬記憶及外觀度身訂造。這款產品測試的不只是機械人市場，而是現代人對親密關係的消費態度。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月 30 日</div>
                <div class="timeline-title">U1 系列正式發布</div>
                <div class="timeline-desc">優必選旗下優世界（UWORLD）發布U1系列人形機械人</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">發布當日</div>
                <div class="timeline-title">股價一度抽升近兩成</div>
                <div class="timeline-desc">投資者對AI陪伴機械人概念反應熱烈，收市仍升逾7%</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">訂單突破</div>
                <div class="timeline-title">1.1 萬台</div>
                <div class="timeline-desc">全渠道訂單已突破1.1萬台，具備十億元級銷售額想像空間</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">預計交付</div>
                <div class="timeline-title">今年內完成</div>
                <div class="timeline-desc">優必選力爭於今年內完成全部1.1萬台機械人交付</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">公司財務</div>
                <div class="timeline-title">2025 年仍虧損</div>
                <div class="timeline-desc">優必選2025年收入20.01億元人民幣，虧損約7.9億元人民幣</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>型號</th>
                    <th>售價（人民幣）</th>
                    <th>售價（港元）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>U1 Lite（半身版）</td>
                    <td>11.98 萬元</td>
                    <td class="highlight-col">約 13.1 萬</td>
                </tr>
                <tr>
                    <td>U1 Pro（全尺寸）</td>
                    <td>16.98 萬元</td>
                    <td class="highlight-col">約 18.5 萬</td>
                </tr>
                <tr>
                    <td>U1 Ultra（女版）</td>
                    <td>88 萬元</td>
                    <td class="highlight-col">約 96 萬</td>
                </tr>
                <tr>
                    <td>U1 Ultra（男版）</td>
                    <td>99 萬元</td>
                    <td class="highlight-col">約 108 萬</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': '優必選U1機械伴侶賣100萬：AI陪伴是科技革命還是孤獨生意？',
    'h1': '優必選U1機械伴侶<br>賣100萬港元',
    'subtitle': 'AI陪伴是科技革命還是孤獨生意？',
    'source_url': 'https://businessfocus.io/article/358641/',
    'source_name': 'BusinessFocus',
    'pub_date': '2026-07-01',
    'img_alt': '優必選U1人形機械人伴侶示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260701_212200',
    article_content=article_content,
    metadata=metadata
)

print(f"\n結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")