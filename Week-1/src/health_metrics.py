from __future__ import annotations
from pathlib import Path
import csv
from datetime import datetime

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# This is the small results log (not the CDC file)
RESULTS_CSV = DATA_DIR / "week1_results.csv"

def bmi(weight_kg: float, height_cm: float) -> float:
    h = height_cm / 100
    return round(weight_kg / (h * h), 2)

def bmr(weight_kg: float, height_cm: float, age: int, sex: str) -> float:
    sex = sex.strip().lower()
    if sex.startswith("m"):
        val = 88.362 + (13.397 * weight_kg) + (4.799 * height_cm) - (5.677 * age)
    else:
        val = 447.593 + (9.247 * weight_kg) + (3.098 * height_cm) - (4.330 * age)
    return round(val, 1)

def daily_hydration(weight_kg: float) -> float:
    return round(weight_kg * 35 / 1000.0, 2)

def lb_to_kg(lb: float) -> float: return lb * 0.45359237
def in_to_cm(inches: float) -> float: return inches * 2.54
def ft_in_to_cm(feet: float, inches: float) -> float: return in_to_cm(feet * 12 + inches)

def save_result(row: dict) -> None:
    write_header = not RESULTS_CSV.exists()
    with RESULTS_CSV.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=[
                "timestamp","units","sex","age","weight_kg","height_cm",
                "BMI","BMR_kcal","Water_L"
            ],
        )
        if write_header: w.writeheader()
        w.writerow(row)

if __name__ == "__main__":
    print("=== Health Metrics Calculator ===")
    units = input("Units? (metric/imperial) [metric]: ").strip().lower() or "metric"
    sex = input("Sex (male/female): ").strip()
    age = int(input("Age (years): ").strip())

    if units.startswith("i"):
        lb  = float(input("Weight (lb): ").strip())
        ft  = float(input("Height (feet): ").strip())
        inch= float(input("Height (inches): ").strip())
        weight_kg = lb_to_kg(lb)
        height_cm = ft_in_to_cm(ft, inch)
    else:
        weight_kg = float(input("Weight (kg): ").strip())
        height_cm = float(input("Height (cm): ").strip())

    bmi_val = bmi(weight_kg, height_cm)
    bmr_val = bmr(weight_kg, height_cm, age, sex)
    water_l = daily_hydration(weight_kg)

    print(f"\nBMI: {bmi_val}")
    print(f"BMR (kcal/day): {bmr_val}")
    print(f"Suggested water (L/day): {water_l}")

    save_result({
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "units": "imperial" if units.startswith("i") else "metric",
        "sex": sex, "age": age,
        "weight_kg": round(weight_kg, 2), "height_cm": round(height_cm, 1),
        "BMI": bmi_val, "BMR_kcal": bmr_val, "Water_L": water_l,
    })
    print(f"\nSaved to: {RESULTS_CSV}")