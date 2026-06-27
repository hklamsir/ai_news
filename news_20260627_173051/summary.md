# Intel Arc Pro B70 (32GB) for Local LLMs - llama.cpp & vLLM Benchmarks

## 📖 新聞導語

Donato Capitella 評測 Intel Arc Pro B70（32GB），這款專為本地 AI 工作負載設計的顯示卡。32GB VRAM 是運行 Qwen 3.6 等本地代理模型的最低門檻。本片深入硬體規格、llama.cpp 和 vLLM 效能表現，以及目前軟體支援的限制與展望。

## 💡 核心內容

### 硬體規格

Intel Arc Pro B70 基於 **Battlemage Xe2 架構**，採用 4nm 製程，配备 **32 Xe cores**。每個核心搭配 **Xe Matrix Extensions**（相當於 Nvidia 的 Tensor Cores 或 AMD 的 Matrix Cores），專門加速 LLM 工作負載中的矩陣運算。

支援格式：BF16（大部分現代模型的原生訓練格式）、FP8、INT8、INT4（對量化模型運行至關重要）。

| 規格 | Intel Arc Pro B70 | AMD Radeon R9 7900 AI Pro |
|------|------------------|--------------------------|
| VRAM | 32 GB GDDR6 | 32 GB GDDR6 |
| 記憶體頻寬 | 608 GB/s | 約 600 GB/s |

### 軟體生態：SYCL / Level Zero

Nvidia 有 CUDA，AMD 有 ROCm，Intel 的方案是 **SYCL + Level Zero**。llama.cpp 和 vLLM 要支援 Intel GPU，必須實作 SYCL backend。

Intel 維護的 **LLM Scaler** 專案是 vLLM 的分支，专门为 Intel 硬體優化 kernels，效能表現優異，但並非最新版 vLLM，且部分模型（如 Gemma 4）尚未支援。

### llama.cpp 效能

llama.cpp 的優勢是**統一生態系**：只要支援就能在任何 backend 運行。但缺點是 Intel GPU 支援優化不足：
- Vulkan backend：最大相容性
- SYCL backend：理論上效能更好但尚未充分優化
- **MTP（Multi-Token Prediction）** 在 SYCL backend 上表現不佳懷疑優化不足

### vLLM（LLM Scaler）效能

這是 Intel 的強項。Qwen 3.5 9B 模型在 B70 上達到 **2,236 tokens/s**，AMD R9 7900 遠遠落後。但 llama 3.1 8B 兩者表現相近（約 2,054 tokens/s）。

### 當前限制

- llama.cpp 對 Intel GPU 支援落後於 AMD
- LLM Scaler 分支非最新版，部分模型/GPU 未支援
- AWQ 量化尚未支援，GPTQ 可用
- CUDA graphs 尚不穩定，須以 eager mode 運行

## 🔮 業界展望

硬體本身有潛力與 AMD R9 7900 AI Pro 競爭，但軟體棧至關重要。期待未來數月 llama.cpp 對 Intel 的支援大幅改善，這將開通更廣大的模型生態系。如果社群有興趣，作者可能製作關於 ComfyUI 圖片/影片生成的專門影片。

---

**📌 資料來源**：YouTube（Donato Capitella）
**📅 發布日期**：2026-06-27
**🔗 影片連結**：https://youtu.be/MnGLqo5cuGQ
