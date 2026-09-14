import json
import os

FILE_NAME = "students.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_data(data):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

# 1. Create (Add Student)
def add_student(roll_no, name, grade):
    students = load_data()
    if any(s["roll_no"] == roll_no for s in students):
        print("Student with this roll number already exists!")
        return
    students.append({"roll_no": roll_no, "name": name, "grade": grade})
    save_data(students)
    print("Student added successfully!")

# 2. Read (Display Students)
def display_students():
    students = load_data()
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for s in students:
        print(f"Roll No: {s['roll_no']} | Name: {s['name']} | Grade: {s['grade']}")

# 3. Update Student
def update_student(roll_no, new_name, new_grade):
    students = load_data()
    for s in students:
        if s["roll_no"] == roll_no:
            s["name"] = new_name
            s["grade"] = new_grade
            save_data(students)
            print("Record updated successfully!")
            return
    print("Student not found!")

# 4. Delete Student
def delete_student(roll_no):
    students = load_data()
    updated = [s for s in students if s["roll_no"] != roll_no]
    if len(students) == len(updated):
        print("Student not found!")
    else:
        save_data(updated)
        print("Student record deleted successfully!")

# CLI Driver Code
def main():
    while True:
        print("\n=== Student Record Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        try:
            if choice == "1":
                r = int(input("Roll No: "))
                n = input("Name: ")
                g = input("Grade: ")
                add_student(r, n, g)
            elif choice == "2":
                display_students()
            elif choice == "3":
                r = int(input("Roll No to update: "))
                n = input("New Name: ")
                g = input("New Grade: ")
                update_student(r, n, g)
            elif choice == "4":
                r = int(input("Roll No to delete: "))
                delete_student(r)
            elif choice == "5":
                print("Exiting application...")
                break
            else:
                print("Invalid choice, please select 1-5.")
        except ValueError:
            print("Error: Roll number must be a valid integer!")

if __name__ == "__main__":
    main()
