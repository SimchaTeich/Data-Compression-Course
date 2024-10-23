from tabulate import tabulate
from math import log2, ceil

def Unary_Code(i):
    """
    Return the unary coade for a simbol s in given index i
    Note: 1 <= i
    """
    return "1" * (i - 1) + "0"



def Simple_Binary_Code(i, n):
    """
    Return the simple binary code for a symbol s by it's
    index i, and by given alphabet size n.
    Encoding: every symbol is assigned a codeword
               of exactly ceil(log2(n)) bits
    Note: 1 <= i
    """
    # codewords start from 0, but 1<=i.
    # So, the encoder takes the index i but encoding by i-1 binary value string.
    return bin(i-1)[2:].zfill(ceil(log2(n)))



def Minimal_Binary_Code(i, n):
    """
    Return the minimal binary code for a simbol s by it's
    index i, and by given alphabet size n.
    Encoding: the first [2^(ceil(log2(n)))-n] symbols are
              assigned a codewords of exaclty int(log2(n)) bits.
              and the rest codewords with ceil(log2(n)) bits per codeword.
    Note: 1 <= i
    """
    max_index_for_short   = 2**(int(ceil(log2(n)))) - n
    num_of_bits_for_short = int(int(log2(n)))
    num_of_bits_for_long  = int(ceil(log2(n)))

    if (i <= max_index_for_short):
        return bin(i - 1)[2:].zfill(num_of_bits_for_short)
    else: # to get the right codeword (prefix-free), omit all the leafs was cancels by shorter codewords and start coding from the first leaf wasn't canceld.
        return bin((2*max_index_for_short - 1) + (i - max_index_for_short))[2:].zfill(num_of_bits_for_long)



def C_gama(i):
    """
    Return the C-gama Elias code for a simbol s by it's index i.
    Encoding:
        first part  - Unary Code for the number of bits in i
        second part - a binary code for i within the range
                      established by the unary part
    Note: 1 <= i
    Note2: Omit the first bit in the second part
    Note3: For readability (just for this example) keep space (' ')
           between the two parts of the code.
    """
    return Unary_Code(1 + int(log2(i))) + ' ' + bin(i)[3:]



def C_delta(i):
    """
    Return the C-delta Elias code for a simbol s by it's index i.
    Encoding:
        first part  - C-gama Code for the number of bits in i
        second part - a binary code for i within the range
                      established by the unary part
    Note: 1 <= i
    Note2: Omit the first bit in the second part
    Note3: For readability (just for this example) keep space (' ')
           between the two parts of the code.
    Note4: using C_gama function, so dont forget remove the space char
           from the result from it.
    """
    return C_gama(1 + int(log2(i))).replace(' ', '') + ' ' + bin(i)[3:]



def example1(n):
    ALPHABET_Indexes = [i for i in range(1, n+1)] # indexes starting from 1
    C                = [Unary_Code(i) for i in range(1, n+1)]
    print(tabulate({'Symbol Index':ALPHABET_Indexes, 'Unary Code':C}, headers="keys", tablefmt="pretty"))



def example2(n):
    ALPHABET_Indexes = [i for i in range(1, n+1)] # indexes starting from 1
    C                = [Simple_Binary_Code(i, n) for i in range(1, n+1)]
    print(tabulate({'Symbol Index':ALPHABET_Indexes, 'Simple Binary Code':C}, headers="keys", tablefmt="pretty"))



def example3(n):
    ALPHABET_Indexes = [i for i in range(1, n+1)] # indexes starting from 1
    C                = [Minimal_Binary_Code(i, n) for i in range(1, n+1)]
    print(tabulate({'Symbol Index':ALPHABET_Indexes, 'Minimal Binary Code':C}, headers="keys", tablefmt="pretty"))



def example4(n):
    ALPHABET_Indexes = [i for i in range(1, n+1)] # indexes starting from 1
    C                = [C_gama(i) for i in range(1, n+1)]
    print(tabulate({'Symbol Index':ALPHABET_Indexes, 'Elias C-gama Code':C}, headers="keys", tablefmt="pretty"))



def example5(n):
    ALPHABET_Indexes = [i for i in range(1, n+1)] # indexes starting from 1
    C                = [C_delta(i) for i in range(1, n+1)]
    print(tabulate({'Symbol Index':ALPHABET_Indexes, 'Elias C-delta Code':C}, headers="keys", tablefmt="pretty"))



def main():
    n = int(input("Give your alphabet size: "))
    print()

    print("Unary Code Example:")
    example1(n)

    print()

    print("Simple Binary Code Example:")
    example2(n)

    print()

    print("Minimal Binary Code Example:")
    example3(n)

    print()

    print("Elias C-gama Code Example:")
    example4(n)

    print()

    print("Elias C-delta Code Example:")
    example5(n)


if __name__ == "__main__":
    main()