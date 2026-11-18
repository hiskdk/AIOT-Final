"""
planner.py — Planner & Reasoning Agent（架構編號 ③）

狀態：☐ Planned（Proposal 階段，尚未實作）

設計說明（來自 DESIGN.md 第 4.1 章）：
- 以 ReAct（Reasoning + Acting）在「推理」與「呼叫工具」之間交錯。
- 職責：意圖辨識、參數抽取、追問（上限 T_max 輪）、任務拆解、工具選擇、輸出前自我檢核。
- 不得：自行計算金額門檻／折舊、自行判定法規是否合規、直接寫入資料庫。

演算法對應（DESIGN.md Algorithm 1）：
  Input : user query Q, user role r, attachments F
  Output: result R with evidence E and audit record A

  01: intent, params <- LLM.parse(Q, F)
  02: if not authorized(r, intent) then return Deny("permission")
  03: while missing(params, intent) and turns < T_max do
  04:     params <- params + ask_user(clarify_questions(intent, params))
  05: end while
  06: if intent in {IMPORT, LEND, VALUE, DISPOSE} then
  07:     R <- ManagementAgent(intent, params)
  08: else if intent = PROCURE then
  09:     R <- ProcurementAgent(params)
  10: end if
  11: E <- KB.retrieve(intent, R)
  12: violations <- RuleEngine.check(R, rules.yaml)
  13: if violations != {} or R.uncertainty > tau or R.commits_state then
  14:     decision <- human_review(R, E, violations)
  15:     if decision = REJECT then
  16:         if retries >= R_max then return Escalate(R, E)
  17:         return LabSteward(Q + feedback, retries + 1)
  18:     end if
  19: end if
  20: commit(R); A <- audit_log(Q, R, E, decision)
  21: return render_docs(R, E)

TODO（實作時依序完成）：
  [ ] 選定 LLM 與 Agent 框架（LangGraph 或自行實作狀態機）
  [ ] 實作意圖辨識與參數抽取
  [ ] 實作追問迴圈（上限 T_max，參數待定）
  [ ] 整合 ManagementAgent 與 ProcurementAgent
  [ ] 整合 Guardrail 規則檢核
  [ ] 整合 Audit Log
  [ ] 實作 RBAC 授權檢查
"""

# TODO: 實作 PlannerAgent 類別
