import pandas as pd
import numpy as np

# Number of rows
num_rows = 1000

# Generating random data
np.random.seed(42)  # For reproducibility

soil_ids = np.arange(1, num_rows + 1)
ph_levels = np.random.uniform(5.0, 8.0, num_rows)
nitrogen = np.random.uniform(20, 80, num_rows)
phosphorus = np.random.uniform(10, 60, num_rows)
potassium = np.random.uniform(30, 90, num_rows)
moisture = np.random.uniform(10, 40, num_rows)
organic_matter = np.random.uniform(2.0, 8.0, num_rows)
textures = np.random.choice(["Sandy Loam", "Clay Loam", "Silt Loam", "Sandy", "Clay", "Loam", "Silt", "Sandy Clay Loam"], num_rows)

# Creating the DataFrame
large_data = {
    "SoilID": soil_ids,
    "pH": ph_levels,
    "Nitrogen (ppm)": nitrogen,
    "Phosphorus (ppm)": phosphorus,
    "Potassium (ppm)": potassium,
    "Moisture (%)": moisture,
    "Organic Matter (%)": organic_matter,
    "Texture": textures
}

large_df = pd.DataFrame(large_data)

# Save DataFrame to CSV
large_csv_file_path = 'C:/Users/arsul/Desktop/large_soil_data.csv'  # Replace with your desired path

large_df.to_csv(large_csv_file_path, index=False)

# Read the CSV file
data = pd.read_csv(large_csv_file_path)

print(data.head())  # Print the first 5 rows
