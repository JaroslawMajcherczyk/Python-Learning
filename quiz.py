# Python quize game

questions = (
    "O której godzinie pracę zaczyna Twój Kierownik?: ",
    "Co uwielbia w pracy robić Twój Kierownik?: ",
    "Jakie są obowiązki Twojego Kierownika?: ",
    "Jaką kawę najczęściej pije Twój Kierownik?: ",
    "Jak reaguje Twój Kierownik, gdy coś działa perfekcyjnie?: ",
    "Jakie motto życiowe mógłby mieć Twój Kierownik?: "
)

options = (
    ("A. 5:00 – bo perfekcja nie śpi",
     "B. 7:00 – z kawą w ręku już przy komputerze",
     "C. 9:00 – po solidnym śniadaniu",
     "D. Jak ma ochote"),

    ("A. Kręcić się bez celu i jarać szlugi",
     "B. Uczyć zespół nowych sztuczek",
     "C. Poprawiać kod, który już działa — żeby działał lepiej",
     "D. Przeglądać logi jak kroniki bohaterskich czynów"),

    ("A. Nadzorować projekty i ludzi z precyzją lasera",
     "B. Podejmować decyzje strategiczne przy kawie",
     "C. Żadne",
     "D. Ratować systemy w krytycznych momentach"),

    ("A. Espresso – szybkie jak jego myśli",
     "B. Cappuccino – z pianą jak chmury nad imperium",
     "C. Czarna jak noc przed deadline’em",
     "D. Latte w brudnym kubku"),

    ("A. Uśmiecha się z satysfakcją i zapisuje commit ‘PerfectFix’",
     "B. Wypowiada słowa: ‘Ja już na siebie dziś zarobiłem’",
     "C. Od razu planuje, jak to jeszcze ulepszyć",
     "D. Milczy – bo perfekcja mówi sama za siebie"),

    ("A. ‘Nie ma rzeczy niemożliwych – są tylko źle skonfigurowane’",
     "B. ‘Trust the process, debug the rest’",
     "C. ‘Ja to pierdole’",
     "D. ‘Kierownik zawsze ma rację – nawet gdy ma rację dwa razy’")
)


answers = ("D","A","C","D","B","C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Odpowiedz na pytanie wpisująć A, B, C lub D: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score +=1
        print("POPRAWNA ODPOWIEDZ!")
    else:
        print("NIEPOPRAWNA ODPOWIEDZ!")
        print("Poznaj sowjego Kierownika lepiej ♥")
        print(f"{answers[question_num]} jest poprawną odpowiedzią ☺")

    question_num +=1
print("---------------")
print("PODSUMOWANIE")
print(f"Twoja liczba poprawnych odpowiedzi to {score} na 6! ♥♥♥")
print("---------------")




