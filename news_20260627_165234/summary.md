# This Retail GPU Works Great for Local AI! - Lon.TV 評測

## 📖 新聞導語

Lon.TV 評測一款華碩 16GB VRAM 顯示卡，搭配 OCuLink Thunderbolt 擴充座與迷你電腦，實測用 LM Studio 運行 Gemma 4 260 億參數專家混合模型。本地 AI 速度可達每秒 30-40 個 Token，效能接近雲端訂閱，但所有資料完全保存在本地。

## 💡 核心內容

### 硬體配置：16GB VRAM 顯卡 + OCuLink 擴充座

評測使用華碩顯示卡（16GB VRAM，售價不到 600 美元）搭配 GT Box OCuLink Thunderbolt 擴充座和 GMK Tech 迷你電腦（64GB 記憶體）。選擇這張卡的主因是其 16GB 顯存足以容納 Gemma 4 26B 專家混合模型。

### LM Studio：免費多平台本地 AI 工具

評測主要使用 **LM Studio**，這是一款免費應用程式，可跨平台運行各類本地 AI 模型。重點功能：
- 一鍵下載和載入模型
- GPU/系統記憶體混合分配（如 GPU VRAM 不夠，可將部分模型放在系統記憶體）
- 內建模型搜尋，支援 Qwen、Google Gemma、Nvidia 等多種模型

### 效能實測：Gemma 4 26B

| 情境 | 速度 |
|------|------|
| 16GB VRAM 完整載入 | 約 30-40 tokens/s |
| 8GB VRAM + 系統記憶體 | 約 5 tokens/s |
| 8B 模型（8GB VRAM） | 還算不錯的結果 |

### 文件分析功能（類 Notebook LM）

測試文件分析功能（類似 Google Notebook LM）：
- 可上傳 PDF 文件並建立索引
- 提問可得到具體答案（如法規金額計算）
- **限制**：需要非常具體的問題才能得到正確答案，模糊問題表現較差
- **結論**：無法完全取代 Notebook LM，但能做很多類似的事情，且所有資料完全保存在本地

### 功耗監控

在生成文字時可即時監控 GPU 功耗，記者對本地 AI 的功耗效率表示驚訝。

## 🔮 業界展望

本地 AI 模型現在真的很有用，不只是「G Wiz」概念。如果電腦有足夠記憶體或 8GB 以上顯存，建議下載 LM Studio 親自體驗。隨著模型推理能力持續提升，本地 AI 有望成為雲端之外的另一個選擇。

---

**📌 資料來源**：YouTube（Lon.TV）
**📅 發布日期**：2026-06-27
**🔗 影片連結**：https://youtu.be/oyBRlKm14zw
