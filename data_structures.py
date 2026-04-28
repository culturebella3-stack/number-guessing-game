fruits = ["apple", "banana", "orange"]
print(fruits)
print(fruits[0])
print(fruits[2])
fruits.append("mango")
print(fruits)
fruits.remove("banana")
print(fruits)
print(len(fruits))    
for items in fruits: 
    print(items)

    
    #Dictionary
student = {"name":"Kofi", "age":20, "grade":"A"}
print(student)
print(student["name"])
student["city"] = "Accra"
print(student)
print("key" and "value")


      #SETS
colors = {"red", "blue", "green", "red"}
print(colors)
colors.add("yellow")
print(colors)
colors.remove("blue")
print(colors)
warm_colors = {"red", "yellow", "orange"}
print(colors.intersection(warm_colors))