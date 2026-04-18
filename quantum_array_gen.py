from pxr import Usd, UsdGeom, Gf, UsdPhysics

def generate_qubit_array(count=10):
    stage_path = "quantum_array_sim.usda"
    stage = Usd.Stage.CreateNew(stage_path)
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
    
    # Create the 'Environment' container
    world = UsdGeom.Xform.Define(stage, "/World")
    
    # Define a Ground Plane
    floor_path = "/World/Ground"
    floor = UsdGeom.Plane.Define(stage, floor_path)
    UsdPhysics.CollisionAPI.Apply(stage.GetPrimAtPath(floor_path))

    # The Logic: Spacing and Placement
    spacing = 150 
    for i in range(count):
        for j in range(count):
            # Unique Namespace: Qubit_0_0, Qubit_0_1...
            qubit_path = f"/World/Qubit_{i}_{j}"
            cube = UsdGeom.Cube.Define(stage, qubit_path)
            
            # Math for Grid Placement
            x_pos = i * spacing
            y_pos = j * spacing
            cube.AddTranslateOp().Set(Gf.Vec3d(x_pos, y_pos, 500))
            
            # Apply Rigid Body & Collision to every single cube
            prim = stage.GetPrimAtPath(qubit_path)
            UsdPhysics.RigidBodyAPI.Apply(prim)
            UsdPhysics.CollisionAPI.Apply(prim)

    stage.GetRootLayer().Save()
    print(f"--- SUCCESS ---")
    print(f"Generated a {count}x{count} Grid (100 Entities) in {stage_path}")

if __name__ == "__main__":
    generate_qubit_array(10)