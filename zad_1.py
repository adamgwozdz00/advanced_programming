# Stworzyć funkcję, która przyjmuje 2 argumenty (typu string ) name i surname , a
# następnie zwróci stringa zgodnie ze wzorem Cześć {name} {surname}! Należy
# uruchomić funkcję, wynik wykonania funkcji zapisać do zmiennej, a następnie
# go wyświetlić ( print )

def say_hello(name: str, surname: str) -> None:
    return f"Cześć {name} {surname}"


if __name__ == '__main__':
    print(say_hello("Adam", "Gwozdz"))
