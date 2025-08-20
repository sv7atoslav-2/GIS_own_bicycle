# from typing import Iterable, Any, Sized
from math import sqrt


def check_container(container: {len,iter }, target_size:int=0) -> bool:
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
        return None

    def __len__(self):
        return 2

    def __eq__(self, other: {__len__, __getitem__ }) -> bool:
        """ A=B if ∀(n): A[n] = B[n] """
        if isinstance(other, Point) or check_container(other, len(self)):
            for n in range(len(self)):
                if self[n] != other[n]:
                    return False
            return True

        return NotImplemented

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        """ A<B if any A[n] < B[n] """
        if isinstance(other, Point): 
            if self.x<other.x and self.y<other.y:
                return True 
            elif self.x>other.x and self.y>other.y:
                return False
            raise NotImplementedError

    def __gt__(self, other):
        """ A>B if any A[n] > B[n] """
        if isinstance(other, Point): 
            if self.x>other.x and self.y>other.y:
                return True
            elif self.x<other.x and self.y<other.y:
                return False
            raise NotImplementedError
                
        
    def __ge__(self, other):
        if isinstance(other, Point):
            if self > other or self == other:
                return True
            else:
                return False
        return False

    def __le__(self, other):
        if isinstance(other, Point):
            if self < other or self == other:
                return True
            else:
                return False
        return False

    def __str__(self):
        if type(self.x) is int and type(self.y) is int:
            return "({0},{1})".format(self.x,self.y)
        else:
            return "({0:.1f}, {1:.1f})".format(self.x,self.y)

    def __repr__(self):
        if type(self.x) is int and type(self.y) is int:
            return "({0},{1})".format(self.x,self.y)
        else:
            return "({0:.1f}, {1:.1f})".format(self.x,self.y)

    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

