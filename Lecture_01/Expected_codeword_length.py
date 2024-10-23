#################################################################
#                                                               #
# Terminology:                                                  #
#    * Source alphabet S = [s1, s2, s3, ..., sn]                #
#                                                               #
#    * Probabiliy      P = [p1, p2, p3, ..., pn]                #
#      * Prob(si) == pi for each 1 <= i <= n                    #
#      * SUM_i->n(pi) = 1                                       #
#      * p1 >= p2 >= p3 >= ... >= pn                            #
#                                                               #
#    * Codewords       C = [c1, c2, c3, ..., cn]                #
#      * Codewords cost |C| = [|c1|, |c2|, |c3|, ..., |cn|]     #
#      * Encode(si) = ci for each 1 <= i <= n                   #
#                                                               #
#    * Expected codeword length E(C, P) = SUM_i->n(pi * |ci|)   #
#                                                               #
#################################################################
from decimal import Decimal
from tabulate import tabulate

def ECL(P, C):
    """
    return the E(P, C)
    """
    n = len(C)
    return float(sum([Decimal(str(P[i])) * Decimal(str(len(C[i]))) for i in range(n)]))



def example1():
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



def example2():
    headers = ['si',  'p1', 'Code 1', 'Code 2', 'Code 3', 'Code 4']
    table  = [['a' ,   0.5, '0'     , '0'     , '0'     , '0'   ],
              ['b' ,  0.25, '0'     , '1'     , '10'    , '01'  ],
              ['c' , 0.125, '1'     , '00'    , '110'   , '011' ],
              ['d' , 0.125, '10'    , '11'    , '111'   , '0111']]
    n = 4
    P  = [table[i][1] for i in range(n)]
    C1 = [table[i][2] for i in range(n)]
    C2 = [table[i][3] for i in range(n)]
    C3 = [table[i][4] for i in range(n)]
    C4 = [table[i][5] for i in range(n)]

    table.append(['Expected length', '',ECL(P, C1), ECL(P, C2), ECL(P, C3), ECL(P, C4)])
    
    print(tabulate(table, headers=headers, tablefmt="pretty"))



def example3():
    headers = ['si', 'p1', 'Code 3']
    table  = [['a' , 0.67, '0'   ],
              ['b' , 0.11, '100' ],
              ['c' , 0.07, '101' ],
              ['d' , 0.06, '110' ],
              ['e' , 0.05, '1110'],
              ['f' , 0.04, '1111']]
    n = 6
    P  = [table[i][1] for i in range(n)]
    C3 = [table[i][2] for i in range(n)]

    table.append(['Expected length', '',ECL(P, C3)])
    
    print(tabulate(table, headers=headers, tablefmt="pretty"))



def main():
    print("Exmaple from PDF 1 slide 10")
    example1()

    print("Exmaple from PDF 1 slide 12")
    example2()

    print("Example from PDF 1 slide 20")
    example3()


if __name__ == "__main__":
    main()
