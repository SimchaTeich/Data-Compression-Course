from PrettyPrint import PrettyPrintTree
from decimal import Decimal
from tabulate import tabulate

def ECL(P, C):
    """
    return the E(P, C)
    """
    n = len(C)
    return float(sum([Decimal(str(P[i])) * Decimal(str(len(C[i]))) for i in range(n)]))



class BinaryTree:
    def __init__(self, weight, simbol='', left=None, right=None, label=None):
        self.weight = Decimal(str(weight))
        self.simbol = simbol
        self.left = left
        self.right = right
        self.label = label
    
    def children(self):
        ret = []
        if self.left:
            ret.append(self.left)
        if self.right:
            ret.append(self.right)
        return ret
    
    def is_leaf(self):
        return self.left == None and self.right == None
    
    def leaves_simbols(self):
        if self.is_leaf():
            return [self.simbol]
        
        l = self.left
        r = self.right

        if l and r:
            return r.leaves_simbols() + l.leaves_simbols()
        elif l:
            return l.leaves_simbols()
        else:
            return r.leaves_simbols()



def Huffman(S_P):
    """
    Returns the Hemman tree where each leaf is containing symbol and probability, and dictionary
    of simbols as keys and codewords as values.
    The tree can be printed with PrettyPrint library
    input: {simbol: probability}
    output: BinaryTrue, {simbol: (probability, codeword)}
    """
    S_P_C = {s: (p, '') for s, p in S_P.items()}
    
    n = len(S_P)
    Q = [BinaryTree(p,s) for s, p in S_P.items()]

    for _ in range(1, n):
        Q = sorted(Q, key=lambda n: n.weight, reverse=True)
        x = Q.pop()
        y = Q.pop()

        # append '0' to the left of all x leafs
        for s in x.leaves_simbols():
            S_P_C[s] = S_P_C[s][0], '0'+S_P_C[s][1]
        
        # appden '1' to the left of all y leafs
        for s in y.leaves_simbols():
            S_P_C[s] = S_P_C[s][0], '1'+S_P_C[s][1]

        # build the new node
        new_node = BinaryTree(0)
        new_node.weight = x.weight + y.weight
        x.label = '0' # mark the edge
        new_node.left = x
        y.label = '1' # mark the edge
        new_node.right = y

        Q.append(new_node)
    
    return Q.pop(), S_P_C



def Canonical_Huffman(S_L):
    """
    Function calcs the canonical codewords for given the input.
    Input: {simbol:length} # length is optimal because Huffman created it.
    Output: {simbol:(length, canonical_codeword, canonical_code)} & simbol table
    """
    n = len(S_L)
    S = list(S_L.keys())
    L = list(S_L.values())
    maxlength = max(L)

    # find the number of codeword of each length
    num = [0] * maxlength
    for l in L:
        num[l-1] +=1 # indexes starts from 0
    
    # store the first codeword
    firstcode = [0] * maxlength
    for l in range(maxlength-1, 0, -1):
        firstcode[l-1] = (firstcode[l] + num[l])//2 # indexes starts from 0
    
    # init the nextcode
    nextcode = firstcode.copy()

    codeword = [None] * n
    symbol = []
    for i in range(maxlength):
        symbol.append(['']*n)

    # fill the codeword array and the simbol table
    for i in range(1, n+1):
        codeword[i-1] = nextcode[L[i-1]-1]
        symbol[L[i-1]-1][nextcode[L[i-1]-1] - firstcode[L[i-1]-1]] = '{}({})'.format(i, S[i-1])
        nextcode[L[i-1]-1] += 1
    
    # build the code according the codeword number and length needed.
    C = [bin(codeword[i])[2:].zfill(L[i]) for i in range(n)]
    
    return {s:(l, codeword, code) for s,l,codeword,code in zip(S,L,codeword, C)}, symbol



