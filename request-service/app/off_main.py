from fastapi import FastAPI
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# -----------------------------------------------------------------
# ★ CORS設定の追加 (ここから)
# -----------------------------------------------------------------
origins = [
    "http://localhost",
    "http://localhost:3000", # フロントエンドが動作しているオリジン
    "http://127.0.0.1:3000",
    # OpenShiftデプロイ後に追加する予定のURL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,         # 許可するオリジン
    allow_credentials=True,        # クッキーなどの資格情報を許可
    allow_methods=["*"],           # すべてのHTTPメソッドを許可
    allow_headers=["*"],           # すべてのヘッダーを許可
)
# -----------------------------------------------------------------
# ★ CORS設定の追加 (ここまで)
# -----------------------------------------------------------------

# DB接続ロジック（このステップでは省略し、ダミーデータを使用）
# 実際にはここでDB接続とスキーマ定義が必要です。

DUMMY_REQUESTS: List[Dict] = [
    {
        "id": 1,
        "title": "ダミー曲 その1",
        "artist": "ダミーアーティストA",
        "requester_name": "あちきラジオ大好き！",
        "is_played": False,
    },
    {
        "id": 2,
        "title": "ダミー曲 その2",
        "artist": "ダミーアーティストB",
        "requester_name": "通りすがりの名無し人",
        "is_played": True,
    },
]

@app.get("/requests")
def get_requests():
    """リクエスト一覧を取得するエンドポイント"""
    return DUMMY_REQUESTS

# Health Check (OpenShift Liveness/Readiness Probe用)
@app.get("/health")
def health_check():
    return {"status": "ok"}
