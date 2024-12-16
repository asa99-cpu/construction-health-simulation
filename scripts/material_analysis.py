import pandas as pd

def load_material_data(file_path):
    """
    Load material data from a CSV file.
    """
    material_data = pd.read_csv(file_path)
    return material_data

def calculate_emissions(material_data):
    """
    Calculate yearly emissions based on the emission rate and surface area of materials.
    """
    # Ensure 'Emission_Rate' and 'Surface_Area' columns exist before performing calculation
    if 'Emission_Rate' in material_data.columns and 'Surface_Area' in material_data.columns:
        material_data['Yearly_Emission'] = material_data['Emission_Rate'] * material_data['Surface_Area']
    else:
        raise ValueError("Missing 'Emission_Rate' or 'Surface_Area' columns in material data.")
    
    return material_data
