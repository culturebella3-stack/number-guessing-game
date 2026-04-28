students = {}
def add_student (name, grade):
 students[name] = grade
 print(f"Student {name} added succesfully!")

def view_students ():
  if not students:
    print("No students added yet.")
  else:
      for name, grade in students.items():
        print(f" {name}: {grade}")

def calculate_average ():
       if not students:  
          print("No students added yet") 
       else:
             average = sum(students.values()) / len(students)
             print(f"Class average: {average}")

def show_menu ():
    print("1.Add student")
    print("2.View students")
    print("3.Calculate average")
    print("4.Quit")

while True:
       show_menu()
       choice = input("Enter your choice")
       if choice == "1":
        name = input("Enter student name")
        grade = int(input("Enter student grade:"))
        add_student (name, grade)
       elif choice == "2":
         view_students()
       elif choice == "3":
          calculate_average()  
       elif choice == "4" :
          print("Goodbye!")
          break  
       else:  
          print("Invalid choice.Please try again.")



          
       
             
