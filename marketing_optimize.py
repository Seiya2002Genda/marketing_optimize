import numpy as np
from scipy.optimize import linprog

def select_from_list(prompt, options, allow_custom=True):
    print(f"\n{prompt}")
    for i, option in enumerate(options):
        print(f"  {i + 1}. {option}")

    selected = input("➡ 数字（カンマ区切り）または新しい名前を直接入力：")

    if all(s.strip().isdigit() for s in selected.split(",") if s.strip().isdigit()):
        indices = [int(s.strip()) - 1 for s in selected.split(",")]
        return [options[i] for i in indices if 0 <= i < len(options)]

    return [s.strip() for s in selected.split(",") if s.strip()]

def get_float_list(prompt, count):
    values = []
    for i in range(count):
        val = float(input(f"{prompt} [{i+1}/{count}]："))
        values.append(val)
    return np.array(values)

def get_cvr_matrix(channels, segments):
    print("\n🔧 チャネル × セグメント の CVR（0.0〜1.0）を入力してください")
    matrix = []
    for ch in channels:
        row = []
        print(f"\n【{ch.strip()}】に対して：")
        for seg in segments:
            val = float(input(f"  - {seg.strip()} のCVR（0〜1）："))
            row.append(val)
        matrix.append(row)
    return np.array(matrix)

# 🎯 ステップ1: ユーザー選択（チャネルとセグメント）
suggested_channels = ["SNS", "TV", "Web広告", "紙媒体", "イベント", "メールマーケ", "YouTube", "ポッドキャスト"]
suggested_segments = ["学生", "社会人", "主婦", "経営者", "シニア", "Z世代"]

channels = select_from_list("📢 チャネル名を選んでください（複数選択OK）", suggested_channels)
segments = select_from_list("👤 顧客セグメントを選んでください（複数選択OK）", suggested_segments)

# 🎯 ステップ2: 各セグメントのLTV
def calculate_ltv_vector(segments):
    print("\n🧮 LTVを以下の式で計算します：LTV = 平均購入単価 × 購入頻度 × 継続期間")
    ltv_values = []

    for i, seg in enumerate(segments):
        print(f"\n👤 セグメント：{seg}")
        unit_price = float(input("  - 平均購入単価（円）："))
        frequency = float(input("  - 年間購入頻度（回/年）："))
        years = float(input("  - 継続年数（何年利用されるか）："))
        ltv = unit_price * frequency * years
        print(f"  👉 推定LTV：{int(ltv)} 円")
        ltv_values.append(ltv)

    return np.array(ltv_values)

# 🎯 ステップ2: 各セグメントのLTV（自動計算）
ltv_vector = calculate_ltv_vector(segments)

# 🎯 ステップ3: CVRマトリクス
cvr_matrix = get_cvr_matrix(channels, segments)

# 🎯 ステップ4: 各チャネルの予算上限・下限・全体予算
print("\n💸 各チャネルの最大投入額を入力（円）")
max_budget = get_float_list("最大予算", len(channels))

print("\n💡 各チャネルの最小投入額を入力（円）")
min_budget = get_float_list("最小予算", len(channels))

total_budget = float(input("\n💰 総予算を入力（円）："))

# 🎯 ステップ5: LTV × CVR で1円あたりの期待LTVリターン
ltv_gain_per_yen = cvr_matrix @ ltv_vector
c = -ltv_gain_per_yen  # 最大化したいため負符号

A = [np.ones(len(channels))]
b = [total_budget]
bounds = list(zip(min_budget, max_budget))

# 🎯 ステップ6: 線形最適化実行
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method="highs")

# 🎯 ステップ7: 結果出力
print("\n📊 最適化結果")
if result.success:
    print("✅ 最適な予算配分：")
    for ch, budget in zip(channels, result.x):
        print(f"  - {ch}: ¥{int(budget):,}")

    total_ltv = ltv_gain_per_yen @ result.x
    print(f"\n🎯 期待されるLTV総和: ¥{int(total_ltv):,}")
    print(f"💰 実際の総投入額: ¥{int(sum(result.x)):,}")
else:
    print("❌ 最適化に失敗しました:", result.message)
# 🔍 セグメントごとのCV推定人数を表示（最適化成功後）
if result.success:
    total_ltv = ltv_gain_per_yen @ result.x
    segment_cvr_total = (cvr_matrix[0]) * ltv_vector  # チャネル0番（SNS）のCVR × LTV
    segment_ratio = segment_cvr_total / segment_cvr_total.sum()

    print("\n👥 推定される到達CV人数（セグメント別）:")
    for i, seg in enumerate(segments):
        seg_ltv = ltv_vector[i]
        est_ltv_portion = segment_ratio[i] * total_ltv
        estimated_cvs = est_ltv_portion / seg_ltv if seg_ltv > 0 else 0
        print(f"  - {seg}: 約 {int(estimated_cvs):,} 人")

    print(f"\n👥 推定CV合計人数: 約 {int(total_ltv / np.mean(ltv_vector)):,} 人（参考値）")
