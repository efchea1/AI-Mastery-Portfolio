## Week 1 Reflection

### Key Learnings
- Set up and successfully used `pre-commit` hooks with `black` and `flake8` to maintain consistent formatting and linting across all commits.
- Practiced executing Python scripts both directly and from subdirectories using `python path/to/script.py`.
- Created visualizations with Matplotlib, comparing Minnesota CDC BMI averages to my own BMI, and saved results for version-controlled sharing.
- Applied `.gitignore` rules effectively to manage large data files, ensuring that only essential, lightweight CSV results are committed.

### Challenges
- Initially attempted to run `health_metrics.py` without the `python` prefix, resulting in `'not recognized as an internal or external command'` errors.
- Learning the balance between what data should be tracked in Git versus what should be excluded.
- Handling Matplotlib’s default plot saving manually rather than automating file naming and storage.

### Improvements for Next Week
- Refactor BMI and BMR logic into **functions** for reusability.
- Implement **unit tests** using `pytest` to validate calculation accuracy.
- Introduce **error handling** for user inputs to make scripts more robust.
- Automate plot saving with **dynamic, descriptive filenames**.
- Keep short **daily reflection notes** to streamline end-of-week summaries.

### Overall Takeaway
This week solidified my workflow for reproducible data science projects:  
- Clean, enforced code formatting through pre-commit hooks.  
- Clear project structure with organized directories for data, notebooks, and scripts.  
- Practical use of Matplotlib for health-related visualizations.  

These foundations—version control hygiene, reproducible Python environments, and basic plotting—set the stage for Week 2, where I will expand into **Python functions, classes, file I/O, and automated testing**. The upcoming project, a **Patient Intake CLI App** using synthetic patient data, will directly build on Week 1 by incorporating structured code design, persistent storage, and enhanced reliability through unit testing.