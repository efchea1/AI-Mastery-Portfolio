import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
readme = ROOT / "README.md"

# map from status keyword to table text
STATUS = {
    "not-started": "⬜ Not Started",
    "in-progress": "🟨 In Progress",
    "done": "✅ Completed",
}

def parse_commit_message(msg_path: pathlib.Path):
    text = msg_path.read_text(encoding="utf-8", errors="ignore")
    m_week = re.search(r"\[week-(\d{1,2})\]", text, re.IGNORECASE)
    m_status = re.search(r"status\s*:\s*(not-started|in-progress|done)", text, re.IGNORECASE)
    if not (m_week and m_status):
        return None, None
    week = int(m_week.group(1))
    status_key = m_status.group(1).lower()
    return week, status_key

def update_table(week: int, status_key: str):
    content = readme.read_text(encoding="utf-8")
    start = content.find("<!-- PROGRESS_TABLE_START -->")
    end   = content.find("<!-- PROGRESS_TABLE_END -->")
    if start == -1 or end == -1:
        print("Progress markers not found; skipping.")
        return False

    table = content[start:end]
    # pattern to match a row starting with | <week> |
    row_re = re.compile(rf"(\|\s*{week}\s*\|\s*[^|]*\|\s*)([^|]*)(\s*\|)", re.MULTILINE)
    if not row_re.search(table):
        print(f"Week {week} row not found; skipping.")
        return False

    new_table = row_re.sub(rf"\1{STATUS[status_key]}\3", table)
    new_content = content[:start] + new_table + content[end:]
    if new_content != content:
        readme.write_text(new_content, encoding="utf-8")
        print(f"Updated Week {week} → {STATUS[status_key]}")
        return True
    return False

def main():
    if len(sys.argv) < 2:
        sys.exit(0)
    msg_path = pathlib.Path(sys.argv[1])
    week, status_key = parse_commit_message(msg_path)
    if week is None:
        print("No [week-NN] or status:... found; no progress update.")
        return
    updated = update_table(week, status_key)
    if not updated:
        print("No changes applied.")

if __name__ == "__main__":
    main()
