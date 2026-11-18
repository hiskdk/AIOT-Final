-- db/schema.sql — SQLite 資料表定義
-- 狀態：☐ Planned（Proposal 階段，尚未實作）
-- 來源：DESIGN.md 第 5.2 章

-- 財產清冊
CREATE TABLE IF NOT EXISTS assets (
    asset_id        TEXT PRIMARY KEY,
    name            TEXT NOT NULL,          -- 品名
    spec            TEXT,                   -- 規格
    category_code   TEXT,                   -- 財物分類代碼（對應 std_class_table.csv）
    unit_price      REAL,                   -- 購置單價（NT$）
    purchase_date   TEXT,                   -- 購置日期（ISO 8601）
    status          TEXT NOT NULL           -- IN_STOCK / LENT / REPAIR / PENDING_DISPOSAL / DISPOSED
                    CHECK(status IN ('IN_STOCK','LENT','REPAIR','PENDING_DISPOSAL','DISPOSED')),
    custodian       TEXT,                   -- 保管人（去識別化）
    location        TEXT,                   -- 存放地點
    working         INTEGER NOT NULL        -- 1=可正常運作, 0=故障
                    CHECK(working IN (0,1)),
    utilization_30d REAL,                   -- 近 30 天使用率（0.0–1.0，由系統計算）
    notes           TEXT                    -- 備註
);

-- 借用紀錄
CREATE TABLE IF NOT EXISTS lending (
    lend_id         TEXT PRIMARY KEY,
    asset_id        TEXT NOT NULL REFERENCES assets(asset_id),
    borrower        TEXT NOT NULL,          -- 借用人（去識別化）
    start_ts        TEXT NOT NULL,          -- 借用開始時間（ISO 8601）
    end_ts          TEXT NOT NULL,          -- 預計歸還時間（ISO 8601）
    returned_ts     TEXT,                   -- 實際歸還時間（NULL 表示未歸還）
    approved_by     TEXT                    -- 核准人
);

-- 二手市場掛牌資料（供 M3 殘值估算使用）
CREATE TABLE IF NOT EXISTS market_listings (
    listing_id      TEXT PRIMARY KEY,
    category_code   TEXT,
    spec            TEXT,
    ask_price       REAL,                   -- 掛牌價（NT$，非成交價）
    listed_at       TEXT,                   -- 掛牌日期（ISO 8601）
    condition       TEXT                    -- 狀況：good / fair / poor
                    CHECK(condition IN ('good','fair','poor'))
);

-- 財物標準分類（由 std_class_table.csv 匯入）
CREATE TABLE IF NOT EXISTS std_class (
    category_code   TEXT PRIMARY KEY,
    name_zh         TEXT NOT NULL,
    name_en         TEXT,
    min_life_years  INTEGER NOT NULL,       -- 最低使用年限（年）
    notes           TEXT
);

-- 稽核紀錄（Audit Log）
CREATE TABLE IF NOT EXISTS audit_log (
    log_id          TEXT PRIMARY KEY,
    ts              TEXT NOT NULL,          -- 時間戳（ISO 8601）
    actor           TEXT NOT NULL,          -- 操作人（去識別化）
    role            TEXT NOT NULL,          -- member / manager / pi
    intent          TEXT NOT NULL,          -- 操作意圖（IMPORT / LEND / VALUE / DISPOSE / PROCURE 等）
    input_summary   TEXT,                   -- 輸入摘要
    output_summary  TEXT,                   -- 輸出摘要
    evidence        TEXT,                   -- 引用法規條文或資料來源
    violations      TEXT,                   -- 違規項目（JSON）
    decision        TEXT                    -- APPROVED / REJECTED / PENDING
                    CHECK(decision IN ('APPROVED','REJECTED','PENDING',NULL))
);

-- TODO（實作時）：
-- [ ] 建立索引（asset_id, status, category_code 等）
-- [ ] 實作 db/init.py --sample 以合成資料初始化
-- [ ] 確認所有寫入路徑均經工具 + 人工核准 + 稽核紀錄
