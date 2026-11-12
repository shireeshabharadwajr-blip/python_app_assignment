class InvalidMarksError(Exception):
    pass

def manage_student_marks():
    while True:
        try:
            name = input("Enter student name: ")
            assert name.strip() != "", "Student name cannot be empty!"
            
            marks = float(input("Enter marks (0-100): "))
            if not (0 <= marks <= 100):
                raise InvalidMarksError("Marks must be between 0 and 100.")
                
            with open("student_records.txt", "a") as f:
                f.write(f"Name: {name}, Marks: {marks}\n")
            print("Record saved successfully.")
            
        except (ValueError, AssertionError, InvalidMarksError) as e:
            print("Error:", e)
        finally:
            choice = input("Do you want to enter another record? (y/n): ")
            if choice.lower() != 'y':
                break

if __name__ == "__main__":
    manage_student_marks()
