import matplotlib.pyplot as plt


class Visualizer:

    def __init__(self, df):
        self.df = df

    # ----------------------------------
    # Employees by Department
    # ----------------------------------

    def department_bar_chart(self):

        department_counts = self.df["Department"].value_counts()

        fig, ax = plt.subplots(figsize=(8,5))

        ax.bar(
            department_counts.index,
            department_counts.values
        )

        ax.set_title("Employees by Department")
        ax.set_xlabel("Department")
        ax.set_ylabel("Employees")

        plt.xticks(rotation=45)

        return fig

    # ----------------------------------
    # Employees by Country
    # ----------------------------------

    def country_pie_chart(self):

        country_counts = self.df["Country"].value_counts()

        fig, ax = plt.subplots(figsize=(7,7))

        ax.pie(
            country_counts.values,
            labels=country_counts.index,
            autopct="%1.1f%%"
        )

        ax.set_title("Employees by Country")

        return fig

    # ----------------------------------
    # Salary Distribution
    # ----------------------------------

    def salary_histogram(self):

        fig, ax = plt.subplots(figsize=(8,5))

        ax.hist(
            self.df["Salary"],
            bins=20
        )

        ax.set_title("Salary Distribution")
        ax.set_xlabel("Salary")
        ax.set_ylabel("Employees")

        return fig

    # ----------------------------------
    # Average Salary by Department
    # ----------------------------------

    def average_salary_department_chart(self):

        avg_salary = (
            self.df
            .groupby("Department")["Salary"]
            .mean()
            .sort_values()
        )

        fig, ax = plt.subplots(figsize=(8,5))

        ax.bar(
            avg_salary.index,
            avg_salary.values
        )

        ax.set_title("Average Salary by Department")
        ax.set_xlabel("Department")
        ax.set_ylabel("Average Salary")

        plt.xticks(rotation=45)

        return fig

    # ----------------------------------
    # Department Salary Expense
    # ----------------------------------

    def department_salary_pie_chart(self):

        salary = (
            self.df
            .groupby("Department")["Salary"]
            .sum()
        )

        fig, ax = plt.subplots(figsize=(7,7))

        ax.pie(
            salary.values,
            labels=salary.index,
            autopct="%1.1f%%"
        )

        ax.set_title("Department Salary Expense")

        return fig

    # ----------------------------------
    # Salary Box Plot
    # ----------------------------------

    def salary_boxplot(self):

        fig, ax = plt.subplots(figsize=(8,2))

        ax.boxplot(self.df["Salary"], vert=False)

        ax.set_title("Salary Box Plot")
        ax.set_xlabel("Salary")

        return fig

    # ----------------------------------
    # Top Paying Departments
    # ----------------------------------

    def top_paying_departments(self):

        return (
            self.df
            .groupby("Department")["Salary"]
            .mean()
            .sort_values(ascending=False)
            .reset_index(name="Average Salary")
        )