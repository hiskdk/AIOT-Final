"""
entity_match.py — 商品實體比對與去重工具（P3）

狀態：☐ Planned（Proposal 階段，尚未實作）

功能（FR-07）：
  - 以結構化規格欄位做二次驗證（非只靠 LLM）
  - 再用 LLM 判斷是否為同一商品
  - 去重後以 TCO 排序：TCO(price, warranty, shipping, lead_time)
  - 標示放寬規格後匹配的商品（mark_relaxed）

設計原則（來自 DESIGN.md 第 6.3 章）：
  不只靠 LLM，因為 LLM 對 prompt 寫法高度敏感 [7]，
  且購物 Agent 在篩選／排序上易出錯 [5]。

TODO：
  [ ] 實作規格欄位結構化比對（型號、容量、頻率等）
  [ ] 實作 LLM 輔助語意比對
  [ ] 實作 dedupe(listings, original_spec) -> List[MatchedListing]
  [ ] 實作 TCO 排序（權重 TBD）
  [ ] 整合至 ProcurementAgent.P3
"""

# TODO: 實作 EntityMatchTool 類別
