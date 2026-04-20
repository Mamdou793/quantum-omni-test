# Quantum-Omni Digital Twin (V4.0 - Autonomous Loop)

An AI-driven Digital Twin that simulates quantum decoherence under physical stress and autonomously optimizes shielding parameters using a closed-loop Agentic workflow.

## 🚀 The Workflow
1. **Simulation:** A 100-qubit grid is generated in a USD environment (macOS compatible).
2. **Physics:** Qubits are subjected to height-based stress (5m to 23m), modeled via **Hadamard Gates** and **RY Rotations** using Qiskit.
3. **Analysis:** Baseline data (CSV) is sent to an **Azure OpenAI Agent**.
4. **Optimization:** The Agent identifies the 'Critical Decoherence Height' and calculates a `RECOMMENDED_SHIELDING` factor.
5. **Iteration:** The system automatically re-runs the simulation with the new parameters to improve Fidelity.

## 📊 Latest Results
- **Baseline Fidelity:** 19.0%
- **AI Recommendation:** 0.76 Shielding Factor
- **Optimized Fidelity:** 32.0%
- **Critical Failure Point:** Identified at 13.0m