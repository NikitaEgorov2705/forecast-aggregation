
import pandas as pd
import os

# List of CSV files to convert
csv_files = [
    'rct-a-daily-forecasts.csv',
    'rct-a-prediction-sets.csv',
    'rct-a-questions-answers.csv'
]

def convert_csv_to_feather(csv_file):
    # Get the base name of the file (without extension)
    base_name = os.path.splitext(csv_file)[0]
    
    # Read the CSV file
    print(f"Reading {csv_file}...")
    df = pd.read_csv(csv_file)
    
    # Create the Feather file name
    feather_file = f"{base_name}.feather"
    
    # Write to Feather format
    print(f"Converting to {feather_file}...")
    df.to_feather(feather_file)
    
    print(f"Conversion complete: {feather_file}")
    
    # Print file size comparison
    csv_size = os.path.getsize(csv_file)
    feather_size = os.path.getsize(feather_file)
    print(f"CSV size: {csv_size:,} bytes")
    print(f"Feather size: {feather_size:,} bytes")
    print(f"Size reduction: {(1 - feather_size/csv_size)*100:.2f}%")
    print()

# Convert each CSV file to Feather
for csv_file in csv_files:
    convert_csv_to_feather(csv_file)

print("All conversions completed.")