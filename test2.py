# Zapytaj użytkownika o imię i wiek
imie = input("Jak masz na imię? ")
wiek = int(input("Ile masz lat? "))

# Sprawdź warunek wieku
if wiek > 18:
    # Jeśli wiek > 18, drukuj "Dzień dobry IMIĘ"
    print("Dzień dobry", imie)
else:
    # W przeciwnym razie, drukuj "Cześć IMIĘ"
    print("Cześć", imie)