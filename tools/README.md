# Tools 模組

> **狀態：Proposal 階段，所有工具均為 Planned，尚未實作。**

本資料夾包含 LabSteward 的 8 項核心工具（來自 DESIGN.md 第 4.8 章）：

| 工具檔案 | 功能 | 對應模組 | 狀態 |
|----------|------|----------|------|
| `inventory.py` | 在庫／閒置／可移撥查詢（`query_inventory`） | P2、FR-09 | ☐ Planned |
| `lending.py` | 借用單建立、衝突檢查、到期提醒 | M2 | ☐ Planned |
| `valuation.py` | 雙軌殘值估算（帳面 + 市場） | M3 | ☐ Planned |
| `web_search.py` | 電商與共同供應契約搜尋（Playwright + 搜尋 API） | P3 | ☐ Planned |
| `docgen.py` | Word / Excel 文件輸出（python-docx / openpyxl） | P4、M4、M2 | ☐ Planned |
| `ingest.py` | OCR 與欄位抽取、財物分類建議 | M1 | ☐ Planned |
| `entity_match.py` | 商品實體比對與去重 | P3 | ☐ Planned |
| `rag.py` | 混合檢索（BM25 + 向量 FAISS/Chroma） | ⑥ | ☐ Planned |
| `audit.py` | Audit Log 寫入與查詢 | ⑧ | ☐ Planned |
