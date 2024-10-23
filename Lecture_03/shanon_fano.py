from decimal import Decimal
from tabulate import tabulate

def ECL(P, C):
    """
    return the E(P, C)
    """
    n = len(C)
    return float(sum([Decimal(str(P[i])) * Decimal(str(len(C[i]))) for i in range(n)]))



def shannon_fano_recursion(li):
    left = []
    right = []

    gap = sum(Decimal(str(p)) for _, p, _ in li)

    # Divide it to two lists. assume |li| > 1
    s, p, c = li[0]
    while gap > Decimal(str(p)):
        left.append((s,p,c+'0'))
        gap -= 2*Decimal(str(p))
        
        # prepare the next
        li = li[1:]
        s, p, c = li[0]
    
    # all the remaining goes to the right
    for (l, p, c) in li:
        right.append((l,p,c+'1'))

    if len(left) == 1 and len(right) == 1:
        return left + right
    elif len(left) == 1:
        return left + shannon_fano_recursion(right)
    elif len(right) == 1:
        return right + shannon_fano_recursion(left)
    else:
        return shannon_fano_recursion(left) + shannon_fano_recursion(right)



def shannon_fano(S, P):
    # make the initial list with the structure [(simbol, probablity, codeword)]
    codewords = [''] * len(S)
    l = list(zip(S, P, codewords))

    # sort by probability before get inside the algorithm
    sorted(l, key=lambda triple: triple[1], reverse=True)
    
    # return the list [(simbol, probablity, codeword)] with full codewords.
    return shannon_fano_recursion(l)



def example1():
    S = ['a', 'b', 'c', 'd', 'e', 'f']
    P = [0.67, 0.11, 0.07, 0.06, 0.05, 0.04]
    
    # get S and P again to check no issues.
    s_p_c = shannon_fano(S, P)
    S = [s for s, _, _ in s_p_c]
    P = [p for _, p, _ in s_p_c]
    C = [c for _, _, c in s_p_c]

    print(tabulate({'simbol':S, 'prob':P, 'codeword':C}, headers="keys", tablefmt="pretty"))
    print("E(P, C) = {}".format(ECL(P, C)))



def example2():
    S = ['a', 'b', 'c', 'd', 'e', 'f', 'G']
    P = [0.4, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    
    # get S and P again to check no issues.
    s_p_c = shannon_fano(S, P)
    S = [s for s, _, _ in s_p_c]
    P = [p for _, p, _ in s_p_c]
    C = [c for _, _, c in s_p_c]

    print(tabulate({'simbol':S, 'prob':P, 'codeword':C}, headers="keys", tablefmt="pretty"))
    print("E(P, C) = {}".format(ECL(P, C)))


def main():
    print("Shannon-Fano Example from PDF 3 slide 22")
    example1()

    print()

    print("Shannon-Fano Example from PDF 3 slide 23")
    example2()


if __name__ == "__main__":
    main()