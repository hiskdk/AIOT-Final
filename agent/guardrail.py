"""
guardrail.py — 規則檢核與人工審核節點（架構編號 ⑦）

狀態：☐ Planned（Proposal 階段，尚未實作）

設計說明（來自 DESIGN.md 第 4.4 章）：
- 讀取 knowledge/rules.yaml，以確定性程式檢核：
    * 財產／物品判定（單價 >= 10,000 且年限 >= 2 年）
    * 金額門檻（小額 150,000 / 公告 1,500,000 等）
    * 最低使用年限
    * 預算
    * 拆單偵測
- LLM 僅負責用自然語言解釋判定結果，不參與判定。
- 觸發人工審核的條件（對應 Algorithm 1 第 13 行）：
    * violations != {}（有違規）
    * R.uncertainty > tau（不確定度超過門檻）
    * R.commits_state（動作會改變帳務狀態）

TODO（實作時依序完成）：
  [ ] 載入並解析 knowledge/rules.yaml
  [ ] 實作財產／物品判定邏輯
  [ ] 實作金額門檻判定（小額 / 公告金額 / 共同供應契約）
  [ ] 實作最低使用年限檢核
  [ ] 實作拆單偵測
  [ ] 實作 human_review() 節點（等待人工核准並記錄決定）
  [ ] 整合 tools/audit.py（寫入稽核紀錄）
"""

# TODO: 實作 RuleEngine 與 Guardrail 類別
