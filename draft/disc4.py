def prime_helper(n, max_factor):
    if max_factor == 1 and n != 1:
        return True
    elif n == 1 or n % max_factor == 0:
        return False
    else:
        return prime_helper(n, max_factor - 1)


def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    return prime_helper(n, n - 1)
