


import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression

# Step 1: Data create karo
X, y = make_regression(n_samples=100, n_features=1, noise=10)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 2: MLflow experiment set karo
mlflow.set_experiment("First_Experiment")

with mlflow.start_run():

    # Step 3: Model create
    model = LinearRegression()

    # Step 4: Train model
    model.fit(X_train, y_train)

    # Step 5: Score
    score = model.score(X_test, y_test)

    # Step 6: MLflow logging
    mlflow.log_metric("accuracy", score)
    mlflow.log_param("model_type", "LinearRegression")

    # Step 7: Model save in MLflow
    mlflow.sklearn.log_model(model, "model")

    print("Experiment completed! Score:", score)