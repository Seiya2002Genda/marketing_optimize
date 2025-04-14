📈 Marketing Budget Optimization Tool
This Python script is designed to help marketers and data analysts optimize marketing budget allocation across multiple channels and customer segments. It aims to maximize the total expected LTV (Lifetime Value) using linear programming.

🚀 Features
Interactive user input:

📢 Marketing channels (select or input custom)

👥 Customer segments (select or input custom)

LTV calculation based on:

Unit Price × Purchase Frequency × Customer Duration

CVR (Conversion Rate) input for every Channel × Segment combination

Budget configuration:

Individual min/max budgets per channel

A total marketing budget constraint

Linear optimization using scipy.optimize.linprog

Outputs:

💰 Optimal budget allocation across channels

🎯 Total expected LTV

👥 Estimated number of conversions per segment

🧮 Mathematical Model
1. LTV Calculation
Each customer segment’s LTV is calculated using:

ini
Copy
Edit
LTV = Unit Price × Purchase Frequency × Customer Duration
This gives the total lifetime value contribution per converted user.

2. Expected Return Per Yen
The expected LTV return per yen for each channel is computed as:

java
Copy
Edit
Expected Return = CVR × LTV (dot product)
Where CVR is the conversion rate of each channel for each segment.

3. Linear Optimization
Objective:
Maximize total expected LTV given budget constraints.

Formulated as a linear programming problem:

Objective Function:
maximize Σ (budget_i × expected_return_i)

Subject to:

Total budget: Σ budget_i ≤ Total Budget

Per channel: Min_i ≤ budget_i ≤ Max_i

📊 Sample Output
yaml
Copy
Edit
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
📦 Requirements
Python 3.7+

numpy

scipy

Install with:

bash
Copy
Edit
pip install numpy scipy
📝 How to Use
Run the script in your terminal or IDE.

Select or input marketing channels and customer segments.

Input unit price, purchase frequency, and customer duration for each segment.

Input CVR values for each Channel × Segment combination.

Define budget constraints and total marketing budget.

View optimal allocation results and conversion estimates.

📌 Notes
This script assumes linear behavior and does not account for diminishing returns.

CVR values should be between 0.0 and 1.0.

The model is ideal for simulation and strategic planning.




