
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
        target = self
        while target.has_next:
            target = target.next
        
        target.next = LinkedListNode(val)

    def add_to_head(self, val: T):
        node = LinkedListNode(val)
        node.next = self
        return node

    def __str__(self) -> str:
        accumulator = str(self.val)
        t = self
        while t.has_next:
            t = t.next
            accumulator += " " + str(t.val)

        return accumulator

if __name__ == "__main__":

    llist = LinkedListNode(1)
    llist.add_to_tail(2)
    llist.add_to_tail(15)

    llist = llist.add_to_head(5)
    llist = llist.add_to_head(17)

    print(llist)