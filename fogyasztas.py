ut = int(input("Megtett út (km): "))
benzin = int(input("Elhasznált benzin (liter): "))
fogyasztas = round(benzin/ut*100,1)
if (fogyasztas < 6.5):
    print(f"Az autó fogyasztása alacsony, {fogyasztas} liter/100km")
elif (fogyasztas > 9):
    print(f"Az autó fogyasztása magas, {fogyasztas} liter/100km")
else:
    print(f"Az autó fogyasztása normál, {fogyasztas} liter/100km")