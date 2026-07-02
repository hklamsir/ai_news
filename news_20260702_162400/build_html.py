#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://inews.hket.com/article/4150499/" target="_blank">香港經濟日報 iNews</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-02</p>
            <p><strong>✍️ 作者</strong>：李曉廬（麥肯錫全球董事合夥人）</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>AI 的顛覆性正由企業核心業務區域釋放價值，而非邊緣地帶。未來 3 至 5 年，懂得由核心業務流程開始思考 AI 發展的企業將成為行業領跑者。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>人機協作創新時代</h4>
                <p>未來的工作不再單靠人來定義，而是建立在人、AI 智能體（Agents）和機器人之間的動態協作上。企業主管部署策略時，不能只著眼於將當下任務自動化，更要從根本上重塑未來的工作流程與崗位職能。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💰</div>
            <div class="tech-card-content">
                <h4>以兆美元計的關鍵業務</h4>
                <p>人機協作在全球的總經濟機遇每年可高達 <strong>25 兆美元</strong>。單是美國，預期人機協作到 2030 年可釋放高達 <strong>2.9 兆美元</strong>的價值，其中約 <strong>1.8 兆美元</strong>的價值在核心營運中，而非邊緣業務。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📈</div>
            <div class="tech-card-content">
                <h4>熟練運用 AI 成必備技能</h4>
                <p>市場對 AI 熟練度的需求增長速度超過任何其他技能，能有效使用和管理 AI 工具的能力需求在短短兩年內飆升了 <strong>7 倍</strong>。組織若仍將 AI 學習與發展視為選項，將日益凸顯結構性劣勢。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🎯</div>
            <div class="tech-card-content">
                <h4>良好領導可放大效益</h4>
                <p>企業領袖需在各個層級展現清晰、堅定的領導能力，具備匯聚人類、AI 智能體和機器人的能力，組織混合團隊以訓練、協調和驅動業績。要成就戰略優勢就不能將發展直接丟給技術團隊。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>下一階段 AI 競爭的關鍵不在於誰能製造最快的晶片，而在於誰能構建最具連接性的生態系統。「我們要停止競爭，開始通力合作。」—— 企業需從閉門造車轉向生態建設。</p>
        </div>

        <div class="quote-box">
            <p>「無論是否科技產業參與者，對所有企業領導者尤關重要的觀點是：AI的顛覆性是由業務的核心區域釋放價值，而非單單在邊緣地帶發揮。」</p>
            <cite>— 李曉廬，麥肯錫全球董事合夥人</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>在 Computex 2026 上，業界正構建 AI 物理基礎設施，行業領袖則致力站在定義 AI 應用的最前線。面對 AI 的關鍵轉折點，懂得由核心業務流程開始思考 AI 發展的企業，在 3 至 5 年後將可成為行業領跑者。AI 生態會是未來關鍵，由核心到邊緣，連結一起才是重點。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">AI 1.0 時代</div>
                <div class="timeline-title">簡單自動化</div>
                <div class="timeline-desc">AI 在邊緣地帶發揮，輔助單一任務</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">AI 2.0 時代</div>
                <div class="timeline-title">組織變革</div>
                <div class="timeline-desc">生成式 AI 滲透核心營運，重塑企業戰略</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2030 年</div>
                <div class="timeline-title">美國人機協作效益</div>
                <div class="timeline-desc">預期釋放 2.9 兆美元價值</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">3-5 年後</div>
                <div class="timeline-title">行業領跑者誕生</div>
                <div class="timeline-desc">懂核心流程 AI 發展的企業崛起</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">生態系統競爭</div>
                <div class="timeline-desc">由晶片競爭轉向生態連接性競爭</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>維度</th>
                    <th>AI 1.0（邊緣）</th>
                    <th>AI 2.0（核心）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>主要任務</td>
                    <td>單一任務自動化</td>
                    <td class="highlight-col">重塑工作流程與崗位職能</td>
                </tr>
                <tr>
                    <td>經濟價值</td>
                    <td>1.1 兆美元（邊緣）</td>
                    <td class="highlight-col">1.8 兆美元（核心）</td>
                </tr>
                <tr>
                    <td>團隊構成</td>
                    <td>人類為主</td>
                    <td class="highlight-col">人 + AI 智能體 + 機器人混合</td>
                </tr>
                <tr>
                    <td>領導角色</td>
                    <td>技術團隊主導</td>
                    <td class="highlight-col">企業領袖統籌各層級</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'AI撼動企業核心流程 | 麥肯錫 Computex 揭示行業4大發展關鍵',
    'h1':          'AI撼動企業核心流程<br>麥肯錫 Computex 揭示4大發展關鍵',
    'subtitle':    '麥肯錫：人機協作經濟機遇達每年25兆美元，企業核心地帶才是轉型勝敗關鍵',
    'source_url':  'https://inews.hket.com/article/4150499/',
    'source_name': '香港經濟日報 iNews',
    'pub_date':    '2026-07-02',
    'img_alt':     'AI 撼動企業核心流程 - Computex 2026 科技展覽示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260702_162400',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print(f"❌ HTML 組裝失敗：{errors}")
    sys.exit(1)
