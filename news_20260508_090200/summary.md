# Google Chrome 悄悄下載 4GB 檔案：用戶知情與否？刪除方法一次看

## 📖 新聞導語

**來源**：ZDNet　**發布日期**：2026-05-08

Google 正在向大量 Chrome 用戶的電腦悄悄下載一個 4GB 的大型檔案。這個名為 `weights.bin` 的檔案與 Gemini Nano 有關，是 Chrome 整合的設備端 AI 模型。部分用戶對此表示關注，因為檔案未經用戶明確知情的情況下被下載，且刪除後會自動重新下載。

## 💡 核心內容

### 什麼是 weights.bin？

這個 4GB 檔案是 Google Chrome 的設備端 AI 模型「Gemini Nano」的權重檔案。電腦科學家 Alexander Hanff（又稱 Privacy Guy）首先披露了這個情況。`weights.bin` 被深埋在用戶數據資料夾中，專門為 Chrome 的設備端 AI 功能而設。

### 為什麼要下載這個檔案？

傳統 AI 模型需要連接雲端才能運作，速度較慢且需要網絡連線。隨著設備端 LLM（大型語言模型）的興起，Google 將 Gemini Nano 整合到 Chrome 中，讓用戶可以在本機運行 AI，無需將數據上傳至雲端，提升速度、離線可用性及安全性。

### 如何知道電腦是否有這個檔案？

1. 開啟 Chrome，進入「設定」→「系統」
2. 檢查「設備端 AI」選項是否開啟
3. 如已開啟，電腦應該已有或即將有 `weights.bin` 檔案

### 檔案位置（Windows 11）

```
C:\Users\[用戶名]\AppData\Local\Google\Chrome\User Data\OptGuideOnDeviceModel\2025.8.8.1141\weights.bin
```

### 如何永久刪除？

1. 刪除 `weights.bin` 檔案
2. 回到 Chrome 設定 → 系統
3. 關閉「設備端 AI」開關

⚠️ **注意**：單純刪除檔案是不夠的，關閉設備端 AI 設定才能阻止重新下載。

### 4GB 空間值得嗎？

- 如果硬碟空間充足，4GB 不是大問題
- 如果空間緊張，這個檔案可能佔用寶貴空間
- 對於想嘗試設備端 AI 的用戶，這是值得的

---

**📌 資料來源**：ZDNet（2026-05-08）