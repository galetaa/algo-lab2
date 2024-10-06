from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional, Iterator


class AbstractLinkedList(ABC):
    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __contains__(self, item: Any) -> bool:
        pass

    @abstractmethod
    def append(self, data: Any) -> None:
        pass

    @abstractmethod
    def reverse(self) -> None:
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[Any]:
        pass


@dataclass
class Node:
    data: Any
    next: Optional[Node] = None


class LinkedList(AbstractLinkedList):
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __contains__(self, item: Any) -> bool:
        return self.contains(item)

    def contains(self, item: Any) -> bool:
        current = self.head
        while current:
            if current.data == item:
                return True
            current = current.next
        return False

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self) -> str:
        nodes = [str(node) for node in self]
        return " -> ".join(nodes)
