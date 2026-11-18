# LabSteward

> **實驗室財產管理 AI Agent**
> AI Agent × 實驗室財產管理 × 採購法規 × 數據分析 × 人工審核

| 項目 | 內容 |
|------|------|
| 專案階段 | Proposal（尚未實作） |
| 課程 | 物聯網（IoT）期末專題 |
| 組員 | 潘兆邠、邱冠霖、林浚偉、張皓崴、黃翊豪 |

---

## 專題簡介

大學實驗室長期面臨「買了不用、用了不登記、壞了不報廢」的困境。  
**LabSteward** 是一個整合 LLM、RAG、規則引擎與確定性分析工具的 **Domain AI Agent**，能夠：

- 以自然語言查詢財產清冊與借用狀態
- 採購前強制查詢庫存與閒置資源（先共享，再採購）
- 雙軌殘值估計（帳面價值 + 市場價值）
- 合規檢核（台灣政府採購法門檻、財物管理辦法年限）
- 產出可直接送審的 Word 採購清單 / 報廢申請草稿
- 所有具法律效力的動作需人工核准並寫入稽核紀錄

---

## 系統架構（八階段）

```
① User/Application Scenario
→ ② Query/Input（自然語言 / PDF / 照片）
→ ③ Planner & Reasoning Agent（LLM + ReAct + Tool Calling）
→ ④ Data Acquisition/Retrieval（SQLite / 網頁搜尋）
→ ⑤ Analytics Engine（殘值模型 / 商品比對 / TCO）
→ ⑥ Domain Knowledge Integration（RAG 法規庫 + rules.yaml）
→ ⑦ Decision/Recommendation（Guardrail → 人工核准）
→ ⑧ Output & Interaction（Word / Excel / Audit Log）
```

詳細設計請見 [DESIGN.md](./DESIGN.md)。

---

## 儲存庫結構

```
labsteward/
├── README.md
├── DESIGN.md                      # 系統設計文件（持續維護）
├── agent/
│   ├── planner.py                 # Planner Agent（③）[Planned]
│   ├── management_agent.py        # 管理子 Agent M1–M4 [Planned]
│   ├── procurement_agent.py       # 採購子 Agent P1–P4 [Planned]
│   └── guardrail.py               # 規則檢核與人工審核（⑦）[Planned]
├── tools/
│   ├── inventory.py               # query_inventory [Planned]
│   ├── lending.py                 # 借用／租用 [Planned]
│   ├── valuation.py               # 雙軌殘值（M3）[Planned]
│   ├── web_search.py              # Playwright 搜尋 [Planned]
│   ├── docgen.py                  # Word / Excel 輸出 [Planned]
│   ├── ingest.py                  # OCR 欄位抽取（M1）[Planned]
│   ├── entity_match.py            # 商品實體比對 [Planned]
│   ├── rag.py                     # 混合檢索 BM25 + 向量 [Planned]
│   └── audit.py                   # Audit Log [Planned]
├── knowledge/
│   ├── regulations/               # 法規與校內規範（切塊來源）
│   ├── rules.yaml                 # 門檻與年限規則（可設定）
│   └── std_class_table.csv        # 財物標準分類（最低使用年限）
├── db/
│   └── schema.sql                 # SQLite 資料表定義 [Planned]
├── data/
│   ├── sample_assets.csv          # 去識別化／合成財產清冊
│   └── market_listings.csv        # 二手掛牌資料（模擬）
├── eval/
│   ├── tasks.jsonl                # 情境任務與標準答案（約 50 題）[Planned]
│   ├── run_eval.py                # 評估腳本 [Planned]
│   └── metrics.py                 # 指標計算 [Planned]
└── app/
    └── streamlit_app.py           # Web 介面 [Planned]
```

---

## Installation（預定）

> ⚠️ 此區段為 Proposal 階段預定指令，程式完成後更新。

```bash
git clone https://github.com/hiskdk/AIOT-Final.git labsteward
cd labsteward
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env             # 填入 LLM API 金鑰
python -m db.init --sample       # 建立 SQLite（合成資料）
streamlit run app/streamlit_app.py
```

---

## How to Run（預定）

```bash
# 執行評估
python eval/run_eval.py --tasks eval/tasks.jsonl --system labsteward --k 4
python eval/run_eval.py --tasks eval/tasks.jsonl --system baseline_llm --k 4
python eval/run_eval.py --tasks eval/tasks.jsonl --system baseline_rag --k 4
```

Demo 情境：「為新進學生準備一台深度學習工作站」  
→ 查庫存 → 比價 → 門檻判定 → 輸出採購清單

---

## 專案進度

| 週次 | 工作項目 | 狀態 |
|------|----------|------|
| W1–W2 | Proposal、GitHub、DESIGN.md 初版；法規知識庫與 rules.yaml | ✅ Proposal 階段 |
| W3–W4 | 財產資料庫、M1 導入、M2 借用登記 | ⏳ Planned |
| W5–W6 | M3 殘值模型、M4 報廢；二手資料蒐集 | ⏳ Planned |
| W7–W8 | P1–P4 採購模組、商品比對、文件輸出 | ⏳ Planned |
| W9–W10 | 實驗評估、Baseline 比較、Final PPT 與 Demo 影片 | ⏳ Planned |

---

## 重要說明

- 本儲存庫**不含**真實財產編號、保管人姓名等個資，僅使用去識別化或合成資料。
- LLM API 金鑰放在 `.env`，已加入 `.gitignore`，**不會提交**。
- 所有具法律效力的操作（採購確認、報廢確認）**需人工核准**。
- 本系統只引用法規規則並標示來源，**不提供法律意見**。

---

## 相關文件

- [DESIGN.md](./DESIGN.md)：完整系統設計文件
- Proposal Document：`labsteward-proposal.pdf`（不含於公開儲存庫）
