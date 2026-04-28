with open("student.txt", "w") as f :
    f.write("kofi-Grade:85\n")
    f.write("Ama-Grade:92\n")
    f.write("kwame-Grade:78\n")
    print("File written successfully!")

with open("student.txt", "r") as f :
    content = f.read()
    print(content)

    import json

    students = [{"name":"Kofi","grade":85},{"name":"Ama","grade":92},{"name":"Kwame","grade":78}]
    with open("students.json", "w") as f :
        json.dump(students, f) 
        print("JSON file saved succesfully!")
    with open("students.json", "r") as f :
        loaded_students = json.load(f)
        print(loaded_students)
