# Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma
# dwóch pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę
# informację jako typ logiczny bool

def compare_sum_to_number(first_number: int, second_number: int, number_to_compare: int) -> bool:
    return first_number + second_number >= number_to_compare


if __name__ == '__main__':
    print(compare_sum_to_number(1, 2, 3))
    print(compare_sum_to_number(1, 2, 4))
    print(compare_sum_to_number(3, 3, 3))
