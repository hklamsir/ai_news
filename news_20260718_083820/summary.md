# Patreon 停止請求 AI 爬蟲「不要抓取」——直接開始封鎖

## 📖 新聞導語

創作人會員平台 Patreon 宣布與網絡基礎設施提供商 Cloudflare 合作，直接封鎖那些未經許可就抓取創作人內容來訓練 AI 模型的 AI 爬蟲。Patreon 表示，過去那種只靠 robots.txt 請求 AI 爬蟲不要抓取的做法已經失效，現在必須主動出擊。

## 💡 核心內容

### 從請求變成封鎖
Patreon 早在 2023 年已設置措施阻止 AI 爬蟲，但 AI 抓取技術日益精密，這些措施已不足以應對。此外，Patreon 的付費牆長期以來將大量創作人內容鎖在爬蟲的範圍之外，但最近平台推出的新發現工具（如重新設計的主頁 Feed 和類似推文的 Quips 功能）可能會暴露更多內容給爬蟲。

### Cloudflare AI Crawl Control 技術
Patreon 擴展與 Cloudflare 的現有合作，使用其 AI Crawl Control 技術來更新 AI 政策及執法工具。關鍵差異在於：以前只是透過 robots.txt 標準做法「請求」AI 爬蟲不要抓取內容，現在則是主動封鎖用於 AI 訓練的爬蟲。

### 成效顯著
Patreon 在部落格文章中指出，測試功能時，個別 AI 訓練爬蟲每週嘗試訪問 Patreon 的次數從「數千次降至零」。這表明 AI 爬蟲一直在無視 Patreon 的 robots.txt 請求，依舊持續抓取網站內容。

### consent 問題
Patreon 部落格文章明確表示：「同意不應該取決於爬蟲是否選擇自律。」這次升級措施正是對這一問題的直接回應。

### 允許什麼？
Patreon 表示仍會允許那些為用戶建立索引、並將用戶導回流朋的工具型爬蟲。

## 🔮 業界展望

此次轉變反映了一個更大趨勢：內容平台越來越不能依賴 robots.txt 的「榮譽制度」，必須採取更主動的技術手段來保護創作者的權益。隨著 AI 訓練數據需求持續增長，這類衝突只會更加激烈。

---

**📌 資料來源**：TechCrunch
**📅 發布日期**：2026-07-17
**🔗 原文連結**：https://techcrunch.com/2026/07/17/patreon-stops-asking-ai-bots-not-to-scrape-and-starts-blocking-them/
