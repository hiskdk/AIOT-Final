# data — 資料資料夾

> **狀態：Proposal 階段，資料為去識別化或合成資料。**
>
> ⚠️ 本資料夾**不得**放入真實財產編號、保管人姓名、位置等個資。
> 公開儲存庫只放去識別化或合成資料（DESIGN.md 第 13 章）。

| 檔案 | 內容 | 狀態 |
|------|------|------|
| `sample_assets.csv` | 去識別化／合成財產清冊（供開發與測試用） | 草案已建立 |
| `market_listings.csv` | 模擬二手掛牌資料（供 M3 殘值估算使用） | 草案已建立 |

## 欄位說明

### sample_assets.csv
對應 `db/schema.sql` 的 `assets` 資料表：
`asset_id, name, spec, category_code, unit_price, purchase_date, status, custodian, location, working, utilization_30d, notes`

### market_listings.csv
對應 `db/schema.sql` 的 `market_listings` 資料表：
`listing_id, category_code, spec, ask_price, listed_at, condition`

注意：掛牌價（ask_price）**非成交價**，殘值估算時應考量此差異（DESIGN.md 第 12.1 章）。
