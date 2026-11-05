import streamlit as st
from analyzer import Analyzer


def show_dashboard(df):

    analyzer = Analyzer(df)

    st.title("📊 Dashboard")

    # ---------------------------------
    # Metrics
    # ---------------------------------

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "📁 Total Records",
        analyzer.total_records()
    )

    col2.metric(
        "💼 Job Titles",
        analyzer.total_job_titles()
    )

    col3.metric(
        "🏭 Industries",
        analyzer.total_industries()
    )

    col4.metric(
        "🌍 Locations",
        analyzer.total_locations()
    )

    st.divider()

    col5, col6, col7, col8 = st.columns(4)

    col5.metric(
        "💰 Average Salary",
        f"${analyzer.average_salary():,.2f}"
    )

    col6.metric(
        "📈 Highest Salary",
        f"${analyzer.highest_salary():,.2f}"
    )

    col7.metric(
        "📉 Lowest Salary",
        f"${analyzer.lowest_salary():,.2f}"
    )

    col8.metric(
        "⭐ Avg Experience",
        f"{analyzer.average_experience():.1f} Years"
    )

    st.divider()

    # ---------------------------------
    # Dataset Preview
    # ---------------------------------

    st.subheader("📄 Dataset Preview")

    st.dataframe(
        df,
        use_container_width=True
    )

    st.divider()

    # ---------------------------------
    # Dataset Information
    # ---------------------------------

    st.subheader("ℹ Dataset Information")

    info = {
        "Rows": len(df),
        "Columns": len(df.columns),
        "Missing Values": int(df.isnull().sum().sum())
    }

    st.json(info)