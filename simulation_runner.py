import pandas as pd
import plotly.express as px
import streamlit as st

# Simulating the creation of synthetic health data over 20 years
years = list(range(2024, 2044))
materials = ['Concrete', 'Cement']

# Example health risks associated with materials and emission rates (can be more detailed)
health_risks = {
    'Concrete': [1.2 * (1 + i*0.05) for i in range(20)],  # Increasing health risk over time
    'Cement': [0.8 * (1 + i*0.03) for i in range(20)]     # Slower increase for Cement
}

# Creating a DataFrame to hold health data over 20 years
data = []

for material in materials:
    for year in years:
        health_data = {
            'Year': year,
            'Material': material,
            'Health_Risk': health_risks[material][years.index(year)],
        }
        data.append(health_data)

df_health = pd.DataFrame(data)

# Create the animation using Plotly (animate health risk over the years)
fig = px.line(df_health, 
              x='Year', 
              y='Health_Risk', 
              color='Material', 
              line_group='Material', 
              animation_frame='Year', 
              animation_group='Material', 
              title="Health Risk Over Time due to Material Exposure",
              labels={"Year": "Year", "Health_Risk": "Health Risk (Scale 0-10)", "Material": "Building Material"})

# Show the animated chart in Streamlit
st.plotly_chart(fig)
