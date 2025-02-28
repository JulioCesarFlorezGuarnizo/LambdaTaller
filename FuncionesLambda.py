from functools import lru_cache

# Factorial
@lru_cache(None)
def factorial(z):
    return 1 if z == 0 else z * factorial(z - 1)

# Saber si un número es primo
def is_prime(n, d=2):
    if n < 2:
        return False
    if d * d > n:
        return True
    if n % d == 0:
        return False
    return is_prime(n, d + 1)

# Algoritmo de Euclides 
def gcd(x, y):
    return y if x == 0 else gcd(y % x, x)

# Algoritmo de Bisección para encontrar raíces de f(x)
def bisection(f, a, b, eps=1e-6):
    mid = (a + b) / 2
    if abs(f(mid)) < eps:
        return mid
    if f(a) * f(mid) < 0:
        return bisection(f, a, mid, eps)
    else:
        return bisection(f, mid, b, eps)

# Calcular cos(x) usando el polinomio de Taylor
def cos_taylor(x, n=10):
    def term(k):
        return ((-1) ** k * x ** (2 * k)) / factorial(2 * k)

    return sum(term(k) for k in range(n))
