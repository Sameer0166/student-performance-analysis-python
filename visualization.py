import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("student_data.csv")
data.fillna(data.mean(numeric_only=True), inplace=True)
subject_avg = data[["Maths", "Science", "English"]].mean()
subject_avg.plot(kind="bar")
plt.title("Average Marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
