# Short review requests

The detailed first-review procedure is stored in
[`skills/llm-free-first-review/SKILL.md`](../skills/llm-free-first-review/SKILL.md) and is
required by `AGENTS.md`. After committing a submission, a short request is sufficient:

```text
課題001を第1段階レビューしてください。開始タグは challenge-001-start、提出コミットは HEAD です。
```

To review a specific commit rather than the current branch tip, replace `HEAD` with that commit
SHA. Codex must still read the challenge documents and follow the no-patch first-review policy.
