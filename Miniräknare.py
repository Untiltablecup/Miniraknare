while True:
    räkna_med = (input("Välkommen till miniräknaren.\n[1] Räkna med +\n[2] Räkna med -\n[3] Räkna med *\n[4] Räkna med /\n[5] Avsluta\n>"))
    if räkna_med == "1":
        nummer_1 = float(input("Skriv ett tal\n>"))
        nummer_2 = float(input("Skriv ett till tal\n>"))
        summa = nummer_1 + nummer_2
        print(f"Summan blev {summa}\n-------")
        continue
    elif räkna_med == "2":
        nummer_1 = float(input("Skriv ett tal\n>"))
        nummer_2 = float(input("Skriv ett till tal\n>"))
        differens = nummer_1 - nummer_2
        print(f"Differensen blev {differens}\n-------")
        continue
    elif räkna_med == "3":
        nummer_1 = float(input("Skriv ett tal\n>"))
        nummer_2 = float(input("Skriv ett till tal\n>"))
        produkt = nummer_1 * nummer_2
        print(f"Produkten blev {produkt}\n-------")
        continue
    elif räkna_med == "4":
        nummer_1 = float(input("Skriv ett tal\n>"))
        nummer_2 = float(input("Skriv ett till tal\n>"))
        kvoten = nummer_1 / nummer_2
        print(f"Kvoten blev {kvoten}\n-------")
        continue
    elif räkna_med == "5":
        print("Hejdå!")
        break
    else:
        print("Vänligen välj ett av förslagen!\n-------")
        continue