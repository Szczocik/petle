liczba_paczek_wyslanych = 0
liczba_kilogramow_wyslanych = 0
suma_pustych_kilogramow = liczba_paczek_wyslanych * 20 - liczba_kilogramow_wyslanych
puste_kilogramy = 0
paczka = 0
suma_elementow = 0
while paczka < 20:
    print("podaj element w kilogramach: ")
    element = int(input())
    if element == 0 or element < 1 or element > 10:
        print('zła wartość w kg ')
        break

