from collections import Counter
from functools import reduce
from datetime import datetime
import random

students = {
    "Tarun": [82, 91, 78],
    "Karthik": [65, 72, 68],
    "Chadrika": [91, 95, 89],
    "Trisha": [76, 81, 79],
    "Atul": [88, 84, 92]
}

def classify_grade(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B"
    else: return "C"

if __name__ == "__main__":
    averages = {name: round(sum(m)/len(m), 2) for name, m in students.items()}
    highest_avg = max(averages.values())
    selected = random.choice(list(students.keys()))
    grades = Counter(classify_grade(avg) for avg in averages.values())
    total_marks = reduce(lambda a, b: a + b, [sum(m) for m in students.values()])
    
    print("Date:", datetime.now().strftime("%d-%m-%Y"))
    print("Averages:", averages)
    print("Highest Average:", highest_avg)
    print("Randomly Selected Student:", selected)
    print("Grade Classification:", dict(grades))
    print("Total Marks Across All Students:", total_marks)
