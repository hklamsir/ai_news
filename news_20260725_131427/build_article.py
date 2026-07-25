#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.ithome.com.tw/news/177586" target="_blank">ITHOME</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-24</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
            <p><strong>📝 作者</strong>：蘇文彬</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>AMD 董事長蘇姿丰在年度 Advancing AI 活動中揭示：全球 AI 算力已有一半以上用於推論，代表 AI 正從模型訓練轉向實際部署階段。Agentic AI 的崛起正在重新拉升 CPU 需求，其成長速度甚至超越 GPU，2030 年全球 AI 加速器市場規模將上看 1.4 兆美元。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🤖</div>
            <div class="tech-card-content">
                <h4>AI從訓練轉向推論部署</h4>
                <p>全球 AI 運算首次有超過一半投入推論，而非模型訓練。生成式 AI 發展初期市場競爭多集中在建立更大模型，但隨著企業開始大規模部署 AI 服務，推論已逐漸成為主要工作負載，代表 AI 正從研發階段走向實際應用。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🧠</div>
            <div class="tech-card-content">
                <h4>Agentic AI重新定義CPU角色</h4>
                <p>Agent 不只是回答問題，而是能持續執行一連串工作。除需要 GPU 完成模型推論外，也需要 CPU 負責執行程式碼、管理記憶體與系統狀態、呼叫 API、存取資料庫，以及協調多個工具與工作流程。蘇姿丰表示，非推論工作負載快速增加，使 CPU 需求成長速度甚至超過 GPU。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🏗️</div>
            <div class="tech-card-content">
                <h4>AMD三層AI資料中心架構</h4>
                <p>AMD 提出三層 AI 資料中心架構：第一層 AI Host Node（驅動 GPU）、第二層 Agent Sandbox（執行 Agent、協調工具呼叫）、第三層通用伺服器（執行資料庫及企業應用）。對應推出三種 EPYC Venice 處理器版本：GPU Host 高時脈版本、Agent 部署 256 核心版本、企業應用 128 核心版本。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💻</div>
            <div class="tech-card-content">
                <h4>Helios機櫃：與OpenAI、Meta共同開發</h4>
                <p>Helios 機櫃整合 MI455 GPU、EPYC Venice 處理器、Pensando 網路及 ROCm 軟體平台，在產品設計初期便與 OpenAI、Meta 及 Anthropic 共同開發（co-develop）。蘇姿丰表示，未來 AI 資料中心的競爭是整體系統整合能力，而非只是 GPU 效能。</p>
            </div>
        </div>


        <div class="highlight-box">
            <h4>📌 重點數據</h4>
            <ul>
                <li><strong>AI推論占比：</strong>全球 AI 算力已有一半以上用於推論</li>
                <li><strong>CPU需求增速：</strong>超越 GPU</li>
                <li><strong>2030年 AI 加速器市場：</strong>上看 1.4 兆美元</li>
                <li><strong>EPYC Venice：</strong>最高 256 核心（Agent 部署專用）</li>
            </ul>
        </div>

        <div class="quote-box">
            <p>「GPU 與 AI 加速器的需求確實十分強勁，但是從市場規模的成長速度來看，CPU 其實更快。AI 仍處於非常早期的階段，每幾個月就會出現新的重大突破。」</p>
            <cite>— 蘇姿丰，AMD 董事長暨執行長</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>AI 從模型訓練走向推論部署，是產業成熟的重要標誌。Agentic AI 的崛起預示了下一波成長方向——能自主規劃、執行複雜任務的 AI 代理。這種轉變重新定義了資料中心的運算架構，CPU 的重要性被重新審視。AMD 提出的三層架構反映晶片廠商對未來 AI 基礎設施的佈局思路，從單一晶片走向整體系統整合。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">生成式 AI 初期</div>
                <div class="timeline-title">模型訓練為主</div>
                <div class="timeline-desc">市場競爭多集中在建立更大模型，GPU 需求飆升</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年</div>
                <div class="timeline-title">轉折點來臨</div>
                <div class="timeline-desc">全球 AI 運算首次有超過一半投入推論</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">Agentic AI 興起</div>
                <div class="timeline-title">CPU 需求回升</div>
                <div class="timeline-desc">非推論工作負載增加，CPU 需求增速超越 GPU</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">AMD 發布</div>
                <div class="timeline-title">三層架構 + Helios</div>
                <div class="timeline-desc">EPYC Venice 處理器 + Helios 機櫃，與 OpenAI、Meta 共同開發</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2030 年</div>
                <div class="timeline-title">市場規模願景</div>
                <div class="timeline-desc">全球 AI 加速器市場規模將提高至 1.4 兆美元</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>對比維度</th>
                    <th>傳統 AI 部署</th>
                    <th>Agentic AI 時代</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>主要工作負載</td>
                    <td>模型訓練 + 簡單推論</td>
                    <td class="highlight-col">複雜推論 + 任務執行</td>
                </tr>
                <tr>
                    <td>GPU 角色</td>
                    <td>核心運算單元</td>
                    <td>模型推論專用加速</td>
                </tr>
                <tr>
                    <td>CPU 角色</td>
                    <td>輔助管理</td>
                    <td class="highlight-col">任務協調、程式執行、記憶體管理</td>
                </tr>
                <tr>
                    <td>資料中心架構</td>
                    <td>GPU 為中心</td>
                    <td class="highlight-col">三層分工（Host / Agent Sandbox / 通用）</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'AMD：AI運算重心轉向推論，蘇姿丰：CPU需求增速甚至超越GPU | ITHOME',
    'h1':          '蘇姿丰：AI轉向推論<br>CPU需求增速超越GPU',
    'subtitle':    '全球AI算力已有一半投入推論，Agentic AI崛起重新定義資料中心三層架構',
    'source_url':  'https://www.ithome.com.tw/news/177586',
    'source_name': 'ITHOME',
    'pub_date':    '2026-07-24',
    'img_alt':     'AMD EPYC 處理器與資料中心',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260725_131427',
    article_content=article_content,
    metadata=metadata
)

if success:
    print("✅ HTML 生成成功")
else:
    print("❌ HTML 生成失敗")
    for err in errors:
        print(f"   - {err}")
