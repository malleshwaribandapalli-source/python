students = {"malleshwari", "bhavitha", "Pallavi", "Lakshmi","Pallavi","Mahesh"}
print(students)
print(len(students))
print("Mahesh" in students)
students.add("harshitha")
print(students)
students.remove("Pallavi")
print(students)
students.pop()
print(students)
for student in students:
 print(student)
maths_students = {"bhavitha","Pallavi"}
science_students = {"Malleshwari","lakshmi"}
all_students = maths_students | science_students
print(all_students)
common_students = maths_students & science_students
print(common_students)
