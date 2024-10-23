from math import log2,ceil
from tabulate import tabulate

def lz78_encode(T):
    """
    lz78 encodeing.
    Input: text T to encode
    Output: a table (list of lists) with the next columns:
            - index of dictionary (not the python dictionary (not the python object))
            - Phrase, the partition of text T
            - Encoding, tuple like (index, symbol)
            - number of bits, that takes to represent the codeword
    """
    ALPHABET        = set(list(T))
    bits_per_symbol = ceil(log2(len(ALPHABET)))
    D               = {'':0}

    #        index  |  phrase  | Encoding  | # of bits
    table = [[D[''] , ''       , None      , None     ]]

    i = 0
    n = len(T)
    while i < n:
        # find the max prefix of text T that exist in dictionary D
        if T and T[:i] in D and T[:i+1] not in D:
            # update table
            table.append([len(D),\
                        T[:i+1],\
                        (D[T[:i]], T[i]),\
                        "{}+{}".format(ceil(log2(len(D))), bits_per_symbol)])
            
            # update dictionary
            D[table[-1][1]] = table[-1][0]
            
            # sliding window moving
            T = T[i+1:]
            i = 0
        else:
            i += 1
    
    return table



def lz78_decode(tokens, bits_per_symbol):
    """
    lz78 decoding.
    Input: tokens and number of bits per symbol.
    Output: a table (list of lists) with the next columns:
            - index of dictionary (not the python dictionary (not the python object))
            - Phrase, the decoded text
            - Encoding (the tokens)
            - number of bits, that takes to represent the codeword
    Note: this table must be the same as in lz78_encode!
    """
    D = {'':0}

    #        index  |  phrase  | Encoding  | # of bits
    table = [[D[''] , ''       , None      , None     ]]

    for index, symbol in tokens:
        # update table
        table.append([len(D),\
                    table[index][1] + symbol,\
                    (index, symbol),\
                    "{}+{}".format(ceil(log2(len(D))), bits_per_symbol)])
            
        # update dictionary
        D[table[-1][1]] = table[-1][0]
    
    return table



def example1():
    T = "badadadabaab"
    ALPHABET        = set(list(T))
    bits_per_symbol = ceil(log2(len(ALPHABET)))
    print("Text: {}, ALPHABET: {}".format(T, ALPHABET))
    
    # encode
    table = lz78_encode(T)
    print(tabulate(table, headers=["index", "Phrase", "Encoding", "# of bits"], tablefmt="pretty"))
    tokens = [row[2] for row in table][1:] # remove the first None
    print("Encoding: {}".format(tokens))
    
    # decode 
    table = lz78_decode(tokens, bits_per_symbol)
    print(tabulate(table, headers=["index", "Phrase", "Encoding", "# of bits"], tablefmt="pretty"))
    phrase = [row[1] for row in table][1:] # remove the first ''
    print("Decoding: {}".format(''.join(phrase)))


def main():
    print("Example for PDF 8 slide 7:")
    example1()



if __name__ == "__main__":
    main()
