import itertools

def kbits(n, k):
    result = []
    for bits in itertools.combinations(range(n), k):
        s = ['1'] * n
        for bit in bits:
            s[bit] = '0'
        result.append(''.join(s))
    return result

