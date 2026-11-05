import pandas as pd
from pathlib import Path


class DatasetLoader:

    def __init__(self):
        print("DatasetLoader Created")

    def load_dataset(self):

        # Get the current folder (src)
        current_folder = Path(__file__).parent

        # Path to data folder
        data_file = current_folder.parent / "data" / "job_salary_dataset.csv"

        # Read dataset
        df = pd.read_csv(data_file)

        # Remove extra spaces from column names
        df.columns = df.columns.str.strip()

        return df


# ----------------------------------------
# Testing
# ----------------------------------------

if __name__ == "__main__":

    loader = DatasetLoader()

    df = loader.load_dataset()

    print("\n========== FIRST 5 ROWS ==========\n")
    print(df.head())

    print("\n========== COLUMN NAMES ==========\n")
    print(df.columns.tolist())

    print("\n========== DATA TYPES ==========\n")
    print(df.dtypes)

    print("\n========== DATASET SHAPE ==========\n")
    print(df.shape)