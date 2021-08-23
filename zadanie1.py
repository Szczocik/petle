# ciąg Collatza


ciag_collatza = len[]
x = (int(input()))
wyraz_ciagu = 0

print("Podaj liczbę x w przedziale od 1 do 100: ")
while x != 1:
    if x % 2 == 0:
        wyraz_ciagu = (x / 2)
        #print(number)
    ciag_collatza += wyraz_ciagu
    elif x % 2 == 1:
        wyraz_ciagu = (3 * x + 1)
        #print(number)
    ciag_collatza += wyraz_ciagu

    continue

print(ciag_collatza)




