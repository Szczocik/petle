import sys
liczba_elementow = int(sys.argv[1])

liczba_kilogramow_wyslanych = 0

puste_kilogramy = 0
paczka_kilogramy = 0
paczka_numer = 0
suma_elementow = 0
najlzejsza_paczka_numer = 0
najlzejsza_paczka_waga = 20

for numer_elementu in range(liczba_elementow):
    print("podaj element w kilogramach: ")
    waga_elementu = int(input())
    #if numer_elementu == 1:
     #   paczka_numer = 1
    if waga_elementu == 0:
        break
    elif waga_elementu < 1 or waga_elementu > 10:
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
print(suma_pustych_kilogramow)
print(najlzejsza_paczka_numer, najlzejsza_paczka_waga)
print(paczka_numer)
print(liczba_kilogramow_wyslanych)



