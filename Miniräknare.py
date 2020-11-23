while True:
    räkna_med = (input("Välkommen till miniräknaren.\n[1] Räkna med +\n[2] Räkna med -\n[3] Räkna med *\n[4] Räkna med /\n[5] Avsluta\n>")) #Ger användaren alternativ på vad miniräknaren kan göra. Tar en input till variabeln räkna_med
    if räkna_med == "1": #Gör detta om användaren väljer nummer 1
        nummer_1 = float(input("Skriv ett tal\n>")) #Frågar användaren om ett tal och tar en input till variablen nummer_1
        nummer_2 = float(input("Skriv ett till tal\n>")) #Frågar användaren om ett till tal
        summa = nummer_1 + nummer_2 #Adderar dom två talen som användaren valde
        print(f"Summan blev {summa}\n-------") #Skriver ut vad summan blev
        continue #Fortsätter while loopen 
    elif räkna_med == "2": #Gör detta om användaren väljer nummer 2
        nummer_1 = float(input("Skriv ett tal\n>")) #Frågar användaren om ett tal och tar en input till variablen nummer_1
        nummer_2 = float(input("Skriv ett till tal\n>")) #Frågar användaren om ett till tal och tar en input till variablen nummer_2
        differens = nummer_1 - nummer_2 #Subtraherar dom två tal som användaren valde
        print(f"Differensen blev {differens}\n-------") #Skriver ut vad differensen blev
        continue #Fortsätter while loopen
    elif räkna_med == "3": #Gör detta om användaren väljer nummer 3
        nummer_1 = float(input("Skriv ett tal\n>")) #Frågar användaren om ett tal och tar en input till variablen nummer_1
        nummer_2 = float(input("Skriv ett till tal\n>")) #Frågar användaren om ett till tal och tar en input till variablen nummer_2
        produkt = nummer_1 * nummer_2 #Multiplicerar dom två tal användaren valde
        print(f"Produkten blev {produkt}\n-------") #Skriver ut vad produkten blev
        continue #Fortsätter while loopen
    elif räkna_med == "4": #Gör detta om användaren väljer nummer 4
        nummer_1 = float(input("Skriv ett tal\n>")) #Frågar användaren om ett tal och tar en input till variablen nummer_1
        nummer_2 = float(input("Skriv ett till tal\n>")) #Frågar användaren om ett till tal och tar en input till variablen nummer_2
        kvoten = nummer_1 / nummer_2 #Dividerar dom två tal användaren valde
        print(f"Kvoten blev {kvoten}\n-------") #Skriver ut vad kvoten blev
        continue #Fortsätter while loopen
    elif räkna_med == "5": #Gör detta om användaren väljer nummer 5
        print("Hejdå!") #Skriver ut Hejdå!
        break #Avslutar while loopen
    else: #Gör detta om användaren inte väljer något av valen
        print("Vänligen välj ett av förslagen!\n-------") #Printar ett medelande 
        continue #Fortsätter while loopen