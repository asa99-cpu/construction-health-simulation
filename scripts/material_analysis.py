import pandas as pd

def load_material_data(file_path):
    """
    Load material data from a CSV file.
    """
    return pd.read_csv(file_path)

def calculate_emissions(material_data):
    """
    Calculate yearly emissions based on material properties.
    """
    material_data['Yearly_Emission'] = material_data['Emission_Rate'] * material_data['Surface_Area']
    return material_data
