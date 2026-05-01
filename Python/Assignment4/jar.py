class Jar:
    def __init__(self, capacity=12):
        """Initialize a cookie jar with the given capacity."""
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        """Return a string representation of the cookie jar."""
        return "🍪" * self._size

    def deposit(self, n):
        """Add n cookies to the cookie jar."""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer")
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies for the jar")
        self._size += n

    def withdraw(self, n):
        """Remove n cookies from the cookie jar."""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Number of cookies must be a non-negative integer")
        if n > self._size:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property
    def capacity(self):
        """Return the cookie jar's capacity."""
        return self._capacity

    @property
    def size(self):
        """Return the number of cookies in the cookie jar."""
        return self._size
