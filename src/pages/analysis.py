import streamlit as st
from analyzer import Analyzer


def show_analysis(df):

    analyzer = Analyzer(df)

    st.title("📊 Data Analysis")

    # ---------------------------------
    # Job Title Analysis
    # ---------------------------------

    st.subheader("💼 Job Title Analysis")

    st.dataframe(
        analyzer.job_title_analysis(),
        use_container_width=True
    )

    st.divider()

    # ---------------------------------
    # Industry Analysis
    # ---------------------------------

    st.subheader("🏭 Industry Analysis")

    st.dataframe(
        analyzer.industry_analysis(),
        use_container_width=True
    )

    st.divider()

    # ---------------------------------
    # Location Analysis
    # ---------------------------------

    st.subheader("🌍 Location Analysis")

    st.dataframe(
        analyzer.location_analysis(),
        use_container_width=True
    )

    st.divider()

    # ---------------------------------
    # Company Size Analysis
    # ---------------------------------

    st.subheader("🏢 Company Size Analysis")

    st.dataframe(
        analyzer.company_size_analysis(),
        use_container_width=True
    )

    st.divider()

    # ---------------------------------
    # Education Analysis
    # ---------------------------------

    st.subheader("🎓 Education Level Analysis")

    st.dataframe(
        analyzer.education_analysis(),
        use_container_width=True
    )

    st.divider()

    # ---------------------------------
    # NumPy Statistics
    # ---------------------------------

    st.subheader("📈 Salary Statistics (NumPy)")

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
        "Std Deviation",
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