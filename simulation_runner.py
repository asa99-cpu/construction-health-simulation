import streamlit as st
import pandas as pd
import os

# Ensure the results directory exists
output_dir = './results'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Example simulation results
simulation_results = pd.DataFrame({
    "Material": ["Concrete", "Cement"],
    "Yearly_Emission": [500, 150],
    "Health_Risk": [1.2, 0.8]
})

# Displaying the DataFrame on Streamlit
st.title("Construction Health Simulation Results")
st.write("The simulation results are shown below:")

# Display the results in a table
st.dataframe(simulation_results)

# Save the results to a CSV file
output_file = os.path.join(output_dir, 'health_simulation_results.csv')
simulation_results.to_csv(output_file, index=False)

st.write(f"Simulation results saved to {output_file}")
