import pandas as pd

def filter_and_save_csv(input_csv, output_csv):
    # Read the CSV into a DataFrame
    df = pd.read_csv(input_csv)

    # Get unique values in the third column
    unique_values = df.iloc[:, 2].unique()

    # Filter the DataFrame based on unique values and create a new CSV
    filtered_df = df[df.iloc[:, 2].isin(unique_values)]
    filtered_df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    input_csv = 'input.csv'  # Replace with the actual input CSV file name
    output_csv = 'output.csv'  # Replace with the desired output CSV file name

    filter_and_save_csv(input_csv, output_csv)
