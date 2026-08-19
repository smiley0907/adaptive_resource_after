# ============================================================
# CELL 24: AFTER GRAPH
# ============================================================

plt.figure(figsize=(9, 5))

plt.plot(
    adaptive_df["Qubits"],
    adaptive_df["Median_Time_sec"],
    marker="o"
)

plt.xlabel("Number of Qubits")
plt.ylabel("Median Execution Time (s)")
plt.title("Adaptive Resource Optimization")
plt.grid(True)
plt.tight_layout()
plt.show()
