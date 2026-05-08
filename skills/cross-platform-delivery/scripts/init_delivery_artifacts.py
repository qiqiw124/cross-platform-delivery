#!/usr/bin/env python3
"""
Generate lightweight delivery artifacts for cross-platform alignment.

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


MEMORY_TEMPLATE = """# Business Memory

## Background
- 

## Entry
- 

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
    args = parser.parse_args()

    root = Path.cwd() / args.output_dir / args.name
    write_file(root / "mapping.md", MAPPING_TEMPLATE)
    write_file(root / "memory.md", MEMORY_TEMPLATE)
    write_file(root / "acceptance.md", ACCEPTANCE_TEMPLATE)
    write_file(root / "ownership.md", OWNERSHIP_TEMPLATE)
    print(root)


if __name__ == "__main__":
    main()
