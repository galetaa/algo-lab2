from typing import Any, List, Optional


class DynamicArray:

    def __init__(self) -> None:
        self._size: int = 0
        self._capacity: int = 8
        self._array: List[Optional[Any]] = [None] * self._capacity

    def _resize(self, new_capacity: int) -> None:
        new_array = [None] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def append(self, item: Any) -> None:
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._size] = item
        self._size += 1

    def get(self, index: int) -> Optional[Any]:
        if 0 <= index < self._size:
            return self._array[index]
        return None

    def set(self, index: int, item: Any) -> None:
        if 0 <= index < self._size:
            self._array[index] = item

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, index: int) -> Optional[Any]:
        return self.get(index)

    def __setitem__(self, index: int, item: Any) -> None:
        self.set(index, item)

    def __iter__(self):
        for i in range(self._size):
            yield self._array[i]


class HashTable:

    def __init__(self, initial_capacity: int = 8) -> None:
        self._capacity = initial_capacity
        self._buckets = DynamicArray()
        for _ in range(self._capacity):
            self._buckets.append([])
        self._size = 0

    def _hash(self, key: Any) -> int:
        return hash(key) % self._capacity

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self._size += 1

    def __getitem__(self, key: Any) -> Any:
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, v in bucket:
            if k == key:
                return v

        raise KeyError(f"Key {key} not found in HashTable")

    def __delitem__(self, key: Any) -> None:
        index = self._hash(key)
        bucket = self._buckets[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._size -= 1
                return

        raise KeyError(f"Key {key} not found in HashTable")

    def __contains__(self, key: Any) -> bool:
        index = self._hash(key)
        bucket = self._buckets[index]

        for k, _ in bucket:
            if k == key:
                return True
        return False

    def contains(self, key: Any) -> bool:
        return key in self

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        items = []
        for bucket in self._buckets:
            for k, v in bucket:
                items.append(f"{k}: {v}")
        return "{" + ", ".join(items) + "}"
