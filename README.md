# 📈 Marketing Budget Optimization Tool

This Python script helps marketers and data analysts **optimize marketing budget allocation** across various channels and customer segments. It aims to **maximize expected Lifetime Value (LTV) returns** based on Conversion Rates (CVR) using linear programming.

---

## 🚀 Features

- Interactive selection of:
  - 📢 Marketing **channels**
  - 👥 Customer **segments**
- Input-based simulation:
  - LTV per segment (calculated via: **Unit Price × Purchase Frequency × Customer Duration**)
  - CVR (Conversion Rate) per Channel × Segment
  - Minimum and maximum budget per channel
  - Total available marketing budget
- Optimization performed using `scipy.optimize.linprog`
- Outputs:
  - 💰 Optimal budget allocation
  - 🎯 Total expected LTV
  - 👥 Estimated number of conversions per segment
- Supports real-world strategic marketing planning with a data-driven approach

---

## 🧮 Mathematical Model

### 1. LTV (Lifetime Value) Calculation

LTV = Unit Price × Purchase Frequency × Customer Duration

### 2. Expected Return per Yen (Channel Effectiveness)

Expected LTV Return = CVR × LTV

---

## 🛠 Requirements

- Python 3.7 or higher  
- Required libraries:  
  - `numpy`  
  - `scipy`  
  - `requests` (only needed for real-time USD/JPY exchange rate support)

Install them via pip:

```bash
pip install numpy scipy requests
🧑‍💻 How to Use
Run the script:

bash
Copy
Edit
python marketing_optimizer.py
Follow the prompts:

Select marketing channels (e.g., SNS, TV, Web Ads)

Select customer segments (e.g., Students, Gen Z, Executives)

Input average unit price, frequency, and duration for LTV calculation

Enter CVR values for each channel-segment pair

Specify min/max budget for each channel and total available budget

Optionally input or fetch real-time USD/JPY exchange rate

View the result:

📊 Optimized budget allocation per channel (in yen and USD)

🎯 Total expected LTV (in yen and USD)

👥 Estimated number of conversions per segment

📦 Example Output
yaml
Copy
Edit
📊 Optimization Result
✅ Optimal Budget Allocation:
  - SNS: ¥300,000 (≈ $1,981.13 USD)
  - TV: ¥200,000 (≈ $1,320.75 USD)

🎯 Total Expected LTV: ¥1,240,000 (≈ $8,190.65 USD)
💰 Actual Total Spending: ¥500,000 (≈ $3,301.88 USD)

👥 Estimated Number of Conversions per Segment:
  - Students: approx. 1,102 people
  - Gen Z: approx. 880 people

👥 Estimated Total Conversions: approx. 1,000 people (approximate)
💱 Currency Conversion Support
Fetch real-time exchange rate via exchangerate.host

Manually input your own custom exchange rate

📌 Notes
CVR matrix is shaped as: Rows = Channels, Columns = Segments

Linear programming uses method="highs" for efficient solving

Conversion estimates are based on relative CVR × LTV weighting of the first selected channel

📄 License
MIT License © 2025 Seiya Genda

🙌 Contributions & Feedback
Feel free to fork, improve, or suggest new features such as:

Graphical dashboards (e.g., with matplotlib, plotly)

Excel or CSV export of results

GUI version (Tkinter or PyQt)

Google Sheets integration

Pull requests are welcome!

yaml
Copy
Edit

---

これを**Markdownに貼れば完璧に見栄えする**し、**そのままGitHubにも貼れる**形やで。

必要なら、これを`.md`ファイルやPDFにも変換可能やけどどうする？

