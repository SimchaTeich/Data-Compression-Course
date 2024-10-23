def longest_mutch(window, look_ahead):
    """
    find the longest look_ahead prefix in window,
    with the shortest offset.
    Input: window - the string to scan for maching inside it
           look-ahead - the prefix of that string to search for.
    Output: (offset, len)
    """
    mutch = None
    maxlen = 0

    for i in range(len(window)):
        length = 0
        j = i
        for k in range(0, len(look_ahead)):
            if j < len(window) and window[j] == look_ahead[k]:
                length += 1
                j += 1
            else:
                break
        
        if length > 0:
            if length >= maxlen:
                mutch = (i, length)
                maxlen = length
    
    return mutch



def lz77_v0_encode(T):
    """
    LZ77 version 0 encoding - no windows size limit
    return list of tokens
    token looks like (offset, length, simbol)
    """
    textlen = len(T)
    simbol_set = set()
    tokens = []

    p = 0 # partition
    while p < textlen:
        window = T[:p]
        look_ahead = T[p:]

        # new character
        if T[p] not in simbol_set:
            tokens.append((0, 0, T[p]))
            simbol_set.add(T[p])
            p = p + 1
        
        else:
            # search fo longet mutch of look_ahead in window.
            start, length = longest_mutch(window, look_ahead)
            if length < len(look_ahead):
                tokens.append((p-start, length, look_ahead[length]))
            else:
                tokens.append((p-start, length, ''))
            p = p + length + 1
    
    return tokens



def lz77_v0_decode(tokens):
    """
    Input: list of tokens [(offset, length, simbol)]
    Output: the deocded text
    """
    T = ""
    
    p = 0
    for f, l, c in tokens:
        T += T[p-f:p-f+l]
        T += c
        p = p+l+1
    
    return T



def example1():
    T = "A walrus in Spain is a walrus in vain."
    lz77_tokens = lz77_v0_encode(T)
    print("Text: {}".format(T))
    print("Encode: {}".format(lz77_tokens))
    print("Decode: {}".format(lz77_v0_decode(lz77_tokens)))



def example2():
    T = "a" * 100
    lz77_tokens = lz77_v0_encode(T)
    print("Text: {}".format(T))
    print("Encode: {}".format(lz77_tokens))
    print("Decode: {}".format(lz77_v0_decode(lz77_tokens)))



def main():
    print("LZ77 example PDF7 slide 9")
    example1()

    print()

    print("LZ77 example from class")
    example2()



if __name__ == "__main__":
    main()
