import random

#print ("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")\

#● ┌ ─ ┐ │ └ ┘

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│ ●       │",
        "│         │",
        "│       ● │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│ ●     ● │",
        "│         │",
        "│ ●     ● │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│ ●     ● │",
        "│ ●     ● │",
        "│ ●     ● │",
        "└─────────┘"),
}


play_again = True

while play_again:
    print("------- RZUĆ KOŚĆMI -------")
    print()
    dice = []
    total = 0
    num_of_dice = int(input("Ile kości rzucić?: "))

    for die in range(num_of_dice):
        dice.append(random.randint(1, 6))

    #for die in range(num_of_dice):
    #    for line in dice_art.get(dice[die]):
    #        print(line)

    for line in range(5):
        for die in dice:
            print(dice_art.get(die)[line], end="")
        print()

    for die in dice:
        total += die

    print(f"Łączna ilość punktów: {total}")
    print()
    if not input("Chcesz zagrac ponownie? (y/n): ").lower() == "y":
        play_again = False
print()
print()
print("Dziękuje za gre ♥")