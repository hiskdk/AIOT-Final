"""
lending.py — 借用／租用工具（M2）

狀態：☐ Planned（Proposal 階段，尚未實作）

功能（FR-02）：
  - 建立借用單（lend_id, asset_id, borrower, start_ts, end_ts）
  - 檢查時段衝突（同一設備不可重疊借用）
  - 到期提醒通知
  - 歸還登記（更新 returned_ts、改回 IN_STOCK 狀態）

資料表（來自 DESIGN.md 第 5.2 章）：
  lending(lend_id, asset_id, borrower, start_ts, end_ts, returned_ts)

財產狀態機（DESIGN.md 第 5.3 章）：
  IN_STOCK -> Lent（借用核准）
  Lent -> IN_STOCK（歸還）

注意：所有改變 assets.status 的動作需人工核准並寫入 audit_log（FR-11）。

TODO：
  [ ] 實作 create_lending(asset_id, borrower, start_ts, end_ts) -> LendingRecord
  [ ] 實作衝突檢查 check_conflict(asset_id, start_ts, end_ts) -> bool
  [ ] 實作 return_asset(lend_id) -> None（需人工核准）
  [ ] 實作到期提醒通知
  [ ] 整合 tools/audit.py
"""

# TODO: 實作 LendingTool 類別
