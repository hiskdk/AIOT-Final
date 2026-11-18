"""
audit.py — Audit Log 寫入與查詢工具（架構編號 ⑧）

狀態：☐ Planned（Proposal 階段，尚未實作）

功能（FR-11、NFR-03）：
  - 記錄每個決策的：輸入、輸出、引用證據、規則檢核結果、核准人與時間
  - 所有改變帳務狀態的動作需先記錄再執行
  - 支援查詢稽核紀錄（供 PI 或財產管理人查閱）

資料表（來自 DESIGN.md 第 5.2 章）：
  audit_log(log_id, ts, actor, role, intent, input, output,
            evidence, violations, decision)

設計原則（來自 DESIGN.md 第 13 章）：
  Audit Log 記錄輸入、輸出、引用證據、規則檢核結果、核准人與時間。
  寫入資料庫的唯一路徑是「工具 + 人工核准 + 稽核紀錄」；
  Agent 不能「口頭」改帳。

TODO：
  [ ] 實作 write_log(actor, role, intent, input, output, evidence, violations, decision)
  [ ] 實作 query_log(filters) -> List[AuditRecord]
  [ ] 確保 log 不可竄改（至少在應用層面）
  [ ] 整合至 PlannerAgent 主迴圈（Algorithm 1 第 20 行）
"""

# TODO: 實作 AuditTool 類別
