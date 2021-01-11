from itertools import permutations
def all_palindromes(str):
    '''This function accepts a string and print all the possible
     palindromes that can be generated using the letters of the string '''
    permut = [] # all possible permutations(list inside list)
    for i in range(1,len(str)):
        permut.append([''.join(j) for j in permutations(str,i)])
    All_possible_words=[]
    Valid_Palindromes = []
    for lists in permut:
        for words in lists:
            All_possible_words.append(words)
    for c in All_possible_words:
        l1 = [i for i in c]
        l2 = l1[::-1]
        if l1==l2:
            Valid_Palindromes.append(c)
    print(f"0.1 {len(set(Valid_Palindromes))}")
    print("0.2",end = " ")
    for c2 in set(Valid_Palindromes):
        print(c2, end = ", ")

all_palindromes('ababcdef')
#code completed
