def print_matrix(M):
    for line in M:
        print(" ".join(list(line)))


def BWT(T):
    matrix = []
    for i in range(len(T)):
        matrix.append(T[i:]+T[:i])
    
    print("Stage 1: matrix")
    print_matrix(matrix)

    print()

    print("Stage 2: sorting")
    matrix = sorted(matrix)
    print_matrix(matrix)

    print()

    print("Stage 3: find index")
    index = matrix.index(T)
    L     = ''.join([line[-1] for line in matrix])
    print("BWT({})=({}, {})".format(T, L, index))

    return L, index


def MTF(T):
    """
    MTF-List: start with sorted alphabet of T
    """
    MTF_List  = sorted(list(set(list(T))))
    code_list = []

    print("MTF-List: {}".format(''.join(MTF_List)))
    for t in T:
        index = MTF_List.index(t)
        code_list.append(index)
        MTF_List.remove(t)
        MTF_List.insert(0, t)
        print("MTF-List: {}".format(''.join(MTF_List)))
    
    print("MTF({})={}".format(T, code_list))
    return code_list



text = "banana"
BWT(text)


print('----------------------')


text = "mississippi"
BWT(text)


print('----------------------')


text = "helloworld"
MTF(text)


print('----------------------')

text = "mississippi"
L, index = BWT(text)
MTF(L)



    