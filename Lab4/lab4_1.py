def validare_input(prompt, tip_valoare, min_val, max_val):
    while True:
        try:
            valoare = tip_valoare(input(prompt))
            if valoare < min_val or valoare > max_val:
                print(f"Valoarea trebuie să fie între {min_val} și {max_val}.")
            else:
                return valoare
        except ValueError:
            print("Introduceți o valoare validă!")

def validare_sex(prompt):
    while True:
        sex = input(prompt).strip().upper()
        if sex in ['M', 'F']:
            return sex
        else:
            print("Introduceți doar 'M' pentru masculin sau 'F' pentru feminin.")

def calculeaza_greutatea_ideala(inaltime, varsta, sex):
    if sex == 'M':
        return round(inaltime - 100 - ((inaltime - 150)/4 + (varsta - 20)/4), 2)
    else:  # sex == 'F'
        return round(inaltime - 100 - ((inaltime - 150)/2.5 + (varsta - 20)/6), 2)

def recomandare(greutate_actuala, greutate_ideala):
    diferenta = round(greutate_actuala - greutate_ideala, 2)
    if diferenta > 0:
        return f"Greutatea este cu {diferenta} kg mai mare decât cea ideală. Este recomandat să slăbiți."
    elif diferenta < 0:
        return f"Greutatea este cu {abs(diferenta)} kg mai mică decât cea ideală. Este recomandat să luați în greutate."
    else:
        return "Felicitări! Greutatea dvs. este ideală."

# Program principal
print("=== Calculator Greutate Ideală (Formula Lorentz) ===")

varsta = validare_input("Introduceți vârsta (ani): ", int, 21, 119)
inaltime = validare_input("Introduceți înălțimea (cm): ", float, 150, 220)
greutate = validare_input("Introduceți greutatea actuală (kg): ", float, 45, 300)
sex = validare_sex("Introduceți sexul (M/F): ")

greutate_ideala = calculeaza_greutatea_ideala(inaltime, varsta, sex)

print(f"\nGreutatea ideală calculată: {greutate_ideala} kg")
print(recomandare(greutate, greutate_ideala))
