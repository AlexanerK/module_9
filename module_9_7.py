from math import sqrt


def is_prime(func):
    def surrogate(*args, **kwargs):
        result = func(*args, **kwargs)
        i = 0
        for k in range(2, result// 2+1):
            if result % k == 0 :
                i = i+1

        if i <= 0:
            print (f'Простое')
        else: print (f'Составное')
        return result
    return surrogate



@ is_prime
def sum_three(*args):
    res = sum(args)
    return res

result = sum_three(2,3,6)
print(result)

