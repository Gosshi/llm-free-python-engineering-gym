# LLM-free Python Engineering Gym

LLMを使わずにPython実装を行い、提出後にCodexからレビューを受けるための継続訓練リポジトリです。これは業務用プロダクトではなく、実装・読解・テスト・デバッグ・設計判断を観測し、段階的に回復させるための環境です。

現在の課題は [`challenges/001-diagnostic-api`](challenges/001-diagnostic-api/README.md) のみです。次の課題は、初回の提出とレビュー記録をもとに1件だけ作成します。

## Quick start

```bash
uv venv --python 3.13.0
uv sync --dev
uv run python scripts/verify_environment.py
uv run python scripts/run_challenge.py start
```

通常の検証コマンドです。

```bash
uv run pytest
uv run ruff check .
```

詳細な運用手順は [`docs/workflow.md`](docs/workflow.md)、評価方法は
[`docs/evaluation-rubric.md`](docs/evaluation-rubric.md) を参照してください。
