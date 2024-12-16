import pandas as pd

def load_material_data():
    material_data = pd.read_csv('data/material_data.csv')  # Make sure the path is correct
    print(material_data.columns)  # This will print the column names
    return material_data

def calculate_emissions(material_data):
    """
    Calculate yearly emissions based on material properties.
    """
    material_data['Yearly_Emission'] = material_data['Emission_Rate'] * material_data['Surface_Area']
    return material_data
