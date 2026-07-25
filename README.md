# income-app

Flask と SQLite を使った、収入管理のシンプルな Web アプリです。  
仕事（時給）を登録し、日ごとの勤務時間を記録して、合計稼働時間や収入の把握に使えます。

## 主な機能

- ユーザー登録 / ログイン / ログアウト
- 仕事（job）の追加・削除
- 仕事ごとの勤務時間記録（年月日・時・分）
- 勤務時間レコードの削除
- 仕事ごとの合計稼働時間の表示
- 勤務記録一覧の表示（グラフ表示ページあり）

## 技術スタック

- Python
- Flask
- SQLite
- Matplotlib

## ディレクトリ構成

```text
income-app/
├── income/
│   ├── main.py          # Flask アプリ本体
│   ├── db.py            # テーブル作成処理
│   └── templates/       # 画面テンプレート
├── requirements.txt
└── database_income.db   # SQLite データベース
```

## セットアップ

1. Python 3.10+ を用意
2. 依存関係をインストール

```bash
pip install -r requirements.txt
```

## 起動方法

以下のどちらかで起動できます。

```bash
python -m flask --app income.main run --debug
```

または

```bash
python /home/runner/work/income-app/income-app/income/main.py
```

起動後、ブラウザで `http://127.0.0.1:5000` にアクセスしてください。

## 使い方

1. `/register` でユーザー登録
2. `/login` でログイン
3. `/add_job` で仕事名と時給を登録
4. `/record` から仕事を選んで稼働時間を記録
5. `/overview` で合計時間を確認

## 補足

- データは `database_income.db` に保存されます。
- 初回起動時に必要なテーブルは自動作成されます。

## ライセンス

必要に応じて追記してください。
