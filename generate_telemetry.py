import pandas as pd
import random

def generate_stress_data(scenario="crisis"):
    qubits = 100
    heights = [5.0, 7.0, 9.0, 11.0, 13.0, 15.0, 17.0, 19.0, 21.0, 23.0]
    data = []

    for h in heights:
        for _ in range(qubits // len(heights)):
            # "Crisis" = high chance of Beta (Red)
            # "Optimized" = high chance of Alpha (Green)
            if scenario == "optimized":
                state = "Alpha" if random.random() > 0.2 else "Beta"
            else:
                # High fall heights cause more Beta states
                threshold = 0.8 if h > 10 else 0.4
                state = "Beta" if random.random() < threshold else "Alpha"
                
            data.append({"Fall_Height": h, "Resulting_State": state})

    df = pd.DataFrame(data)
    df.to_csv("quantum_stress_results.csv", index=False)
    print(f"📡 New telemetry generated for scenario: {scenario.upper()}")

if __name__ == "__main__":
    # Toggle between "crisis" and "optimized" here
    generate_stress_data(scenario="optimized")