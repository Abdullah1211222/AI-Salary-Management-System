from pathlib import Path
import joblib
import pandas as pd

from dataset_loader import DatasetLoader

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


class SalaryPredictor:

    def __init__(self):

        loader = DatasetLoader()

        self.df = loader.load_dataset()

        self.best_model = None

        self.results = {}

    # ------------------------------------------
    # Train Models
    # ------------------------------------------

    def train(self):

        X = self.df.drop(columns=["salary"])

        y = self.df["salary"]

        categorical = [

            "job_title",
            "education_level",
            "industry",
            "company_size",
            "location",
            "remote_work"

        ]

        numeric = [

            "experience_years",
            "skills_count",
            "certifications"

        ]

        preprocessor = ColumnTransformer(

            transformers=[

                (

                    "cat",

                    Pipeline(

                        steps=[

                            (
                                "imputer",
                                SimpleImputer(
                                    strategy="most_frequent"
                                )
                            ),

                            (
                                "encoder",
                                OneHotEncoder(
                                    handle_unknown="ignore"
                                )
                            )

                        ]

                    ),

                    categorical

                ),

                (

                    "num",

                    Pipeline(

                        steps=[

                            (
                                "imputer",
                                SimpleImputer(
                                    strategy="median"
                                )
                            )

                        ]

                    ),

                    numeric

                )

            ]

        )

        X_train, X_test, y_train, y_test = train_test_split(

            X,

            y,

            test_size=0.20,

            random_state=42

        )

        models = {

            "Linear Regression":

                LinearRegression(),

            "Decision Tree":

                DecisionTreeRegressor(

                    max_depth=15,

                    random_state=42

                ),

            "Random Forest":

                RandomForestRegressor(

                    n_estimators=30,

                    max_depth=15,

                    random_state=42,

                    n_jobs=-1

                )

        }

        best_r2 = -1

        best_model_name = ""

        models_dir = Path("../models")

        models_dir.mkdir(exist_ok=True)

        for name, model in models.items():

            print("\n==============================")
            print(name)
            print("==============================")
            print("Training...")

            pipeline = Pipeline(

                steps=[

                    ("preprocessor", preprocessor),

                    ("model", model)

                ]

            )

            pipeline.fit(

                X_train,

                y_train

            )

            predictions = pipeline.predict(

                X_test

            )

            mae = mean_absolute_error(

                y_test,

                predictions

            )

            mse = mean_squared_error(

                y_test,

                predictions

            )

            rmse = mse ** 0.5

            r2 = r2_score(

                y_test,

                predictions

            )

            print(f"MAE  : {mae:.2f}")
            print(f"MSE  : {mse:.2f}")
            print(f"RMSE : {rmse:.2f}")
            print(f"R²   : {r2:.4f}")

            self.results[name] = {

                "MAE": mae,

                "MSE": mse,

                "RMSE": rmse,

                "R2": r2

            }

            if r2 > best_r2:

                best_r2 = r2

                best_model_name = name

                self.best_model = pipeline

        joblib.dump(

            self.best_model,

            models_dir / "salary_model.pkl"

        )

        print("\n===================================")
        print("BEST MODEL")
        print("===================================")
        print(best_model_name)
        print(f"R² Score : {best_r2:.4f}")

        print("\nModel Saved Successfully!")

        return self.results

    # ------------------------------------------
    # Predict Salary
    # ------------------------------------------

    def predict(self, input_df):

        if self.best_model is None:

            model_path = Path("../models") / "salary_model.pkl"

            if not model_path.exists():

                raise FileNotFoundError(
                    "Train the model first."
                )

            self.best_model = joblib.load(model_path)

        return self.best_model.predict(input_df)


# ------------------------------------------
# Run File
# ------------------------------------------

if __name__ == "__main__":

    predictor = SalaryPredictor()

    predictor.train()