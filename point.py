from typing import Iterable, Sized
from math import sqrt


def check_container(container: {Iterable, Sized }, target_size:int=0) -> bool:
    """
    Check if container is iterable, support __len__, and every value is not None.
    Optionally can check size.

    :parameter container target for checks
    :parameter target_size get False if len() not equal to this value, but ignored if 0

    :return result of checks
    """
    try:
        iter(container)
        if target_size != 0 and len(container) !=target_size:
            return False
        for n in range(len(container)):
            if container[n] is None:
                return False
    except TypeError:
        return False

    return True

class Point:
    def __init__(self, x=None, y=None):
        self.x, self.y = x, y

    def __getitem__(self, i):
        if i==0: return self.x
        if i==1: return self.y
        raise IndexError("Point index out of range")

    def __len__(self):
        return 2

    def __eq__(self, other: {Iterable, Sized }) -> bool:
        """ A=B if ∀(n): A[n] = B[n] """
        if isinstance(other, Point) or check_container(other, len(self)):
            return all(self[n] == other[n] for n in range(len(self)))
        return NotImplemented

    def __ne__(self, other):
        eq_result = self.__eq__(other)
        return NotImplemented if eq_result is NotImplemented else not eq_result

    def __lt__(self, other):
        """ A<B if any A[n] < B[n] """
        if isinstance(other, Point): 
            if self.x<other.x and self.y<other.y:
                return True 
            elif self.x>other.x and self.y>other.y:
                return False
            return NotImplemented

    def __gt__(self, other):
        """ A>B if any A[n] > B[n] """
        if isinstance(other, Point): 
            if self.x>other.x and self.y>other.y:
                return True
            elif self.x<other.x and self.y<other.y:
                return False
            return NotImplemented
                
        
    def __ge__(self, other):
        return self > other or self == other if isinstance(other, Point) else False

    def __le__(self, other):
        return self < other or self == other if isinstance(other, Point) else False

    def __str__(self):
        if isinstance(self.x, int) and isinstance(self.y, int):
            return f"({self.x},{self.y})"
        else:
            return f"({self.x:.1f}, {self.y:.1f})"

    def __repr__(self):
        if isinstance(self.x, int) and isinstance(self.y, int):
            return f"({self.x},{self.y})"
        else:
            return f"({self.x:.1f}, {self.y:.1f})"

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

