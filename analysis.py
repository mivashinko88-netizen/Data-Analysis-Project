import pandas as pd

import numpy as np

import seaborn as sns

import matplotlib.pyplot as plt

data_frame = pd.read_csv("student_habits_performance.csv")

sns.lmplot(
    x="exam_score",
    y="mental_health_rating",
    data=data_frame,
    height=6, aspect=1.2,
    scatter_kws={"color": "orange", "alpha": 0.6},
    line_kws={"color": "blue", "linewidth": 2},  
)

plt.title("Mental Health vs Exam Score with Regression Line")
plt.show()