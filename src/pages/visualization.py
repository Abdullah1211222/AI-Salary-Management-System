import streamlit as st
import matplotlib.pyplot as plt


def show_visualization(df):

    st.title("📈 Data Visualization")

    # ---------------------------------
    # Average Salary by Job Title
    # ---------------------------------

    st.subheader("💼 Average Salary by Job Title")

    fig, ax = plt.subplots(figsize=(12, 5))

    (
        df.groupby("job_title")["salary"]
        .mean()
        .sort_values(ascending=False)
        .plot(kind="bar", ax=ax)
    )

    ax.set_ylabel("Average Salary")
    ax.set_xlabel("Job Title")
    plt.xticks(rotation=45, ha="right")

    st.pyplot(fig)

    # ---------------------------------

    st.subheader("🏭 Average Salary by Industry")

    fig, ax = plt.subplots(figsize=(10, 5))

    (
        df.groupby("industry")["salary"]
        .mean()
        .sort_values(ascending=False)
        .plot(kind="bar", ax=ax)
    )

    ax.set_ylabel("Average Salary")
    plt.xticks(rotation=45, ha="right")

    st.pyplot(fig)

    # ---------------------------------

    st.subheader("🌍 Employees by Location")

    fig, ax = plt.subplots(figsize=(10, 5))

    (
        df["location"]
        .value_counts()
        .plot(kind="bar", ax=ax)
    )

    ax.set_ylabel("Employees")
    plt.xticks(rotation=45, ha="right")

    st.pyplot(fig)

    # ---------------------------------

    st.subheader("🏢 Employees by Company Size")

    fig, ax = plt.subplots(figsize=(7, 5))

    (
        df["company_size"]
        .value_counts()
        .plot(kind="pie", autopct="%1.1f%%", ax=ax)
    )

    ax.set_ylabel("")

    st.pyplot(fig)

    # ---------------------------------

    st.subheader("🎓 Average Salary by Education Level")

    fig, ax = plt.subplots(figsize=(8, 5))

    (
        df.groupby("education_level")["salary"]
        .mean()
        .plot(kind="bar", ax=ax)
    )

    ax.set_ylabel("Average Salary")

    st.pyplot(fig)

    # ---------------------------------

    st.subheader("📈 Salary Distribution")

    fig, ax = plt.subplots(figsize=(10, 5))

    ax.hist(df["salary"], bins=30)

    ax.set_xlabel("Salary")
    ax.set_ylabel("Frequency")

    st.pyplot(fig)