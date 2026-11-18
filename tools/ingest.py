"""
ingest.py — OCR 與欄位抽取工具（M1）

狀態：☐ Planned（Proposal 階段，尚未實作）

功能（FR-01）：
  - 從發票／報價單 PDF 或照片 OCR 抽取：
      品名、規格、金額、日期、廠商
  - 建議財物分類（對照 knowledge/std_class_table.csv）
  - 輸出財產建檔草稿（需人工確認後寫入資料庫）

注意：
  OCR 結果可能有誤，建議在 UI 顯示原始擷取結果供人工核對。

TODO：
  [ ] 選定 OCR 方案（例如 pdfplumber、pytesseract 或 LLM Vision）
  [ ] 實作 ingest_document(file_path) -> AssetDraft
  [ ] 實作財物分類建議（對照 std_class_table.csv）
  [ ] 整合至 ManagementAgent.M1
"""

# TODO: 實作 IngestTool 類別（OCR + 欄位抽取）
