import unittest
from app import is_valid_email, calculate_circle_area, filter_positive_numbers, convert_date_format, is_palindrome

class TestApp(unittest.TestCase):
    def setUp(self):
        """Przygotowanie wspólnych danych do testów."""
        self.valid_emails = [
            "test@example.com",
            "user.name@domain.co",
            "john_smith@domain.info"
        ]
        self.invalid_emails = [
            "user@",
            "plainaddress",
            "@domain.com"
        ]
        self.radius_cases = [
            (1, 3.141592653589793),
            (2.5, 19.634954084936208)
        ]
        self.invalid_radius = [-1, -10]
        self.numbers_cases = [
            ([1, -2, 3, 0], [1, 3]),        # dodatnie liczby
            ([-1, -2, -3], []),             # tylko ujemne
            ([10, 20], [10, 20])            # tylko dodatnie
        ]
        self.date_cases = [
            # format domyślny
            ("2025-10-26", "%Y-%m-%d", "%d/%m/%Y", "26/10/2025"),
            # format własny
            ("31.12.2023", "%d.%m.%Y", "%Y/%m/%d", "2023/12/31"),
        ]
        self.palindrome_cases = [
            ("kajak", True),               # prosty palindrom
            ("A man a plan a canal Panama", True), # palindrom z odstępami i wielkością liter
            ("hello", False),              # nie-palindrom
            (" ", True)                    # pusty/pusta spacja jako palindrom
        ]

    def test_valid_email(self):
        """Testuje funkcję walidacji adresów e-mail – pozytywne i negatywne przypadki."""
        for email in self.valid_emails:
            with self.subTest(email=email):
                # Sprawdza poprawne adresy
                self.assertTrue(is_valid_email(email), f"Email powinien być poprawny: {email}")
        for email in self.invalid_emails:
            with self.subTest(email=email):
                # Sprawdza błędne adresy
                self.assertFalse(is_valid_email(email), f"Email powinien być błędny: {email}")

    def test_circle_area(self):
        """Testuje funkcję liczącą pole koła – typowe promienie oraz błąd dla wartości ujemnych."""
        for radius, expected in self.radius_cases:
            with self.subTest(radius=radius):
                self.assertAlmostEqual(calculate_circle_area(radius), expected, msg=f"Promień {radius}")
        for radius in self.invalid_radius:
            with self.subTest(radius=radius):
                # Powinien zwracać wyjątek ValueError dla ujemnego promienia
                with self.assertRaises(ValueError):
                    calculate_circle_area(radius)

    def test_filter_positive_numbers(self):
        """Testuje funkcję filtrującą liczby dodatnie z listy."""
        for numbers, expected in self.numbers_cases:
            with self.subTest(numbers=numbers):
                self.assertEqual(filter_positive_numbers(numbers), expected, f"Z wejścia {numbers} wynik powinien być {expected}")

    def test_convert_date_format(self):
        """Testuje funkcję zmiany formatu daty – różne formaty wejściowe i oczekiwane wyjściowe."""
        for date_str, input_fmt, output_fmt, expected in self.date_cases:
            with self.subTest(date_str=date_str, input_fmt=input_fmt, output_fmt=output_fmt):
                self.assertEqual(convert_date_format(date_str, input_fmt, output_fmt), expected, f"Data {date_str}")

    def test_is_palindrome(self):
        """Testuje funkcję sprawdzającą czy tekst jest palindromem – typowe i nietypowe przypadki."""
        for text, expected in self.palindrome_cases:
            with self.subTest(text=text):
                self.assertEqual(is_palindrome(text), expected, f"Tekst: {text}")

if __name__ == "__main__":
    unittest.main()
