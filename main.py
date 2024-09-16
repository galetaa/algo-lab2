import ctypes
from typing import Type, Any


class DynamicArray:
    def __init__(self, dtype: Type[Any]) -> None:
        self.n: int = 0  # Количество элементов
        self.cap: int = 1  # Емкость
        self.dtype: Type[Any] = dtype  # Python тип массива
        self.ctype = self._python_type_to_ctype(dtype)  # C тип массива
        self.array = self._make_array(self.cap)

    def __len__(self) -> int:
        return self.n

    def __getitem__(self, index: int) -> Any:
        if not (0 <= index < self.n):
            raise IndexError('Неверный индекс')
        return self.array[index]

    def __delitem__(self, index: int) -> None:
        self.remove_at(index)

    def __contains__(self, element: Any) -> bool:
        for i in range(self.n):
            if self.array[i] == element:
                return True
        return False

    def append(self, element: Any) -> None:
        if not isinstance(element, self.dtype):
            raise TypeError(f"Элемент должен быть типа {self.dtype.__name__}")

        if self.n == self.cap:  # Удвоение ёмкости при переполнении
            self._resize(2 * self.cap)

        self.array[self.n] = element
        self.n += 1

    def remove_at(self, index: int) -> None:
        if not (0 <= index < self.n):
            raise IndexError("Неверный индекс")

        for i in range(index, self.n - 1):  # Сдвиг элементов влево
            self.array[i] = self.array[i + 1]

        self.n -= 1

        if self.dtype in {int, float}:
            self.array[self.n] = 0
        elif self.dtype == str:
            self.array[self.n] = ""
        elif self.dtype == bool:
            self.array[self.n] = False
        else:
            self.array[self.n] = None

        # Сокращаем ёмкость массива, если нужно
        if 0 < self.n < self.cap // 4:
            self._resize(self.cap // 2)

    def _resize(self, new_cap: int) -> None:
        new_array = self._make_array(new_cap)
        for i in range(self.n):
            new_array[i] = self.array[i]
        self.array = new_array
        self.cap = new_cap

    def _make_array(self, capacity: int) -> Any:
        return (capacity * self.ctype)()

    @staticmethod
    def _python_type_to_ctype(dtype: Type[Any]) -> Any:
        if dtype == int:
            return ctypes.c_int
        elif dtype == float:
            return ctypes.c_float
        elif dtype == str:
            return ctypes.c_wchar_p
        elif dtype == bool:
            return ctypes.c_bool
        else:
            return ctypes.py_object

    def contains_linear(self, elem: Any) -> bool:
        for i in range(self.n):
            if self.array[i] == elem:
                return True
        return False

    def reverse(self) -> None:
        left, right = 0, self.n - 1
        while left < right:
            self.array[left], self.array[right] = self.array[right], self.array[left]
            left += 1
            right -= 1
