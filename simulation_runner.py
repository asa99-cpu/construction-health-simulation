import pandas as pd
import plotly.express as px
import streamlit as st
from scripts.material_analysis import load_material_data, calculate_emissions
from scripts.health_impact_model import calculate_health_risks

# Load material data and health data
material_data = load_material_data('./data/material_data.csv')

# Calculate emissions
material_data = calculate_emissions(material_data)

# Simulate health risks based on material emissions
health_data = pd.read_csv('./data/health_data.csv')
simulation_results = calculate_health_risks(material_data, health_data)

# Save the simulation results to a CSV file
simulation_results.to_csv('./results/health_simulation_results.csv', index=False)

# Display the simulation results in the Streamlit app
st.title("Construction Health Simulation Results")
st.subheader("The simulation results are shown below:")
st.write(simulation_results)

# Bar chart for Yearly Emissions by Material
st.subheader("Yearly Emissions by Material")
fig = px.bar(simulation_results, x='Material', y='Yearly_Emission',
             title="Yearly Emission by Material",
             labels={'Yearly_Emission': 'Yearly Emission (g/m²/year)', 'Material': 'Material'})
st.plotly_chart(fig)

# Line chart for Health Risk by Material
st.subheader("Health Risk by Material")
fig2 = px.line(simulation_results, x='Material', y='Health_Risk',
               title="Health Risk by Material",
               labels={'Health_Risk': 'Health Risk', 'Material': 'Material'})
st.plotly_chart(fig2)

# Display a success message
st.success("Simulation results saved to './results/health_simulation_results.csv'")
