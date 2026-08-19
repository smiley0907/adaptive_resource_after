# ============================================================
# CELL 26: PERFORMANCE IMPROVEMENT
# ============================================================

comparison_df["Execution_Time_Improvement_%"] = (
    (
        comparison_df["Median_Time_sec_Baseline"]
        -
        comparison_df["Median_Time_sec_Adaptive"]
    )
    /
    comparison_df["Median_Time_sec_Baseline"]
) * 100

comparison_df
