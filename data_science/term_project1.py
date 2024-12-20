import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# File path
file_path = r'C:\Users\Cay\data_science\cleaned_energy_usage.csv'

# Load the dataset
try:
    data = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred while loading the file: {e}")
    exit()

# Validate required columns
required_columns = ['Timestamp', 'EnergyConsumption']
missing_columns = [col for col in required_columns if col not in data.columns]

if missing_columns:
    print(f"Error: Missing required columns in the dataset: {missing_columns}")
    print(f"Available columns: {data.columns.tolist()}")
    exit()

# Preprocessing
data['Timestamp'] = pd.to_datetime(data['Timestamp'])  
data.set_index('Timestamp', inplace=True)


categorical_cols = data.select_dtypes(include=['object']).columns
data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)


data['Month'] = data.index.month
data['Day'] = data.index.day
data['Hour'] = data.index.hour


X = data.drop(columns=['EnergyConsumption'])
y = data['EnergyConsumption']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Models
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(random_state=42),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
}

# Train and evaluate models
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    results[name] = {"MSE": mse, "MAE": mae, "R2": r2}

# Display results
for model_name, metrics in results.items():
    print(f"Model: {model_name}")
    for metric, value in metrics.items():
        print(f"  {metric}: {value:.2f}")
    print("-" * 30)



rf_model = models["Random Forest"]
y_pred_rf = rf_model.predict(X_test)

plt.figure(figsize=(10, 6))
sns.lineplot(data=y_test.reset_index(drop=True), label='Actual', color='blue')
sns.lineplot(data=pd.Series(y_pred_rf), label='Random Forest Predictions', color='orange')
plt.title('Actual vs Predicted Energy Consumption (Random Forest)')
plt.xlabel('Sample Index')
plt.ylabel('Energy Consumption')
plt.legend()
plt.show()
