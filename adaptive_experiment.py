# ============================================================
# CELL 20: AFTER EXPERIMENT
# ADAPTIVE RESOURCE OPTIMIZATION
# ============================================================

adaptive_records = []
selection_records = []

for n in QUBIT_CONFIGS:

    circuit = circuits[n]
    executable_circuit = execution_circuits[n]

    gate_count = circuit.size()
    circuit_depth = circuit.depth()

    # --------------------------------------------------------
    # Obtain ARS
    # --------------------------------------------------------
    ars_value = float(
        workload_df.loc[
            workload_df["Qubits"] == n,
            "ARS"
        ].iloc[0]
    )

    print()
    print("=" * 70)
    print(
        f"Adaptive workload: {n} qubits | "
        f"ARS={ars_value:.4f}"
    )
    print("=" * 70)

    # --------------------------------------------------------
    # Candidate resource evaluation
    # --------------------------------------------------------
    selected_threads, candidate_df = (
        select_best_cpu_configuration(
            executable_circuit,
            candidate_threads=ADAPTIVE_CANDIDATES,
            selection_runs=SELECTION_RUNS,
            warmup_runs=WARMUP_RUNS,
            shots=SHOTS,
            seed=RANDOM_SEED + n
        )
    )

    print(
        f"Selected CPU configuration: "
        f"{selected_threads} threads"
    )

    # Store candidate-selection results
    for _, row in candidate_df.iterrows():

        selection_records.append({
            "Qubits": n,
            "ARS": ars_value,
            "CPU_Threads": int(row["CPU_Threads"]),
            "Selection_Median_Time_sec":
                float(row["Selection_Median_Time_sec"])
        })

    # --------------------------------------------------------
    # Final adaptive execution
    # --------------------------------------------------------
    execution_times = collect_execution_times(
        executable_circuit,
        cpu_threads=selected_threads,
        warmup_runs=WARMUP_RUNS,
        measurement_runs=MEASUREMENT_RUNS,
        shots=SHOTS,
        seed=RANDOM_SEED + 100 + n
    )

    median_time = float(np.median(execution_times))
    mean_time = float(np.mean(execution_times))
    std_time = float(np.std(execution_times, ddof=1))

    min_time = float(np.min(execution_times))
    max_time = float(np.max(execution_times))

    adaptive_records.append({
        "Qubits": n,
        "Gate_Count": gate_count,
        "Circuit_Depth": circuit_depth,
        "Shots": SHOTS,
        "ARS": ars_value,
        "CPU_Threads": selected_threads,
        "Median_Time_sec": median_time,
        "Mean_Time_sec": mean_time,
        "Std_Time_sec": std_time,
        "Min_Time_sec": min_time,
        "Max_Time_sec": max_time
    })

adaptive_df = pd.DataFrame(adaptive_records)

adaptive_df
