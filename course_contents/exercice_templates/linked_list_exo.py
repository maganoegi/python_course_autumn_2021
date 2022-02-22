




from typing import TypeVar, Optional

T = TypeVar("T")

class LinkedListNode:
    def __init__(
            self, 
            content: T=None, 
            next: Optional['LinkedListNode']=None, 
            prev: Optional['LinkedListNode']=None 
        ) -> None:
        self._next = next
        self._prev = prev
        self._content = content

    @property
    def next(self) -> Optional['LinkedListNode']:
        return self._next

    @property
    def prev(self) -> Optional['LinkedListNode']:
        return self._prev

    @property
    def content(self) -> T:
        return self._content

    def add_to_head(self, value: T) -> None:
        if self.content == None:
            self._content = value
        else:
            tmp = self
            while tmp.has_prev():
                tmp = tmp.prev
            
            tmp._prev = self.__class__(content=value, next=tmp)

    def add_to_tail(self, value: T) -> None:
        if self.content == None:
            self._content = value
        else:
            tmp = self
            while tmp.has_next():
                tmp = tmp.next
            
            tmp._next = self.__class__(content=value, prev=tmp)

    def has_next(self) -> bool:
        return self.next != None
    
    def has_prev(self) -> bool:
        return self.prev != None

    def __str__(self) -> str:
        # RECURSIVE
        # return " ".join(
        #     [str(self.content)] + ([str(self.next)] if self.has_next() else [])
        # )

        # ITERATIVE
        return str(self.content)

    def all_to_string(self):
        root = self

        while root.has_prev():
            root = root.prev
        
        # RECURSIVE
        # return str(root)

        # ITERATIVE
        accumulator = str(root)
        while root.has_next():
            root = root.next
            accumulator += " " + str(root)
            
        return accumulator


def main() -> None:
    data = [1, 2, 3, 4]

    root = LinkedListNode()

    for value in data:
        root.add_to_head(value)
        print(root.all_to_string())


    data2 = [10, 11, 12, 13]

    for value in data2:
        root.add_to_tail(value)
        print(root.all_to_string())

    

if __name__ == '__main__':
    main()