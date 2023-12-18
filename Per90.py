import pandas as pd

# Load the CSV file into a DataFrame, skipping the header row
df = pd.read_csv('PlayerDataRaw.csv')

# Choose the column by which you want to divide all other columns
divisor_column = '90s'

# Divide all other columns by the specified column
# Convert columns to numeric (assuming columns 1 and onwards are numeric)
df.iloc[:, 1:] = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Perform the division
df.iloc[:, 1:] = df.iloc[:, 1:].div(df[divisor_column], axis=0)

df.iloc[:, 1:] = df.iloc[:, 1:].round(4)

# Save the modified DataFrame to a new CSV file
df.to_csv('PlayerDataRefined.csv', index=False)
