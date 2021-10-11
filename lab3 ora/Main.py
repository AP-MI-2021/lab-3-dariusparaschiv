"""
Toate numerele același număr de divizori.
Funcția de calcul: get_longest_same_div_count(lst: list[int]) -> list[int]
"""


def div_count(t):
    if t == 1:
        return 1
    elif t == 2:
        return 2
    else:
        k = 0
        i = 1
        while i <= t:
            if t % i == 0:
                k = k + 1
            i = i + 1
    return k


def all_div_count(lst):
    d = div_count(lst[0])
    for x in lst:
        if div_count(x) != d:
            return False
    return True


def test_numar_divizori():
    assert div_count(1) == 1
    assert div_count(2) == 2
    assert div_count(9) == 3
    assert div_count(20) == 6


def get_longest_same_div_count(lst):
    """
    determina cea mai lunga subsecventa de nr. cu acelasi nr de divizori
    :param lst: lista de nr. intregi
    :return: cea mai lunga subsecventa de nr. cu acelasi nr de divizori din lst
    """
    longest_subsequence = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if all_div_count(lst[i:j + 1]) and len(lst[i:j + 1]) > len(longest_subsequence):
                longest_subsequence = lst[i:j + 1]
    return longest_subsequence


def test_get_longest_same_div_count():
    assert get_longest_same_div_count([2]) == [2]
    assert get_longest_same_div_count([9, 8, 6]) == [8, 6]
    assert get_longest_same_div_count([2, 20, 48, 5, 23]) == [5, 23]


def read_list():
    lst = []
    given_sting = input("Dati o lista cu numerele separate prin virgula ")
    numbers_as_string = given_sting.split(",")
    for x in numbers_as_string:
        lst.append(int(x))
    return lst


def solve_problem(lst):
    test_numar_divizori()
    test_get_longest_same_div_count()
    print(get_longest_same_div_count(lst))


def print_menu():
    print("1.Citire date.")
    print("2.Determinare cea mai lungă subsecvență cu toate numerele același număr de divizori. ")
    print("3.Iesire")


def main():
    print(get_longest_same_div_count([2, 1, 3, 4, 9]))
    while True:
        print_menu()
        optiune = input("Alegeti o optiune ")
        if optiune == "1":
            lst = read_list()
        elif optiune == "2":
            solve_problem(lst)
        elif optiune == "3":
            break
        else:
            print("optiune gresita!")


main()
