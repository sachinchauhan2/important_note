# atm
def atm_strike(n,m):
    a = (n // m) * m
    b = a + m
    return int(b if n - a > b - n else a)
