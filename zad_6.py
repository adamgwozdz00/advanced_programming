# Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu
# list . Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć
# duplikaty, każdy element podnieść do potęgi 3 stopnia, a następnie zwrócić
# powstałą listę.


def merge_and_power_3(first_list: [int], second_list: [int]) -> [int]:
    merged = list(set(first_list + second_list))
    return [el**3 for el in merged]


if __name__ == "__main__":
    print(merge_and_power_3([1, 2, 3], [1, 2, 3]))
    print(merge_and_power_3([1, 2, 3], [1, 2, 4]))
