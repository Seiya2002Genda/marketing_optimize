# marketing_optimize
# 📈 Marketing Budget Optimization Tool

This Python script helps marketers and analysts **optimize marketing budget allocation** across various channels and customer segments, in order to **maximize expected Lifetime Value (LTV) returns** based on Conversion Rates (CVR).

## 🚀 Features

- Select marketing **channels** and **customer segments** interactively
- Input:
  - **LTV per segment** (calculated using Unit Price × Frequency × Duration)
  - **CVR per channel × segment combination**
  - **Minimum / Maximum budget per channel**
  - **Total marketing budget**
- Perform **linear programming** optimization using `scipy.optimize.linprog`
- Display:
  - 💰 Optimal budget allocation
  - 🎯 Total expected LTV
  - 👥 Estimated conversions per segment
- Designed for both **flexibility** and **usability** in real-world marketing scenarios

---

## 🧮 Formulae

### 1. Lifetime Value (LTV) per Segment

