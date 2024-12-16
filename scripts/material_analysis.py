import pandas as pd

# Function to load material data from CSV
def load_material_data(file_path):
    try:
        # Read the material data CSV file
        material_data = pd.read_csv(file_path)
        # Check if the necessary columns are present
        expected_columns = ['Material', 'Emission_Rate', 'Toxicity_Score', 'Surface_Area']
        if not all(col in material_data.columns for col in expected_columns):
            raise ValueError(f"Missing one or more expected columns: {expected_columns}")
        return material_data
    except Exception as e:
        print(f"Error loading material data: {e}")
        return None

# Function to calculate the yearly emissions for each material
def calculate_emissions(material_data):
    if material_data is None:
        return None
    
    # Ensure the columns exist in the data
    if 'Emission_Rate' not in material_data.columns or 'Surface_Area' not in material_data.columns:
        raise KeyError("Missing required columns 'Emission_Rate' or 'Surface_Area'.")
    
    # Calculate the yearly emissions for each material
    material_data['Yearly_Emission'] = material_data['Emission_Rate'] * material_data['Surface_Area']
    return material_data

# Example usage of the functions
if __name__ == "__main__":
    # Load material data from the CSV file
    file_path = './data/material_data.csv'  # Adjust path if necessary
    material_data = load_material_data(file_path)

    # If data is loaded successfully, calculate emissions
    if material_data is not None:
        material_data = calculate_emissions(material_data)
        print(material_data)  # Display the calculated data (for testing)
