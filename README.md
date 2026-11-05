# AI-Powered Salary Management System

An interactive salary analytics and prediction application built with Python, Streamlit, and Machine Learning. The system allows users to explore salary data, analyze compensation trends, visualize insights, and predict salaries using multiple regression algorithms.

## Features

- **Interactive Dashboard:** Explore salary data through an interactive dashboard.
- **Data Analysis:** Analyze salary trends across job titles, industries, and locations.
- **Data Visualization:** Explore salary patterns using visualizations.
- **Salary Prediction:** Predict salaries using trained Machine Learning models.
- **Model Comparison:** Compare multiple regression algorithms using evaluation metrics.
- **Report Generation:** Generate reports based on salary analysis.
- **Interactive Filters:** Filter data by job title, industry, location, and salary range.

## Machine Learning Models

The project implements and compares three regression algorithms:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

### Data Preprocessing

- One-Hot Encoding for categorical features.
- Missing value handling using SimpleImputer.
- Median imputation for numerical features.
- Most-frequent imputation for categorical features.
- 80/20 training and testing split.

### Model Evaluation

The models are evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

The best-performing model based on R² score is saved using Joblib for future predictions.

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

## Project Structure

```text
AI-Salary-Management-System/
│
├── data/
│   └── job_salary_dataset.csv
│
├── models/
│   ├── label_encoders.pkl
│   └── salary_model.pkl
│
├── src/
│   ├── pages/
│   │   ├── dashboard.py
│   │   ├── analysis.py
│   │   ├── visualization.py
│   │   ├── prediction.py
│   │   └── report.py
│   │
│   ├── app.py
│   ├── analyzer.py
│   ├── data_cleaner.py
│   ├── dataset_loader.py
│   ├── report_generator.py
│   ├── salary_predictor.py
│   └── visualizer.py
│
├── .gitignore
└── requirements.txt
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Abdullah1211222/AI-Salary-Management-System.git
```

### 2. Navigate to the project directory

```bash
cd AI-Salary-Management-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run src/app.py
```

The application will open in your default web browser.

## Author

**Abdullah Farrukh**

BS Artificial Intelligence Student

University of Management and Technology (UMT)

[GitHub](https://github.com/Abdullah1211222)

[LinkedIn](https://linkedin.com/in/abdullahfarrukh1/)

---

*Developed as a Machine Learning and Data Analytics portfolio project.*