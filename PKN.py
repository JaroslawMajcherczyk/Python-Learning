import random

options = ("kamień", "papier", "nożyce")

runing = True

while runing:
    player = None
    computer = random.choice(options)
    print("---------- ROZPOCZNIJ GRE! ----------")

    while player not in options:
        player = input("Wybierz jedną z opcji (kamień, papier lub nożyce): ")


    print(f"Gracz: {player}")
    print(f"Komputer: {computer}")

    if player == computer:
        print("REMIS!")
    elif player == "kamień" and computer == "nożyce":
        print("WYGRAŁEŚ!")
    elif player == "papier" and computer == "kamień":
        print("WYGRAŁEŚ!")
    elif player == "nożyce" and computer == "papier":
        print("WYGRAŁEŚ!")
    else:
        print("PRZECIWNIK WYGRAŁ!")

    if not input("Chcesz zagrac ponownie? (y/n): ").lower() == "y":
        runing = False
print()
print("Dziękuje za gre ♥")

