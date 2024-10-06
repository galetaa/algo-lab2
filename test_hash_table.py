import pytest
from hash_table import HashTable


def test_add_and_get():
    ht = HashTable()

    ht['key1'] = 'value1'
    ht['key2'] = 'value2'
    ht['key3'] = 'value3'

    assert ht['key1'] == 'value1'
    assert ht['key2'] == 'value2'
    assert ht['key3'] == 'value3'

    with pytest.raises(KeyError):
        _ = ht['key4']


def test_contains():
    ht = HashTable()

    ht['key1'] = 'value1'
    ht['key2'] = 'value2'

    assert 'key1' in ht
    assert 'key2' in ht
    assert 'key3' not in ht

    assert ht.contains('key1') == True
    assert ht.contains('key3') == False


def test_delete():
    ht = HashTable()

    ht['key1'] = 'value1'
    ht['key2'] = 'value2'

    del ht['key1']

    with pytest.raises(KeyError):
        _ = ht['key1']

    assert ht['key2'] == 'value2'


def test_size():
    ht = HashTable()

    assert len(ht) == 0

    ht['key1'] = 'value1'
    ht['key2'] = 'value2'

    assert len(ht) == 2

    del ht['key1']

    assert len(ht) == 1


def test_benchmark_add(benchmark):
    ht = HashTable()

    def add_elements():
        for i in range(1000):
            ht[f'key{i}'] = f'value{i}'

    benchmark.pedantic(add_elements, iterations=10, rounds=5)


def test_benchmark_get(benchmark):
    ht = HashTable()

    for i in range(1000):
        ht[f'key{i}'] = f'value{i}'

    def get_elements():
        for i in range(1000):
            _ = ht[f'key{i}']

    benchmark.pedantic(get_elements, iterations=10, rounds=5)


def test_benchmark_contains(benchmark):
    ht = HashTable()

    for i in range(1000):
        ht[f'key{i}'] = f'value{i}'

    def check_contains():
        for i in range(1000):
            _ = f'key{i}' in ht

    benchmark.pedantic(check_contains, iterations=10, rounds=5)


def test_benchmark_delete(benchmark):
    def delete_elements():
        ht = HashTable()

        for i in range(1000):
            ht[f'key{i}'] = f'value{i}'

        for i in range(1000):
            del ht[f'key{i}']

    benchmark.pedantic(delete_elements, iterations=10, rounds=5)
