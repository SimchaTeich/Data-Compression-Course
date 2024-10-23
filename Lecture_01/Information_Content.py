#################################################################
#                                                               #
# Terminology:                                                  #
#    * Shannon at 1948: The amount of information contained in  #
#      a symbol si of probaility pi is:                         #
#      I(si) = -log2(pi)                                        #
#      * A code shuold be able to be devised such that the      #
#      codeword for si contains I(si) bits                      #
#                                                               #
#    * Entropy is the average of the information per symbol.    #
#      * Given a probability distribution P With alphabet size  #
#        n, define:                                             #
#        H(P) = -SUM_1->n(pi * log2(pi))                        #
#        H(P) = SUM_1->n(pi * I(si))                            #
#      * For all unambiguous codes C:                           #
#        H(P) <= E(P, C)                                        #
#                                                               #
#    * Kraft inequality for code C is:                          #
#      K(C) = SUM_i=1->n(2^(-|ci|))                             #
#                                                               #
#################################################################
from math import log2
from decimal import Decimal
from tabulate import tabulate
from Expected_codeword_length import ECL

def I(p):
    """
    return the Information content of symbol s
    with probability p. It means that the codeword
    for s, shuold be represented with [-log2(p)]
    bits only for the best encode
    """
    return -log2(p)



def H(P):
    """
    return the entropy for given distribution P
    """
    return float(sum([Decimal(str(p)) * Decimal(str(I(p))) for p in P]))



def K(C):
    """
    return the kraft of given code C
    """
    return float(sum([Decimal(str(2**(-len(c)))) for c in C]))



def example1():
    ALPHABET    = ['a' ,'b'  ,'c'  ,'d'  ,'e'  ,'f'  ]
    Probability = [0.67, 0.11, 0.07, 0.06, 0.05, 0.04]
    Information = [float("{:0.2f}".format(I(p))) for p in Probability]

    print(tabulate({'si':ALPHABET, 'pi':Probability, 'I(si)':Information}, headers="keys", tablefmt="pretty"))
    print("H(P)={:0.2f}".format(H(Probability)))



def example2():
    headers = ['si', 'p1', 'Code 1', 'Code 2']
    table  = [['a' , 0.67, '000'   , '00'],
              ['b' , 0.11, '001'   , '01'],
              ['c' , 0.07, '010'   , '100'],
              ['d' , 0.06, '011'   , '101'],
              ['e' , 0.05, '100'   , '110'],
              ['f' , 0.04, '101'   , '111']]
    n = 6
    P  = [table[i][1] for i in range(n)]
    C1 = [table[i][2] for i in range(n)]
    C2 = [table[i][3] for i in range(n)]

    table.append(['Expected length', '',ECL(P, C1), ECL(P, C2)])
    
    print(tabulate(table, headers=headers, tablefmt="pretty"))
    print("Code 1: K(C)={0}".format(K(C1)))
    print("Code 2: K(C)={0}".format(K(C2)))



def main():
    print("example from PDF 1 slide 21 and 23")
    example1()

    print()

    print("example from PDF 1 slide 27")
    example2()



if __name__ == "__main__":
    main()
