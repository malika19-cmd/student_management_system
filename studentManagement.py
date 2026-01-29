students = []

def show_options():
  print("STUDENT MANAGEMENT SYSTEM")
  print("1. Add Student")
  print("2. View Students")
  print("3. Search Students")
  print("4. Exit")

def add_student():
  roll = input("Enter roll number: ")
  name = input("Enter name: ")
  marks = input("Enter student marks: ")

  student = {"roll": roll, "name": name, "marks": marks}

  students.append(student)
  print("Student added successfully!")

def view_students():
  if not students:
    print("No students available.")
    return

  print("\n---Student List---)
  for student in students:
    print(f"Roll: {student['roll']}, Name: {student['name']}, Marks: {student['marks']}")

def search_student():
  roll = input("Enter roll number to search: ")

  for student in students:
    if student["roll"] == roll:
      print(f"Found: Name: {student['name']}, Marks: {student['marks']}")
      return
  print("Student not found.")

while True:
  show_options()
  choice = input("Choose an option (1-4): ")

  if choice == "1":
    add_student()
  elif choice == "2":
    view_students()
  elif choice == "3":
    search_student()
  elif choice == "4":
    print("Thankyou for using the Student Management System")
    break
  else:
    print("Invalid Choice, Try Again!")
  


  
  
  
