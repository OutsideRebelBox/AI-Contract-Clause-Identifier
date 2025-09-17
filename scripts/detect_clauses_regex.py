# scripts/detect_clauses_regex.py
from pathlib import Path
import re, json, pandas as pd

# --- Paths ---
HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
CONTRACTS_DIR = ROOT / "contracts"
CONFIG_PATH = HERE / "target_clauses.json"
OUTPUTS_DIR = ROOT / "outputs"
OUTPUTS_DIR.mkdir(exist_ok=True)

# --- Load clause patterns ---
with open(CONFIG_PATH, "r", encoding="utf-8") as f:
    CLAUSE_PATTERNS = json.load(f)

# Compile regexes (case-insensitive)
COMPILED = {k: re.compile(v, flags=re.IGNORECASE) for k, v in CLAUSE_PATTERNS.items()}

# --- Helpers to extract text from different file types ---
def extract_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".txt":
        return path.read_text(errors="ignore", encoding="utf-8", newline=None)
    if suffix == ".docx":
        try:
            import docx  # python-docx
        except ImportError:
            raise SystemExit("Install dependency: pip install python-docx")
        doc = docx.Document(path)
        return "\n".join(p.text for p in doc.paragraphs)
    if suffix == ".pdf":
        try:
            import pdfplumber
        except ImportError:
            raise SystemExit("Install dependency: pip install pdfplumber")
        text_chunks = []
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                text_chunks.append(page.extract_text() or "")
        return "\n".join(text_chunks)
    # Old .doc not supported—convert to .docx first.
    return ""

def paragraphs(text: str):
    # Split on blank lines or hard breaks
    return [p.strip() for p in re.split(r"\n\s*\n+", text) if p.strip()]

def find_matches(file_path: Path):
    text = extract_text(file_path)
    if not text:
        return []
    rows = []
    for i, para in enumerate(paragraphs(text), start=1):
        for clause, rx in COMPILED.items():
            if rx.search(para):
                snippet = (para[:220] + "…") if len(para) > 220 else para
                rows.append({
                    "file": file_path.name,
                    "clause": clause,
                    "paragraph": i,
                    "snippet": snippet
                })
    return rows

def main():
    all_rows = []
    for path in sorted(CONTRACTS_DIR.iterdir()):
        if path.suffix.lower() in {".txt", ".docx", ".pdf"}:
            all_rows.extend(find_matches(path))
        else:
            print(f"Skipping unsupported file (convert to .docx): {path.name}")

    df = pd.DataFrame(all_rows)
    out_csv = OUTPUTS_DIR / "report_regex.csv"
    if not df.empty:
        df.sort_values(["file", "clause", "paragraph"], inplace=True)
        df.to_csv(out_csv, index=False)
        print(f"✅ Saved: {out_csv}")
        print(df.head(10))
    else:
        print("No clause matches found. Check patterns or templates.")

if __name__ == "__main__":
    main()
