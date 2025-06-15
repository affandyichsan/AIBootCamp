# 1. write a program to reverse a list and remove duplicates using a set.
# 2. create a program that store students grade in a dictionary and calculate the average grade.


# 1. practice
# program1_set1 = input("inputkan kalimat jamak:")
# program1_set2 = input("inputkan kalimat tunggal:")

# set1 = set(program1_set1.split())
# set2 = set(program1_set2.split())
# olah_set = (set1 |  set2)

# print("1. practice, hasil olah set:", olah_set)
# print("1. practice, hasil olah set:", program1_set1.split())

# 2. practice

# Create a dictionary to store student names and their grades
students_grade = {
    'affandy':90,
    'nanda':70,
    'asroi':80,
    'nadila':80,
    'nug':90,
    'ilyas':90
}

nilai = sum(students_grade.values())
jumlah = len(students_grade)
rata_rata = nilai / jumlah


print(rata_rata)


for name, value in students_grade.items():
    print(f"{name}:{value}")