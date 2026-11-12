import csv
import json
import io

raw_data = """Name, Age, Salary, Join Date
Alice, 30, 95000, 2015-03-01
Bob,, 60000, 2018-07-15
Charlie, 35, Unknown, 2024-02-01
Diana, 40, 110000, 2021-11-03"""

def clean_csv_data(raw_data_str):
    f = io.StringIO(raw_data_str.strip())
    reader = csv.DictReader(f)
    cleaned_records = []
    for row in reader:
        try:
            name = row['Name'].strip()
            age_str = row['Age'].strip()
            salary_str = row['Salary'].strip()
            join_date = row['Join Date'].strip()
            
            if not age_str or not salary_str or salary_str == "Unknown":
                continue
                
            cleaned_records.append({
                "name": name,
                "age": int(age_str),
                "salary": float(salary_str),
                "join_date": join_date
            })
        except ValueError:
            continue
            
    with open("cleaned_data.json", "w") as outfile:
        json.dump(cleaned_records, outfile, indent=2)
    return cleaned_records

if __name__ == "__main__":
    print(json.dumps(clean_csv_data(raw_data), indent=2))
