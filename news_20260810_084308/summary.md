# Meta Muse Glimmer brings local AI agents to consumer GPUs

## 📖 新聞導語

Meta 發布 Muse Glimmer，這是一款 300 億參數的多模態模型，可在一張消費級 GPU 上本地運行，並以 Apache 2.0 許可開源釋出。

## 💡 核心內容

### 300 億參數模型，單卡可跑
Muse Glimmer 是從 Muse Spark 蒸餾而來的多模態模型，僅需一張消費級 GPU（如 RTX 3090/4090 等具備 24GB 以上 VRAM）即可運行。開發者可用於本地編程、函數調用、本地代理，以及 LLM-as-a-judge 評估。

### Apache 2.0 開源，Weights 已上傳 Hugging Face
Meta 的 Superintelligence Labs 將模型權重公開在 Hugging Face，採用 Apache 2.0 許可，允許商業使用。這代表任何人都可以下載、在本地部署，無需雲端 API 費用。

### 基準測試表現亮眼
在多項基準測試中，Muse Glimmer 與同規模模型（Gemma4-31B、Qwen3.6-27B）相比表現相當：
- **AIME 2026**：94.7 分（領先 Qwen3.6-27B 的 94.1）
- **AA-LCR**：80.0 分（領先 Gemma4-31B 的 68.3）
- **Beam 128K**：65.1 分（領先 Qwen3.6-27B 的 63.0）
- **GPQA Diamond**：83.5 分

### 本地部署的硬體限制
模型需要至少 **24GB VRAM**，這對消費級 GPU 來說是個不低的門檻，但相較於需要多卡集群的模型已大幅降低門檻。

## 🔮 業界展望

Muse Glimmer 代表了本地 AI 代理的重大一步——將強大的多模態能力帶入消費級硬體。隨著開源和本地化趨勢，邊緣 AI 的應用場景將持續擴展，開發者可在無需依賴雲端的情況下構建智能代理系統。

---

**📌 資料來源**：Artificial Intelligence News
**📅 發布日期**：2026-08-10
**🔗 原文連結**：https://www.artificialintelligence-news.com/news/meta-muse-glimmer-local-ai-agents-consumer-gpus/
