#!/usr/bin/env python3
"""
Generate delivery artifacts for cross-platform alignment.

Usage:
  python3 scripts/init_delivery_artifacts.py --name websocket-popup
"""

from __future__ import annotations

import argparse
from pathlib import Path


MAPPING_TEMPLATE = """# Mapping

| Design Meaning | Frontend Field/State | Backend Field | Client Field | Tracking Field | Empty Fallback | Error Fallback | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
"""


SPEC_TEMPLATE = """# Spec

## Background
- 

## Scope
- 

## Entry
- 

## Source of Truth
- code:
- api/schema:
- spec owner:

## Core Models
- 

## State Flow
- 

## API Mapping
- 

## Tracking
- 

## Risks
- 

## Regression
- 
"""


ACCEPTANCE_TEMPLATE = """# Acceptance Checklist

## Covered
- 

## Risks
- 

## Minimum Regression Path
- 

## Joint Debug Cases
- 
"""


OWNERSHIP_TEMPLATE = """# Ownership

| Item | Frontend Repo | Backend Repo | Client Repo | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
"""


SPEC_DIR_FILES = {
    "overview.md": """# Overview

## Background
- 

## Scope
- 

## Entry
- 

## Source of Truth
- code:
- api/schema:
- spec owner:

## Core Models
- 
""",
    "rules.md": """# Rules

## Display Rules
- 

## Interaction Rules
- 

## State Machine
- 

## Idempotency / Dedup
- 

## Fallback / Degrade
- 
""",
    "tracking.md": """# Tracking

## Events
- 

## Trigger Timing
- 

## Field Sources
- 

## No-report Conditions
- 
""",
    "acceptance.md": """# Acceptance

## Covered
- 

## Risks
- 

## Minimum Regression Path
- 

## Joint Debug Cases
- 
""",
}


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True, help="Feature or domain name, e.g. websocket-popup")
    parser.add_argument(
        "--output-dir",
        default="artifacts",
        help="Output directory relative to current working directory",
    )
    parser.add_argument(
        "--spec-mode",
        choices=("flat", "dir"),
        default="flat",
        help="Generate a single spec.md file or a spec/ directory template",
    )
    args = parser.parse_args()

    root = Path.cwd() / args.output_dir / args.name
    write_file(root / "mapping.md", MAPPING_TEMPLATE)
    if args.spec_mode == "flat":
        write_file(root / "spec.md", SPEC_TEMPLATE)
        write_file(root / "acceptance.md", ACCEPTANCE_TEMPLATE)
    else:
        spec_root = root / "spec"
        for filename, content in SPEC_DIR_FILES.items():
            write_file(spec_root / filename, content)
    write_file(root / "ownership.md", OWNERSHIP_TEMPLATE)
    print(root)


if __name__ == "__main__":
    main()
