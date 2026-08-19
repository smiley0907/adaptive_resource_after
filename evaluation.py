# ============================================================
# CELL 31: OVERALL EVALUATION
# ============================================================

baseline_average = (
    final_comparison["Median_Time_sec_Baseline"]
    .mean()
)

adaptive_average = (
    final_comparison["Median_Time_sec_Adaptive"]
    .mean()
)

overall_improvement = (
    (
        baseline_average
        -
        adaptive_average
    )
    /
    baseline_average
) * 100

print("Overall Evaluation")
print("=" * 50)

print(
    f"Average Baseline Median Time : "
    f"{baseline_average:.6f} sec"
)

print(
    f"Average Adaptive Median Time : "
    f"{adaptive_average:.6f} sec"
)

print(
    f"Overall Improvement          : "
    f"{overall_improvement:.2f}%"
)
