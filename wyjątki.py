

try:
    number = int(input("Wprowadz liczbe: "))
    print(1/ number)
except ZeroDivisionError:
    print("Nie możesz podzielić przez zero.")
except ValueError:
    print("Możesz wpisywać wyłącznie numery.")
except Exception:
    print("Cos poszło nie tak.")
finally:
    print("Zrób tu porządzek")