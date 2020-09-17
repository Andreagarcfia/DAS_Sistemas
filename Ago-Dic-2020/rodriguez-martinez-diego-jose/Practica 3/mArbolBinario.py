from IIterableCollection import IIterableCollection
from BTIterator import BTIterator

class mBTree(IIterableCollection):
    def __init__(self, x = None):
        self._val = x
        self._left = None
        self._right = None

    def insert(self, _val):
    # Compara el nuevo _valor con el nodo raiz

        #Checa si las posiciones estan vacias
        if self._val:
            if _val < self._val:
                if self._left is None:
                    self._left = mBTree(_val)
                else:
                    self._left.insert(_val)
            elif _val > self._val:
                if self._right is None:
                    self._right = mBTree(_val)
                else:
                    self._right.insert(_val)
        else:
            self._val = _val

###############
    def createIterator(self):
        return BTIterator(self)