# cross-platform-delivery

`cross-platform-delivery` is a portable multi-agent skill repository for cross frontend, backend, and client delivery alignment.

It is designed for:

- new feature delivery across multiple ends
- cross-platform field, state, and tracking alignment
- joint debugging across repos
- shared spec and repo spec maintenance
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

## How to Use

After installation, invoke the skill in your agent prompt with:

```text
使用 $cross-platform-delivery
```

Then provide only the inputs that matter for the current task. The minimum useful inputs are usually:

- participating repos: `frontend_repo`, `backend_repo`, `client_repo`
- requirement summary
- API or schema reference
- tracking / analytics rules
- current concern: new feature, joint debug, or review

## Usage Workflow

The intended workflow is:

1. use `cross-platform-delivery` to align requirements first
2. let the agent read code, schema, tests, and existing spec
3. produce mapping / ownership / delivery plan
4. enter end-specific implementation
5. return to cross-platform review and acceptance

This skill is best used as an orchestrator, not as a replacement for end-specific implementation skills.

## Common Prompt Patterns

### 1. New Feature

```text
使用 $cross-platform-delivery

frontend_repo: /path/to/frontend
backend_repo: /path/to/backend
client_repo: /path/to/client

需求：会员页新增活动入口
接口：/member/activity/entry
重点：先给我字段映射、仓库归属、联调清单
```

### 2. Joint Debug

```text
使用 $cross-platform-delivery

frontend_repo: /path/to/frontend
backend_repo: /path/to/backend
client_repo: /path/to/client

现象：客户端按钮不可点击，但接口返回正常
重点：按前端、后端、客户端分层排查，并给最小验证路径
```

### 3. Cross-End Review

```text
使用 $cross-platform-delivery

frontend_repo: /path/to/frontend
backend_repo: /path/to/backend
client_repo: /path/to/client

基于当前改动，帮我做一轮跨端 review，并补 spec 缺口与验收清单
```

## What This Skill Does

This skill acts as a delivery orchestrator rather than an end-specific implementation skill.

It helps the agent:

- validate required inputs before coding
- search existing code, contracts, specs, and reusable logic first
- produce field, state, and tracking mapping tables
- define repo ownership across frontend, backend, and client
- drive implementation and joint-debug flow in small steps
- maintain shared business spec and per-repo spec
- run cross-end review and output acceptance checklists

## Best Fit

This skill is especially useful when:

- one person owns frontend, backend, and client work
- the three ends live in different repositories
- requirements need repeated switching between repos
- cross-end consistency matters more than single-end speed

## Included Resources

- `references/quickstart.md`
- `references/delivery_checklist.md`
- `references/mapping_template.md`
- `references/multi_repo_mode.md`
- `references/shared-spec-template.md`
- `references/repo-spec-template.md`
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
