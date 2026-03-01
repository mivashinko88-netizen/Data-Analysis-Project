# Student Habits & Academic Performance Analysis

Data analysis project exploring how student lifestyle habits correlate with exam scores. Uses Python with pandas, matplotlib, and seaborn to uncover patterns in sleep, social media use, mental health, and study routines.

## Key Findings

- Visualized relationships between exam scores and factors like sleep hours, social media usage, and study time
- Generated regression plots to identify linear trends in student behavior data
- Explored mental health ratings as a predictor of academic performance

## Visualizations

| Sleep Hours vs Exam Score | Social Media vs Exam Score | Study Hours vs Exam Score |
|:---:|:---:|:---:|
| ![Sleep](Sleep%20Hours%20vs%20Exam%20Score.png) | ![Social](Social%20Media%20Hours%20vs%20Exam%20Scores.png) | ![Study](Study%20Hours%20Vs%20Exam%20Score.png) |

## Tech Stack

- **Python 3**
- **pandas** — data loading and manipulation
- **seaborn** — statistical visualization with regression plots
- **matplotlib** — plot rendering and customization
- **NumPy** — numerical computation

## Dataset

`student_habits_performance.csv` — contains student-level records with fields for exam scores, sleep hours, study hours, social media usage, mental health ratings, and more.

## Running

```bash
pip install pandas numpy seaborn matplotlib
python analysis.py
```

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
