import pytest
from jar import Jar


def test_init():
    """Test initialization of the cookie jar."""
    # Test default capacity
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test custom capacity
    jar = Jar(5)
    assert jar.capacity == 5
    assert jar.size == 0

    # Test zero capacity
    jar = Jar(0)
    assert jar.capacity == 0

    # Test invalid capacity (negative)
    with pytest.raises(ValueError):
        Jar(-1)

    # Test invalid capacity (non-integer)
    with pytest.raises(ValueError):
        Jar("12")

    with pytest.raises(ValueError):
        Jar(3.5)


def test_str():
    """Test string representation of the cookie jar."""
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"

    jar.withdraw(1)
    assert str(jar) == "🍪🍪"


def test_deposit():
    """Test depositing cookies into the jar."""
    jar = Jar(10)

    # Test normal deposit
    jar.deposit(3)
    assert jar.size == 3

    # Test multiple deposits
    jar.deposit(2)
    assert jar.size == 5

    # Test depositing zero cookies
    jar.deposit(0)
    assert jar.size == 5

    # Test exceeding capacity
    with pytest.raises(ValueError):
        jar.deposit(6)

    # Test negative deposit
    with pytest.raises(ValueError):
        jar.deposit(-1)

    # Test non-integer deposit
    with pytest.raises(ValueError):
        jar.deposit(2.5)


def test_withdraw():
    """Test withdrawing cookies from the jar."""
    jar = Jar(10)
    jar.deposit(8)

    # Test normal withdrawal
    jar.withdraw(3)
    assert jar.size == 5

    # Test multiple withdrawals
    jar.withdraw(2)
    assert jar.size == 3

    # Test withdrawing zero cookies
    jar.withdraw(0)
    assert jar.size == 3

    # Test withdrawing all cookies
    jar.withdraw(3)
    assert jar.size == 0

    # Test withdrawing more than available
    with pytest.raises(ValueError):
        jar.withdraw(1)

    # Add some back for further tests
    jar.deposit(5)

    # Test negative withdrawal
    with pytest.raises(ValueError):
        jar.withdraw(-1)

    # Test non-integer withdrawal
    with pytest.raises(ValueError):
        jar.withdraw(1.5)


def test_capacity():
    """Test the capacity property."""
    jar1 = Jar()
    assert jar1.capacity == 12

    jar2 = Jar(20)
    assert jar2.capacity == 20

    jar3 = Jar(0)
    assert jar3.capacity == 0


def test_size():
    """Test the size property."""
    jar = Jar(15)
    assert jar.size == 0

    jar.deposit(7)
    assert jar.size == 7

    jar.deposit(3)
    assert jar.size == 10

    jar.withdraw(4)
    assert jar.size == 6

    jar.withdraw(6)
    assert jar.size == 0


def test_edge_cases():
    """Test edge cases and boundary conditions."""
    # Test jar at full capacity
    jar = Jar(5)
    jar.deposit(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar.deposit(1)

    # Test empty jar
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.withdraw(1)

    # Test filling and emptying completely
    jar = Jar(3)
    jar.deposit(3)
    jar.withdraw(3)
    assert jar.size == 0
    jar.deposit(3)
    assert jar.size == 3
