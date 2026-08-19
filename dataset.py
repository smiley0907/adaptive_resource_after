# ============================================================
# CELL 23: EXPORT AFTER DATASET
# ============================================================

adaptive_df.to_csv(
    "adaptive_results.csv",
    index=False
)

selection_df.to_csv(
    "adaptive_selection_results.csv",
    index=False
)

print("Saved:")
print("  adaptive_results.csv")
print("  adaptive_selection_results.csv")
