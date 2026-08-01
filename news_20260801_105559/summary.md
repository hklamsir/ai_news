# Token Saver: An Open-Source MCP Extension Using Local Hybrid RAG

## 📖 新聞導語

Marktechpost AI 團隊發布了 Token Saver，這是一款開源的 Model Context Protocol（MCP）擴展，專為 Claude Desktop 設計（MIT 授權，目前版本為 v1.0）。該工具由羅徹斯特理工學院電腦科學系學生 Arnav Rai 在實習期間開發，可將 PDF 文件的 Token 消耗降低 92% 至 99%，同時確保資料永不離開本地設備。

## 💡 核心內容

### 什麼是 Token Saver？

Token Saver 是一款本地 MCP 伺服器，作為後台程式運行於用戶機器上，Claude 可以將其作為工具呼叫。其核心採用 Local Hybrid RAG（本地混合檢索增強生成）技術，允許用戶針對大型 PDF 提問，但永遠不需要將實際文件上傳給模型。

### Hybrid RAG 的運作原理

混合檢索是目前文件檢索的黃金標準，結合兩種強大的搜索方法：

1. **關鍵詞匹配（BM25）**：透過 SQLite 內建的 FTS5 搜索（權重 0.4）找出精確術語
2. **語義搜索（餘弦相似度）**：使用本地 all-MiniLM-L6-v2 嵌入模型（權重 0.6）理解問題含義，而不僅僅是匹配確切字詞

### 主要特點

- **巨幅成本降低**：使用本地混合 RAG 僅傳遞相關段落給 LLM，Token 成本降幅高達 99%
- **可驗證的準確性**：Token Saver 為每個檢索區塊附上精確頁碼，用戶可即時打開本地 PDF 驗證 Claude 的聲明
- **絕對隱私保障**：界線就是你的本地機器，專有資料永遠不會上傳至 AI 提供商的伺服器
- **零門檻設定**：無需安裝 Python，簡單的 .mcpb 檔案即可在 Claude Desktop 中立即運行

## 🔮 業界展望

Token Saver 的出現代表了一種新趨勢：將 AI 能力與本地隱私結合。隨著企業和個人對資料隱私的重視程度提升，這類本地化 AI 工具的需求將持續成長。開發者 Arnav Rai 的背景（電腦科學學生）也顯示，越來越多新一代開發者正在重視工具的易用性與隱私保護之間的平衡。

---

**📌 資料來源**：Marktechpost
**📅 發布日期**：2026-07-30
**🔗 原始連結**：https://www.marktechpost.com/2026/07/30/token-saver-an-open-source-mcp-extension-using-local-hybrid-rag/
