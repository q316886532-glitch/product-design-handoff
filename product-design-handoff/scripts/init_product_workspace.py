#!/usr/bin/env python3
"""Initialize a product-design handoff workspace from bundled templates."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create docs/, AGENTS.md, and README.md for a product design handoff workspace."
    )
    parser.add_argument(
        "target_dir",
        nargs="?",
        default=".",
        help="Project directory to initialize. Defaults to the current directory.",
    )
    parser.add_argument(
        "--project-name",
        default=None,
        help="Project name used in template headings. Defaults to the target directory name.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow replacing existing files. Without this flag, existing files are never overwritten.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned writes and conflicts without changing files.",
    )
    return parser.parse_args()


def iter_template_paths(template_root: Path) -> list[Path]:
    return sorted(path for path in template_root.rglob("*") if path.is_file())


def render_template(text: str, project_name: str) -> str:
    replacements = {
        "{{PROJECT_NAME}}": project_name,
        "{{DATE}}": date.today().isoformat(),
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text


def destination_is_blocked(dest: Path, target_root: Path) -> bool:
    if dest.exists():
        return True

    if target_root.exists() and not target_root.is_dir():
        return True

    relative = dest.relative_to(target_root)
    cursor = target_root
    for part in relative.parts[:-1]:
        cursor = cursor / part
        if cursor.exists() and not cursor.is_dir():
            return True

    return False


def find_conflicts(template_files: list[Path], template_root: Path, target_root: Path) -> list[Path]:
    conflicts: list[Path] = []
    for src in template_files:
        dest = target_root / src.relative_to(template_root)
        if destination_is_blocked(dest, target_root):
            conflicts.append(dest)
    return conflicts


def main() -> int:
    args = parse_args()
    skill_root = Path(__file__).resolve().parents[1]
    template_root = skill_root / "assets" / "project-template"
    target_root = Path(args.target_dir).expanduser().resolve()
    project_name = args.project_name or target_root.name

    if not template_root.is_dir():
        print(f"Template directory not found: {template_root}", file=sys.stderr)
        return 1

    template_files = iter_template_paths(template_root)
    conflicts = find_conflicts(template_files, template_root, target_root)

    if conflicts and not args.overwrite:
        print(
            "Refusing to overwrite or write through existing files. Re-run with --overwrite only if replacement is intended.",
            file=sys.stderr,
        )
        for path in conflicts:
            print(f"  {path}", file=sys.stderr)
        return 2

    planned = [target_root / src.relative_to(template_root) for src in template_files]
    if args.dry_run:
        print(f"Would initialize product workspace at: {target_root}")
        for path in planned:
            marker = "overwrite" if path.exists() else "create"
            print(f"  {marker}: {path}")
        return 0

    target_root.mkdir(parents=True, exist_ok=True)
    for src in template_files:
        dest = target_root / src.relative_to(template_root)
        dest.parent.mkdir(parents=True, exist_ok=True)
        text = src.read_text(encoding="utf-8")
        dest.write_text(render_template(text, project_name), encoding="utf-8")

    print(f"Initialized product workspace at: {target_root}")
    for path in planned:
        print(f"  wrote: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
