"""
inventory.py — 在庫／閒置／可移撥財產查詢工具

狀態：☐ Planned（Proposal 階段，尚未實作）

功能（FR-06、FR-09）：
  - 依規格、類別、狀態查詢財產清冊（SQLite assets 資料表）
  - 支援狀態過濾：IN_STOCK（在庫）、IDLE（閒置）、LENT（借出）
  - 供 ProcurementAgent P2 步驟強制查詢庫存使用
  - 支援自然語言查詢（由 Planner 解析後傳入結構化參數）

資料表（來自 DESIGN.md 第 5.2 章）：
  assets(asset_id, name, spec, category_code, unit_price, purchase_date,
         status, custodian, location, working, utilization_30d)

TODO：
  [ ] 建立 SQLite 連線（讀取 db/schema.sql）
  [ ] 實作 query_inventory(spec, category, status_filter) -> List[Asset]
  [ ] 實作使用率計算（依 lending 紀錄計算 utilization_30d）
  [ ] 整合至 ProcurementAgent.P2
"""

# TODO: 實作 query_inventory() 函式
