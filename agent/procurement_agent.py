"""
procurement_agent.py — 採購子 Agent（P1–P4）

狀態：☐ Planned（Proposal 階段，尚未實作）

設計說明（來自 DESIGN.md 第 4.3 章）：

| 模組 | 功能 |
|------|------|
| P1 確認需求 | 追問用途、規格、數量、預算、期限，並正規化規格 |
| P2 查詢庫存 | 查詢在庫、閒置、可移撥財產；可滿足則建議借用／移撥 |
| P3 上網比價 | 搜尋電商與共同供應契約；商品實體比對與去重；有效報價不足 3 筆時放寬條件重搜 |
| P4 採購清單 | 依 TCO 排序、依金額判定流程、偵測拆單、輸出含報價來源的清單 |

演算法對應（DESIGN.md Algorithm 3）：
  Input : requirement params p (spec, qty, budget, deadline)
  Output: purchase list PL or borrow/transfer suggestion

  01: S0 <- normalize_spec(p.spec); S <- S0                    // P1
  02: I <- Inventory.query(S0, status in {IN_STOCK, IDLE})     // P2
  03: if I satisfies p.qty then return Suggest(borrow_or_transfer, I)
  04: offers <- {}; k <- 0
  05: repeat                                                    // P3
  06:     raw <- WebSearch(S) + JointSupplyContract(S)
  07:     matched <- dedupe(EntityMatch(raw, S0))
  08:     offers <- offers ∪ mark_relaxed(matched, S, S0)
  09:     S <- relax(S); k <- k + 1
  10: until |offers| >= 3 or k >= K_max
  11: if |offers| < 3 then mark NEED_MANUAL_QUOTES
  12: ranked <- sort(offers, by = TCO(price, warranty, shipping, lead_time))
  13: total <- best(ranked).price * p.qty
  14: route <- Rules.threshold(total)      // small / under-announce / announce
  15: if split_order_suspected(p, history) then flag VIOLATION
  16: PL <- build_list(ranked, route, sources, budget_check(total, p.budget))
  17: return PL                                                 // P4

參數（待定，見 DESIGN.md 第 12.2 章）：
  K_max — 放寬條件最大重搜次數（TBD）
  TCO 權重（price, warranty, shipping, lead_time）— TBD

TODO（實作時依序完成）：
  [ ] P1：規格正規化（LLM 追問）
  [ ] P2：整合 tools/inventory.py
  [ ] P3：整合 tools/web_search.py + tools/entity_match.py
  [ ] P3：有效報價不足 3 筆時放寬條件重搜邏輯（累積、去重、mark_relaxed）
  [ ] P4：TCO 排序 + 整合 knowledge/rules.yaml 門檻判定
  [ ] P4：拆單偵測 split_order_suspected()
  [ ] P4：整合 tools/docgen.py（Word 採購清單輸出）
"""

# TODO: 實作 ProcurementAgent 類別（P1–P4）
