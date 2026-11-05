import numpy as np


class Analyzer:

    def __init__(self, df):
        self.df = df

    # ---------------------------------
    # Basic Statistics
    # ---------------------------------

    def total_records(self):
        return len(self.df)

    def total_job_titles(self):
        return self.df["job_title"].nunique()

    def total_industries(self):
        return self.df["industry"].nunique()

    def total_locations(self):
        return self.df["location"].nunique()

    def average_salary(self):
        return round(self.df["salary"].mean(), 2)

    def highest_salary(self):
        return round(self.df["salary"].max(), 2)

    def lowest_salary(self):
        return round(self.df["salary"].min(), 2)

    def total_salary(self):
        return round(self.df["salary"].sum(), 2)

    def average_experience(self):
        return round(self.df["experience_years"].mean(), 2)

    def average_skills(self):
        return round(self.df["skills_count"].mean(), 2)

    def average_certifications(self):
        return round(self.df["certifications"].mean(), 2)

    # ---------------------------------
    # Job Title Analysis
    # ---------------------------------

    def job_title_analysis(self):

        return (
            self.df
            .groupby("job_title")
            .agg(
                Employees=("job_title", "count"),
                Average_Salary=("salary", "mean")
            )
            .round(2)
            .reset_index()
        )

    # ---------------------------------
    # Industry Analysis
    # ---------------------------------

    def industry_analysis(self):

        return (
            self.df
            .groupby("industry")
            .agg(
                Employees=("industry", "count"),
                Average_Salary=("salary", "mean")
            )
            .round(2)
            .reset_index()
        )

    # ---------------------------------
    # Location Analysis
    # ---------------------------------

    def location_analysis(self):

        return (
            self.df
            .groupby("location")
            .agg(
                Employees=("location", "count"),
                Average_Salary=("salary", "mean")
            )
            .round(2)
            .reset_index()
        )

    # ---------------------------------
    # Company Size Analysis
    # ---------------------------------

    def company_size_analysis(self):

        return (
            self.df
            .groupby("company_size")
            .agg(
                Employees=("company_size", "count"),
                Average_Salary=("salary", "mean")
            )
            .round(2)
            .reset_index()
        )

    # ---------------------------------
    # Education Analysis
    # ---------------------------------

    def education_analysis(self):

        return (
            self.df
            .groupby("education_level")
            .agg(
                Employees=("education_level", "count"),
                Average_Salary=("salary", "mean")
            )
            .round(2)
            .reset_index()
        )

    # ---------------------------------
    # NumPy Statistics
    # ---------------------------------

    def mean_salary_numpy(self):
        return round(np.mean(self.df["salary"]), 2)

    def median_salary_numpy(self):
        return round(np.median(self.df["salary"]), 2)

    def std_salary_numpy(self):
        return round(np.std(self.df["salary"]), 2)

    def variance_salary_numpy(self):
        return round(np.var(self.df["salary"]), 2)

    def minimum_salary_numpy(self):
        return round(np.min(self.df["salary"]), 2)

    def maximum_salary_numpy(self):
        return round(np.max(self.df["salary"]), 2)

    # ---------------------------------
    # Report Insights
    # ---------------------------------

    def highest_paying_job(self):
        return (
            self.df.groupby("job_title")["salary"]
            .mean()
            .idxmax()
        )

    def lowest_paying_job(self):
        return (
            self.df.groupby("job_title")["salary"]
            .mean()
            .idxmin()
        )

    def highest_paying_industry(self):
        return (
            self.df.groupby("industry")["salary"]
            .mean()
            .idxmax()
        )

    def most_common_job(self):
        return self.df["job_title"].value_counts().idxmax()

    def total_salary_expense(self):
        return round(self.df["salary"].sum(), 2)

    def average_experience_report(self):
        return round(self.df["experience_years"].mean(), 2)