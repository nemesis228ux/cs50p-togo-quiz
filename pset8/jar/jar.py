class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self.size if self.size > 0 else  ""

    def deposit(self, n):
        if n > 0 and self.size + n <= self.capacity:
            self._size += n
        else:
            raise ValueError

    def withdraw(self, n):
        if n > 0 and self.size >= n:
            self._size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity


    