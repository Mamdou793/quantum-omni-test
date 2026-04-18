import random
from pxr import Usd, UsdGeom, Gf

def apply_quantum_measurement(stage_path):
    # 1. Open the stage you just created
    stage = Usd.Stage.Open(stage_path)
    qubit_prim = stage.GetPrimAtPath("/World/QubitCube")
    
    # 2. Define the 'Quantum Measurement' Logic
    # In physics, the state collapses only upon observation (collision)
    possible_states = {
        "State_Alpha": Gf.Vec3f(0, 1, 0), # Green (Spin Up)
        "State_Beta": Gf.Vec3f(1, 0, 0)   # Red (Spin Down)
    }
    
    # Randomly select a state
    collapsed_state, color_value = random.choice(list(possible_states.items()))
    
    # 3. Apply the visual change to the USD file
    # We use the 'Display Color' attribute
    cube_geom = UsdGeom.Cube(qubit_prim)
    color_attr = cube_geom.GetDisplayColorAttr()
    
    if not color_attr:
        color_attr = cube_geom.CreateDisplayColorAttr()
    
    color_attr.Set([color_value])
    
    # 4. Save the new "Measured" state
    stage.GetRootLayer().Save()
    print(f"--- QUANTUM MEASUREMENT COMPLETE ---")
    print(f"Observation Result: {collapsed_state}")
    print(f"The Qubit has collapsed and is now visible as {color_value}")

if __name__ == "__main__":
    apply_quantum_measurement("quantum_sim.usda")