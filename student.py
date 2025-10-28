class Student:

    class_year = 2026
    num_students = 0

    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
        Student.num_students += 1

student1 = Student("John","Smith","19")
student2 = Student("Jarek","Kanarel","35")
student3 = Student("John","Smith","13")
#print(f"Siema jestem {student1.name} {student1.surname} i mam {student1.age} lat")

print(f"Siema jestem {student2.name} {student2.surname} i mam {student2.age} lat, skoncze studia w {Student.class_year}")
print(Student.num_students)