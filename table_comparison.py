# ============================================================
# CELL 27: FINAL COMPARISON TABLE
# ============================================================

final_comparison = comparison_df[
    [
        "Qubits",
        "Median_Time_sec_Baseline",
        "Median_Time_sec_Adaptive",
        "Execution_Time_Improvement_%"
    ]
].copy()

display(final_comparison)
