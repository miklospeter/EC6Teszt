class Auto:
    def __init__(self,sor):
        resz = sor.strip().split(";")
        self.rendszam = resz[0]
        self.evjarat = int(resz[1])
        self.marka = resz[2]

def auto_kora(aktevszam, evjarat):
    return aktevszam-evjarat

adatok = []
with open("autok.txt",encoding="utf-8") as f:
    for sor in f:
        adatok.append(Auto(sor))

print(f"A kereskedésben kapható autók száma: {len(adatok)}")
print("Azonos számjegyeket tartalmazó rendszámok:")
for i in range(0,len(adatok)):
    if (adatok[i].rendszam[3] == adatok[i].rendszam[4] and
        adatok[i].rendszam[4] == adatok[i].rendszam[5]):
        print(adatok[i].rendszam)
marka = input("Adjon meg egy márkát! ").upper()
db = 0
for i in range(0,len(adatok)):
    if (adatok[i].marka.upper() == marka):
        db += 1
print(f"A kereskedésben {db} db ilyen márkájú autó van.")
ezev = 2026
max = 0
for i in range(1,len(adatok)):
    if (auto_kora(ezev,adatok[i].evjarat) > auto_kora(ezev,adatok[max].evjarat)):
        max = i
print(f"A legidősebb autó a kereskedésben: {adatok[max].rendszam} {adatok[max].marka} {auto_kora(ezev,adatok[max].evjarat)}")
print()