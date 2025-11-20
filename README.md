# AI-Contract-Clause-Identifier
A tool that scans legal/financial contracts and flags high-risk clauses (indemnification, liability caps, warranty terms, etc.), helping businesses quickly assess potential exposure.

## 🎯 Target Clauses (Red Flags)

This project focuses on detecting the following high-risk contract clauses:

1. **Indemnification** – Obligations to cover losses or damages.  
2. **Limitation of Liability** – Caps on damages a party must pay.  
3. **Warranty / Defects** – Promises about product/service quality.  
4. **Termination Clauses** – Conditions under which the contract ends.  
5. **Confidentiality / Trade Secrets** – Restrictions on sharing information.  

# AI Contract Clause Identifier

This project uses NLP (starting with regex, later with spaCy/Legal-BERT) to identify high-risk clauses in contracts, such as indemnification, limitation of liability, warranty, termination, and confidentiality.

---

## 🚀 Quick Start (Colab)

You can run this project directly in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/OutsideRebelBox/AI-Contract-Clause-Identifier/blob/main/notebooks/demo.ipynb)

---

## 📂 Repository Structure
- `contracts/` → sample agreements  
- `scripts/target_clauses.json` → list of clauses & regex patterns  
- `scripts/detect_clauses_regex.py` → main detector script  
- `outputs/` → reports (CSV)  
- `notebooks/demo.ipynb` → interactive demo notebook  

---

## 📝 Example Output

| file | clause | paragraph | snippet |
|------|--------|-----------|---------|
| `NDA.docx` | confidentiality | 12 | “The parties agree to keep confidential…” |
| `MSA.pdf`  | limitation of liability | 18 | “Liability shall not exceed fees paid…” |

---

## 💻 JavaScript & TypeScript Support

The project now includes a full **JavaScript + TypeScript implementation** for clause detection.

### ✔️ Features
- Browser-based scanner  
- Node-compatible script  
- Shared pattern file (`clauses.json`)  
- Upload → Scan → Highlight high-risk clauses  

## 📁 File Structure
```text
/js
 ├── src
 │    ├── detectClauses.js
 │     ├── clauses.json
 │    └── detectClauses.ts
 └── demo
      ├── index.html
      ├── styles.css
      └── app.js
```
### ▶️ Run the Browser Demo Locally

1. Download `js/demo/index.html` in any browser  
2. Upload a `.txt`, `.docx`, or `.pdf` file (must be text-extractable)  
3. Click **Scan**  
4. High-risk clauses will be highlighted automatically  

