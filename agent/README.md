# Agent 模組

> **狀態：Proposal 階段，所有模組均為 Planned，尚未實作。**
>
> 本資料夾包含 LabSteward 的四個核心 Python 模組：
>
> | 檔案 | 功能 | 架構編號 | 狀態 |
> |------|------|----------|------|
> | `planner.py` | Planner & Reasoning Agent（LLM + ReAct + Tool Calling） | ③ | ☐ Planned |
> | `management_agent.py` | 管理子 Agent（M1 導入、M2 借用、M3 殘值、M4 報廢） | M1–M4 | ☐ Planned |
> | `procurement_agent.py` | 採購子 Agent（P1 確認需求、P2 查庫存、P3 比價、P4 清單） | P1–P4 | ☐ Planned |
> | `guardrail.py` | 規則檢核與人工審核節點 | ⑦ | ☐ Planned |
>
> 詳細設計請見 [DESIGN.md](../DESIGN.md) 第 4 章（Components）與第 8 章（Algorithm）。
