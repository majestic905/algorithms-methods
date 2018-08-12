from math import sqrt, log, factorial

def f01(n): return 3 ** log(n, 2)
def f02(n): return 4 ** n
def f03(n): return n ** sqrt(n)
def f04(n): return sqrt(log(n, 4))
def f05(n): return 2 ** (2 ** n)
def f06(n): return sqrt(n)
def f07(n): return log(n, 2) ** 2
def f08(n): return n / log(n, 5)
def f09(n): return log(factorial(n), 2)
def f10(n): return log(n, 3)
def f11(n): return log(n, 2) ** log(n, 2)
def f12(n): return 2 ** n
def f13(n): return 7 ** log(n, 2)
def f14(n): return log(log(n, 2), 2)
def f15(n): return 2 ** (3*n)
def f16(n): return n ** log(n, 2)
def f17(n): return factorial(n)
def f18(n): return n ** 2

functions = [
    [f14, '14. log(log(n, 2), 2)'],
    [f04, '04. sqrt(log(n, 4))'],
    [f10, '10. log(n, 3)'],
    [f07, '07. log(n, 2) ** 2'],
    [f06, '06. sqrt(n)'],
    [f08, '08. n / log(n, 5)'],
    [f09, '09. log(factorial(n), 2)'],
    [f01, '01. 3 ** log(n, 2)'],
    [f18, '18. n ** 2'],
    [f13, '13. 7 ** log(n, 2)'],
    [f11, '11. log(n, 2) ** log(n, 2)'],
    [f16, '16. n ** log(n, 2)'],
    [f03, '03. n ** sqrt(n)'],
    [f12, '12. 2 ** n'],
    [f02, '02. 4 ** n'],
    [f15, '15. 2 ** (3*n)'],
    [f17, '17. factorial(n)'],
    [f05, '05. 2 ** (2 ** n)']
]