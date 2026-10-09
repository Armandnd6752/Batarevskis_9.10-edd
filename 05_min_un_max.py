skaitļi = int(input("Cik skaitļus gribi ievadīt?:"))
if skaitļi <= 0:
    print("Kļuda.")
else:
    for i in range(skaitļi):
        skaitlis = int(input(f"Ievadi {i + 1} skaitli:"))
        if i == 0:
         mazakais = skaitlis
         lielakais = skaitlis
        else:
            if skaitlis < mazakais:
               mazakais = skaitlis
            if skaitlis > mazakais:
               lielakais = skaitlis
            print(f"Mazakais skaitlis: {mazakais}")
            print(f"Lielakais skaitlis: {lielakais}")

