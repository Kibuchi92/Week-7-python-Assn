import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Load dataset (replace 'your_dataset.csv' with your file path)
    df = pd.read_csv('your_dataset.csv')

    # Data Exploration
    print("----- Dataset Info -----")
    df.info()

    print("\n----- First 5 rows -----")
    print(df.head())

    # Basic Data Analysis
    print("\n----- Summary Statistics -----")
    print(df.describe())

    print("\n----- Missing Values -----")
    print(df.isnull().sum())

    # Visualization 1: Histogram of a numerical column (replace 'ColumnName')
    plt.figure(figsize=(8,5))
    plt.hist(df['ColumnName'].dropna(), bins=30, color='skyblue', edgecolor='black')
    plt.title('Distribution of ColumnName')
    plt.xlabel('ColumnName')
    plt.ylabel('Frequency')
    plt.show()

    # Visualization 2: Scatter plot for two numerical columns (replace 'Col1' and 'Col2')
    plt.figure(figsize=(8,5))
    plt.scatter(df['Col1'], df['Col2'], alpha=0.6, color='green')
    plt.title('Scatter Plot of Col1 vs Col2')
    plt.xlabel('Col1')
    plt.ylabel('Col2')
    plt.show()

    # Observations:
    # - Describe distribution, any notable data characteristics observed.
    # - Note any correlation or pattern visible in the scatter plot.

if __name__ == "__main__":
    main()
