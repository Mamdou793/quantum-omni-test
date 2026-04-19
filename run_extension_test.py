import sys
import os
sys.path.append(os.getcwd())

from ext.quantum_omni_tool.quantum.omni.tool.logic import QuantumTool

# 1. Initialize
log_name = "quantum_stress_results.csv"
my_tool = QuantumTool(stage_path="stress_test_v2.usda")

# 2. Run
print("📊 Running Quantum Data Acquisition...")
my_tool.generate_grid(count=10)
stats = my_tool.run_measurement(log_file=log_name)

# 3. Output
print(f"\n--- DATA COLLECTION COMPLETE ---")
print(f"Results saved to: {os.path.abspath(log_name)}")
print(f"Stable (Alpha): {stats['Alpha']} | Decohered (Beta): {stats['Beta']}")