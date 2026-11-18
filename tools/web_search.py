"""
web_search.py — 網頁搜尋與商品擷取工具（P3）

狀態：☐ Planned（Proposal 階段，尚未實作）

功能（FR-07）：
  - 以 Playwright 搜尋電商網站（如 PChome、蝦皮、露天）
  - 查詢共同供應契約（政府電子採購網）
  - 擷取商品名稱、規格、價格、廠商、保固
  - 遵守網站使用條款、robots.txt 與頻率限制

注意（來自 DESIGN.md 第 12.1 章）：
  電商版面與條款會變動；實作時需定期維護擷取邏輯。

TODO：
  [ ] 實作 search_products(spec, keywords) -> List[RawListing]
  [ ] 實作共同供應契約查詢（awa.gov.tw 或 電子採購網 API）
  [ ] 設定頻率限制與重試邏輯
  [ ] 整合至 ProcurementAgent.P3
"""

# TODO: 實作 WebSearchTool 類別（Playwright + 搜尋 API）
