"""
run_eval.py — 評估腳本

狀態：☐ Planned（Proposal 階段，尚未實作）

用法（預定）：
  python eval/run_eval.py --tasks eval/tasks.jsonl --system labsteward --k 4
  python eval/run_eval.py --tasks eval/tasks.jsonl --system baseline_llm --k 4
  python eval/run_eval.py --tasks eval/tasks.jsonl --system baseline_rag  --k 4

說明（DESIGN.md 第 11 章）：
  --tasks   : 情境任務檔案路徑（JSONL 格式）
  --system  : 要評估的系統（labsteward / baseline_llm / baseline_rag）
  --k       : pass^k 的 k 值（預設 4，每題重跑 k 次）

Baselines（DESIGN.md 第 11.1 章）：
  B1 baseline_manual : 人工 Excel 流程（由人工記錄結果，不由腳本執行）
  B2 baseline_llm    : 單一 LLM 端到端（無工具）
  B3 baseline_rag    : 純 RAG 問答（有法規、無工具）

TODO：
  [ ] 定義 tasks.jsonl 格式（input, expected_output, applicable_rules, ...）
  [ ] 實作各系統的執行介面
  [ ] 實作 pass^k 計算邏輯
  [ ] 整合 metrics.py 計算各指標
  [ ] 輸出評估報告（CSV / Markdown）
"""

# TODO: 實作評估腳本
