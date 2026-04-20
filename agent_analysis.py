import pandas as pd
from openai import AzureOpenAI
import os
import re

# --- 1. Configuration ---
# Update these with your specific Azure Details
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_API_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_API_VERSION = "2024-06-01" 
DEPLOYMENT_NAME = "gpt-4o-mini" # e.g. "Mamdouh-GPT4o"

def get_ai_recommendation(csv_file):
    """
    Analyzes quantum stress data and extracts a shielding parameter.
    """
    # Load the results from the simulation
    if not os.path.exists(csv_file):
        return "Error: CSV file not found.", 0.0

    df = pd.read_csv(csv_file)
    total_qubits = len(df)
    alpha_count = len(df[df['Resulting_State'] == 'Alpha'])
    fidelity = (alpha_count / total_qubits) * 100

    # Create a summary table for the AI to look at
    height_stats = df.groupby('Fall_Height')['Resulting_State'].value_counts(normalize=True).unstack().fillna(0)

    # Initialize the Azure Client
    client = AzureOpenAI(
        azure_endpoint=AZURE_ENDPOINT,
        api_key=AZURE_API_KEY,
        api_version=AZURE_API_VERSION
    )

    # The "Hybrid" Prompt: Asks for a human report AND a machine-readable value
    prompt = f"""
    You are a Senior Quantum Systems Architect. 
    Analyze the following experimental data from a Digital Twin stress test:
    
    - Total Qubits: {total_qubits}
    - System Fidelity: {fidelity:.2f}%
    - Max Fall Height: 23.0 meters
    
    Height Data Summary (Probability of Alpha/Beta):
    {height_stats.to_string()}

    TASK:
    1. Provide a professional Engineering Report in Markdown (Summary, Critical Decoherence Height, and Recommendations).
    2. Based on the 25% fidelity, calculate a RECOMMENDED_SHIELDING factor between 0.0 and 1.0 
       (where 1.0 is maximum protection). 

    CRITICAL: You must include the following line at the very end of your response:
    RECOMMENDED_SHIELDING: [value]
    """

    # Call the AI
    response = client.chat.completions.create(
        model=DEPLOYMENT_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    full_content = response.choices[0].message.content

    # --- REGEX LOGIC: Extracting the shielding value ---
    # This looks for the pattern "RECOMMENDED_SHIELDING: " followed by a number
    match = re.search(r"RECOMMENDED_SHIELDING:\s*([\d\.]+)", full_content)
    
    if match:
        shielding_value = float(match.group(1))
    else:
        print("⚠️ Warning: AI did not provide a clear shielding value. Defaulting to 0.5")
        shielding_value = 0.5

    return full_content, shielding_value

# This allows you to run the script standalone for testing
if __name__ == "__main__":
    print("🔬 Running Agent Analysis on latest data...")
    report, value = get_ai_recommendation("quantum_stress_results.csv")
    
    # Save the professional report for the user
    with open("Quantum_Stability_Report.md", "w") as f:
        f.write(report)
    
    print(f"✅ Report generated: 'Quantum_Stability_Report.md'")
    print(f"🤖 AI Recommended Shielding Factor: {value}")