# cross-platform-delivery

`cross-platform-delivery` is a portable multi-agent skill repository for cross frontend, backend, and client delivery alignment.

It is designed for:

- new feature delivery across multiple ends
- cross-platform field, state, and tracking alignment
- joint debugging across repos
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

This repository follows the `skills/` layout so it can be installed by compatible skill installers and mapped into different agent skill directories.

## Install

Install from GitHub with:

```bash
npx skills add https://github.com/qiqiw124/cross-platform-delivery.git --skill cross-platform-delivery
```

The installer may ask which local agent skill directory to use. That selection only affects the local install target and does not change the portability of this repository.

If you want to install manually for Codex, copy:

```text
skills/cross-platform-delivery
```

to:

```text
~/.codex/skills/cross-platform-delivery
```

## What This Skill Does

This skill acts as a delivery orchestrator rather than an end-specific implementation skill.

It helps the agent:

- validate required inputs before coding
- search existing memory and reusable logic first
- produce field, state, and tracking mapping tables
- define repo ownership across frontend, backend, and client
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

## Recommended Published Contents

For a clean public repository, keep:

- `README.md`
- `skills/cross-platform-delivery/**`

Local installer artifacts such as `.agents/` or `skills-lock.json` do not need to be committed to the public repository.

## Notes

- `agents/openai.yaml` is included for Codex and compatible UI metadata.
- Keep the skill name stable as `cross-platform-delivery`.
- When updating business rules or workflows, update `SKILL.md` and the relevant reference files together.
