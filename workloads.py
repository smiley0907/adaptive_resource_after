# ============================================================
# CELL 32: WORKLOAD LEVEL ANALYSIS
# ============================================================

improved = final_comparison[
    final_comparison["Execution_Time_Improvement_%"] > 0
]

degraded = final_comparison[
    final_comparison["Execution_Time_Improvement_%"] < 0
]

print("Workloads with improvement:")
display(improved)

print()
print("Workloads with performance degradation:")
display(degraded)
