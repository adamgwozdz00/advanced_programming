# Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w
# parametrze jest parzysta i zwróci tą informację jako typ logiczny bool
# ( True / False ). Należy uruchomić funkcję, wynik wykonania zapisać do
# zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy
# tekst "Liczba parzysta" / "Liczba nieparzysta"

def is_even(number: int) -> bool:
    return number % 2 == 0


if __name__ == '__main__':
    test_numbers = [1, 2, 3]
    for i in range(len(test_numbers)):
        if (is_even(test_numbers[i])):
            print("Liczba parzysta")
        else:
            print("Liczba nieparzysta")
