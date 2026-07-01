#!/usr/bin/env python3
import sys
sys.path.insert(0, '/home/lamsir/.openclaw/workspace/skills/ai-news/script')
from html_utils import assemble_article

article_content = """
        <div class="meta-info">
            <p><strong>📺 資料來源</strong>：<a href="https://www.pcmarket.com.hk/openclaw-app-launch-features/" target="_blank">PCM（pcmarket.com.hk）</a></p>
            <p><strong>📅 發布日期</strong>：2026-07-01</p>
            <p><strong>🤖 處理方式</strong>：AI 智能摘要生成</p>
        </div>

        <h3>🎯 核心觀點</h3>
        <p>OpenClaw 正式推出官方手機 App，將用戶的智能手機轉化為 OpenClaw 的移動節點。支援即時文字及語音聊天、動作審批、內容分享，以及相機、螢幕截圖、位置等裝置能力整合。App 完全免費，支援 iOS、iPadOS、Android 及 Apple Watch。</p>

        <div class="tech-card">
            <div class="tech-card-icon">📱</div>
            <div class="tech-card-content">
                <h4>QR Code 快速配對</h4>
                <p>只需掃描 QR Code 或輸入設定碼，即可與自家 OpenClaw Gateway 連接，支援 LAN 或 Tailscale 等網絡環境，配對過程簡單快捷。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">💬</div>
            <div class="tech-card-content">
                <h4>即時聊天與 Talk Mode</h4>
                <p>支援即時文字聊天，以及即時和背景語音模式，方便隨時與 AI 助理對話。另有 ClawVoice companion App 強化 CarPlay 語音體驗，實現車內無縫語音互動。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">✅</div>
            <div class="tech-card-content">
                <h4>動作審批（Approvals）</h4>
                <p>在手機上即時審核 Gateway 執行的自動化動作，大幅提升安全性，確保所有自動化操作都在用戶掌控之中。</p>
            </div>
        </div>

        <div class="tech-card">
            <div class="tech-card-icon">🔗</div>
            <div class="tech-card-content">
                <h4>內容分享與裝置整合</h4>
                <p>直接從手機分享文字、連結、媒體到 OpenClaw 進行處理。用戶可按需授予權限，讓 AI 存取相機、螢幕截圖、位置、照片、聯絡人、日曆和提醒事項等功能，用於裝置感知自動化。</p>
            </div>
        </div>

        <div class="highlight-box">
            <h4>📌 重點提示</h4>
            <p>由於 App Store 和 Google Play Store 有很多以 OpenClaw 為名的魚目混珠 App，建議使用「OpenClaw Foundation」作關鍵字搜尋，或直接點擊官方連結下載，避免下載到假冒 App。</p>
        </div>

        <div class="quote-box">
            <p>「OpenClaw 強調所有資料控制權在用戶手中，裝置存取嚴格遵循 iOS/Android 權限管理，用戶可隨時啟用或停用特定功能。」</p>
            <cite>— OpenClaw 官方</cite>
        </div>

        <h3>🔮 業界展望</h3>
        <p>OpenClaw 的移動 App 推出，標誌著這款本地 AI 平台進一步向日常移動使用場景延伸。對於重視私隱、希望自控 AI 助理的用戶來說，OpenClaw 提供高度客製化體驗。平台源自開源社區，並獲得 OpenAI 支援，適合希望在 Mac Mini、Windows PC 或 VPS 上全天候運行 AI 代理的用戶。</p>

        <div class="timeline">
            <div class="timeline-item">
                <div class="timeline-date">第一步</div>
                <div class="timeline-title">完成 Gateway 架設</div>
                <div class="timeline-desc">在 Mac Mini、Windows PC 或 VPS 上架設 OpenClaw Gateway</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第二步</div>
                <div class="timeline-title">呼叫配對指令</div>
                <div class="timeline-desc">在 OpenClaw 對話中呼叫「/pair qr」指令取得配對 QR Code</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第三步</div>
                <div class="timeline-title">掃描配對</div>
                <div class="timeline-desc">開啟 OpenClaw 手機 App，點擊 Scan QR Code 與 Gateway 配對</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">第四步</div>
                <div class="timeline-title">開始使用</div>
                <div class="timeline-desc">開始透過手機使用聊天、Talk Mode、審批和自動化功能</div>
            </div>
            <div class="timeline-item">
                <div class="timeline-date">額外</div>
                <div class="timeline-title">ClawVoice 強化</div>
                <div class="timeline-desc">使用 ClawVoice companion App 強化 CarPlay 語音體驗</div>
            </div>
        </div>

        <table class="comparison-table">
            <thead>
                <tr>
                    <th>功能</th>
                    <th>說明</th>
                    <th>用途</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>即時聊天</td>
                    <td>文字訊息即時對話</td>
                    <td class="highlight-col">日常溝通</td>
                </tr>
                <tr>
                    <td>Talk Mode</td>
                    <td>即時和背景語音模式</td>
                    <td class="highlight-col">車內語音助理</td>
                </tr>
                <tr>
                    <td>動作審批</td>
                    <td>即時審核自動化動作</td>
                    <td class="highlight-col">安全管控</td>
                </tr>
                <tr>
                    <td>內容分享</td>
                    <td>分享文字、連結、媒體</td>
                    <td class="highlight-col">快速處理</td>
                </tr>
                <tr>
                    <td>裝置整合</td>
                    <td>相機、位置、照片、聯絡人等</td>
                    <td class="highlight-col">自動化場景</td>
                </tr>
            </tbody>
        </table>
"""

metadata = {
    'title': 'OpenClaw 推出官方手機 App　審批動作、語音交談、內容分享．手機作安全節點',
    'h1': 'OpenClaw 推出官方手機 App<br>審批動作、語音交談、內容分享',
    'subtitle': '手機作安全節點',
    'source_url': 'https://www.pcmarket.com.hk/openclaw-app-launch-features/',
    'source_name': 'PCM（pcmarket.com.hk）',
    'pub_date': '2026-07-01',
    'img_alt': 'OpenClaw 官方手機 App 介面示意圖',
}

success, errors = assemble_article(
    article_dir='/home/lamsir/ai_news/news_20260701_210700',
    article_content=article_content,
    metadata=metadata
)

print(f"\n結果：{'✅ 成功' if success else '❌ 失敗'}")
if errors:
    print(f"錯誤：{errors}")