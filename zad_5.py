# Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi
# typu int . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z
# parametru pierwszego zawiera taką wartość jaką przekazano w parametrze
# drugim.


def contains(numbers: [int], number: int) -> bool:
    for i in range(len(numbers)):
        if numbers[i] == number:
            return True
    return False


if __name__ == "__main__":
    print(contains([1, 2, 3], 3))
    print(contains([1, 2, 3], 4))
