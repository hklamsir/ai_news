# NVIDIA 推 0.6B 本地串流語音辨識模型 Nemotron 3.5 ASR 支援 40 種語言只要 CPU 就能運作

## 📖 新聞導語

NVIDIA 推出 Nemotron 3.5 ASR，僅 6 億參數即可支援 40 種語言的本地串流語音辨識，最低延遲僅 80ms，WER 更低於 Whisper large-v3-turbo，且可用 CPU 運行，為資源受限環境的即時語音轉換提供全新選擇。

## 💡 核心內容

### 🔧 模型架構
Nemotron 3.5 ASR 是 NVIDIA 繼英文串流版本 nemotron-speech-streaming-en-0.6b 的多語言擴充版，同樣採用 600M 參數。透過「語言 ID 提示」機制，單一模型處理 40 種語言語音轉錄，毋需為每種語言準備獨立模型。架構採用 Cache-Aware FastConformer-RNNT，由 24 層 FastConformer 編碼器搭配 RNNT 解碼器，每個音訊幀只需處理一次，有效降低計算量與延遲。

### 🌍 40 種語言三層級支援
- **即用型（19 種）**：英文、西班牙文、法文、德文、日文、韓文、中文、阿拉伯文、印地文等
- **廣泛覆蓋（13 種）**：波蘭文、瑞典文、捷克文、挪威文等歐洲語言
- **適配型（8 種）**：分詞器已支援但需針對特定領域資料微調

### ⏱️ 可調延遲模式
透過 `att_context_size` 參數調整延遲與準確率平衡：
- 80ms 超低延遲（適合即時互動）
- 160ms 低延遲
- 560ms 平衡模式（預設值）
- 1,120ms 最高準確率

### 📊 與 Whisper 比較
根據 Microsoft Research 超過 50 個配置的大型基準測試，Nemotron 0.6B 平均 WER 為 **7.07%**，低於 Whisper large-v3-turbo 的 **7.83%**。在 L40S GPU 上延遲僅 **43ms**，較 Whisper medium 的 916ms 快達 **21 倍**。但 Whisper 在嘈雜環境及帶口音音訊上穩健性較強。

### ✨ 內置功能
- **Word Boosting**：自訂優先辨識詞彙，毋需重新訓練
- **Speaker Diarization**：辨識並區分不同說話者
- **自動標點與大寫**：輸出文字自帶標點及正確大寫

### 📥 部署與授權
以 OpenMDW-1.1 開源授權，模型權重已上架 HuggingFace，可直接用於商業用途。支援 NeMo 框架、OpenAI 相容 HTTP 伺服器、NVIDIA NIM 雲端服務及標準 HuggingFace Transformers 流程。即時語音平台 LiveKit 亦提供整合指南。

## 🔮 業界展望

Nemotron 3.5 ASR 的出現，標誌著小型本地語音模型的成熟。在 Whisper 主导語音轉文字市場多年後，NVIDIA 以極低參數量實現更佳效能與更低延遲，且支援 CPU 運行，大幅降低部署門檻。對於需要在邊緣設備或資源受限環境中運行即時語音辨識的開發者而言，這是一個值得關注的選擇。

---

**📌 資料來源**：UNWIRE（NVIDIA / HuggingFace）
**📅 發布日期**：2026-06-21
**🔗 原文連結**：https://unwire.hk/2026/06/21/nvidia-nemotron-35-asr-streaming-40-languages/ai/
