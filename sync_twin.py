import pandas as pd
import time
import os

USDA_FILE = "quantum_simulation_v3.usda"

def update_usda_color(fidelity):
    if not os.path.exists(USDA_FILE):
        return
    
    # Calculate a color based on fidelity: 100% = Green, 0% = Red
    # Simplified RGB: (Red_intensity, Green_intensity, 0)
    green_val = round(fidelity / 100, 2)
    red_val = round(1 - green_val, 2)
    new_color = f"({red_val}, {green_val}, 0)"

    with open(USDA_FILE, 'r') as f:
        content = f.read()

    # This assumes your qubits have a displayColor attribute in the USD
    # We will look for 'color3f[] displayColor' and swap it
    import re
    updated_content = re.sub(r'color3f\[\] displayColor = \[\(.*?\)', 
                             f'color3f[] displayColor = [{new_color}', content)

    with open(USDA_FILE, 'w') as f:
        f.write(updated_content)
    print(f"🎨 USD Visuals Updated: System Glow is now {new_color}")

def update_visual_twin():
    print("🔄 Watcher active: Monitoring for system changes...")
    last_processed = None

    while True:
        if os.path.exists("dashboard_metrics.csv"):
            df = pd.read_csv("dashboard_metrics.csv")
            latest_run = df.iloc[-1]
            
            if latest_run['Timestamp'] != last_processed:
                shielding = latest_run['Shielding']
                fidelity = latest_run['Fidelity']
                
                print(f"🚀 New Data Detected! Updating Twin: Shielding={shielding}, Fidelity={fidelity}%")
                
                # TRIGGER THE VISUAL CHANGE
                update_usda_color(fidelity)
                
                last_processed = latest_run['Timestamp']
        
        time.sleep(5)

if __name__ == "__main__":
    update_visual_twin()