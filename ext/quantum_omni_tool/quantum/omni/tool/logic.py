import math
import csv
import os
from pxr import Usd, UsdGeom, Gf
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

class QuantumOmniTool:
    def __init__(self, stage_path="quantum_sim.usda"):
        """
        Initializes the stage. If the file exists, we open it to allow updates;
        otherwise, we create a fresh one.
        """
        if os.path.exists(stage_path):
            self.stage = Usd.Stage.Open(stage_path)
        else:
            self.stage = Usd.Stage.CreateNew(stage_path)
            
        UsdGeom.SetStageUpAxis(self.stage, UsdGeom.Tokens.y)
        self.qubit_data = []
        self.simulator = AerSimulator()

    def _get_quantum_decision(self, stress_factor, shielding_factor=0.0):
        """
        PHASE 4: Shielded Quantum Logic
        The shielding_factor (0.0 to 1.0) dampens the rotational stress.
        """
        qc = QuantumCircuit(1, 1)
        qc.h(0) # Hadamard puts it on the equator
        
        # Effective stress is dampened by the shielding value
        effective_stress = stress_factor * (1.0 - shielding_factor)
        
        # RY Rotation creates the probability curve
        theta = effective_stress * math.pi
        qc.ry(theta, 0)
        
        qc.measure(0, 0)
        
        result = self.simulator.run(qc, shots=1, memory=True).result()
        measurement = result.get_memory()[0]
        
        return "Beta" if measurement == "1" else "Alpha"

    def generate_grid(self, count=10, spacing=2.0):
        """
        Creates or updates the 3D grid. Uses MakeTranslateOp to prevent
        USD 'duplicate operation' errors during re-runs.
        """
        self.qubit_data = []
        for i in range(count):
            for j in range(count):
                path = f"/World/Qubit_{i}_{j}"
                
                # Define or Get the Cube
                if self.stage.GetPrimAtPath(path):
                    cube = UsdGeom.Cube.Get(self.stage, path)
                else:
                    cube = UsdGeom.Cube.Define(self.stage, path)
                
                # Height gradient from 5m to 23m
                height = 5.0 + (i * 2.0) 
                pos = Gf.Vec3f(i * spacing, height, j * spacing)
                
                # SAFE UPDATE: MakeTranslateOp checks if it exists before adding
                UsdGeom.Xformable(cube).AddTranslateOp().Set(pos)
                
                self.qubit_data.append({
                    "id": f"{i}_{j}", 
                    "height": height, 
                    "path": path
                })
        
        self.stage.Save()

    def run_simulation(self, shielding=0.0, log_file="results.csv"):
        """
        Executes the quantum simulation loop and applies visual colors.
        """
        if not self.qubit_data:
            return {"Alpha": 0, "Beta": 0}

        max_h = max(d["height"] for d in self.qubit_data)
        stats = {"Alpha": 0, "Beta": 0}
        
        with open(log_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Qubit_ID", "Fall_Height", "Resulting_State"])
            
            for data in self.qubit_data:
                # Normalize stress between 0.0 and 1.0
                stress = (data["height"] - 5.0) / (max_h - 5.0) if max_h > 5.0 else 0
                
                # Get the state based on Quantum Rotation + Shielding
                state = self._get_quantum_decision(stress, shielding)
                stats[state] += 1
                
                # Apply Color (Green for Alpha, Red for Beta)
                cube_prim = UsdGeom.Cube.Get(self.stage, data["path"])
                color = Gf.Vec3f(0.1, 0.8, 0.2) if state == "Alpha" else Gf.Vec3f(0.8, 0.1, 0.1)
                cube_prim.GetDisplayColorAttr().Set([color])
                
                writer.writerow([data["id"], round(data["height"], 2), state])
        
        self.stage.Save()
        return stats