from tabulate import tabulate

def lzw_encode(T):
    """
    lzw encoder
    Input: text T to encode
    Output: code (list) and table represent the dictionary (tabulate)
    """
    ALPHABET = sorted(list(set(list(T)))) # sort for strinct order..
    D        = {} # dictionary {phrase:code}
    E        = [] # encoding. list of tokens
    table    = [] # presenting the full dictionary D as table (tabulate type)
    
    EOF      = '$'
    T        += EOF # assume '$' doesnt in T

    # Dictionary <- single characters
    for i in range(len(ALPHABET)):
        D[ALPHABET[i]] = i
        table.append([i, ALPHABET[i]])
    
    # w <- first char of input
    w = T[0]
    T = T[1:]

    # repeat
    while (T):
        # k <- next char
        k = T[0]
        T = T[1:]

        # if (EOF)
        if k == EOF:
            # output code(w)
            E.append(D[w])
        
        # else if (w * k) in Dictionary
        elif w+k in D:
            # w <- w * k # (remembe: '*' is concatenation, not mul)
            w = w + k
        
        # else
        else:
            # output code(w)
            E.append(D[w])
            # Dictionary <- w * k
            D[w+k] = len(D)
            table.append([len(D), w+k])
            # w <- k
            w = k
    
    return E, tabulate(table, headers=["code", "phrase"], tablefmt="pretty")



def lzw_decode(E, ALPHABET):
    """
    lzw decoder
    Input: list of codes E and relevant ALPHABET list
    Output: decoded text T and table represent the dictionary (tabulate)
    """
    ALPHABET = sorted(ALPHABET) # sort for strinct order..
    D        = {} # dictionary {code:phrase}
    T        = [] # the decoded text as phrases
    table    = [] # presenting the full dictionary D as table (tabulate type)
    
    # Initialize table with single character strings
    for i in range(len(ALPHABET)):
        D[i] = ALPHABET[i]
        table.append([i, ALPHABET[i]])
    
    # OLD = fisrt input code
    OLD = E[0]
    E = E[1:]

    # output translation of OLD
    T.append(D[OLD])

    # while not end of input stream
    C = ''
    while (E):
        # NEW = next input code
        NEW = E[0]
        E   = E[1:]

        # if NEW is not in the string table
        if NEW not in D:
            # S = translation of OLD
            S = D[OLD]
            # S = S * C # C is first character of S
            S = S + C
        
        # else
        else:
            # S = translation of NEW
            S = D[NEW]
        
        # output S
        T.append(S)
        # C = first character of S
        C = S[0]
        # Translation(OLD) * C to the string table
        D[len(D)] = D[OLD] + C
        table.append([len(D)-1, D[OLD] + C])
        # OLD = NEW
        OLD = NEW

    return T, tabulate(table, headers=["code", "phrase"], tablefmt="pretty")



def example1():
    T = "wabba_wabba_wabba_wabba_woo_woo"
    ALPHABET = list(set(list(T)))
    print("Text: {}, ALPHABET: {}".format(T, ALPHABET))

    # encode
    E, table = lzw_encode(T)
    print(table)
    print("encode({})={}".format(T, E))

    # decode
    T, table = lzw_decode(E, ALPHABET)
    print(table)
    print("decode({})={}".format(E, ''.join(T)))



def example2():
    E = [0,1,3,2,4,7,0,9,10,0]
    ALPHABET = ['a', 'b', 'c']

    # docode
    T, table = lzw_decode(E, ALPHABET)
    print(table)
    print("decode({})={}".format(E, ' '.join(T)))



def main():
    print("Example for PDF 8 slide 11:")
    example1()

    print()

    print("Example for PDF 8 slide 13:")
    example2()



if __name__ == "__main__":
    main()
