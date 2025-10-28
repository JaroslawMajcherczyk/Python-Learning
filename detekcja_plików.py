import os

file_path = "C:\\Users\\jmajcherczyk\\Desktop\\test"

if os.path.exists(file_path):
    print(f"Lokacja '{file_path}' istnieje")

    if os.path.isfile(file_path):
        print(f"To jest ten plik")
    elif os.path.isdir(file_path):
        print(f"To jest ten folder")
else:
    print("Nie można odnaleść lokalizacji dla podanej ścieżki")

