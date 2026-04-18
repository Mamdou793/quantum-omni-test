A cloud-native simulation pipeline for generating 3D digital twins with embedded quantum measurement logic. This project demonstrates the integration of OpenUSD (Universal Scene Description) with custom Python-based physics metadata.

This project utilizes a multi-platform development strategy to bypass local hardware constraints:

Development Environment: MacBook Air (macOS ARM64).

Compute Bridge: GitHub Codespaces (Ubuntu Linux x86_64) to support NVIDIA/Pixar USD binaries.

Target Simulation: NVIDIA Omniverse RTX Renderer.



Features:

USD Scene Generation: Programmatically creates a 3D environment including a "Qubit" (Rigid Body Cube) and a "Measurement Plane" (Static Collision Floor).

Physics Metadata: Injects PhysicsRigidBodyAPI and PhysicsCollisionAPI directly into the .usda layer.

Quantum State Collapse: A Python-based observer script that simulates wavefunction collapse upon interaction, randomly assigning a discrete state (Red vs. Green) to the object.
