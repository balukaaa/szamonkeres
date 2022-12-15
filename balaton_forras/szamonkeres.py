"""
nev = input("Vezetéknév: ")
nev1 = input("Keresztmév: ")
print(nev,nev1)
print(nev1,nev)

szam0 = int(input("Adj egy számot: "))
print(szam0 - 1)
print(szam0 + 1)


szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy számot: "))
print("A két szám összege:",(szam1 + szam2))
print("A két szám különbsége:", (szam1 - szam2))
print("A két szám szorzata:" ,(szam1 * szam2))
print("A két szám hányadosa:" (szam1 / szam2))

#4Feladat
szam = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy számot: "))
c =(2* szam + 3*szam2)
d =(2* szam - 3*szam2)
print(c)
print(d)

#5Feladat


print("Páros számok 1-20-ig")
for szam0 in range(1,21):
    if szam0 % 2 == 0:
        print(szam0,end=",")
print()
print("Páratlan számok 1-20-ig")
for szam1 in range(1,21):
    if szam1 % 2 == 1:
        print(szam1,end=",")  

"""
#7Feledat
szam = int(input("Alső szám: "))
szam0 = int(input("Felső szám: "))

list = range(szam,szam0+1)
sum = 0
i = 0
for x in list:
    sum = sum + x
    i += 1

print(sum, sum/i)
