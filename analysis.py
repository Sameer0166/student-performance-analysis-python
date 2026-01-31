import pandas as pd
import numpy as np
data = pd.read_csv("student_data.csv")
# Handle missing values
data.fillna(data.mean(numeric_only=True), inplace=True)
data["Average"] = data[["Maths", "Science", "English"]].mean(axis=1)
data["Result"] = np.where(data["Average"] >= 50, "Pass", "Fail")
print(data)
