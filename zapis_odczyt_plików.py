import json
import csv
from os import write

# txt_data = "Lubie pizze"

#employees = ["Jarek", "Marek", "Darek"]

# file_path = "C:\\Users\\jmajcherczyk\\Desktop\\test.csv"

#employess = {
#    "name": "Jarek",
#    "age": 35,
#    "job": "Python Developer",
#}

# employess = [["Name","Age","Job"],
#              ["Jarek","35","Python Developer"],
#              ["Marel","40","C# Developer"],
#              ["Darek","45","JS Developer"],]


# try:
#     with open(file=file_path, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         for row in employess:
#             writer.writerow(row)
#         print(f"csv plik '{file_path}' został stworzony")
# except FileExistsError:
#         print("plik już istnieje")


file_path = "C:\\Users\\jmajcherczyk\\Desktop\\test.csv"

try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)

except FileNotFoundError:
    print("Nie znaleziono pliku")
except PermissionError:
    print("Nie znaleziono pliku")