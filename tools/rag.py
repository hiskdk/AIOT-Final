"""
rag.py — 混合檢索工具（架構編號 ⑥）

狀態：☐ Planned（Proposal 階段，尚未實作）

功能（FR-10）：
  - 以 BM25 + 向量檢索（FAISS 或 Chroma）+ 數值過濾，
    從法規條文與財產資料中取回相關段落
  - 知識庫來源（knowledge/regulations/）：
      * 國立雲林科技大學財物管理辦法 [13]
      * 行政院財物標準分類 [14]
      * 國立臺灣大學請購作業規範 [15]
      * 其他校內規範（TBD）
  - 每個建議必須附上引用的條文或資料來源（FR-10）

設計說明（來自 DESIGN.md 第 6.4 章）：
  混合檢索（BM25 + 向量）提升法規條文命中率 [9]。
  Agentic RAG：由 Agent 決定檢索策略 [8]。

TODO：
  [ ] 建立法規文件切塊（chunk）與索引
  [ ] 實作 BM25 索引（rank-bm25）
  [ ] 實作向量索引（FAISS 或 Chroma + embedding model）
  [ ] 實作混合排序（RRF 或加權融合）
  [ ] 實作數值過濾（金額門檻、年限）
  [ ] 整合至 Guardrail 與 Planner
"""

# TODO: 實作 RAGTool 類別（BM25 + 向量混合檢索）
