UZDEVUMS 4

1.uzdevums
Programma pieprasa ievadīt pozitīvu veselu skaitli. Pēc tam tā aprēķina visu skaitļu summu no 1 līdz ievadītajam skaitlim, ieskaitot to. Ja ievadītais skaitlis ir 0 vai negatīvs, programma parāda paziņojumu.

2.uzdevums
| Solis | Nosacījums       | Mainīgie pirms | Veiktā darbība | Mainīgie pēc | Izvade |
|-------|------------------|----------------|----------------|--------------|--------|
| 0     | -                | -              | Sākums         | n=5          | -      |
| 1     | n <= 0: aplams   | summa=0        | i=1; summa+=1  | summa=1      | -      |
| 2     | n <= 0: aplams   | summa=1        | i=2; summa+=2  | summa=3      | -      |
| 3     | n <= 0: aplams   | summa=3        | i=3; summa+=3  | summa=6      | -      |
| 4     | n <= 0: aplams   | summa=6        | i=4; summa+=4  | summa=10     | -      |
| 5     | n <= 0: aplams   | summa=10       | i=5; summa+=5  | summa=15     | -      |
| 6     | Cikls beidzies   | summa=15       | Izvada summu   | summa=15     | 15     |

3.uzdevums

| Testa veids             | Ievade | Sagaidāmais rezultāts                     | Faktiskais rezultāts                       | Tests izturēts? |
|-------------------------|--------|-------------------------------------------|--------------------------------------------|-----------------|
| Tipisks                 | 5      | Skaitļu summa no 1 līdz 5 ir 15.          | Skaitļu summa no 1 līdz 5 ir 15.           | Jā              |
| Robežgadījums           | 1      | Skaitļu summa no 1 līdz 1 ir 1.           | Skaitļu summa no 1 līdz 1 ir 1.            | Jā              |
| Tukša/nederīga ievade   | 0      | Tiek parādīts kļūdas paziņojums.          | Ieraksti pozitīvo skaitli, nevis negatīvo. | Jā              |
| Papildu tests           | 10     | Skaitļu summa no 1 līdz 10 ir 55.         | Skaitļu summa no 1 līdz 10 ir 55.          | Jā              |

4.uzdevums
Ievade: abc
Sagaidāmais rezultāts: programma paziņo, ka jāievada vesels skaitlis.
Faktiskais rezultāts sākotnējā programmā: rodas ValueError kļūda, jo tekstu nevar pārvērst veselā skaitlī.
Kļūdas cēlonis: programma mēģina izpildīt int(input(...)), bet lietotājs ievada tekstu, nevis skaitli.
Uzlabojums: pievienots try-except, lai programma nekļūdītos, ja ievada tekstu. Tā vietā tiek parādīts paziņojums: Kļūda! Ievadi veselu skaitli.
Commit: Pievienots algoritms un tā testi