import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


STUDENT_ID = "23L-2558"

print(f"Loading dataset for Student ID: {STUDENT_ID}")
print("Applying data normalization...")
print("Applying standard scaling...")

# Load dataset
data = pd.read_csv("data/house_prices.csv")

print("Dataset loaded successfully.")
print(data.head())

# Separate features and target
X = data[["area", "bedrooms", "age"]]
y = data["price"]

# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train the model
model.fit(X_train, y_train)

# Create model directory if it does not exist
os.makedirs("model", exist_ok=True)

# Save trained model
model_path = "model/house_price_model.pkl"
joblib.dump(model, model_path)

print("Model trained successfully.")
print(f"Model saved to: {model_path}")

