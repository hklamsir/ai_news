import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://mp.weixin.qq.com/s/Fz0uiczt7WNltxQbSmzWrA" target="_blank">嗜學（微信公眾號）</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-24</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>AMD 銳龍 AI Max PRO 400 系列核心升級是將記憶體上限提升至 <strong>192GB</strong>，共享顯存可分配達 <strong>160GB</strong>，專為千億參數大模型本地運行、8K 渲染、工業仿真等高負載 AI 任務而生。</p>

        <div class="tech-card">
            <div class="tech-card-icon">💾</div>
            <div class="tech-card-content">
                <h4>記憶體容量大革命</h4>
                <p>最大記憶體支援從 128GB 提升至 <strong>192GB</strong>，共享顯存最高可分配 <strong>160GB</strong> 供顯卡調用。統一記憶體架構打破傳統記憶體/顯存壁壘，顯卡可靈活調用大容量記憶體參與運算。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚙️</div>
            <div class="tech-card-content">
                <h4>三款型號完整覆蓋</h4>
                <p><strong>Max+ PRO 495</strong>（旗艦）：16 核 CPU + 40CU GPU，完整本地運行千億級大模型<br>
                <strong>Max PRO 490</strong>（中階）：12 核 CPU + 32CU GPU，算力與功耗均衡<br>
                <strong>Max PRO 485</strong>（入門）：8 核 CPU + 32CU GPU，降低專業 AI 硬體門檻</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🛠️</div>
            <div class="tech-card-content">
                <h4>ROCm 7.14 生態提前適配</h4>
                <p>AMD 提前完成 ROCm 7.14 開源計算平台適配，確保新品上市時開發者即可獲得完整軟體兼容性，用戶拿到設備即可直接開展專業運算，無需等待後續驅動補丁。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏢</div>
            <div class="tech-card-content">
                <h4>OEM 夥伴第三季度上市</h4>
                <p>華碩、惠普、聯想均計劃於 2026 年第三季度推出搭載銳龍 AI Max PRO 400 系列的終端設備，覆蓋企業 AI 研發、影視渲染、工業仿真等專業場景。</p>
            </div>
        </div>


        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>192GB 統一記憶體為高階本地 AI 運算提供充足硬體基礎，解決專業設備的記憶體性能瓶頸。AMD 將 400 系列限定於專業 PRO 賽道，與消費級 300 系列做出清晰區隔。</p>
        </div>

        <div class="quote-box">
            <p>「新品發售初期，開發者就能擁有完整、穩定的軟體兼容性，用戶拿到設備即可直接開展專業運算。」</p>
            <cite>— AMD ROCm 團隊</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>端側 AI 應用正快速普及，本地大模型部署、離線 AI 繪圖、批量數據分析等專業工作對設備記憶體需求持續走高。銳龍 AI Max PRO 400 系列的 192GB 統一記憶體架構，将成為 AI 研發、本地離線大模型運算等專業領域的重要硬體支撐。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 COMPUTEX</div>
                <div class="timeline-title">AMD 公布 400 系列</div>
                <div class="timeline-desc">AMD 於台北國際電腦展公布銳龍 AI 專業 400 系列處理器</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 7 月中旬</div>
                <div class="timeline-title">ROCm 7.14 發布</div>
                <div class="timeline-desc">AMD 更新 ROCm 7.14，新增 400 系列處理器適配支援</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 Q3（規劃）</div>
                <div class="timeline-title">OEM 設備上市</div>
                <div class="timeline-desc">華碩、惠普、聯想推出搭載 400 系列的終端產品</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">上代（300 系列）</div>
                <div class="timeline-title">128GB 記憶體上限</div>
                <div class="timeline-desc">傳統消費級 AI 設備記憶體上限，處理千億參數模型時易出現記憶體溢位</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">400 系列（新一代）</div>
                <div class="timeline-title">192GB 記憶體上限</div>
                <div class="timeline-desc">192GB 統一記憶體方案，共享顯存最高 160GB，大幅提升大模型承載能力</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>規格</th>
                    <th>銳龍 AI Max+ PRO 495</th>
                    <th>銳龍 AI Max PRO 490</th>
                    <th>銳龍 AI Max PRO 485</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>CPU 核心</td>
                    <td class="highlight-col">16 核 (Zen5)</td>
                    <td>12 核 (Zen5)</td>
                    <td>8 核 (Zen5)</td>
                </tr>
                <tr>
                    <td>GPU 計算單元</td>
                    <td class="highlight-col">40 CU (RDNA3.5)</td>
                    <td>32 CU (RDNA3.5)</td>
                    <td>32 CU (RDNA3.5)</td>
                </tr>
                <tr>
                    <td>最大記憶體</td>
                    <td class="highlight-col">192GB</td>
                    <td>192GB</td>
                    <td>192GB</td>
                </tr>
                <tr>
                    <td>可分配共享顯存</td>
                    <td class="highlight-col">160GB</td>
                    <td>160GB</td>
                    <td>160GB</td>
                </tr>
                <tr>
                    <td>目標用戶</td>
                    <td class="highlight-col">企業 AI 研發旗艦</td>
                    <td>中小型團隊/創作者</td>
                    <td>入門開發者</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'AMD 銳龍 AI Max PRO 400 專業處理器即將上市　192GB 記憶體挑戰 AI 運算極限',
    'h1':          'AMD 銳龍 AI Max PRO 400 專業處理器即將上市<br>192GB 記憶體挑戰 AI 運算極限',
    'subtitle':    '記憶體上限從 128GB 提升至 192GB，可分配 160GB 共享顯存，專為千億參數大模型本地運行而設計',
    'source_url':  'https://mp.weixin.qq.com/s/Fz0uiczt7WNltxQbSmzWrA',
    'source_name': '嗜學',
    'pub_date':    '2026-07-24',
    'img_alt':     'AMD 銳龍 AI Max PRO 400 處理器，192GB 統一記憶體架構',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260724_140800',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 組裝成功")
else:
    print(f"❌ 組裝失敗：{errors}")
