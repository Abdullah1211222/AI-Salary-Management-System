import streamlit as st

from dataset_loader import DatasetLoader

from pages.dashboard import show_dashboard
from pages.analysis import show_analysis
from pages.visualization import show_visualization
from pages.prediction import show_prediction
from pages.report import show_report

# ---------------------------------------------------
# Page Settings
# ---------------------------------------------------

st.set_page_config(
    page_title="Salary Management System",
    page_icon="💰",
    layout="wide"
)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

loader = DatasetLoader()
df = loader.load_dataset()

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("💰 Salary Management")

st.sidebar.header("🔍 Filters")

job_title = st.sidebar.selectbox(
    "Job Title",
    ["All"] + sorted(df["job_title"].unique().tolist())
)

industry = st.sidebar.selectbox(
    "Industry",
    ["All"] + sorted(df["industry"].unique().tolist())
)

location = st.sidebar.selectbox(
    "Location",
    ["All"] + sorted(df["location"].unique().tolist())
)

min_salary = int(df["salary"].min())
max_salary = int(df["salary"].max())

salary_range = st.sidebar.slider(
    "Salary Range",
    min_value=min_salary,
    max_value=max_salary,
    value=(min_salary, max_salary)
)

# ---------------------------------------------------
# Apply Filters
# ---------------------------------------------------

filtered_df = df.copy()

if job_title != "All":
    filtered_df = filtered_df[
        filtered_df["job_title"] == job_title
    ]

if industry != "All":
    filtered_df = filtered_df[
        filtered_df["industry"] == industry
    ]

if location != "All":
    filtered_df = filtered_df[
        filtered_df["location"] == location
    ]

filtered_df = filtered_df[
    (filtered_df["salary"] >= salary_range[0]) &
    (filtered_df["salary"] <= salary_range[1])
]

# ---------------------------------------------------
# Navigation
# ---------------------------------------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📊 Analysis",
        "📈 Visualization",
        "🤖 Prediction",
        "📄 Report"
    ]
)

# ---------------------------------------------------
# Open Pages
# ---------------------------------------------------

if page == "🏠 Dashboard":
    show_dashboard(filtered_df)

elif page == "📊 Analysis":
    show_analysis(filtered_df)

elif page == "📈 Visualization":
    show_visualization(filtered_df)

elif page == "🤖 Prediction":
    show_prediction(filtered_df)

elif page == "📄 Report":
    show_report(filtered_df)