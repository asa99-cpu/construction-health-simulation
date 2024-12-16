import streamlit as st
import pandas as pd
import plotly.express as px
from scripts.material_analysis import load_material_data, calculate_emissions
from scripts.health_impact_model import calculate_health_risks

# Load data
material_data = load_material_data('./data/material_data.csv')
health_data = pd.read_csv('./data/health_data.csv')

# Calculate emissions
material_data = calculate_emissions(material_data)

# Calculate health risks based on material data
simulation_results = calculate_health_risks(material_data, health_data)

# Display simulation results
st.title("Construction Health Simulation Results")
st.write("The simulation results are shown below:")
st.write(simulation_results)

# Bar chart for Yearly Emissions by Material
st.subheader("Yearly Emissions by Material")
fig = px.bar(simulation_results, x='Material', y='Yearly_Emission',
             title="Yearly Emission by Material",
             labels={'Yearly_Emission': 'Yearly Emission (g/m²/year)', 'Material': 'Material'})
st.plotly_chart(fig)

# Scatter plot for Health Risks vs Emissions
st.subheader("Health Risks vs Yearly Emissions")
fig = px.scatter(simulation_results, x='Yearly_Emission', y='Health_Risk',
                 color='Material', title="Health Risks vs Yearly Emissions",
                 labels={'Yearly_Emission': 'Yearly Emission (g/m²/year)', 'Health_Risk': 'Health Risk'})
st.plotly_chart(fig)

# Animation: Emissions vs Health Risks Over Time (if you have time-related data)
# If you have time-based data for the emission rates, you can create an animated graph like this:
# You would need to add a 'Year' column to your data for this animation.

# Example of an animation setup (assuming you have a 'Year' column in the data)
# st.subheader("Emissions Over Time")
# fig = px.scatter(simulation_results, x='Year', y='Health_Risk', animation_frame='Year', 
#                  animation_group='Material', color='Material',
#                  title="Health Risk vs Emissions Over Time",
#                  labels={'Health_Risk': 'Health Risk', 'Year': 'Year'})
# st.plotly_chart(fig)

# Save the results to CSV
st.write("Simulation results saved to ./results/health_simulation_results.csv")
simulation_results.to_csv('./results/health_simulation_results.csv', index=False)

# Add download button for results
st.download_button(
    label="Download Simulation Results",
    data=simulation_results.to_csv(index=False).encode(),
    file_name="health_simulation_results.csv",
    mime="text/csv"
)
