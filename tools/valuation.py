"""
valuation.py — 雙軌殘值估算工具（M3）

狀態：☐ Planned（Proposal 階段，尚未實作）

功能（FR-03）：
  - 帳面價值（法定直線法）：V_book = C * max(0, 1 - t/L)
  - 市場價值（經濟）：V_mkt = C * (1-d)^t * q(c)
    * 資料量足夠：Gradient Boosting + Bootstrap 80% 預測區間
    * 資料不足：log-linear 迴歸，標示 LOW_CONFIDENCE
  - 建議：KEEP_USING / DISPOSE / TRANSFER_OR_SHARE / REPAIR_OR_KEEP
  - 輸出兩種價值與區間、差異說明、建議與依據

演算法：見 DESIGN.md Algorithm 2（第 8.3 章）

參數（待定，見 DESIGN.md 第 12.2 章）：
  N_min  — GBM 最小訓練樣本數（TBD）
  u_min  — 閒置使用率門檻（TBD）
  delta  — 低信心區間寬度係數（TBD）
  default_rate(k) — 各類別預設年貶值率（TBD）

資料來源：
  - knowledge/std_class_table.csv：最低使用年限 L
  - data/market_listings.csv：二手掛牌資料

TODO：
  [ ] 實作帳面價值計算（讀取 std_class_table.csv 取得 L）
  [ ] 實作 log-linear 迴歸估計年貶值率 d
  [ ] 實作 GBM 模型訓練與 Bootstrap 預測區間
  [ ] 實作建議規則（KEEP_USING / DISPOSE / TRANSFER_OR_SHARE / REPAIR_OR_KEEP）
  [ ] 實作低信心標示 LOW_CONFIDENCE
  [ ] 整合至 ManagementAgent.M3
"""

# TODO: 實作 ValuationTool 類別（含雙軌殘值計算）
