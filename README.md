## petle i argumenty w konsoli
Napisz program do obsługi ładowarki paczek.

Każda paczka może maksymalnie zmieścić 20 kg towaru.

Do paczki dodawane są elementy.

Każdy z nich może ważyć od 1 do 10 kg. Jeśli dodanie elementu do paczki zwiększyłoby ciężar paczki powyżej 20kg, paczka powinna zostać wysłana (nie można już do niej dodać w przyszłości elementów), a bieżący element powinien zostać dodany do nowej paczki.

Wszystkie elementy powinny zostać wysłane.

Program powinien pobierać maksymalną liczbę elementów do wysyłki. Jeśli podano element o wadze 0, program powinien zakończyć działanie, tak jakby maksymalna liczba paczek została osiągnięta.

Na koniec działania program powinien wyświetlić w podsumowaniu:
- liczbę paczek wysłanych
- liczbę kilogramów wysłanych
- suma "pustych" - kilogramów (brak optymalnego pakowania). Liczba paczek * 20 - liczba kilogramów wysłanych
- która paczka miała najwięcej "pustych" kilogramów, jaki to był wynik
- program powinien kończyć się z błędem, gdy element dodawany ma więcej niż 10kg, lub mniej niż 1 kg i nie był dokładnie równy 0.
