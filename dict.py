student = {
"name" : "Malleshwari",
"age" : 20 ,
"branch" : "CSE"
}
print(student)
print(type(student))
print(student["name"])
print(student.get("age"))
print("age" in  student)
print(student.keys())
print(student.values())
print(student.items())
student["phone"] = "9398623651"
print(student)
student["age"] = 22
print(student)
student.pop("branch")
print(student)
student.popitem()
print(student)
for key in student:
 print(key)
for value in student:
 print(value)
print(len(student))
del student["age"]
print(student)
student.clear()
print(student)

