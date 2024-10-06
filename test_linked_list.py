import pytest
from linked_list import LinkedList


def test_append():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    assert len(lst) == 2
    assert list(lst) == [1, 2]


def test_contains():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    assert 1 in lst
    assert not 3 in lst


def test_reverse():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.reverse()
    assert list(lst) == [3, 2, 1]


def test_len():
    lst = LinkedList()
    assert len(lst) == 0
    lst.append(1)
    assert len(lst) == 1


def test_custom_contains():
    lst = LinkedList()
    lst.append(1)
    lst.append(2)
    assert lst.contains(2) == True
    assert lst.contains(3) == False


def test_benchmark_append(benchmark):
    lst = LinkedList()

    benchmark.pedantic(lst.append, args=(1,), iterations=1000, rounds=10)


def test_benchmark_reverse(benchmark):
    lst = LinkedList()

    for i in range(1000):
        lst.append(i)

    benchmark.pedantic(lst.reverse, iterations=10, rounds=5)


def test_benchmark_contains(benchmark):
    lst = LinkedList()

    for i in range(1000):
        lst.append(i)

    benchmark.pedantic(lst.contains, args=(500,), iterations=1000, rounds=10)


def test_benchmark_iter(benchmark):
    lst = LinkedList()

    for i in range(1000):
        lst.append(i)

    benchmark.pedantic(lambda: list(lst), iterations=100, rounds=10)
