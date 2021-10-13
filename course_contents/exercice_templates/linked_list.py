
from typing import TypeVar

T = TypeVar("T")

class LinkedListNode:
    def __init__(self, val: T):
        self._val = val
        self.next = None

    @property
    def val(self) -> T:
        return self._val

    @property
    def has_next(self) -> bool:
        return self.next is not None

    def add_to_tail(self, val: T) -> None:
        current = self
        while current.has_next:
            current = current.next
        
        current.next = LinkedListNode(val)

    def add_to_head(self, val: T):
        node = LinkedListNode(val)
        node.next = self
        return node

    def __str__(self) -> str:
        accumulator = str(self.val)
        current = self
        while current.has_next:
            current = current.next
            accumulator += " " + str(current.val)

        return accumulator

class Animal:
    def __str__(self):
        return "Animal"

class Dog( Animal ):
    def __str__(self):
        return "Dog"

class Cat( Animal ):
    def __str__(self):
        return "Cat"

    
if __name__ == "__main__":

    llist = LinkedListNode(Dog())
    llist.add_to_tail(Cat())
    llist.add_to_tail(Dog())

    llist = llist.add_to_head(Animal())
    llist = llist.add_to_head(Dog())

    print(llist)