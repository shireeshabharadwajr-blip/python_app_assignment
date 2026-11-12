import sys
import itertools
import random
from functools import reduce
from datetime import datetime
from collections import defaultdict

students_data = [
    ("CSE", "Anita", 85), ("CSE", "Rahul", 78), ("CSE", "Priya", 92), ("CSE", "Kiran", 81),
    ("AI", "Vikram", 88), ("AI", "Sneha", 90), ("AI", "Rohan", 76),
    ("Data Science", "Meera", 94), ("Data Science", "Arjun", 83), ("Data Science", "Neha", 87),
    ("Cyber Security", "Karthik", 79), ("Cyber Security", "Divya", 91)
]

if __name__ == "__main__":
    team_size = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    grouped = defaultdict(list)
    for dept, name, marks in students_data:
        grouped[dept].append((name, marks))
        
    dept = "CSE"
    combos = list(itertools.combinations(grouped[dept], team_size))
    selected = random.choice(combos)
    total = reduce(lambda acc, s: acc + s[1], selected, 0)
    avg = total / team_size
    
    print("PROJECT TEAM ALLOCATION")
    print("Team Size:", team_size)
    print("Allocation Date:", datetime.now().strftime("%d-%m-%Y"))
    print("Department:", dept)
    print("Selected Team:")
    for idx, (name, marks) in enumerate(selected, 1):
        print(f"{idx}. {name} - {marks}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {avg:.2f}")
