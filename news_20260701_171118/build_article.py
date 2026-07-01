#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.bnext.com.tw/article/91380/meta-bans-claude-code-codex" target="_blank">BNEXT（鉅亨網）/ The Information</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-30 / 2026-07-01</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Meta 傳要求旗下 Applied AI 部門工程師全面禁用 Claude Code 與 Codex，主要擔心競爭對手模型的輸出內容，透過日常開發流程無意間混入自家 Llama 模型的訓練資料，形成「模型蒸餾」（Model Distillation）風險。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📋</div>
            <div class="tech-card-content">
                <h4>禁令詳情</h4>
                <p>Meta 要求 Applied AI 部門工程師禁用 Claude Code 與 Codex，相關規範最早可追溯至今年 5 月，6 月底正式實施。措施主要針對直接參與 AI 模型研發的工程師，而非全面適用於所有員工。截稿前 Meta 未發表公開評論。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔬</div>
            <div class="tech-card-content">
                <h4>什麼是模型蒸餾？</h4>
                <p>模型蒸餾是 AI 領域常見的訓練方法，利用能力較強的「教師模型」（Teacher Model）產生的輸出，協助訓練能力較弱的「學生模型」（Student Model）。Meta 擔心工程師使用競爭對手的 AI 開發工具後，建議的程式碼、架構、除錯邏輯等會逐步流入 Llama 訓練資料，最終讓競爭對手模型的能力被「蒸餾」至 Meta 自家模型。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⚠️</div>
            <div class="tech-card-content">
                <h4>智慧財產權風險</h4>
                <p>Meta 同時擔心工程師在使用 Claude Code 或 Codex 時，可能將公司內部的程式碼、產品設計或開發背景資訊傳送至 Anthropic 或 OpenAI 的伺服器，造成商業機密外洩。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📈</div>
            <div class="tech-card-content">
                <h4>市場背景</h4>
                <p>Claude Code 與 Codex 已成為許多軟體工程師進行 AI Agent 開發的主要工具，可協助規劃程式架構、撰寫程式碼、除錯及持續優化大型專案。Meta 股價在 6 月 29 日上漲 2.24% 至每股 562.60 美元，連續兩個交易日收紅，但今年以來跌幅達 13.50%。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Meta 的禁令並非全面適用於所有員工，而是僅針對 Applied AI 部門中直接參與 AI 模型研發的工程師。禁令目的是避免競爭對手 AI 模型的輸出內容，被直接或間接納入公司內部的 AI 開發流程。</p>
        </div>

        <div class="quote-box">
            <p>「隨著 AI 軍備競賽持續升溫，各家公司對內部 AI 工具的使用規範預料將更加嚴格，以避免技術外流或形成對競爭對手模型的依賴。」</p>
            <cite>— 分析人士，BNEXT 報導</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>分析指出，AI 大廠已將模型輸出、訓練資料與開發流程視為核心競爭資產，未來針對第三方 AI 工具的限制措施可能會進一步擴大。各家公司對內部 AI 工具的使用規範預料將更加嚴格，以避免技術外流或形成對競爭對手模型的依賴。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026 年 5 月</div>
                <div class="timeline-title">規範初稿形成</div>
                <div class="timeline-desc">Meta 內部文件顯示，相關禁令規範最早可追溯至今年 5 月</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月 29 日</div>
                <div class="timeline-title">消息曝光</div>
                <div class="timeline-desc">《The Information》取得 Meta 內部文件並報導此事件</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月 29 日</div>
                <div class="timeline-title">Meta 股價上漲</div>
                <div class="timeline-desc">Meta 股價上漲 2.24% 至每股 562.60 美元，連續兩個交易日收紅</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月底</div>
                <div class="timeline-title">禁令正式實施</div>
                <div class="timeline-desc">禁令於 6 月底正式實施，針對 Applied AI 部門工程師</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">未來</div>
                <div class="timeline-title">規範範圍可能擴大</div>
                <div class="timeline-desc">隨著 AI 軍備競賽升溫，各公司對內部 AI 工具的限制預計將更加嚴格</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>項目</th>
                    <th>Claude Code（Anthropic）</th>
                    <th>Codex（OpenAI）</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>開發商</td>
                    <td>Anthropic</td>
                    <td>OpenAI</td>
                </tr>
                <tr>
                    <td>主要功能</td>
                    <td>AI Agent 開發、程式架構規劃、程式碼撰寫、除錯</td>
                    <td>AI Agent 開發、程式碼生成、除錯、持續優化</td>
                </tr>
                <tr>
                    <td>Meta 禁令狀態</td>
                    <td class="highlight-col">禁止使用</td>
                    <td class="highlight-col">禁止使用</td>
                </tr>
                <tr>
                    <td>市場普及度</td>
                    <td>快速普及，訂閱成本相對低廉</td>
                    <td>快速普及，廣受軟體工程師採用</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'Meta不準工程師用Claude Code、Codex！擔心自家模型被「蒸餾」污染',
    'h1': 'Meta不準工程師用<br>Claude Code、Codex！',
    'subtitle': '擔心自家模型被「蒸餾」污染',
    'source_url': 'https://www.bnext.com.tw/article/91380/meta-bans-claude-code-codex',
    'source_name': 'BNEXT（鉅亨網）/ The Information',
    'pub_date': '2026-06-30 / 2026-07-01',
    'img_alt': 'Meta 禁止工程師使用 Claude Code、Codex示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260701_171118',
    article_content=article_content,
    metadata=metadata
)

print(f"\n結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")