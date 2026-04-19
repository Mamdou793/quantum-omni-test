import random
import math
import csv # New import for data logging
from pxr import Usd, UsdGeom, Gf

class QuantumTool:
    def __init__(self, stage_path="extension_output.usda"):
        # We use 'try' to avoid errors if the file exists from a previous run
        try:
            self.stage = Usd.Stage.CreateNew(stage_path)
        except:
            self.stage = Usd.Stage.Open(stage_path)
            
        UsdGeom.SetStageUpAxis(self.stage, UsdGeom.Tokens.y)
        self.qubit_data = []

    def generate_grid(self, count=10, spacing=2.0):
        self.qubit_data = [] # Reset data for new run
        for i in range(count):
            for j in range(count):
                path = f"/World/Qubit_{i}_{j}"
                cube = UsdGeom.Cube.Define(self.stage, path)
                height = 5.0 + (i * 2.0) 
                pos = Gf.Vec3f(i * spacing, height, j * spacing)
                cube.AddTranslateOp().Set(pos)
                self.qubit_data.append({"id": f"{i}_{j}", "height": height})
        
        self.stage.Save()
        return f"Generated {count*count} Qubits for data collection."

    def run_measurement(self, log_file="quantum_data_log.csv"):
        results = {"Alpha": 0, "Beta": 0}
        max_height = max(d["height"] for d in self.qubit_data)
        
        # Prepare the CSV file
        with open(log_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Qubit_ID", "Fall_Height", "Resulting_State"])
            
            for data in self.qubit_data:
                stress_factor = data["height"] / max_height
                
                # Logic: Probability of Beta increases with height
                state = "Alpha" if random.random() > (stress_factor * 0.8) else "Beta"
                
                results[state] += 1
                # Log the specific data point
                writer.writerow([data["id"], round(data["height"], 2), state])
                
        return results