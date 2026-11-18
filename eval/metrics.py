"""
metrics.py — 評估指標計算

狀態：☐ Planned（Proposal 階段，尚未實作）

指標（DESIGN.md 第 11.2 章）：

| 指標 | 說明 |
|------|------|
| task_success_rate  | 任務最終輸出符合標註答案的比例 |
| pass_k             | 同一任務重跑 k 次皆成功的比例（NFR-02 穩定度） |
| field_extraction_f1| M1 從發票抽取欄位的 F1 |
| residual_mape      | 市場價值預測的平均絕對百分比誤差 |
| price_gap          | 系統最低價相對人工最低價的差距 |
| entity_match_precision | P3 商品比對 precision |
| rule_violation_rate| 輸出違反 rules.yaml 的情境比例 |
| false_pass_rate    | 應被攔截卻被放行的比例 |
| evidence_accuracy  | 引用條文正確支持結論的比例 |
| task_time_sec      | 輸入到產出文件的平均時間（秒） |

TODO：
  [ ] 實作各指標計算函式
  [ ] 實作 pass_k(results, k) -> float
  [ ] 實作 residual_mape(predictions, actuals) -> float
  [ ] 實作 rule_violation_rate(outputs, rules) -> float
  [ ] 整合至 run_eval.py
"""

# TODO: 實作各評估指標計算函式
