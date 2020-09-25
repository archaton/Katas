def has_number(n: int):
    def _has_number(i: int):
        for j in map(int, str(i)):
            if n == j:
                return True
        return False
    return _has_number


def is_divisible_by(n: int):
    def _is_divisible_by(i: int):
        return 0 == i % n
    return _is_divisible_by


def fizzbuzz(n: int):
    for i in range(1, n+1):
        to_print = ''
        if is_divisible_by(3)(i) or has_number(3)(i):
            to_print += 'Fizz'
        if is_divisible_by(5)(i) or has_number(5)(i):
            to_print += 'Buzz'
        if '' == to_print:
            to_print = i
        print(to_print)
