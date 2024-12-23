import pandas as pd

def calculate_health_risks(material_data, health_data, years=20):
    """
    Simulate long-term health risks based on material emissions and sensitivity factors.
    """
    results = []
    for year in range(1, years + 1):
        yearly_risks = []
        for _, mat_row in material_data.iterrows():
            for _, health_row in health_data.iterrows():
                # Risk = Emissions * Toxicity * Sensitivity * Time
                risk = (
                    mat_row['Yearly_Emission']
                    * mat_row['Toxicity_Score']
                    * health_row['Sensitivity_Factor']
                    * year
                )
                yearly_risks.append(risk)
        results.append({'Year': year, 'Health_Risk_Score': sum(yearly_risks)})
    return pd.DataFrame(results)
