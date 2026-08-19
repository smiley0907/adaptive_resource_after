# ============================================================
# CELL 33: FINAL EXPERIMENT SUMMARY
# ============================================================

print("=" * 70)
print("ADAPTIVE RESOURCE OPTIMIZATION EXPERIMENT SUMMARY")
print("=" * 70)

print(f"Workloads tested       : {QUBIT_CONFIGS}")
print(f"Shots                  : {SHOTS}")
print(f"Baseline CPU threads   : {BASELINE_THREADS}")
print(f"Adaptive candidates    : {ADAPTIVE_CANDIDATES}")
print(f"Warm-up executions     : {WARMUP_RUNS}")
print(f"Measurement repetitions: {MEASUREMENT_RUNS}")
print(f"Primary metric         : Median execution time")
print()

print("Final comparison:")
display(final_comparison)

print()
print(f"Average baseline time : {baseline_average:.6f} sec")
print(f"Average adaptive time : {adaptive_average:.6f} sec")
print(f"Overall improvement   : {overall_improvement:.2f}%")
