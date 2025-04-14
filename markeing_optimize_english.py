import numpy as np
from scipy.optimize import linprog

def select_from_list(prompt, options, allow_custom=True):
    print(f"\n{prompt}")
    for i, option in enumerate(options):
        print(f"  {i + 1}. {option}")

    selected = input("➡ Enter numbers (comma-separated) or type new names directly: ")

    if all(s.strip().isdigit() for s in selected.split(",") if s.strip().isdigit()):
        indices = [int(s.strip()) - 1 for s in selected.split(",")]
        return [options[i] for i in indices if 0 <= i < len(options)]

    return [s.strip() for s in selected.split(",") if s.strip()]

def get_float_list(prompt, count):
    values = []
    for i in range(count):
        val = float(input(f"{prompt} [{i+1}/{count}]: "))
        values.append(val)
    return np.array(values)

def get_cvr_matrix(channels, segments):
    print("\n🔧 Enter CVR (0.0 to 1.0) for each Channel × Segment combination.")
    matrix = []
    for ch in channels:
        row = []
        print(f"\nFor 【{ch.strip()}】:")
        for seg in segments:
            val = float(input(f"  - CVR for {seg.strip()} (0 to 1): "))
            row.append(val)
        matrix.append(row)
    return np.array(matrix)

# 🎯 Step 1: User selects channels and customer segments
suggested_channels = ["SNS", "TV", "Web Ads", "Print Media", "Events", "Email Marketing", "YouTube", "Podcast"]
suggested_segments = ["Students", "Working Adults", "Housewives", "Executives", "Seniors", "Gen Z"]

channels = select_from_list("📢 Please select channels (multiple allowed)", suggested_channels)
segments = select_from_list("👤 Please select customer segments (multiple allowed)", suggested_segments)

# 🎯 Step 2: LTV calculation for each segment
def calculate_ltv_vector(segments):
    print("\n🧮 LTV will be calculated as: LTV = Unit Price × Purchase Frequency × Duration")
    ltv_values = []

    for i, seg in enumerate(segments):
        print(f"\n👤 Segment: {seg}")
        unit_price = float(input("  - Average Unit Price (in yen): "))
        frequency = float(input("  - Purchase Frequency (times/year): "))
        years = float(input("  - Customer Duration (years): "))
        ltv = unit_price * frequency * years
        print(f"  👉 Estimated LTV: ¥{int(ltv)}")
        ltv_values.append(ltv)

    return np.array(ltv_values)

ltv_vector = calculate_ltv_vector(segments)

# 🎯 Step 3: CVR Matrix
cvr_matrix = get_cvr_matrix(channels, segments)

# 🎯 Step 4: Budget constraints for each channel
print("\n💸 Enter the *maximum* budget for each channel (in yen)")
max_budget = get_float_list("Max Budget", len(channels))

print("\n💡 Enter the *minimum* budget for each channel (in yen)")
min_budget = get_float_list("Min Budget", len(channels))

total_budget = float(input("\n💰 Enter the total marketing budget (in yen): "))

# 🎯 Step 5: Expected LTV return per yen = CVR × LTV
ltv_gain_per_yen = cvr_matrix @ ltv_vector
c = -ltv_gain_per_yen  # Negative for maximization

A = [np.ones(len(channels))]
b = [total_budget]
bounds = list(zip(min_budget, max_budget))

# 🎯 Step 6: Linear Optimization
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")

# 🎯 Step 7: Output Results
print("\n📊 Optimization Result")
if result.success:
    print("✅ Optimal Budget Allocation:")
    for ch, budget in zip(channels, result.x):
        print(f"  - {ch}: ¥{int(budget):,}")

    total_ltv = ltv_gain_per_yen @ result.x
    print(f"\n🎯 Total Expected LTV: ¥{int(total_ltv):,}")
    print(f"💰 Actual Total Spending: ¥{int(sum(result.x)):,}")
else:
    print("❌ Optimization failed:", result.message)

# 🔍 Show estimated conversions per segment (if optimization succeeded)
if result.success:
    total_ltv = ltv_gain_per_yen @ result.x
    segment_cvr_total = (cvr_matrix[0]) * ltv_vector  # Using CVR from the first channel (e.g., SNS)
    segment_ratio = segment_cvr_total / segment_cvr_total.sum()

    print("\n👥 Estimated Number of Conversions per Segment:")
    for i, seg in enumerate(segments):
        seg_ltv = ltv_vector[i]
        est_ltv_portion = segment_ratio[i] * total_ltv
        estimated_cvs = est_ltv_portion / seg_ltv if seg_ltv > 0 else 0
        print(f"  - {seg}: approx. {int(estimated_cvs):,} people")

    print(f"\n👥 Estimated Total Conversions: approx. {int(total_ltv / np.mean(ltv_vector)):,} people (approximate)")
