# Microsoft fixes 421 bugs and a Windows zero-day in August Patch Tuesday - update ASAP

## 📖 新聞導語

Microsoft 發布 2026 年 8 月 Patch Tuesday，修補共 421 個漏洞，其中包括一個正被北韓 Lazarus 組織利用的 Windows 零日漏洞 CVE-2026-68820。該漏洞涉及 Windows Sockets API 核心驅動程式 afd.sys，攻擊者已利用它部署 FudModule 核心模式木馬。

## 💡 核心內容

### 🔴 主動被利用的零日漏洞：CVE-2026-68820
- **漏洞類型**：Use-after-free（釋放後使用），位於 Windows Ancillary Function Driver for WinSock（afd.sys）
- **CVSS 分數**：7.0（高風險）
- **攻擊方式**：本地已認證攻擊者可透過特定應用程式觸發 race condition，以 SYSTEM 層級權限執行代碼
- **攻擊者**：北韓 Lazarus 組織（曾於 2024 年利用同類型漏洞 CVE-2024-38193）
- **後續行動**：利用該漏洞部署新版 FudModule 核心模式木馬

### 📊 微軟 8 月漏洞統計
| 產品 | 漏洞數量 |
|------|---------|
| Windows | 236 |
| Office / Office 2016 | 196 |
| SharePoint Server | 30 |
| 開發者工具 | 26 |
| Azure | 17 |
| Exchange Server | 7 |
| Defender | 1 |
| 其他 | 6 |

- **嚴重漏洞（Critical）**：62 個
- **零日漏洞**：3 個（其中 1 個已確認被主動利用）

### ⚠️ 其他值得關注的漏洞
- **CVE-2026-62832**：Windows User Profile Service 權限提升漏洞（link following 問題），已被公開披露
- **CVE-2026-62893**：Windows Deployment Services TFTP Server 遠端代碼執行漏洞
- **CVE-2026-62878**：Windows DNS Server 遠端代碼執行漏洞
- **CVE-2026-62815**：Microsoft QUIC 遠端代碼執行漏洞
- **CVE-2026-62911**：Exchange Server 權限提升漏洞
- **CVE-2026-6726 / CVE-2026-6727**：TPM 2.0 參考實作中的欺騙及資訊洩露漏洞（非微軟產品）

### 🕐 過去同類型漏洞
自 2022 年起，afd.sys 已出現過三個被實際利用的零日漏洞：
- CVE-2025-32709
- CVE-2025-21418
- CVE-2024-38193

## 🔮 業界展望

這是連續第三個月微軟在例行 Patch Tuesday 中出現「已確認被主動利用」的零日漏洞，顯示網絡攻擊者正加快利用公開披露漏洞的速度。安全團隊需優先修補 CVE-2026-68820，同時留意 Trend Micro ZDI 額外標記的五個漏洞。大型軟體商發布安全更新的頻率及規模持續增加，顯示 AI 輔助漏洞挖掘正發現更多以往隱藏的安全缺陷。

---

**📌 資料來源**：ZDNET、SecurityWeek、The Register、Malwarebytes、TechInsider
**📅 發布日期**：2026-08-11 至 2026-08-16
**🔗 原始連結**：https://www.zdnet.com/article/microsoft-august-windows-update-421-bugs-zero-day-exploited/
