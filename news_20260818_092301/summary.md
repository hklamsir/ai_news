# Google Workspace 預設讓 Gemini 讀取公司數據——如何關閉？

## 📖 新聞導語

ZDNet 揭露 Google Workspace 預設允許 Gemini 存取所有Workspace 服務（Gmail、Docs、Calendar、Chat 等），公司管理員如不主動關閉，員工的 AI 助理將自動有權讀取企業內部數據，存在合規及私隱風險。

## 💡 核心內容

### 預設風險
Google 預設讓 Gemini 有權存取 Gmail、Docs、Calendar、Chat 等所有 Workspace 服務。這意味著企業員工使用的 AI 助理，會自動獲得查看公司內部數據的權限，而大多數用戶並不知情。

### 如何關閉（管理員步驟）
1. 前往 Google Admin Console
2. 點擊「Generative AI」再選「Gemini in Workspace」
3. 進入「Workspace Intelligence Sources」頁面
4. 點擊選項即可為整個企業禁用該功能

### 個人用戶限制
作者在測試中發現，為單一用戶關閉功能時介面不完整，無法在「Drive and Docs」等來源上單獨禁用。這是 Google 介面的一個缺陷。

### 隱私與合規風險
企業 AI 存取內部數據可能引發合規及私隱問題，特別是使用商業 Google Workspace 服務的企業更需注意。

## 🔮 業界展望

越來越多企業引入 AI 助理，但預設開放數據存取的設計令人擔憂。專家建議企業 IT 管理員應主動審視並限制 AI 的數據存取權限，以符合企業保安及合規要求。員工亦應了解所用 AI 工具的數據權限範圍。

---

**📌 資料來源**：ZDNet（David Gewirtz）
**📅 發布日期**：2026-08-17
**🔗 原始連結**：https://www.zdnet.com/article/google-workspace-lets-gemini-access-your-company-data-by-default-how-to-shut-it-down/
