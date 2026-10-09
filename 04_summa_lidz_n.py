n = int(input("Ievadi pozitivo skaitli: "))
if n <= 0:
    print("Ieraksti pozitivo skaitli,nevis negativo.")
else:
    summa = 0
    for i in range (1, n + 1):
        summa += i
    print(f"Skaitļu summa no 1 līdz{n} ir {summa}.")
 

