"""
streamlit_app.py — LabSteward Web 介面（架構編號 ②⑧）

狀態：☐ Planned（Proposal 階段，尚未實作）

功能（來自 DESIGN.md 第 9.3 章）：
  - 使用者輸入介面（自然語言查詢、PDF 上傳、財產標籤照片上傳）
  - 顯示 Planner Agent 的推理過程與工具呼叫記錄
  - 顯示殘值估算結果（帳面價值 + 市場價值區間）
  - 顯示採購建議與報價清單
  - 人工核准介面（管理人 / PI 核准或退回）
  - 稽核紀錄查閱

技術選型（DESIGN.md 第 9.3 章）：
  Streamlit（快速原型，可展示 Demo）；LINE Bot 為後續延伸。

Demo 情境（DESIGN.md 第 10.4 章）：
  「為新進學生準備一台深度學習工作站」
  → 查庫存 → 比價 → 門檻判定 → 輸出採購清單

TODO：
  [ ] 建立 Streamlit 基本頁面結構（側邊欄、主內容區）
  [ ] 實作自然語言輸入與 Planner Agent 整合
  [ ] 實作 PDF / 照片上傳（整合 tools/ingest.py）
  [ ] 實作人工核准介面（整合 agent/guardrail.py）
  [ ] 實作殘值估算結果顯示（整合 tools/valuation.py）
  [ ] 實作稽核紀錄查閱頁面（整合 tools/audit.py）
  [ ] 實作 RBAC 登入（member / manager / pi）
"""

# TODO: 實作 Streamlit 應用程式
