import logging

logging.basicConfig(level=logging.INFO)

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if a != 0:
        return a/b
    else:
        logging.error("Nie można dzielić przez 0")
        return None
    
print("odaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")

choice = int(input())

if choice not in[1, 2, 3, 4]:
    logging.error("wybrano nie poprawna opcje")
else:
    licz1 = float(input("podaj 1 liczbe: "))
    licz2 = float(input("podaj 2 liczbe: "))


if choice == 1:
    logging.info(f"dodaje {licz1} i {licz2} ")
elif choice == 2:
    logging.info(f"odejmuje od {licz1} liczbe {licz2} ")
elif choice == 3:
    logging.info(f"mnoze {licz1} przez {licz2} ")
elif choice == 4:
    if licz1 != 0:
        logging.info(f"dziele {licz1} przez {licz2} ")

wynik = 0

if choice == 1:
    wynik = dodawanie(licz1, licz2)
elif choice == 2:
    wynik = odejmowanie(licz1, licz2)
elif choice == 3:
    wynik = mnozenie(licz1, licz2)
elif choice == 4:
    wynik = dzielenie(licz1, licz2)

if wynik is not None:
    logging.info(f"wynik to {wynik}")

