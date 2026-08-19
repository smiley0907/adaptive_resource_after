# ============================================================
# CELL 34: FINAL CIRCUIT CHARACTERISTICS
# ============================================================

circuit_summary = []

for n in QUBIT_CONFIGS:

    circuit = circuits[n]

    circuit_summary.append({
        "Qubits": n,
        "Gate_Count": circuit.size(),
        "Circuit_Depth": circuit.depth()
    })

circuit_summary_df = pd.DataFrame(
    circuit_summary
)

display(circuit_summary_df)
