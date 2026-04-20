import sys
import os
# Ensure the current directory is in the path so we can find our extension
sys.path.append(os.getcwd())

# 1. Update the import to match the new Class name
from ext.quantum_omni_tool.quantum.omni.tool.logic import QuantumOmniTool

# 2. Setup file paths
log_name = "quantum_stress_results.csv"
usd_name = "quantum_simulation_v3.usda"

# 3. Initialize the tool
print("🧪 Initializing Quantum Digital Twin...")
my_tool = QuantumOmniTool(stage_path=usd_name)

# 4. Phase 1: Generate the Grid
print("🎨 Building 100-Qubit Simulation Grid...")
init_msg = my_tool.generate_simulation_grid(count=10)
print(init_msg)

# 5. Phase 2: Execute Quantum Stress Test
# This now runs the Hadamard gates and RY rotations internally
print("⚛️  Running Quantum Measurement (H-Gate + RY Rotation)...")
stats = my_tool.execute_stress_test(log_file=log_name)

# 6. Scientific Analysis Output
total = stats['Alpha'] + stats['Beta']
fidelity = (stats['Alpha'] / total) * 100

print(f"\n--- SIMULATION V3.0 COMPLETE ---")
print(f"USD Visual Stage: {os.path.abspath(usd_name)}")
print(f"Quantum Data Log: {os.path.abspath(log_name)}")
print(f"--------------------------------")
print(f"Stable States (Alpha):   {stats['Alpha']}")
print(f"Decohered States (Beta): {stats['Beta']}")
print(f"System Fidelity:         {fidelity:.2f}%")
print(f"--------------------------------")

if fidelity < 50:
    print("⚠️  CRITICAL: System Decoherence detected beyond acceptable threshold.")
else:
    print("✅ System within operational quantum parameters.")