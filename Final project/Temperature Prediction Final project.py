import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("Environment_Temperature_change_E_All_Data_NOFLAG.csv", encoding="latin1")
egypt = df[(df["Area"] == "Egypt") & (df["Element"] == "Temperature change")]

temp_values = egypt.loc[:, "Y1961":"Y2019"].iloc[0]
years = temp_values.index.str.extract(r"(\d+)").astype(int)
temperatures = pd.to_numeric(temp_values.values, errors="coerce")

data = pd.DataFrame({"year": years[0], "temperature": temperatures}).dropna()

X = data[["year"]]
y = data["temperature"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared Score:", r2)

future = pd.DataFrame([[2025]], columns=["year"])
pred = model.predict(future)
print("Predicted temperature change in 2025:", pred[0])

plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.scatter(2025, pred[0], color='green')
plt.xlabel("Year")
plt.ylabel("Temperature Change (°C)")
plt.title("Egypt Temperature Prediction")
plt.legend(["Regression Line", "Actual Data", "2025 Prediction"])
plt.show()



