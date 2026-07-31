# Google Gemini Robotics 2 實現全身智能控制

## 📖 新聞導語

Google DeepMind 發布 Gemini Robotics 2，這是首個能控制整個人形機器人——從雙腳到指尖——的視覺語言動作（VLA）模型。不再局限於桌面上的上半身的操控，機器人可以走路、蹲下、伸手、搬物件，還能與其他機器人協作完成複雜任務。

## 💡 核心內容

### 三型號家族：從研究到商業落地
Gemini Robotics 2 包含三個不同層次的模型：
- **Gemini Robotics 2（旗艦 VLA）**：將視覺和語言輸入轉換為馬達控制，可驅動完整人形機器人（從腳到指尖）及其他雙臂機器人，支援多種夾爪和靈巧操作
- **Gemini Robotics-ER 2**：專為泛化設計，在看不見的新環境中表現更強，適合需要快速適應新場景的商業應用
- **Gemini Robotics 2 Accelerated**：針對延遲敏感場景優化的高速版本

### 全身控制：從桌面到整個空間
以往 Gemini Robotics 模型主要控制人形機器人的上半身，專注桌面任務。Gemini Robotics 2 首次將控制範圍擴展到全身運動，包括走路、蹲下、伸展、重心轉移等動作，並保留雙手的精細操控能力。在 Apollo 2 人形機器人上的實際演示中，輸入「把澆水壺放到底部架子的綠色箱子裏」，機器人便走動到桌子旁、拿起澆水壺、走到架子前、精確放置到目標位置。

### 精細操控仍有挑戰
評估顯示，Gemini Robotics 2 在不同場景的抓取成功率有明顯差異：
- 從桌面抓取：68.4%
- 從地面抓取：45.7%（最具挑戰性）
- 從架子抓取：76.3%（最佳）

測試中雙指夾爪表現優於多指靈巧手，反映出當前算法在復雜手指協調上的局限。

### 團隊協作：機器人之間的配合
除了個體控制，Gemini Robotics 2 還支援多機器人協作，能共同完成需要協調的複雜任務。

### 商業化時間表：尚屬早期
Google 明確表示不會很快推出面向消費者的機器人產品。相比之下，Elon Musk 宣稱 Tesla 的 Optimus 機器人將是「史上最大產品」，但其設定的 2025 年底部署 1000 個工廠機器人的目標並未實現，2026 年部署 5 萬至 10 萬台的承諾也不會兌現。

## 🔮 業界展望

Gemini Robotics 2 的發布代表 Google 將 AI 模型與實體機器人結合的重要一步。從應用場景看，工廠自動化、倉儲物流、家庭助理都是潛在方向，但當前精細操控成功率仍待提升，特別是地面抓取場景（45.7%）距離實用還有距離。隨著模型持續迭代，全身控制 + 靈巧操作的組合將是人形機器人走向通用場景的關鍵台階。

---

**📌 資料來源**：Engadget（[Google's new Gemini Robotics 2 platform allows for 'intelligent whole-body control'](https://www.engadget.com/2227268/google-gemini-robotics-2-platform-intelligent-whole-body-control/)）
**📅 發布日期**：2026-07-30
**🔗 原文連結**：https://www.engadget.com/2227268/google-gemini-robotics-2-platform-intelligent-whole-body-control/
