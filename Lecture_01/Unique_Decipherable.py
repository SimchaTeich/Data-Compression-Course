#################################################################
#                                                               #
# Terminology:                                                  #
#    * UD Code is any given sequence of codewords can be        #
#      decoded in a single way                                  #
#                                                               #
#    * Let 'a' and 'b' be two binary codewords where |'a'|=k    #
#      bits and |'b'|=n bits, k<n. If the first k bits of 'b'   #
#      are identical to 'a' then 'a' is called a PREFFIX of     #
#      'b'. The last n - k bits are called the DANGLING SUFFIX. #
#                                                               #
#      * Example: a=010, b=01011, dangling-sufffix=11           #
#                                                               #
#    * UD Test is an algorithm to test if given C is a UD Code  #
#      * Examine all pairs of codewords:                        #
#        1. Construct a list of all codewords.                  #
#        2. If there exist a codeword, 'a', witch is a preffix  #
#           of another codeword, 'b', add the dangling suffix   #
#           to the list (if it is not there already), until:    #
#           I. You get a dangling suffix that is an ORIGINAL    #
#              codeword --> the code is not UD                  #
#           II. There are no more unique dangling suffix -->    #
#               the code is UD                                  #
#################################################################

def dangling_suffix(c1, c2):
    """
    Return the dangling suffix of c1 and c2. (order does matter)
    """
    if c1 == c2[:len(c1)]:
        return c2[len(c1):]
    else:
        return None



def left_quotient(S, T):
    """
    Return the left quotient group of two groups (order does matter)
    """
    ret = set()

    for s in S:
        for t in T:
            dangling = dangling_suffix(s,t)
            if dangling:
                ret.add(dangling)
    
    return list(ret)



def UD_test(C):
    """
    Run the Sardinas-Patterson algorithm for UD test
    Return: True if the given codeword list C is UD,
            or False if C isn't UD
    """
    print("List: ", C)
    S = [None] # S[1], S[2]... are dangling list (from index 1, not 0)

    S.append(left_quotient(C, C))
    i = 1
    print("List: ", S[i])
    while True:
        S.append(list(set(left_quotient(C,S[i]) + left_quotient(S[i], C))))
        i += 1
        print("List: ", S[i])

        for c in C:
            if c in S[i]:
                return False
        
        if set(S[i]) == set(S[i-1]):
            return True



def example1():
    C = ['0', '01', '11']
    if UD_test(C):
        print("UD")
    else:
        print("Not UD")



def example2():
    C = ['0', '01', '10']
    if UD_test(C):
        print("UD")
    else:
        print("Not UD")



def example3():
    C = ['01', '10', '0', '11']
    if UD_test(C):
        print("UD")
    else:
        print("Not UD")



def main():
    print("Exmaple from PDF 1 slide 17")
    example1()

    print("Exmaple from PDF 1 slide 18")
    example2()

    print("Exmaple of student in the class")
    example3()



if __name__ == "__main__":
    main()
