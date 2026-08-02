# Challenge 001: Diagnostic Task API

## 背景

小規模チームが、個人タスクを記録する社内用APIの最初の版を作り始めています。既存の
コードには利用できる部分がありますが、未実装のAPI、小さな不具合、設計上の粗さが
残っています。仕様に従って、利用可能な最小APIにしてください。

## ユーザーストーリー

- 利用者として、タイトル、説明、優先度を指定してタスクを登録したい。
- 利用者として、タスク一覧と状態別の一覧を確認したい。
- 利用者として、1件を確認・更新・削除したい。
- 利用者として、不正な入力や存在しないタスクに対して、予測可能なHTTP応答を受けたい。

## 機能要件

- タスクは `id`、`title`、`description`、`priority`、`status` を持つ。`id` はサーバーが
  作る正の整数で、作成後に変更しない。
- `title` は必須で、前後の空白を除いた長さが1〜100文字である。空白だけのタイトルは
  無効とする。
- `description` は省略または `null` を許可し、指定時は500文字以下とする。
- `priority` は1〜5の整数で、指定しないときは3とする。
- `status` は `todo`、`in_progress`、`done` のいずれかで、作成時は常に `todo` とする。
- 有効なタスク（`todo` または `in_progress`）では、前後の空白を除いたタイトルが同じ
  タスクを同時に登録できない。重複時は409を返す。`done` のタスクと同名の新規作成は
  許可する。
- 一覧は任意の `status` で絞り込める。作成順で返す。
- 更新では、送られたフィールドだけを変更する。空の更新内容は受け付けない。
- 状態は `todo` から `in_progress` または `done`、`in_progress` から `done` へだけ変更
  できる。`done` の状態は変更できない。許可されない状態変更は409を返す。
- 状態を `done` 以外へ更新した結果、同名の有効タスクが存在する場合は409を返す。
- 存在しないタスクの取得、更新、削除は404を返す。
- 削除成功時は204を返し、応答本文を含めない。
- 入力値の形式・範囲違反は422を返す。API内部の実装エラーを意図的にクライアントへ
  公開しない。

## 非機能要件

- Pythonの型ヒントを、関数・公開モデルの意図が分かる範囲で使うこと。
- 保存はプロセス内メモリだけを使用すること。データベース、ORM、Dockerは不要であり、
  使用しないこと。
- HTTPの入出力と保存・業務ルールを、小規模でも読みやすく分けること。
- 課題終了後に、`submission-notes.md` の設計質問へ文章で回答すること。

## API仕様

| メソッド | パス | 成功時 | 説明 |
| --- | --- | --- | --- |
| `POST` | `/tasks` | 201 | タスクを作成 |
| `GET` | `/tasks` | 200 | タスク一覧。任意の `status` クエリで絞込 |
| `GET` | `/tasks/{task_id}` | 200 | 1件を取得 |
| `PATCH` | `/tasks/{task_id}` | 200 | 指定項目だけを更新 |
| `DELETE` | `/tasks/{task_id}` | 204 | 1件を削除 |

作成リクエスト例:

```json
{
  "title": "Release notes",
  "description": "Prepare the first draft",
  "priority": 2
}
```

作成成功時の応答例:

```json
{
  "id": 1,
  "title": "Release notes",
  "description": "Prepare the first draft",
  "priority": 2,
  "status": "todo"
}
```

更新リクエスト例:

```json
{
  "status": "in_progress",
  "priority": 1
}
```

エラー時は、入力不正なら422、存在しない対象なら404、重複または不正な状態変更なら409を
返す。エラー本文の詳細な形式はFastAPIの標準形式または一貫した独自形式でよい。

## 完了条件

- 仕様の5エンドポイントを実装する。
- 既存コードを読み、小さな不具合を含めて仕様に合うようにする。
- 公開テストが通る。
- 少なくとも2つ、公開テストにない観点のpytestテストを追加する。
- `uv run ruff check .` が通る。
- `submission-notes.md` の記録と設計質問への回答を行う。

## 実施条件

- 制限時間: 90分（休憩を除く）
- 使用可能: エディタ、ターミナル、Git、Python REPL、Python／FastAPI／Pydantic／pytestの
  公式ドキュメント、ローカルテスト、Ruff、エラーログ、デバッガ
- 使用禁止: ChatGPT、Codex、Claude、GitHub Copilot、Cursor等のAI、解答検索、完成コードの
  転用、既存類似実装のコピー

## テストと提出

```bash
uv run pytest
uv run ruff check .
```

終了後に `submission-notes.md` を記入して提出コミットを作成する。

```bash
git add challenges/001-diagnostic-api
git commit -m "feat: submit challenge 001 attempt"
git rev-parse HEAD
```

## 実装後の設計質問

`submission-notes.md` に、次を短く回答する。

1. HTTP層、業務ルール、データ保存をどのように分け、なぜその境界にしたか。
2. PostgreSQLへ移行するなら、どのデータ制約をアプリケーションだけでなくDBでも守るか。
3. 同時リクエストを扱う必要が出た場合、このインメモリ実装のどこに問題が出るか。
4. 今回、時間制限のために優先したことと後回しにしたことは何か。
