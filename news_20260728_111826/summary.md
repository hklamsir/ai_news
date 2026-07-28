# NVIDIA 發布 Nemotron-Labs-TwoTower：基於凍結自迴歸骨架的開源權重擴散語言模型

## 📖 新聞導語

NVIDIA 發布了 Nemotron-Labs-TwoTower，這是一款區塊式自迴歸擴散模型，基於 Nemotron-3-Nano-30B-A3B 開放權重混合骨架構建。該模型將幹擾工作與乾淨標記表示分離到兩個塔樓中，保持 98.7% 的 AR 基線品質，同時實現 2.42 倍更高的生成吞吐量。

## 💡 核心內容

### 🏗️ 雙塔架構
TwoTower 的核心創新在於雙塔設計：每個塔有 52 層，包括 23 層 Mamba-2、6 層自注意力和 23 層 MoE。兩個塔總共約 600 億參數，每個標記的活躍參數約為 30 億。MoE 使用 128 個可路由專家，其中 6 個被激活，外加 2 個共享專家。

### 🔄 訓練機制
兩個塔從相同的骨架檢查點副本開始。只有幹擾塔（denoiser tower）接受訓練，而 AR 上下文塔保持凍結狀態。幹擾塔在約 2.1 兆個標記上訓練，僅為骨架 25 兆標記預訓練的一小部分。

### ⚡ 效能表現
TwoTower 保持了 98.7% 的 AR 基線 aggregate benchmark 品質，並報告 2.42 倍更高的牆上時鐘生成吞吐量。在多項基準測試中表現接近原始 AR 模型，包括 MMLU、ARC-Challenge、WinoGrande 等。

## 🔮 業界展望

TwoTower 的出現標誌著擴散語言模型的重要進展。透過將 AR 上下文能力與擴散生成相結合，這種架構可能在未來的高效能 AI 推理任務中找到廣泛應用場景。

---

**📌 資料來源**：MarkTechPost
**📅 發布日期**：2026-07-28
**🔗 原文連結**：https://www.marktechpost.com/2026/07/01/nvidia-releases-nemotron-labs-twotower/
