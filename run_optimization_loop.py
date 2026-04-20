from ext.quantum_omni_tool.quantum.omni.tool.logic import QuantumOmniTool
from agent_analysis import get_ai_recommendation

tool = QuantumOmniTool(stage_path="optimized_sim.usda")
tool.generate_grid()

# RUN 1: Baseline
print("🚀 Running Baseline Simulation (Shielding: 0.0)...")
stats1 = tool.run_simulation(shielding=0.0, log_file="baseline.csv")
print(f"Initial Fidelity: {(stats1['Alpha']/100)*100}%")

# THE BRAIN: Ask the AI
print("🧠 Consulting AI Agent for Optimization...")
report, suggested_shielding = get_ai_recommendation("baseline.csv")

# RUN 2: Optimized
print(f"🛠 Applying Shielding {suggested_shielding} and Re-running...")
stats2 = tool.run_simulation(shielding=suggested_shielding, log_file="optimized.csv")
new_fidelity = (stats2['Alpha']/100)*100

print(f"\n✅ OPTIMIZATION COMPLETE")
print(f"Final Fidelity: {new_fidelity}%")
with open("Final_Report.md", "w") as f: f.write(report)