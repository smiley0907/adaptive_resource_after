# ============================================================
# CELL 35: MASTER EXPERIMENTAL DATASET
# ============================================================

master_df = pd.merge(
    baseline_df,
    adaptive_df,
    on="Qubits",
    suffixes=(
        "_Baseline",
        "_Adaptive"
    )
)

master_df.to_csv(
    "master_experiment_results.csv",
    index=False
)

display(master_df)

print("Saved: master_experiment_results.csv")
