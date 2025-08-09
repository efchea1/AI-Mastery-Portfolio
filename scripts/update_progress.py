#!/usr/bin/env python3
"""
Update the Progress Tracker table in README.md.

Modes:
  - json   : read statuses from weeks_status.json
  - commit : parse last commit message like 'week-7: done' or 'week 3: start'

Examples:
  python scripts/update_progress.py --mode json --status weeks_status.json --readme README.md
  python scripts/update_progress.py --mode commit --readme README.md
"""

from __future__ import annotations
import argparse, json, os, re, subprocess
from pathlib import Path
from typing import Dict

# Normalized status keywords -> rendered text
RENDER = {
    "not_started": "⬜ Not Started",
    "in_progress": "🟨 In Progress",
    "done":        "✅ Completed",
}

VALID = set(RENDER.keys())

# Regex that finds the Progress Tracker rows that begin with '|  1', '|  2', ... '| 22'
ROW_RE = re.compile(r'^\|\s*(\d{1,2})\s*\|', re.M)

def load_status_from_json(path: Path) -> Dict[int, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    out: Dict[int, str] = {}
    for k, v in data.items():
        try:
            wk = int(k)
        except ValueError:
            continue
        norm = v.strip().lower().replace(" ", "_")
        if norm in VALID:
            out[wk] = norm
    return out

def parse_status_from_commit() -> Dict[int, str]:
    """
    Parse last commit message for tokens like:
      week-7: done
      week 3: in_progress
      week12 done
    """
    try:
        msg = subprocess.check_output(["git", "log", "-1", "--pretty=%B"], text=True).strip()
    except Exception:
        msg = ""
    statuses: Dict[int, str] = {}
    # accept 'week-7', 'week 7', 'wk7', 'w7'
    wk_re = re.compile(r'\b(?:week|wk|w)[\s\-]*(\d{1,2})\b', re.I)
    # accept ': done', '-> in progress', 'start', 'progress', 'done'
    status_re = re.compile(r'\b(done|complete|completed|in[_\-\s]?progress|start|started|not[_\-\s]?started)\b', re.I)

    # Try to map the first status keyword that appears after each week mention
    tokens = msg.splitlines()
    for line in tokens:
        weeks = wk_re.findall(line)
        st = status_re.search(line)
        if not weeks or not st:
            continue
        raw = st.group(1).lower().replace("-", "_").replace(" ", "_")
        if raw in ("completed", "complete"):
            norm = "done"
        elif raw in ("start", "started"):
            norm = "in_progress"   # starting implies in_progress
        elif raw in ("not_started",):
            norm = "not_started"
        elif raw in ("in_progress",):
            norm = "in_progress"
        elif raw in ("done",):
            norm = "done"
        else:
            continue
        for w in weeks:
            try:
                wk = int(w)
                statuses[wk] = norm
            except ValueError:
                pass
    return statuses

def replace_table(readme_text: str, updates: Dict[int, str]) -> str:
    """
    Replace the Status column for any week numbers present in `updates`.
    Assumes the table has rows like:
      | 1 | Python Basics ... | ⬜ Not Started |
    We split each matching row on '|' and replace the last cell with rendered text.
    """
    lines = readme_text.splitlines()
    for i, line in enumerate(lines):
        m = ROW_RE.match(line)
        if not m:
            continue
        wk = int(m.group(1))
        if wk not in updates:
            continue
        # split cells, keep leading/trailing pipes
        parts = [p.strip() for p in line.split("|")]
        # Expected minimal columns: ['', '1', 'Week title', 'Status', '']
        if len(parts) < 4:
            continue
        # Status is the penultimate non-empty cell (usually index -2)
        parts[-2] = RENDER[updates[wk]]
        # Rebuild line with single spaces around pipes
        new_line = " | ".join(parts)
        lines[i] = new_line
    return "\n".join(lines) + ("\n" if not readme_text.endswith("\n") else "")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["json", "commit"], required=True)
    ap.add_argument("--status", type=Path, help="Path to weeks_status.json (json mode)")
    ap.add_argument("--readme", type=Path, default=Path("README.md"))
    args = ap.parse_args()

    if args.mode == "json":
        if not args.status or not args.status.exists():
            raise SystemExit("weeks_status.json not found — pass --status path")
        updates = load_status_from_json(args.status)
    else:
        updates = parse_status_from_commit()

    if not updates:
        print("No status updates detected. Exiting.")
        return

    rdme_text = args.readme.read_text(encoding="utf-8")
    new_text = replace_table(rdme_text, updates)

    if new_text != rdme_text:
        args.readme.write_text(new_text, encoding="utf-8")
        print("README updated.")
    else:
        print("README already up to date.")

if __name__ == "__main__":
    main() 

###