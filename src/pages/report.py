import streamlit as st
from analyzer import Analyzer


def show_report(df):

    analyzer = Analyzer(df)

    st.title("📄 Salary Analysis Report")

    st.write(
        "This report summarizes the salary dataset using descriptive statistics and key insights."
    )

    st.divider()

    # ---------------------------------
    # Dataset Summary
    # ---------------------------------

    st.header("📊 Dataset Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Records", analyzer.total_records())
        st.metric("Job Titles", analyzer.total_job_titles())
        st.metric("Industries", analyzer.total_industries())
        st.metric("Locations", analyzer.total_locations())

    with col2:
        st.metric("Average Salary", f"${analyzer.average_salary():,.2f}")
        st.metric("Highest Salary", f"${analyzer.highest_salary():,.2f}")
        st.metric("Lowest Salary", f"${analyzer.lowest_salary():,.2f}")
        st.metric(
            "Average Experience",
            f"{analyzer.average_experience():.2f} Years"
        )

    st.divider()

    # ---------------------------------
    # Key Insights
    # ---------------------------------

    st.header("💡 Key Insights")

    st.success(
        f"💼 Highest Paying Job Title: **{analyzer.highest_paying_job()}**"
    )

    st.info(
        f"🏭 Highest Paying Industry: **{analyzer.highest_paying_industry()}**"
    )

    st.warning(
        f"📉 Lowest Paying Job Title: **{analyzer.lowest_paying_job()}**"
    )

    st.success(
        f"⭐ Most Common Job Title: **{analyzer.most_common_job()}**"
    )

    st.info(
        f"💰 Total Salary in Dataset: **${analyzer.total_salary_expense():,.2f}**"
    )

    st.divider()

    # ---------------------------------
    # Salary Statistics
    # ---------------------------------

    st.header("📈 Salary Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Mean Salary",
        f"${analyzer.mean_salary_numpy():,.2f}"
    )

    col2.metric(
        "Median Salary",
        f"${analyzer.median_salary_numpy():,.2f}"
    )

    col3.metric(
        "Standard Deviation",
        f"{analyzer.std_salary_numpy():,.2f}"
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Variance",
        f"{analyzer.variance_salary_numpy():,.2f}"
    )

    col5.metric(
        "Minimum Salary",
        f"${analyzer.minimum_salary_numpy():,.2f}"
    )

    col6.metric(
        "Maximum Salary",
        f"${analyzer.maximum_salary_numpy():,.2f}"
    )

    st.divider()

    # ---------------------------------
    # Conclusion
    # ---------------------------------

    st.header("📌 Conclusion")

    st.write("""
This Salary Management System provides:

- Employee salary analysis
- Industry-wise salary comparison
- Job title analysis
- Location-wise insights
- Interactive visualizations
- AI-based salary prediction using Machine Learning
- Automated reporting

The Machine Learning model compares multiple regression algorithms and automatically selects the best-performing model for salary prediction.
""")