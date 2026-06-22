import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://unwire.hk/2026/06/21/nvidia-nemotron-35-asr-streaming-40-languages/ai/" target="_blank">UNWIRE</a></p>
            <p><strong>📅 發布日期</strong>：2026-06-21</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>NVIDIA 推出 Nemotron 3.5 ASR，僅 6 億參數即可支援 40 種語言的本地串流語音辨識，最低延遲僅 80ms，詞錯率（WER）更低於 Whisper large-v3-turbo，且可用 CPU 運行，為資源受限環境的即時語音轉換提供全新選擇。</p>

        <div class="tech-card">
            <div class="tech-card-icon">⚙️</div>
            <div class="tech-card-content">
                <h4>模型架構</h4>
                <p>Nemotron 3.5 ASR 採用 Cache-Aware FastConformer-RNNT 架構，由 24 層 FastConformer 編碼器搭配 RNNT 解碼器組成，每個音訊幀只需處理一次。透過「語言 ID 提示」機制，單一模型處理 40 種語言語音轉錄，毋需為每種語言準備獨立模型。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🌍</div>
            <div class="tech-card-content">
                <h4>40 種語言三層級支援</h4>
                <p><strong>即用型（19 種）</strong>：英文、西班牙文、法文、德文、日文、韓文、中文、阿拉伯文、印地文等<br>
                <strong>廣泛覆蓋（13 種）</strong>：波蘭文、瑞典文、捷克文、挪威文等歐洲語言<br>
                <strong>適配型（8 種）</strong>：分詞器已支援但需針對特定領域資料微調</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">⏱️</div>
            <div class="tech-card-content">
                <h4>可調延遲模式</h4>
                <p>透過 <code>att_context_size</code> 參數調整延遲與準確率平衡：<br>
                80ms 超低延遲（適合即時互動）｜ 160ms 低延遲｜ 560ms 平衡模式（預設）｜ 1,120ms 最高準確率</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">📊</div>
            <div class="tech-card-content">
                <h4>對比 Whisper：更小、更快、更準</h4>
                <p>Nemotron 0.6B 平均 WER 為 7.07%，低於 Whisper large-v3-turbo 的 7.83%。在 L40S GPU 上延遲僅 43ms，較 Whisper medium 的 916ms 快達 <strong>21 倍</strong>。但 Whisper 在嘈雜環境及帶口音音訊上穩健性較強。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 關鍵規格</h4>
            <p>參數量：<strong>600M</strong>｜ 支援語言：<strong>40 種</strong>｜ 最低延遲：<strong>80ms</strong>｜ 平均 WER：<strong>7.07%</strong>｜ CPU 運行：<strong>支援</strong></p>
        </div>

        <div class="quote-box">
            <p>「資源受限硬件上即時串流 ASR 最強候選模型」</p>
            <cite>— Microsoft Research 基準測試結論</cite>
        </div>

        <h3>✨ 內置功能</h3>
        <p><strong>Word Boosting</strong>：自訂優先辨識詞彙，毋需重新訓練模型，適合醫療及科技等專業領域。<br>
        <strong>Speaker Diarization</strong>：辨識並區分不同說話者，適合會議及播客等多語境。<br>
        <strong>自動標點與大寫</strong>：輸出文字自帶標點符號及正確大寫，省卻額外處理步驟。</p>

        <h3>📥 部署與授權</h3>
        <p>Nemotron 3.5 ASR 以 <strong>OpenMDW-1.1</strong> 開源授權，模型權重已上架 HuggingFace，可直接用於商業用途。支援 NeMo 框架、OpenAI 相容 HTTP 伺服器、NVIDIA NIM 雲端服務及標準 HuggingFace Transformers 流程。即時語音平台 LiveKit 亦提供整合指南。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">早期</div>
                <div class="timeline-title">nemotron-speech-streaming-en-0.6b</div>
                <div class="timeline-desc">NVIDIA 推出英文串流版本，600M 參數即实现高性能</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">2026 年 6 月</div>
                <div class="timeline-title">Nemotron 3.5 ASR 發布</div>
                <div class="timeline-desc">多語言擴充版發布，支援 40 種語言，OPENMDW-1.1 授權</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">發布同期</div>
                <div class="timeline-title">LiveKit 整合指南</div>
                <div class="timeline-desc">即時語音平台 LiveKit 發布詳細整合指南</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">進行中</div>
                <div class="timeline-title">大型基準測試</div>
                <div class="timeline-desc">Microsoft Research 對逾 50 個配置進行測試，Nemotron 被評為最佳候選</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">當前</div>
                <div class="timeline-title">HuggingFace 上架</div>
                <div class="timeline-desc">模型權重已上架，可直接下載用於商業用途</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>比較項目</th>
                    <th>Nemotron 3.5 ASR 0.6B</th>
                    <th>Whisper large-v3-turbo</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>參數量</td>
                    <td class="highlight-col">600M</td>
                    <td>809M</td>
                </tr>
                <tr>
                    <td>架構</td>
                    <td class="highlight-col">FastConformer-RNNT（串流優先）</td>
                    <td>Encoder-Decoder（批次優先）</td>
                </tr>
                <tr>
                    <td>平均 WER</td>
                    <td class="highlight-col">7.07%</td>
                    <td>7.83%</td>
                </tr>
                <tr>
                    <td>最低延遲</td>
                    <td class="highlight-col">80ms</td>
                    <td>不適用（批次處理）</td>
                </tr>
                <tr>
                    <td>CPU 運行</td>
                    <td class="highlight-col">支援</td>
                    <td>較慢</td>
                </tr>
                <tr>
                    <td>多語言支援</td>
                    <td class="highlight-col">40 種（單一模型）</td>
                    <td>99 種（多模型）</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title':       'NVIDIA Nemotron 3.5 ASR：6 億參數支援 40 語言、80ms 低延遲語音辨識',
    'h1':          'NVIDIA Nemotron 3.5 ASR<br>6 億參數挑戰 Whisper',
    'subtitle':    '支援 40 種語言、WER 7.07%、延遲最低 80ms，可用 CPU 運行的本地串流語音辨識模型',
    'source_url':  'https://unwire.hk/2026/06/21/nvidia-nemotron-35-asr-streaming-40-languages/ai/',
    'source_name': 'UNWIRE',
    'pub_date':    '2026-06-21',
    'img_alt':     'NVIDIA Nemotron 3.5 ASR 語音辨識模型示意圖，音頻波形轉換文字，支援多語言',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260622_131318',
    article_content=article_content,
    metadata=metadata
)

print(f"Success: {success}")
if errors:
    print(f"Errors: {errors}")
