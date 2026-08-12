#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.artificialintelligence-news.com/news/meta-muse-glimmer-local-ai-agents-consumer-gpus/" target="_blank">Artificial Intelligence News</a></p>
            <p><strong>📅 發布日期</strong>：2026-08-10</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>Meta 發布 <strong>Muse Glimmer</strong>，一款 300 億參數的多模態開源模型，可在單張消費級 GPU（24GB+ VRAM）上本地運行，標誌著本地 AI 代理的重大突破。</p>

        <div class="tech-card">
            <div class="tech-card-icon">🧠</div>
            <div class="tech-card-content">
                <h4>300 億參數，單卡可跑</h4>
                <p>Muse Glimmer 是從 Meta 自家 <strong>Muse Spark</strong> 蒸餾而來的多模態模型，僅需一張消費級 GPU（如 RTX 3090/4090 等具備 24GB 以上 VRAM）即可運行，大幅降低本地部署門檻。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔓</div>
            <div class="tech-card-content">
                <h4>Apache 2.0 開源，Weights 已上 Hugging Face</h4>
                <p>Meta Superintelligence Labs 將模型權重公開在 Hugging Face，採用 <strong>Apache 2.0 許可</strong>，允許商業使用。開發者可自由下載、本地部署，無需雲端 API 費用。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💻</div>
            <div class="tech-card-content">
                <h4>本地應用場景</h4>
                <p>可用於：<strong>本地編程</strong>、<strong>函數調用</strong>、<strong>本地代理</strong>、以及 <strong>LLM-as-a-judge</strong> 評估。完全離線運行，無需數據上傳雲端。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>基準測試表現亮眼</h4>
                <p>與同規模模型 Gemma4-31B、Qwen3.6-27B 相比毫不遜色：<br>
                AIME 2026 <strong>94.7</strong>（Qwen 94.1）｜AA-LCR <strong>80.0</strong>（Gemma4 68.3）｜Beam 128K <strong>65.1</strong>（Qwen 63.0）</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>Muse Glimmer 的硬體需求為<strong>至少 24GB VRAM</strong>，這對消費級 GPU 而言門檻不低，但相較需要多卡集群的模型已大幅降低，讓個人開發者也能運行強大的本地 AI 代理。</p>
        </div>

        <div class="quote-box">
            <p>「Meta is releasing Muse Glimmer under an Apache 2.0 licence for local AI agents that can run on a consumer GPU.」</p>
            <cite>— Ryan Daws, Artificial Intelligence News</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>Muse Glimmer 代表了本地 AI 代理的重大突破——將強大的多模態能力帶入消費級硬體。隨著開源和本地化趨勢持續，邊緣 AI 的應用場景將大幅擴展。開發者可在無需依賴雲端的情況下，構建完全私密的智能代理系統，這對企業和重視隱私的用戶尤為重要。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">2026-08-10</div>
                <div class="timeline-title">Muse Glimmer 發布</div>
                <div class="timeline-desc">Meta 正式發布 300 億參數多模態模型，開源 Apache 2.0</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">模型規格</div>
                <div class="timeline-title">300 億參數</div>
                <div class="timeline-desc">從 Muse Spark 蒸餾而來，多模態能力支援</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">硬體需求</div>
                <div class="timeline-title">24GB+ VRAM</div>
                <div class="timeline-desc">單張消費級 GPU 即可運行（如 RTX 3090/4090）</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">開源許可</div>
                <div class="timeline-title">Apache 2.0</div>
                <div class="timeline-desc">可商用，完全開源，Weights 在 Hugging Face</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">應用場景</div>
                <div class="timeline-title">本地編程 + 代理</div>
                <div class="timeline-desc">本地編程、函數調用、代理系統、LLM-as-a-judge</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>基準測試</th>
                    <th>Muse Glimmer</th>
                    <th>Qwen3.6-27B</th>
                    <th>Gemma4-31B</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>AIME 2026</td>
                    <td class="highlight-col">94.7 ✅</td>
                    <td>94.1</td>
                    <td>89.2</td>
                </tr>
                <tr>
                    <td>AA-LCR</td>
                    <td class="highlight-col">80.0 ✅</td>
                    <td>73.3</td>
                    <td>68.3</td>
                </tr>
                <tr>
                    <td>Beam 128K</td>
                    <td class="highlight-col">65.1 ✅</td>
                    <td>63.0</td>
                    <td>58.2</td>
                </tr>
                <tr>
                    <td>GPQA Diamond</td>
                    <td>83.5</td>
                    <td>84.2</td>
                    <td class="highlight-col">85.7 ✅</td>
                </tr>
                <tr>
                    <td>Humanity's Last Exam</td>
                    <td>22.0</td>
                    <td>—</td>
                    <td class="highlight-col">23.6 ✅</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'Meta Muse Glimmer brings local AI agents to consumer GPUs',
    'h1': 'Meta Muse Glimmer：<br>本地 AI 代理<br>進入消費級 GPU 時代',
    'subtitle': '300 億參數開源模型，單卡可跑，Apache 2.0 商業可用',
    'source_url': 'https://www.artificialintelligence-news.com/news/meta-muse-glimmer-local-ai-agents-consumer-gpus/',
    'source_name': 'Artificial Intelligence News',
    'pub_date': '2026-08-10',
    'img_alt': 'Meta Muse Glimmer 本地 AI 模型在消費級 GPU 上運行示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260810_084308',
    article_content=article_content,
    metadata=metadata
)

print(f"組裝結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    for e in errors:
        print(f"  錯誤：{e}")
