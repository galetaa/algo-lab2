from main import DynamicArray
import unittest
import time


class TestDynamicArray(unittest.TestCase):
    def setUp(self):
        self.int_array = DynamicArray(int)
        self.str_array = DynamicArray(str)

    def test_append_and_len(self):
        self.int_array.append(10)
        self.int_array.append(20)
        self.assertEqual(len(self.int_array), 2)

    def test_get_item(self):
        self.int_array.append(10)
        self.int_array.append(20)
        self.assertEqual(self.int_array[1], 20)

    def test_contains(self):
        self.int_array.append(10)
        self.int_array.append(20)
        self.assertTrue(10 in self.int_array)
        self.assertFalse(30 in self.int_array)

    def test_reverse(self):
        self.int_array.append(10)
        self.int_array.append(20)
        self.int_array.append(30)
        self.int_array.reverse()
        self.assertEqual(self.int_array[0], 30)
        self.assertEqual(self.int_array[2], 10)

    def test_remove(self):
        self.int_array.append(10)
        self.int_array.append(20)
        del self.int_array[0]
        self.assertEqual(len(self.int_array), 1)
        self.assertEqual(self.int_array[0], 20)


def benchmark_append(n: int) -> None:
    arr = DynamicArray(int)
    start_time = time.time()
    for i in range(n):
        arr.append(i)
    end_time = time.time()
    print(f"Appending {n} elements took {end_time - start_time:.6f} seconds.")


def benchmark_reverse(n: int) -> None:
    arr = DynamicArray(int)
    for i in range(n):
        arr.append(i)
    start_time = time.time()
    arr.reverse()
    end_time = time.time()
    print(f"Reversing an array of {n} elements took {end_time - start_time:.6f} seconds.")


# unittest.main(argv=[''], exit=False)
benchmark_append(100000)
benchmark_reverse(100000)
