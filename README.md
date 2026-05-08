# cross-platform-delivery

`cross-platform-delivery` is a reusable Codex skill for cross frontend/backend/client delivery alignment.

It is designed for:

- new feature delivery across multiple ends
- cross-platform field/state/tracking alignment
- joint debugging
- shared memory and repo memory maintenance
- cross-end review and acceptance checklist generation

## Repository Layout

```text
skills/
  cross-platform-delivery/
    SKILL.md
    agents/openai.yaml
    references/
    examples/
    scripts/
```

This repository uses the `skills/` layout so it can be installed as a multi-skill style repository, even though it currently contains one skill.

## Install

If this repository is published to GitHub, install with:

```bash
npx skills add https://github.com/<owner>/<repo> --skill cross-platform-delivery
```

If the repository is imported into your local Codex skills directory manually, copy:

```text
skills/cross-platform-delivery
```

to:

```text
~/.codex/skills/cross-platform-delivery
```

## What This Skill Does

The skill acts as a delivery orchestrator rather than an end-specific implementation skill.

It helps Codex:

- validate required inputs before coding
- search existing memory and reusable logic first
- produce field/state/tracking mapping tables
- define repo ownership across frontend/backend/client
- drive implementation and joint-debug flow in small steps
- maintain shared business memory and per-repo memory
- run cross-end review and output acceptance checklists

## Best Fit

This skill is especially useful when:

- one person owns frontend, backend, and client work
- the three ends live in different repositories
- requirements need repeated switching between repos
- cross-end consistency matters more than single-end speed

## Typical Prompt

```text
使用 $cross-platform-delivery

frontend_repo: /path/to/frontend
backend_repo: /path/to/backend
client_repo: /path/to/client

需求：会员页新增活动入口
接口：/member/activity/entry
重点：先给我字段映射、仓库归属、联调清单
```

## Included Resources

- `references/quickstart.md`
- `references/delivery_checklist.md`
- `references/mapping_template.md`
- `references/multi_repo_mode.md`
- `references/shared-memory-template.md`
- `references/repo-memory-template.md`
- `references/maintenance.md`
- `references/anti-patterns.md`
- `examples/`
- `scripts/init_delivery_artifacts.py`

## Publish Steps

1. Create a new GitHub repository.
2. Copy the contents of this folder into that repository.
3. Commit and push.
4. Verify the skill path is `skills/cross-platform-delivery/SKILL.md`.
5. Install with `npx skills add https://github.com/<owner>/<repo> --skill cross-platform-delivery`.

## Notes

- `agents/openai.yaml` is included for Codex UI metadata.
- Keep the skill name stable as `cross-platform-delivery`.
- When updating business rules or workflows, update `SKILL.md` and the relevant reference files together.
