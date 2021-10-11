"""
1. Toate numerele sunt pătrate perfecte.
  - Funcția de calcul: **get_longest_all_perfect_squares(lst: list[int]) -> list[int]**
13.	Toate numerele sunt formate din cifre prime.
  - Funcția de calcul: **get_longest_prime_digits(lst: list[int]) -> list[int]**
"""

import math


def perfect_square(lst):
    """"
    determina daca toate nr. dintr-o lista sunt patrate perfecte
    :param lst: lista de numere intregi
    :return: True, daca toatee nr. din lst sunt patrate perfecte sau False, in caz contrar
    """
    for x in lst:
        rad = math.sqrt(x)
        if int(rad + 0.5) ** 2 != x:
            return False
    return True


def test_perfect_square():
    assert perfect_square([4, 9]) is True
    assert perfect_square([3]) is False
    assert perfect_square([]) is True


def get_longest_all_perfect_squares(lst):
    """
    determina cea mai lunga subsecventa de nr. patrate perfecte
    :param lst: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. patrate perfecte din lst
    """
    longest_subsequence = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if perfect_square(lst[i:j + 1]) and len(lst[i:j + 1]) > len(longest_subsequence):
                longest_subsequence = lst[i:j + 1]
    return longest_subsequence


def test_get_longest_all_perfect_squares():
    assert get_longest_all_perfect_squares([4, 5]) == [4]
    assert get_longest_all_perfect_squares([32, 0, 81]) == [0, 81]
    assert get_longest_all_perfect_squares([55, 60, 82]) == []


def prime_digits(n):
    while n > 0:
        c = n % 10
        if not ((c == 2) or (c == 3) or (c == 5) or (c == 7)):
            return False
        n = n // 10
    return True


def all_prime_digits(lst):
    for x in lst:
        if not (prime_digits(x)):
            return False
    return True


def get_longest_prime_digits(lst):
    """
    determina cea mai lunga subsecventa de nr. formate doar din cifre prime
    :param lst: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. formate doar din cifre prime
    """
    longest_subsequence = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if all_prime_digits(lst[i:j + 1]) and len(lst[i:j + 1]) > len(longest_subsequence):
                longest_subsequence = lst[i:j + 1]
    return longest_subsequence


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([4, 2, 3, 6, 257]) == [2, 3]
    assert get_longest_prime_digits([4, 21]) == []
    assert get_longest_prime_digits([2, 23, 4, 7, 5, 53, 9, 0]) == [7, 5, 53]


def read_list():
    lst = []
    given_string = input("Dati o lista cu elementele separate prin virgula: ")
    numbers_as_string = given_string.split(",")
    for x in numbers_as_string:
        lst.append(int(x))
    return lst


def problem_1(lst):
    test_perfect_square()
    test_get_longest_all_perfect_squares()
    print(get_longest_all_perfect_squares(lst))


def problem_2(lst):
    test_get_longest_prime_digits()
    print(get_longest_prime_digits(lst))


def print_menu():
    print("1.Citire date.")
    print("2.Determinare cea mai lungă subsecvență cu proprietatea 1.")
    print("3.Determinare cea mai lungă subsecvență cu proprietatea 2.")
    print("4.Iesire")


def main():
    while True:
        print_menu()
        # lst = read_list()
        optiune = input("Alegeti o optiune ")
        if optiune == "1":
            lst = read_list()
        elif optiune == "2":
            problem_1(lst)
        elif optiune == "3":
            problem_2(lst)
        elif optiune == "x":
            break
        else:
            print("optiune gresita!")


main()
