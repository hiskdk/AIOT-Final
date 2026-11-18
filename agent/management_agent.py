"""
management_agent.py — 管理子 Agent（M1–M4）

狀態：☐ Planned（Proposal 階段，尚未實作）

設計說明（來自 DESIGN.md 第 4.2 章）：

| 模組 | 功能 | 主要輸入 | 主要輸出 |
|------|------|----------|----------|
| M1 導入 | 從發票／報價單 OCR 抽取品名、規格、金額、日期，建議財物分類 | PDF、照片 | 財產建檔草稿 |
| M2 借用 | 檢查時段衝突、建立借用單、到期提醒 | 設備、時段、借用人 | 借用單、提醒通知 |
| M3 殘值 | 計算雙軌殘值（帳面價值 + 市場價值） | 設備資料、購置價、年數、狀況 | 帳面價值、市場價值區間、建議 |
| M4 報廢 | 檢核最低使用年限與狀態，產生報廢申請草稿 | 設備、狀態 | 報廢申請草稿 |

演算法對應（DESIGN.md Algorithm 2 — M3 雙軌殘值）：
  Input : asset a (cost C, category k, purchase_date, condition c)
  Output: book value Vb, market value interval [Vl, Vh], advice

  01: t <- years_since(a.purchase_date)
  02: L <- StdClassTable.min_life(k)
  03: Vb <- C * max(0, 1 - t / L)
  04: D <- MarketData.listings(similar_to(a))
  05: if |D| >= N_min then
  06:     model <- GBM.fit(D); [Vl, Vh] <- bootstrap_interval(model, a)
  07: else
  08:     d <- LogLinear.fit(category_data(k)).rate or default_rate(k)
  09:     Vm <- C * (1 - d)^t * q(c); [Vl, Vh] <- Vm * (1 -/+ delta)
  10:     flag LOW_CONFIDENCE
  11: end if
  12: if t >= L and a.working then advice <- KEEP_USING
  13: else if not a.working and repair_cost(a) > Vh then advice <- DISPOSE
  14: else if utilization(a) < u_min then advice <- TRANSFER_OR_SHARE
  15: else advice <- REPAIR_OR_KEEP
  16: return Vb, [Vl, Vh], advice

參數（待定，見 DESIGN.md 第 12.2 章）：
  N_min, u_min, delta — 待資料蒐集後決定

TODO（實作時依序完成）：
  [ ] M1：整合 tools/ingest.py（OCR + 欄位抽取）
  [ ] M1：整合 knowledge/std_class_table.csv（建議財物分類）
  [ ] M2：整合 tools/lending.py（衝突檢查、借用單）
  [ ] M3：整合 tools/valuation.py（雙軌殘值）
  [ ] M4：整合 tools/docgen.py（報廢申請草稿）
  [ ] M4：整合 knowledge/rules.yaml（最低使用年限檢核）
"""

# TODO: 實作 ManagementAgent 類別（M1–M4）
