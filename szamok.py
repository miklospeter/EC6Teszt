import random

n = int(input("Adja meg, hány számot szeretne generálni! "))
szamok = []
atlag = 0
print("A generált számok:")
for i in range(0,n):
    szamok.append(random.randint(100,999))
    atlag += szamok[i]
    print(szamok[i])
atlag /= n
print(f"A számok átlaga: {round(atlag,2)}")
nagyobb = []
kisebb = []
for i in range(0,n):
    if (szamok[i] < atlag):
        kisebb.append(szamok[i])
    elif (szamok[i] > atlag):
        nagyobb.append(szamok[i])
print("Az átlagnál nagyobb számok: ",end=" ")
for i in range(0,len(nagyobb)):
    print(nagyobb[i],end=" ")
print()
print("Az átlagnál kisebb számok: ",end=" ")
for i in range(0,len(kisebb)):
    print(kisebb[i],end=" ")