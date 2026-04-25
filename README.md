# Quantum-Omni Digital Twin

A closed-loop Digital Twin system integrating **NVIDIA Omniverse**, **Azure OpenAI**, and **Streamlit** to monitor and optimize quantum qubit stability.

##  System Architecture
- **Ingestion:** `generate_telemetry.py` simulates qubit stress testing (Fall Height vs. Decoherence).
- **Analysis:** `agent_analysis.py` uses GPT-4o-mini to calculate shielding factors and generate Engineering Reports.
- **Orchestration:** `sync_twin.py` monitors data logs and pushes visual updates to the USD asset.
- **Presentation:** `dashboard.py` provides a real-time TPM view of Fidelity KPIs.

##  Latest Results
- **Baseline Fidelity:** 19.0%
- **AI Recommendation:** 0.81 Shielding Factor
- **Optimized Fidelity:** 36.0%
- **Critical Failure Point:** Identified at 13.0m
=======
##  Results
- **Baseline Fidelity:** 17% (Critical decoherence at 9.0m)
- **Optimized Fidelity:** 83% (Critical decoherence pushed to 21.0m)
- **Visuals:** Integrated with `.usda` for real-time voxel state visualization.

