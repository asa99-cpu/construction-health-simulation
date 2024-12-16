import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np

# Simulate the timeline of a human's life over 20 years
years = list(range(2024, 2044))  # From 2024 to 2044 (20 years)
age_groups = ['Child', 'Adolescent', 'Adult', 'Senior']

# Simulated health effects over time for construction materials (e.g., Concrete, Cement)
# The health risk scales here would depend on the years exposed to each material.
health_risks = {
    'Concrete': [0.5 + i*0.03 for i in range(20)],  # Gradually increasing health risk for Concrete
    'Cement': [0.3 + i*0.02 for i in range(20)],    # Gradual increase for Cement, slower than Concrete
}

# Creating a DataFrame to simulate a human's health over the 20 years
data = []

for year in years:
    for material in ['Concrete', 'Cement']:
        # For simplicity, let's assume a person starts from a "Child" and goes through life stages.
        age = year - 2024
        if age < 5:
            life_stage = 'Child'
        elif 5 <= age < 12:
            life_stage = 'Adolescent'
        elif 12 <= age < 60:
            life_stage = 'Adult'
        else:
            life_stage = 'Senior'
        
        health_data = {
            'Year': year,
            'Material': material,
            'Health_Risk': health_risks[material][years.index(year)],
            'Age': age,
            'Life_Stage': life_stage,
        }
        data.append(health_data)

df_health = pd.DataFrame(data)

# Create an animated bar chart using Plotly to visualize the health risk over time
fig = px.bar(df_health, 
             x='Year', 
             y='Health_Risk', 
             color='Material', 
             animation_frame='Year', 
             animation_group='Material', 
             title="Health Risk Over Time due to Material Exposure",
             labels={"Year": "Year", "Health_Risk": "Health Risk", "Material": "Construction Material", "Age": "Age Group"},
             facet_col='Life_Stage',  # Creating a facet for each life stage (Child, Adolescent, etc.)
             height=600)

# Show the animated chart in Streamlit
st.plotly_chart(fig)
