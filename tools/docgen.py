"""
docgen.py — Word / Excel 文件輸出工具（⑧）

狀態：☐ Planned（Proposal 階段，尚未實作）

功能（FR-12）：
  - 輸出 Word 採購清單（python-docx）
  - 輸出 Word 報廢申請草稿（python-docx）
  - 輸出 Excel 財產清冊（openpyxl）
  - 輸出借用單與通知

所有輸出文件為「草稿」，需人工核准後才具法律效力（FR-11）。

TODO：
  [ ] 實作 gen_purchase_list(ranked_offers, route, sources) -> Path  （Word）
  [ ] 實作 gen_disposal_draft(asset, valuation_result) -> Path       （Word）
  [ ] 實作 gen_asset_registry(assets) -> Path                        （Excel）
  [ ] 實作 gen_lending_form(lending_record) -> Path                   （Word/PDF）
  [ ] 設計文件模板（與校方送審格式對齊）
"""

# TODO: 實作 DocGenTool 類別（python-docx + openpyxl）
