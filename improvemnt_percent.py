# ============================================================
# CELL 30: PERFORMANCE IMPROVEMENT GRAPH
# ============================================================

plt.figure(figsize=(9, 5))

plt.bar(
    final_comparison["Qubits"].astype(str),
    final_comparison["Execution_Time_Improvement_%"]
)

plt.axhline(
    y=0,
    linewidth=1
)

plt.xlabel("Number of Qubits")
plt.ylabel("Execution Time Improvement (%)")
plt.title("Adaptive Execution Time Improvement")
plt.grid(axis="y")

plt.tight_layout()
plt.show()
