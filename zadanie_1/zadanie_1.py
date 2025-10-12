# Tworzenie dwóch list liczb i nazw
numbers = [1, 2, 3, 4]
animals = ['pies', 'koty', 'dziki', 'łosie']

# Łączenie list w pary (krotki) za pomocą funkcji zip()
# Dokumentacja: https://docs.python.org/3/library/functions.html#zip
paired = list(zip(numbers, animals))
print("Połączone listy:", paired)

# Wykorzystanie funkcji z modułu math (pierwiastek z pierwszej liczby)
# Dokumentacja: https://docs.python.org/3/library/math.html#math.sqrt
import math
try:
    result = math.sqrt(numbers[0])  # obliczenie pierwiastka
    print("Pierwiastek z", numbers[0], "to", result)
except ValueError as ve:
    print("Błąd ValueError:", ve)  # obsługa wyjątku, np. dla wartości ujemnej

# Obsługa wyjątku ZeroDivisionError jako przykład
try:
    division = numbers[2] / 0  # celowo wywołany błąd
except ZeroDivisionError as zde:
    print("Błąd dzielenia przez zero:", zde)  # dokumentacja: https://docs.python.org/3/library/exceptions.html#ZeroDivisionError
