# Google 實驗性開放模型 DiffusionGemma，專用 GPU 上文字產生速度提高 4 倍

## 📖 新聞導語

Google 發表了一款實驗性開放模型 **DiffusionGemma**，採用擴散（Diffusion）方式而非逐字（word by word）形式來生成文字。在單一 GPU 以單一使用者模式運行時，速度最高可比傳統語言模型快上 4 倍，硬體最佳化作業由 NVIDIA 負責處理。

## 💡 核心內容

### 🔄 與傳統語言模型的不同
大多數語言模型會接續產生一個又一個 token，並以前一個 token 為基礎來產生新的 token（自回歸模型）。DiffusionGemma 則從 **256 個隨機占位 token 所組成的區塊**開始，透過多次迭代加以精煉，直到可讀的文字浮現為止。這個概念源自圖像 AI，以擴散方式將雜訊轉化為清晰圖像。

### ⚡ 速度提升的關鍵：更好的 GPU 使用率
在自回歸模型中，單一使用者的推理作業往往受到記憶體頻寬限制，GPU 的運算單元在大部分時間閒置等候資料（稱為 memory-bound）。DiffusionGemma 透過**平行處理最多 256 個 token** 的方式迴避這個問題，使 GPU 保持忙碌運作。

**NVIDIA 效能數據**：
- H100 GPU：每秒約 1,000 個 token
- DGX Station：每秒 800 個 token
- DGX Spark：每秒 150 個 token
- GeForce RTX 5090：每秒超過 700 個 token

### 🧠 模型架構
DiffusionGemma 建構在 Gemma 4 系列之上，共有 **260 億參數**，但每一步驟僅啟用 38 億參數。這要歸功於**混合專家（Mixture of Experts，MoE）架構**，僅由合適的專門子網路依輸入內容啟動。量化至較低精度版本後，可在高階消費級 GPU 以 **18GB VRAM** 運行。

### ⚠️ 速度換品質的取捨
DiffusionGemma 以輸出品質換取速度提升，Google 仍建議在最重視品質的情境下使用一般 Gemma 4 模型。DiffusionGemma 定位為供研究人員和開發者用於實驗地端、快速工作流程的工具。

### 💡 真正的優勢：非順序任務
DiffusionGemma 每個 token 都能參考區塊內任何其他 token（不同於傳統語言模型只能向前回溯），因此適合：
- 將文字插入既有段落
- 填補程式碼中的空缺
- 處理胺基酸序列和數學圖形等結構化資料

### ☁️ 雲端效能反而較差
在雲端服務、面對大量平行請求的情境下，優勢會被反轉。自回歸模型在這類情境本來就能讓硬體保持忙碌，因此 DiffusionGemma 反而可能會推升成本。

## 🔮 業界展望

DiffusionGemma 的發布顯示，擴散模型技術正從圖像領域擴展至文字生成。隨著 NVIDIA 為 RTX 5090、RTX 4090 以及 Hopper 和 Blackwell 架構進行優化，地端 AI 推理的效能競賽將進入新階段。這種以速度換取 GPU 效率的模式，可能為需要快速生成結果的應用場景（如程式碼補全、資料處理）開闢新道路。

---

**📌 資料來源**：科技新報 TechNews（2026-06-12）
**📅 發布日期**：2026-06-12
**🔗 新聞連結**：https://technews.tw/2026/06/11/google-introduces-diffusiongemma/