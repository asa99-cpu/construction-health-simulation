import pandas as pd
import plotly.express as px
import streamlit as st

# Simulating loading data
simulation_results = pd.DataFrame({
    'Material': ['Concrete', 'Cement'],
    'Yearly_Emission': [500, 150],
    'Health_Risk': [1.2, 0.8],
    'Time_Period': ['2024', '2025']  # Example for animation (can be time or another variable)
})

# Ensure the 'Yearly_Emission' is numeric for animation
simulation_results['Yearly_Emission'] = pd.to_numeric(simulation_results['Yearly_Emission'], errors='coerce')

# Create animated bar chart with Plotly
fig = px.bar(simulation_results, 
             x='Material', 
             y='Yearly_Emission', 
             color='Material', 
             animation_frame='Time_Period',  # Animate over the time periods
             animation_group='Material',  # Group by material for animation
             range_y=[0, simulation_results['Yearly_Emission'].max() * 1.1],  # Adjust y-range
             title="Yearly Emission of Materials Over Time",
             labels={"Yearly_Emission": "Emission (g/m²/year)", "Material": "Material"})

# Show plot in Streamlit
st.plotly_chart(fig)
