def pisica_sub_un_an():
    echivalenta = {
        1: "6 luni",
        2: "10 luni",
        3: "2 ani",
        4: "5 ani",
        5: "8 ani",
        6: "14 ani",
        7: "15 ani",
        8: "16 ani",
        9: "16 ani",
        10: "17 ani",
        11: "17 ani"
    }

    while True:
        try:
            luni = int(input("Câte luni are pisica ta? (1-11): "))
        except ValueError:
            print("Vă rugăm introduceți o valoare numerică validă!")
            if luni < 1 or luni > 11:
                print("Introduceți un număr între 1 și 11.")
                continue
        print(f"În ani omenești, pisica ta are aproximativ: {echivalenta[luni]}")
        break


def pisica_mai_mare_de_un_an():
    while True:
        try:
            ani = int(input("Câți ani are pisica ta? (1-35): "))
        except ValueError:
            print("Introduceți o valoare numerică validă!")
            continue

        ani = int(ani)
        if ani < 1 or ani >= 35:
            print("Vârsta trebuie să fie între 1 și 34.")
            continue


def d(ani):
    if ani == 1:
        echiv = 18
    elif ani == 2:
        echiv = 25
    elif 3 <= ani <= 15:
        echiv = 25 + (ani - 2) * 4
    else:  # 16 <= ani < 35
        echiv = 25 + 13 * 4 + (ani - 15) * 3
    return echiv;

    print(f"În ani omenești, pisica ta ar avea aproximativ: {echiv} ani.")


# Program principal
def a():
    print("=== Calculator vârstă pisică în ani omenești ===")
    while True:
        raspuns = input("Pisica este mai mică de un an? (Da/Nu sau Yes/No): ").strip().lower()
        if raspuns in ["da", "yes"]:
            pisica_sub_un_an()
            break
        elif raspuns in ["nu", "no"]:
            pisica_mai_mare_de_un_an()
            break
        else:
            print("Răspuns invalid. Vă rugăm introduceți 'Da' sau 'Nu'.")


def test():
    assert d(1) == 18
    assert d(2) == 25
    assert d(3) == 29
    assert d(4) == 33
    assert d(25) == 107

test()
