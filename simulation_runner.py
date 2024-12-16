import os
import pandas as pd

# Ensure the results directory exists
output_dir = './results'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Your simulation results data
simulation_results = pd.DataFrame({
    # Example data (replace with your actual simulation results)
    "Material": ["Concrete", "Cement"],
    "Yearly_Emission": [500, 150],
    "Health_Risk": [1.2, 0.8]
})

# Save the results to a CSV file inside the results folder
output_file = os.path.join(output_dir, 'health_simulation_results.csv')
simulation_results.to_csv(output_file, index=False)

print(f"Simulation results saved to {output_file}")
