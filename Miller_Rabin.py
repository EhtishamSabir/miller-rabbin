from random import randint


def milrab(p):
    if p == 1: return False
    if p == 2: return True
    if p % 2 == 0: return False
    m, k = p - 1, 0
    while m % 2 == 0:
        m, k = m // 2, k + 1
    a = randint(2, p - 1)
    x = pow(a, m, p)
    if x == 1 or x == p - 1: return True
    while k > 1:
        x = pow(x, 2, p)
        if x == 1: return False
        if x == p - 1: return True
        k = k - 1
    return False


def is_prime(p):
    if not milrab(p):
        return False
    if (p - 1) % (2 * 8192) != 0:
        return False
    return True


if __name__ == '__main__':
    c = 0
    for i in range(10000000000000000000000, 90000000000000000000000):
        if is_prime(i):
            print(i)
            c += 1
            if c >= 15:
                break
