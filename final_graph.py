# ============================================================
# CELL 29: BEFORE VS AFTER
# ============================================================

plt.figure(figsize=(10, 6))

plt.plot(
    final_comparison["Qubits"],
    final_comparison["Median_Time_sec_Baseline"],
    marker="o",
    label="Static Baseline"
)

plt.plot(
    final_comparison["Qubits"],
    final_comparison["Median_Time_sec_Adaptive"],
    marker="s",
    label="Adaptive Strategy"
)

plt.xlabel("Number of Qubits")
plt.ylabel("Median Execution Time (s)")
plt.title(
    "Static Resource Allocation vs Adaptive Resource Optimization"
)

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