def example1():
    S_P = {'a':0.67, 'b':0.11, 'c':0.07, 'd':0.06, 'e':0.05, 'f':0.04}
    Huffman_tree, S_P_C = Huffman(S_P)

    # print the tree
    pt = PrettyPrintTree(lambda x: x.children(), lambda x: x.simbol+":"+str(x.weight), lambda x: x.label)
    pt(Huffman_tree)

    # print the table
    table = [[s, p, c] for s, (p, c) in S_P_C.items()]
    table.append(['E(P, C)', ECL([p for [_,p,_] in table], [c for [_,_,c] in table])])
    print(tabulate(table, headers=['S', 'P', 'C'], tablefmt="pretty"))



def example2():
    S_P = {'f':0.05, 'e':0.09, 'c':0.12, 'b':0.13, 'd':0.16, 'a':0.45}
    Huffman_tree, S_P_C = Huffman(S_P)

    # print the tree
    pt = PrettyPrintTree(lambda x: x.children(), lambda x: x.simbol+":"+str(x.weight), lambda x: x.label)
    pt(Huffman_tree)

    # print the table
    table = [[s, p, c] for s, (p, c) in S_P_C.items()]
    table.append(['E(P, C)', ECL([p for [_,p,_] in table], [c for [_,_,c] in table])])
    print(tabulate(table, headers=['S', 'P', 'C'], tablefmt="pretty"))



def example3():
    S_P = {'1':0.1, '2':0.15, '3':0.05, '4':0.09, '5':0.14, '6':0.27, '7':0.2}
    Huffman_tree, S_P_C = Huffman(S_P)

    # print the tree
    pt = PrettyPrintTree(lambda x: x.children(), lambda x: x.simbol+":"+str(x.weight), lambda x: x.label)
    pt(Huffman_tree)

    # print the table
    table = [[s, p, c] for s, (p, c) in S_P_C.items()]
    table.append(['E(P, C)', ECL([p for [_,p,_] in table], [c for [_,_,c] in table])])
    print(tabulate(table, headers=['S', 'P', 'C'], tablefmt="pretty"))



def example4():
    S_L = {'a':2, 'b':5, 'c':5, 'd':3, 'e':2, 'f':5, 'g':5, 'h':2}
    S_L_Codeword_Code, simbol_table = Canonical_Huffman(S_L)

    # print the code book:
    table = [[s, l, cw, c] for s, (l, cw, c) in S_L_Codeword_Code.items()]
    print(tabulate(table, headers=['si', 'li', 'codeword[i]', 'Code'], tablefmt="pretty"))

    # print the simbol table:
    print(tabulate(simbol_table ,tablefmt="grid"))



def example5():
    S_P = {'1(a)':0.1, '2(b)':0.15, '3(c)':0.05, '4(d)':0.09, '5(e)':0.14, '6(f)':0.27, '7(g)':0.2}
    _, S_P_C = Huffman(S_P)

    # exstract detais from Huffman algo
    S    = [s for s,(_, _) in S_P_C.items()]
    P    = [p for _,(p, _) in S_P_C.items()]
    Code = [c for _,(_, c) in S_P_C.items()]
    L    = [len(c) for c in Code]

    S_L  =  {s:l for s, l in zip(S, L)}
    S_L_Codeword_Code, _ = Canonical_Huffman(S_L)

    # exstract details from Canonical Huffman algo
    Canonical_Code = [c for _,(_, _, c) in S_L_Codeword_Code.items()]

    # build the summary table
    print(tabulate({'si':S, 'pi':P, 'Code Huffman':Code, 'Canonical Huffman':Canonical_Code}, headers="keys", tablefmt="pretty"))



def main():
    print("Huffman Example PDF 4 slide 4")
    example1()

    print()

    print("Huffman Example PDF 4 slide 10")
    example2()

    print()

    print("Huffman Example PDF 4 slide 14")
    example3()

    print()

    print("Canonical Huffman PDF 4 slide 19")
    example4()

    print()

    print("Canonical Huffman PDF 4 slide 15")
    example5()


if __name__ == "__main__":
    main()
