paczka <= 20
liczba_kilogramow_wyslanych = 0
suma_pustych_kilogramow = 0
paczka_puste_kilogramy = 0
while paczka:
    print("podaj elementw kilogramach: ")
 element = int(input())
    if element == 0 and element < 1 and element > 10:
        break
