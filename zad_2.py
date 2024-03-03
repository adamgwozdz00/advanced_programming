# Dla osób posiadających podstawową wiedzę o pythonie:
# a. Utwórz funkcję, która otrzyma w parametrze listę 5 imion, a następnie
# wyświetli każde z nich.
# b. Utwórz funkcję, która otrzyma w parametrze listę zawierającą 5
# dowolnych liczb, każdy jej element pomnoży przez 2, a na końcu ją
# zwróci. Zadanie należy wykonać w 2 wersjach:
# i. Wykorzystując pętle for .
# ii. Wykorzystując listę składaną.
# c. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli
# jedynie parzyste elementy.
# d. Utwórz funkcję, która otrzyma w parametrze listę 10 liczb
# (rekomendowane wykorzystanie funkcji range ), a następnie wyświetli co
# drugi element.

def print_names(names: [str]) -> None:
    for name in names:
        print(name)


def print_names2(names: [str]) -> None:
    [print(name) for name in names]


def multiply_by_two(numbers: [int]) -> [int]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i] * 2)
    return result


def multiply_by_two2(numbers: [int]) -> [int]:
    return [number * 2 for number in numbers]


if __name__ == '__main__':
    print_names(["Adam", "Krzysztof", "Weronika", "Jakub", "Marian"])
    print_names2(["Adam", "Krzysztof", "Weronika", "Jakub", "Marian"])
    print(multiply_by_two([1, 2, 3, 4, 5]))
    print(multiply_by_two2([1, 2, 3, 4, 5]))
