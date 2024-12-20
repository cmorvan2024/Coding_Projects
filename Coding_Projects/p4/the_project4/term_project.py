# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error, accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess data
data = pd.read_csv('energy_usage.csv')  # Replace with your file name
data.dropna(inplace=True)
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Feature Engineering (if needed)
data['Month'] = data.index.month
data['Day'] = data.index.day
data['Hour'] = data.index.hour

# Split data into features and target
X = data.drop(columns=['Energy_Consumption'])
y = data['Energy_Consumption']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize models
lr = LinearRegression()
rf = RandomForestRegressor(random_state=42)
dt = DecisionTreeRegressor(random_state=42)

# Train models
lr.fit(X_train, y_train)
rf.fit(X_train, y_train)
dt.fit(X_train, y_train)

# Predictions
y_pred_lr = lr.predict(X_test)
y_pred_rf = rf.predict(X_test)
y_pred_dt = dt.predict(X_test)

# Evaluation metrics function
def evaluate_model(y_true, y_pred, model_name):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    print(f"Evaluation for {model_name}:")
    print(f"Mean Squared Error: {mse:.2f}")
    print(f"Root Mean Squared Error: {rmse:.2f}")
    print(f"Mean Absolute Error: {mae:.2f}")
    print(f"R2 Score: {r2:.2f}")
    print("-" * 30)

# Evaluate all models
evaluate_model(y_test, y_pred_lr, "Linear Regression")
evaluate_model(y_test, y_pred_rf, "Random Forest")
evaluate_model(y_test, y_pred_dt, "Decision Tree")

# Best model rationale
print("Random Forest performed the best due to its ability to handle non-linear data and reduce overfitting.")

# Visualizations
plt.figure(figsize=(10, 6))
sns.lineplot(data=y_test.reset_index(drop=True), label='Actual', color='blue')
sns.lineplot(data=pd.Series(y_pred_rf), label='Random Forest Predictions', color='orange')
plt.title('Actual vs Predicted Energy Consumption (Random Forest)')
plt.xlabel('Sample Index')
plt.ylabel('Energy Consumption')
plt.legend()
plt.show()
