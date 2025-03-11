# b) 
valori = [10, 20, 30, 40, 50]

print(valori[0], valori[2])

valori[1] = 25

sublista = valori[1:4]

valori.append(60)

suma_elemente = sum(valori)
lungime_lista = len(valori)

produs_primul_ultimul = valori[0] * valori[-1]
diferenta = valori[3] - valori[2]
verificare_contine = 30 in valori

print(sublista, suma_elemente, lungime_lista, produs_primul_ultimul, diferenta, verificare_contine)


# c) 
date = (5, 15, 25, 35, 45)

print(type(date))

print(date[0], date[-1])

subtuplu = date[1:4]

lungime = len(date)
valoare_maxima = max(date)
valoare_minima = min(date)

print(subtuplu, lungime, valoare_maxima, valoare_minima)


# d) 
elemente = {10, 20, 30, 40, 40, 20, 50}

print(elemente)

elemente.add(60)

dimensiune = len(elemente)

print(elemente, dimensiune)


# e) 
dict_text = {"nume": "Alex", "varsta": 25, "oras": "Bucuresti"}

dict_num = {1: "unu", 2: "doi", 3: "trei"}

print(dict_text["nume"], dict_text["oras"])
print(dict_num[1], dict_num[3])

dict_text.update({"profesie": "inginer"})
dict_num.pop(2)

chei_text = list(dict_text.keys())
valori_num = list(dict_num.values())

print(dict_text, dict_num, chei_text, valori_num)


# f) 
date = (5, 15, 25, 35, 45)

lista_date = list(date)

lista_date.append(55)

print(lista_date)


# Sarcina 2a) 
preturi = [100, 250, 400]
produse = ["Laptop", "Telefon", "Tableta"]

info1 = "Produs: {} - Pret: {} RON".format(produse[0], preturi[0])
info2 = "Produs: {} - Pret: {} RON".format(produse[1], preturi[1])
info3 = "Produs: {} - Pret: {} RON".format(produse[2], preturi[2])

print(info1)
print(info2)
print(info3)


# Sarcina 2b) 
varsta = input("Introdu vârsta ta: ")

varsta = int(varsta)

varsta_in_5_ani = varsta + 5

print("În 5 ani veți avea " + str(varsta_in_5_ani) + " ani.")


# Sarcina 2c) 
fructe = ["mar", "para", "banana", "cireasa"]

exista_banana = "banana" in fructe
nuexista_struguri = "struguri" not in fructe

print(exista_banana)  
print(nuexista_struguri)
