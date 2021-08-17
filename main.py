#print("Hello world!")

'''
if <warunek>:
    <instrukcje wewnatrz warunku>
'''
'''
a = 3

if a % 2 == 0: #True/False
    print("Liczba a jest parzysta")
    print("Ala ma kota")
print("Liczba a jest całkowita")

c = True
if c:
    print("Warunek prawdziwy!")


a = 5

if a % 5 == 0 and a % 3 == 0:
    print("Liczba a jest podzielna 15")
else:
    if a % 5 == 0:
        print("Liczba a jest podzielna 5")
    if a % 3 == 0:
        print("Liczba a jest podzielna 3")


a = 4

if (a % 5 == 0 and a % 3 == 0) or a % 2 == 0:
    print("Liczba a jest podzielna 15 albo parzysta")
elif a % 5 == 0:
    print("Liczba a jest podzielna 5")
elif a % 3 == 0:
    print("Liczba a jest podzielna 3")
else:
    print("Liczba nie jest podzielna przez 3,5,15")