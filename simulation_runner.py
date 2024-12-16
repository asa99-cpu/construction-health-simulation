import streamlit as st
import pandas as pd
import plotly.express as px
from scripts.material_analysis import load_material_data, calculate_emissions

# Load material data from CSV
material_data = load_material_data('./data/material_data.csv')

# Check the columns in the material data
st.write("Material Data Columns: ", material_data.columns)

# Calculate emissions based on loaded material data
material_data = calculate_emissions(material_data)

# Ensure the 'Yearly_Emission' column exists
st.write("Material Data with Emissions: ", material_data.head())

# Perform your simulation calculations or any other logic here (if needed)

# Display the results in Streamlit
st.write("Simulation Results", material_data)

# Create a bar chart to visualize the data
fig = px.bar(material_data, x='Material', y='Yearly_Emission', 
             title="Yearly Emissions by Material",
             labels={'Yearly_Emission': 'Yearly Emission (g/m²/year)', 'Material': 'Material'})
st.plotly_chart(fig)

# Optionally, you can save the results to a CSV file
material_data.to_csv('./results/health_simulation_results.csv', index=False)
