import random
from pxr import Usd, UsdGeom, Gf

def run_monte_carlo_measurement(stage_path):
    stage = Usd.Stage.Open(stage_path)
    all_prims = stage.Traverse()
    
    stats = {"Alpha (Green)": 0, "Beta (Red)": 0}

    for prim in all_prims:
        if "Qubit" in prim.GetName():
            # 50/50 Probability
            is_alpha = random.choice([True, False])
            color = Gf.Vec3f(0, 1, 0) if is_alpha else Gf.Vec3f(1, 0, 0)
            
            # Apply Color to the individual Qubit
            cube_geom = UsdGeom.Cube(prim)
            display_color = cube_geom.GetDisplayColorAttr()
            if not display_color:
                display_color = cube_geom.CreateDisplayColorAttr()
            display_color.Set([color])
            
            # Update Stats
            if is_alpha: stats["Alpha (Green)"] += 1
            else: stats["Beta (Red)"] += 1

    stage.GetRootLayer().Save()
    
    # Final Report
    total = stats["Alpha (Green)"] + stats["Beta (Red)"]
    print(f"\n--- QUANTUM MEASUREMENT REPORT ---")
    print(f"Total Entities: {total}")
    for state, count in stats.items():
        percentage = (count / total) * 100
        print(f"{state}: {count} ({percentage:.1f}%)")

if __name__ == "__main__":
    run_monte_carlo_measurement("quantum_array_sim.usda")