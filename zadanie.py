import sys
liczba_elementow = int(sys.argv[1])
liczba_kilogramow_wyslanych = 0
waga_elementu_min = 1
waga_elementu_max = 10
puste_kilogramy = 0
paczka_kilogramy = 0
paczka_numer = 0
suma_elementow = 0
najlzejsza_paczka_numer = 0
najlzejsza_paczka_waga = 20

for numer_elementu in range(liczba_elementow):
    print("podaj element w kilogramach: ")
    waga_elementu = int(input())
    if waga_elementu == 0:
        break
    elif waga_elementu < waga_elementu_min or waga_elementu > waga_elementu_max:
        print('zła wartość w kg ')
        break
    else:
        liczba_kilogramow_wyslanych += waga_elementu
        if paczka_kilogramy + waga_elementu <= 20:
            paczka_kilogramy += waga_elementu
        else:
            paczka_numer += 1
            if paczka_kilogramy < najlzejsza_paczka_waga:
                najlzejsza_paczka_waga = paczka_kilogramy
                najlzejsza_paczka_numer = paczka_numer
            paczka_kilogramy = waga_elementu
paczka_numer += 1
if paczka_kilogramy < najlzejsza_paczka_waga:
    najlzejsza_paczka_waga = paczka_kilogramy
    najlzejsza_paczka_numer = paczka_numer

suma_pustych_kilogramow = paczka_numer * 20 - liczba_kilogramow_wyslanych
print("\n")
print('Liczba paczek wysłanych', paczka_numer)
print('Liczba kilogramów wysłanych', liczba_kilogramow_wyslanych)
print('Suma pustych kilogramów', suma_pustych_kilogramow)
print('Najlżejsza paczka miała nr', najlzejsza_paczka_numer,'wartość tej paczki w kg to:', najlzejsza_paczka_waga)





