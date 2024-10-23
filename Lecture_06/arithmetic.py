from decimal import Decimal
from tabulate import tabulate
from fractions import Fraction

def interval_bounds(S_P):
    """
    divide interval [0,1] py probabilities P
    Input: list of probabilities P
    Output: {S: (low, high)}
    """
    S = list(S_P.keys())
    P = list(S_P.values())
    n = len(S_P)
    l = [0]

    for i in range(n):
        l.append(float(Decimal(str(l[-1])) + Decimal(str(P[i]))))
    
    return {s: (l, h) for s, l, h in zip(S,l[:-1], l[1:])}



def encode(M, S_P):
    """
    Arithmetic encoding.
    Input: msg M to encode
    Output: 1) number inside the last range,
            2) table (tabulate type) of calculates with the next columns:
               - Low
               - High
               - Range
            3) msg length (for the decoder)
    """
    S_L_H = interval_bounds(S_P)
    n     = len(S_P)
    k     = len(M)
    Low   = [0.0]
    High  = [1.0]
    Range = [1.0]
    
    low = 0.0
    high = 1.0
    for i in range(k):
        r = Range[i]
        symbol = M[i]
        
        high = float(Decimal(str(low)) + Decimal(str(S_L_H[symbol][1])) * Decimal(str(r)))
        High.append(high)
        
        low = float(Decimal(str(low)) + Decimal(str(S_L_H[symbol][0])) * Decimal(str(r)))
        Low.append(low)

        Range.append(float(Decimal(str(high)) - Decimal(str(low))))

    T = tabulate({'M[i]':'-'+M, 'Low':Low, 'High':High, 'Range':Range}, headers="keys", tablefmt="pretty")
    e = float(Decimal(str(Low[-1])) + (Decimal(str(High[-1])) - Decimal(str(Low[-1])))/2)

    return e, T, k



def decode(e, S_P, k):
    """
    Arithmetic decoding.
    Input: encoded number e,
           Symbols with Probabilities S_P,
           k is number of characters in M.
    Output: msg M
    """
    S_L_P = interval_bounds(S_P)
    M = ""

    for _ in range(k):
        symbol = ''
        for s, (l, h) in S_L_P.items():
            if l <= e and e < h:
                symbol = s
                M += symbol
                break
        
        r = Decimal(str(S_L_P[symbol][1])) - Decimal(str(S_L_P[symbol][0]))
        e = float((Decimal(str(e)) - Decimal(str(S_L_P[symbol][0])))/r)

    return M


def adaptive_p(s, N):
    numerator = N[s] + 1
    denominator = sum([N[s] for s in N.keys()]) + len(N)
    return numerator/denominator


def adaptive_print_level(Il, Ih, N, S_P):
    ALPHABET = sorted(N.keys())
    Interval_str = "Interval [{}, {})".format(Il, Ih)
    N_str        = "    "
    P_str        = "    "
    for s in ALPHABET:
        N_str += "N({})={} ".format(s, N[s])
    for s in ALPHABET:
        P_str += "P({})={} ".format(s, S_P[s])
    print(Interval_str)
    print(N_str)
    print(P_str)


def adaptive_encode(T):
    ALPHABET = sorted(list(set(list(T))))
    
    N = {}
    for s in ALPHABET:
        N[s] = 0
    
    S_P = {}
    for s in ALPHABET:
        S_P[s] = float(adaptive_p(s, N))
    S_L_H = interval_bounds(S_P)
    
    Il = 0.0
    Ih = 1.0
    adaptive_print_level(Il, Ih, N, S_P)
    
    for t in T:
        print("Encode {}:".format(t))
        r = (Decimal(str(Ih)) - Decimal(str(Il)))
        Ih = float(Decimal(str(Il)) + (Decimal(str(S_L_H[t][1]))) * r)
        Il = float(Decimal(str(Il)) + (Decimal(str(S_L_H[t][0]))) * r)
        
        N[t] += 1
        S_P = {}
        for s in ALPHABET:
            S_P[s] = float(adaptive_p(s, N))
        S_L_H = interval_bounds(S_P)
        adaptive_print_level(Il, Ih, N, S_P)


def print_table(S_P):
    S_L_H = interval_bounds(S_P)
    S = [s for s, (_, _) in S_L_H.items()]
    L = [l for _, (l, _) in S_L_H.items()]
    H = [h for _, (_, h) in S_L_H.items()]
    P = list(S_P.values())

    print(tabulate({'Si':S, 'Pi':P, 'low_bound':L, 'high_bound':H}, headers="keys", tablefmt="pretty"))



def example1():
    S_P = {'A': 0.67,
        'B': 0.11,
        'C': 0.07,
        'D': 0.06,
        'E': 0.05,
        'F': 0.04}
    print_table(S_P)



def example2():
    M       = "ABAAAEAABA"
    S_P     = {'A': 0.67,
              'B': 0.11,
              'C': 0.07,
              'D': 0.06,
              'E': 0.05,
              'F': 0.04}
    e, T, k = encode(M, S_P)
    print(T)
    print("encode({})={}".format(M, e))
    print("decode({})={}".format(e, decode(e, S_P, k)))



def example3():
    M       = "AAAAAAA$"
    S_P     = {'A':0.9, '$':0.1}
    e, T, k = encode(M, S_P)
    print(T)
    print("encode({})={}".format(M, e))
    print("decode({})={}".format(e, decode(e, S_P, k)))



def example4():
    M       = "BILL"
    S_P     = {'B':0.25, 'I':0.25, 'L':0.5}
    print_table(S_P)

    e, T, k = encode(M, S_P)
    print(T)
    print("encode({})={}".format(M, e))
    print("decode({})={}".format(e, decode(e, S_P, k)))



def example5():
    print(adaptive_encode("bccba"))



def main():
    print("Example for PDF 6 slide 6:")
    example1()

    print()

    print("Example for PDF 6 slide 8")
    example2()

    print()

    print("Example for PDF 6 slide 11")
    example3()

    print()

    print("Example for PDF 6 slide 15")
    example4()

    print()

    print("Example for PDF 6 slide 19")
    example5()


if __name__ == "__main__":
    main()
