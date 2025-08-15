# Week 1 — Python Basics & Environment Setup

### Goal
Set up a clean Python dev env; build a small CLI that computes BMI, BMR, and water intake; and analyze CDC BMI data in a notebook.

## Setup
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Mac/Linux: source .venv/bin/activate

pip install -r requirements.txt
pre-commit install

## 📊 Results & Notes
- Saved personal BMI/BMR results to `data/week1_results.csv` for reproducibility.
- Generated Matplotlib visualizations comparing my BMI to Minnesota’s CDC BMI averages.
- Final outputs and plots are documented in the [Week 1 Reflection](REFLECTION.md).

## 🖼️ Screenshots
<p align="center">
  <img src="assets/cli_output.png" alt="CLI output" width="520">
  <img src="assets/bmi_chart.png" alt="Example BMI chart" width="520">
</p>

## 🔗 Resources used
- FreeCodeCamp Python (YouTube)  
- W3Schools Python (reference)  
- Python for Everybody (Coursera – audit)  

---

🔄 **Next Steps:** Moving into [Week 2](../Week-2) to expand these concepts into **functions, OOP, file I/O, and automated testing** using `pytest`.

---

📜 Licensed under CC BY-NC 4.0 — see [../LICENSE](../LICENSE) for details.