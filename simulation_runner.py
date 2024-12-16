import pandas as pd
import matplotlib.pyplot as plt
from scripts.material_analysis import load_material_data, calculate_emissions
from scripts.health_impact_model import calculate_health_risks

# Step 1: Load Data
material_data = load_material_data('./data/material_data.csv')
health_data = pd.read_csv('./data/health_data.csv')

# Step 2: Analyze Material Emissions
material_data = calculate_emissions(material_data)

# Step 3: Simulate Health Risks
simulation_results = calculate_health_risks(material_data, health_data, years=20)

# Step 4: Save Results
simulation_results.to_csv('./results/health_simulation_results.csv', index=False)

# Step 5: Visualize Results
plt.plot(simulation_results['Year'], simulation_results['Health_Risk_Score'], marker='o')
plt.title('Long-Term Health Impact of Construction Materials')
plt.xlabel('Years')
plt.ylabel('Cumulative Health Risk Score')
plt.grid()
plt.savefig('./results/health_impact_graph.png')
plt.show()
