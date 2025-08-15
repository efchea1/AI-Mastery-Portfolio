# Week 1 — Python Basics & Environment Setup

**Status:** ✅ Completed  
**Dates:** Aug 12–16, 2025

## 🎯 Goals
- Practice Python fundamentals (functions, I/O, conditionals)
- Build a **BMI / BMR / Hydration** CLI
- Log results to CSV and explore CDC BMI-related data in a notebook

## 🗂 What’s in this folder
- **`src/health_metrics.py`** — CLI app (metric/imperial) that saves runs to `data/week1_results.csv`
- **`notebooks/Week1_CDC_BMI_Analysis.ipynb`** — CDC BMI exploration + compare with my BMI
- **`data/week1_results.csv`** — small run log (kept in Git); big CDC CSV is *not* tracked

## Data for Week 1
- `week1_results.csv` — Log of BMI/BMR/Hydration results from CLI runs
- Large CDC CSV is excluded from repo (see `.gitignore`)

## ▶️ How to run
```bash
# from repo root
python Week-1/src/health_metrics.py
# then open the notebook and Run All 

---
## 📄 License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

© 2025 Emmanuel Fle Chea. See the LICENSE file for full terms and usage guidelines.