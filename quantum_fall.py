from pxr import Usd, UsdGeom, Gf, UsdPhysics

def generate_quantum_scene():
    # 1. Create a Stage (The file itself)
    stage_path = "quantum_sim.usda"
    stage = Usd.Stage.CreateNew(stage_path)
    
    # 2. Set the "Universe" rules
    UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)
    world = UsdGeom.Xform.Define(stage, "/World")
    
    # 3. Create the 'Qubit' (Our Cube)
    cube_path = "/World/QubitCube"
    cube = UsdGeom.Cube.Define(stage, cube_path)
    
    # Lift it high (Z=500) so it has room to fall
    cube.AddTranslateOp().Set(Gf.Vec3d(0, 0, 500))
    
    # 4. Attach Physics Metadata
    # This is the 'DNA' that tells Omniverse to treat this as a solid object
    prim = stage.GetPrimAtPath(cube_path)
    UsdPhysics.RigidBodyAPI.Apply(prim)
    UsdPhysics.CollisionAPI.Apply(prim)
    
    # 5. Create a 'Measurement Plane' (The Floor)
    floor_path = "/World/Ground"
    floor = UsdGeom.Plane.Define(stage, floor_path)
    UsdPhysics.CollisionAPI.Apply(stage.GetPrimAtPath(floor_path))
    
    # 6. Finalize and Save
    stage.GetRootLayer().Save()
    print(f"--- SUCCESS ---")
    print(f"Generated {stage_path} with Physics Metadata.")
    print(f"You can now download this file to your Mac.")

if __name__ == "__main__":
    generate_quantum_scene()