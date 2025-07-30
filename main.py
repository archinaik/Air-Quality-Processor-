"""
# main.py

This script reads air quality datasets for different pollutants,
adds a label to each, merges them, and prints a summary.

Written by: Archi Naik
"""

import pandas as pd


files = {
    "TEMPERATURE": "temperature.csv",
    "RELATIVEHUMIDITY": "humidity.csv",
    "SO2": "so2.csv",
    "PM2.5": "pm25.csv"
}

dataframes = []

def load_and_label_data():
    """
    Function to load data and label it with the pollutant type.
    """
    for pollutant, file in files.items():
        try:
            df = pd.read_csv(file, sep=";", encoding="utf-8")  
            df['pollutant'] = pollutant
            dataframes.append(df)
        except Exception as e:
            print(f"Error loading {file}: {e}")
    return dataframes


def merge_data(dataframes):
    """
    Combines all pollutant DataFrames into one single DataFrame.
    """
    return pd.concat(dataframes, ignore_index=True)

def save_combined_data(df):
    """
    Saves the combined DataFrame to a CSV file.
    """
    df.to_csv("merged_data.csv", index=False)

def print_summary(df):
    """
    Prints the number of files processed and the total number of rows.
    """
    print("Number of files downloaded:", len(dataframes))
    print("Total number of records in merged file:", len(df))

def print_max_min_summary(df):
    """
    Prints the maximum and minimum values for each pollutant.
    """
    print("\nPollutant\tMax\tMin")
    value_column = "Value"
    
    for pollutant in df["pollutant"].unique():
        subset = df[df["pollutant"] == pollutant]
        if value_column in subset.columns:
            max_val = subset[value_column].max()
            min_val = subset[value_column].min()
            print(f"{pollutant}:\t{max_val}\t{min_val}")
        else:
            print(f"{pollutant}:\t[Value column missing]")

def main():
    dataframes = load_and_label_data()
    combined_df = merge_data(dataframes)
    save_combined_data(combined_df)
    print_summary(combined_df)
    print_max_min_summary(combined_df)


if __name__ == "__main__":
    main()
