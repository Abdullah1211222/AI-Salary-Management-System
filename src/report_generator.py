
import pandas as pd


class ReportGenerator:

    def __init__(self, df):
        self.df = df

    def generate_department_report(self):

        report = (
            self.df
            .groupby("Department")
            .agg(
                Employees=("Employee_ID", "count"),
                Average_Salary=("Salary", "mean"),
                Highest_Salary=("Salary", "max"),
                Lowest_Salary=("Salary", "min"),
                Total_Salary=("Salary", "sum")
            )
            .reset_index()
        )

        report["Average_Salary"] = report["Average_Salary"].round(2)

        return report

    def generate_country_report(self):

        report = (
            self.df
            .groupby("Country")
            .agg(
                Employees=("Employee_ID", "count"),
                Average_Salary=("Salary", "mean")
            )
            .reset_index()
        )

        report["Average_Salary"] = report["Average_Salary"].round(2)

        return report