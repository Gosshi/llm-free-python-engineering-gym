---
name: llm-free-first-review
description: Perform the first-stage review of a completed LLM-free Python engineering-gym challenge. Use when the user asks to review a submitted gym challenge, requests a 第1段階レビュー, or asks for the diagnostic challenge review without repeating the review procedure.
---

# LLM-free challenge first review

Act as a reviewer and evaluator, never as the submitter's implementation proxy.

## Required reading

Before any review action, read these repository files for the requested challenge number:

1. `AGENTS.md`
2. `docs/background.md`
3. `docs/review-policy.md`
4. `docs/evaluation-rubric.md`
5. `challenges/<number>-<name>/README.md`
6. `challenges/<number>-<name>/submission-notes.md`

## Evidence collection

1. Confirm the requested start tag exists. Record its exact name and commit.
2. Identify the submitted commit as `HEAD`. Record its SHA.
3. Inspect the start-tag-to-HEAD diff and list changed files before making review files.
4. Run the public test command and Ruff command documented by the repository.
5. Run mypy only when it is configured in `pyproject.toml` or explicitly enabled for the
   challenge. Otherwise record `not configured`.
6. Derive additional tests only from the written specification. Cover applicable boundary
   values, invalid input, missing resources, duplicates, state transitions, exception paths,
   data independence, and unintended side effects.
7. Save those tests under `reviews/` and run them explicitly. They may be added after
   submission, but never modify files under the user's implementation source directory.
8. Read the submission notes and use them as supporting evidence, not as a substitute for
   tests or code inspection.

## Review output and persistence

Save the full first review as `reviews/<number>-first-review.md`. Save a provisional progress
record derived from `progress/template.md` as `progress/<number>.md`. Mark observations as
unobserved instead of inventing a score when the challenge did not exercise an ability.

Include all of the following:

- Execution information: start tag and commit, commands, public/additional-test/Ruff/mypy
  results.
- Requirement evaluation: met, partly met, unmet, misunderstood, and implemented-but-different
  behavior.
- Bugs, each with severity (`Critical`, `High`, `Medium`, or `Low`), reproduction, expected and
  actual behavior, plus code or test evidence.
- Code evaluation: Python basics, data structures, functions, classes/models, types, naming,
  readability, responsibility and module boundaries, duplication, error handling, and ease of
  change.
- API evaluation: endpoints, HTTP methods/statuses, validation, response and error models,
  missing resources, duplicates, and state transitions.
- Test evaluation: normal, invalid, boundary, independence, naming, Arrange-Act-Assert clarity,
  coupling to implementation, and missing coverage.
- Design evaluation: requirement decomposition, data model, separation, persistence migration,
  dependency direction, trade-offs, and over/under-design.
- Security and performance: invalid input, information disclosure, shared mutable state, data
  destruction, needless scans/copies, and obvious performance problems. Explicitly say when no
  issue is found within scope.
- Rubric scores (0–10) and code/test evidence for every observable criterion; distinguish current
  strengths, clear weaknesses, insufficient evidence, Python-specific gaps, general engineering
  gaps, and likely time-limit effects.
- A final summary: largest weakness, best point, whether the root issue is Python syntax,
  decomposition, or design, what can and cannot yet be concluded about LLM-free implementation,
  up to three next assessment targets, recommended next challenge format, and time limit. Never
  infer senior, tech-lead, or EM level from one challenge.

## Hint policy

For every major issue, give three progressively more actionable, non-code hints:

1. **Hint 1:** name the relevant file, feature, or observation point.
2. **Hint 2:** name the specification clause and concept or test category to inspect.
3. **Hint 3:** describe the correction direction in prose only.

Do not include replacement code, pseudocode that is directly translatable to a patch, a patch,
a model answer, or implementation edits. Do not write tests designed merely to force one
particular implementation.
