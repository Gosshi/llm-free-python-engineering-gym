# Workflow

## 初回セットアップ

リポジトリ直下で実行する。

```bash
uv venv --python 3.13.0
uv sync --dev
uv run python scripts/verify_environment.py
```

`uv` が利用できない環境では、Python 3.13系を用意してから次を使う。

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

## 課題の開始

開始前に環境を確認し、開始タグの存在を確認する。

```bash
uv run python scripts/verify_environment.py
git show --no-patch challenge-001-start
uv run python scripts/run_challenge.py start
```

最後のコマンドが表示する時刻を `submission-notes.md` の開始時刻に記録し、90分のタイマー
を自分で開始する。休憩は開始・終了をメモして実作業時間から除く。課題中はエディタ、
ターミナル、Git、Python REPL、ローカルテスト、Ruff、デバッガ、エラーログ、および
Python／FastAPI／Pydantic／pytestの公式ドキュメントを使用できる。

ChatGPT、Codex、Claude、GitHub Copilot、Cursor等のAI、解答を探す検索、完成コードの転用、
既存の類似実装のコピーは使用しない。公式ドキュメントを確認した範囲は提出ノートへ残す。

## 実装中の確認

```bash
uv run pytest
uv run ruff check .
```

必要なら、対象を絞って実行できる。

```bash
uv run pytest challenges/001-diagnostic-api/tests
uv run ruff check challenges/001-diagnostic-api/src
```

## 提出

時間終了後、`submission-notes.md` を記入し、変更内容を確認して提出コミットを作成する。

```bash
git status
git diff --check
git add challenges/001-diagnostic-api
git commit -m "feat: submit challenge 001 attempt"
git rev-parse HEAD
```

Codexには開始タグと提出コミットを渡して第1段階レビューを依頼する。Codexは差分確認、
仕様に基づく追加テスト、レビュー、採点を行うが、修正コードは示さない。

修正後は同様にコミットを作る。

```bash
git add challenges/001-diagnostic-api
git commit -m "fix: revise challenge 001 submission"
git rev-parse HEAD
```

第2段階レビュー後、必要なら `progress/template.md` を複製して結果を記録する。明示的に
模範解答を求める場合だけ、第3段階レビューを依頼する。
