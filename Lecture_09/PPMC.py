
from tabulate import tabulate

def init_table(K_max):
    table = [{'':{'$':0}}]
    for _ in range(1, K_max+1):
        table.append({})
    return table



def append_symbol_to_table(text, table, s):
    """
    text
    Table table - [{contex:{symbol:count}}]
    symbol s
    """
    for i in range(len(table)):
        context = '' if i == 0 else text[-i:]
        
        if context in table[i]:
            if s in table[i][context]:
                table[i][context][s] += 1
            else:
                table[i][context][s] = 1
                table[i][context]['$'] += 1
        elif len(context) == i:
            table[i][context] = {s:1, '$':1}
    
    return table



def encode_symbol(text, table, s):
    """
    text
    Table table - [{contex:{symbol:count}}]
    symbol s
    """
    e = []
    for k in range(len(table)-1,-2,-1):
        if k == -1:
            e.append((s, k))
            break

        context = '' if k == 0 else text[-k:]

        if context in table[k]:
            if s in table[k][context]:
                e.append((s, k))
                break
            else:
                e.append(('$', k))
        else:
            e.append(('$', k))
    
    return e


def encode(text, K_max):
    """
    PPMC Encoding
    Input: text to encode and K-max
    Output: encoded text, current table of ppm and table (tabulate) for encoding
    """
    output_table = []
    encoded_text = ""

    table = init_table(K_max)
    for i in range(len(text)):
        
        # encode
        e = encode_symbol(text[:i], table, text[i])
        output_table += e
        encoded_text += "".join([symbol for symbol,_ in e])
        
        # update table
        table = append_symbol_to_table(text[:i], table, text[i])
    
    return encoded_text, table, tabulate(output_table, headers=["Encoded symbol", "Order"], tablefmt="pretty")



def example1():
    K_max = 2
    table = init_table(K_max)
    text = "ACCBACCACBA"
    for i in range(len(text)):
        table = append_symbol_to_table(text[:i], table, text[i])

    print(table)



def example2():
    K_max = 2
    table = init_table(K_max)
    text = "saccessors"
    for i in range(len(text)):
        table = append_symbol_to_table(text[:i], table, text[i])

    print(table)



def example3():
    K_max = 2
    text = "abracadabra"
    encoded_text, _, output_table = encode(text, K_max)
    print(output_table)
    print("Encoded text: {}".format(encoded_text))



def example4():
    K_max = 2
    text = "aabbaabb"
    encoded_text, _, output_table = encode(text, K_max)
    print(output_table)
    print("Encoded text: {}".format(encoded_text))



def example5():
    K_max = 2
    text = "abracadabra"
    _, inisde_table, _ = encode(text, K_max)
    print(inisde_table)



def example6():
    K_max = 1
    text = "aabb"
    encoded_text, _, output_table = encode(text, K_max)
    print(output_table)
    print("Encoded text: {}".format(encoded_text))


def example7():
    K_max = 1
    text = "aabb"
    _, inisde_table, _ = encode(text, K_max)
    print(inisde_table)



def example8():
    K_max = 1
    text = "aabbc"
    encoded_text, inisde_table, _ = encode(text, K_max)
    print("Encoded text: {}".format(encoded_text))
    print(inisde_table)



def main():
    print("Example for PDF 9 slide 15:")
    example1()

    print()
    
    print("Example from final exam q4-1:")
    example2()

    print()
    
    print("Example from PDF 9 slide 16:")
    example3()

    print()
    
    print("Example from PDF 9 slide 18:")
    example4()

    print()

    print("Example from PDF 9 slide 19:")
    example5()

    print()

    print("Example from PDF 9 slide 20:")
    example6()

    print()

    print("Example from PDF 9 slide 25:")
    example7()

    print()

    print("Example from PDF 9 slide 27:")
    example8()

if __name__ == "__main__":
    main()
