# Air Quality Processor

This is a Python project that downloads and processes air quality data for multiple pollutants like Temperature, Humidity, SO2, and PM2.5. The data is then cleaned, merged into one CSV file, and summary statistics are printed.

## What this project does

- Reads four CSV files from the internet using `pandas`
- Adds a column for each pollutant name
- Merges them all into one combined DataFrame
- Saves the final merged data as `mereged_data.csv`
- Prints a summary:
  - Total number of files
  - Number of rows
  - Max and min values for each pollutant

##  Technologies Used

- Python 3.13
- pandas
- Ruff (for linting)
- unit testing

