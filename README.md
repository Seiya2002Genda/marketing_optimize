# 📈 Marketing Budget Optimization Tool

This Python script is designed to help **marketers and data analysts** optimize marketing budget allocation across multiple channels and customer segments.  
It aims to **maximize the total expected LTV (Lifetime Value)** using **linear programming**.

---

## 🚀 Features

Interactive user input:

- 📢 Marketing channels (select or input custom)  
- 👥 Customer segments (select or input custom)

LTV calculation based on:

- Unit Price × Purchase Frequency × Customer Duration

CVR (Conversion Rate) input for every Channel × Segment combination

Budget configuration:

- Individual min/max budgets per channel  
- A total marketing budget constraint

Linear optimization using `scipy.optimize.linprog`

Outputs:

- 💰 Optimal budget allocation across channels  
- 🎯 Total expected LTV  
- 👥 Estimated number of conversions per segment

---

## 🧮 Mathematical Model

### 1. LTV Calculation

Each customer segment’s LTV is calculated using:

LTV = Unit Price × Purchase Frequency × Customer Duration

This gives the total lifetime value contribution per converted user.

---

### 2. Expected Return Per Yen

The expected LTV return per yen for each channel is computed as:

Expected Return = CVR × LTV (dot product)


Where CVR is the conversion rate of each channel for each segment.

---

### 3. Linear Optimization

**Objective:**  
Maximize total expected LTV given budget constraints.

Formulated as a **linear programming problem**:

**Objective Function:**

maximize Σ (budget_i × expected_return_i)


**Subject to:**

- Total budget: `Σ budget_i ≤ Total Budget`  
- Per channel: `Min_i ≤ budget_i ≤ Max_i`

---

## 📊 Sample Output

```yaml
✅ Optimal Budget Allocation:
  - SNS: ¥120,000
  - TV: ¥250,000
  - Email Marketing: ¥130,000

🎯 Total Expected LTV: ¥4,320,000
💰 Actual Total Spending: ¥500,000

👥 Estimated Number of Conversions per Segment:
  - Students: approx. 850 people
  - Working Adults: approx. 620 people
  ...

👥 Estimated Total Conversions: approx. 2,100 people






















