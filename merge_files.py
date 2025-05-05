import pandas as pd
import os

# Set the folder where all your listings.csv files are saved
folder_path = 'Data/'

# Initialize empty list to hold DataFrames
all_dfs = []

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        city = filename.split('.')[0]  # get filename without .csv
        df = pd.read_csv(os.path.join(folder_path, filename))
        df['city'] = city  # add city column for distinction
        all_dfs.append(df)

# Combine all DataFrames into one
df_combined = pd.concat(all_dfs, ignore_index=True)

# Optional: Save combined file
df_combined.to_csv("all_listings_combined.csv", index=False)
