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

count = 0
sum = 0
print("Podaj liczbę: ")
last_number = input()
while not last_number.isnumeric():
    print("Podaj liczbę: ")
    last_number = input()
last_number = int(last_number)
while last_number:
    sum += last_number
    count += 1 # count = count + 1
    print("Podaj liczbę: ")
    last_number = input()
    while not last_number.isnumeric():
        print("Podaj liczbę: ")
        last_number = input()
    last_number = int(last_number)
if count:
    print("Suma: ", sum, "średnia: ", sum/count)
else:
    print("Suma: ", 0, "średnia: ", 0)

counter = 0
product = 1
while counter < 10:
    counter += 1
    print("obliczam {}".format(counter))
    product *= counter
    if product > 1000:
        break
    print("{}: {}".format(counter, product))


wine_count = 0
children_count = 0
adult_count = 0
passenger_count = 0
while passenger_count < 20:
    print("podaj wiek pasażera")
    age = int(input())
    if age == 0:
        break
    elif age < 18:
        children_count += 1
        passenger_count += 1
        continue
    print("podaj liczbę lampek wina")
    wine_current = int(input())
    if wine_current < 0 or wine_current > 3:
        print("nieprawidłowa liczba lampek wina")
        continue
    wine_count += wine_current
    adult_count += 1
    passenger_count += 1
print("Dorosłych: {}, Dzieci: {}, lampek wina: {}, Przychód: {}".format(
    adult_count,
    children_count,
    wine_count,
    adult_count*400 + children_count*200 + wine_count*10
))



for i in range(6):
    print("Pętla 1 {}".format(i))
for i in range(2,6):
    print("Pętla 2 {}".format(i))
for i in range(14, 6, -2):
    print("Pętla 3 {}".format(i))

napis = "Ala ma kota"
for litera in napis:
    print(litera)

lista = [1,4,67756,324234,546]

for i in lista:
    print(i)



print("Podaj liczbę zleceń")
job_count = int(input())
workload1 = 0
workload2 = 0
workload3 = 0
for job in range(job_count):
    print("Podaj liczbę godzin pracy dla zlecenia")
    job_hours = int(input())
    if job_hours <= 0:
        print("Błąd: Nieprawidłowa liczba godzin!")
        break
    if workload3 < workload1 and workload3 < workload2:
        workload3 += job_hours
    elif workload2 < workload1:
        workload2 += job_hours
    else:
        workload1 += job_hours
print("Najbliży mechanik będzie wolny w ciągu {} dni".format(
    int((min(workload1, workload2, workload3)+7)  / 8)
))
print("Wszyscy mechanicy będą wolni w ciągu {} dni".format(
    int((max(workload1, workload2, workload3)+7)  / 8)
))

import sys

#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])

print("Podaj liczbę zleceń")
job_count = int(sys.argv[1])
workload1 = 0
workload2 = 0
workload3 = 0
for job in range(job_count):
    print("Podaj liczbę godzin pracy dla zlecenia")
    job_hours = int(input())
    if job_hours <= 0:
        print("Błąd: Nieprawidłowa liczba godzin!")
        break
    if workload3 < workload1 and workload3 < workload2:
        workload3 += job_hours
    elif workload2 < workload1:
        workload2 += job_hours
    else:
        workload1 += job_hours
print("Najbliży mechanik będzie wolny w ciągu {} dni".format(
    int((min(workload1, workload2, workload3)+7)  / 8)
))
print("Wszyscy mechanicy będą wolni w ciągu {} dni".format(
    int((max(workload1, workload2, workload3)+7)  / 8)
))
'''
