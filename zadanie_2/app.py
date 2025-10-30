import re
import math
from datetime import datetime

# Funkcja: sprawdzanie poprawności adresu e-mail
def is_valid_email(email: str) -> bool:
    pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")
    return bool(pattern.match(email))


# Funkcja: obliczanie pola koła
def calculate_circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Promień nie może być ujemny.")
    return math.pi * (radius ** 2)


# Funkcja: filtrowanie listy danych
def filter_positive_numbers(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n > 0]


# Funkcja: konwersja formatu daty
def convert_date_format(date_str: str, input_format: str = "%Y-%m-%d", output_format: str = "%d/%m/%Y") -> str:
    date_obj = datetime.strptime(date_str, input_format)
    return date_obj.strftime(output_format)


# Funkcja: sprawdzanie, czy tekst jest palindromem
def is_palindrome(text: str) -> bool:
    clean_text = "".join(c.lower() for c in text if c.isalnum())
    return clean_text == clean_text[::-1]
