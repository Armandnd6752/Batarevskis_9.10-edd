parole = "676767"
meginajumi = 3

while meginajumi > 0:
    ievad_parole = input("Ievadi paroli: ")

    if ievad_parole == parole:
        print("Piekļuve atļauta!")
        break
    else:
        meginajumi -= 1

        if meginajumi == 0:
            print("Piekļuve ir bloķēta!")
        else:
            print(f"Parole ir nepareiza! Jums ir atlikuši {meginajumi} mēģinājumi.")

    
   