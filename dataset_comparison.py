# ============================================================
# CELL 25: STATIC VS ADAPTIVE COMPARISON
# ============================================================

comparison_df = pd.merge(
    baseline_df[
        [
            "Qubits",
            "Median_Time_sec"
        ]
    ],
    adaptive_df[
        [
            "Qubits",
            "Median_Time_sec"
        ]
    ],
    on="Qubits",
    suffixes=(
        "_Baseline",
        "_Adaptive"
    )
)

comparison_df
