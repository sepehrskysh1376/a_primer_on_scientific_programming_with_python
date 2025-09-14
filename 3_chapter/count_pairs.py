# Count_substr.py actually

def count_pairs(dna, pair):
    """
    Returning the number of occurrences of a sequence of characters in dna string
    """
    c = 0
    pair_ind = 0
    pair_len = len(pair)
    for i in range(len(dna)):
        if dna[i] == pair[pair_ind]:
            pair_ind += 1
        elif dna[i] == pair[0]:
            pair_ind = 1
        else:
            pair_ind = 0
        if pair_ind == pair_len:
            c += 1
            pair_ind = 0

    return c


print(count_pairs("ACTGCTATCCATT", "AT"))
print(count_pairs("ACGTTACGGAACG", "ACG"))
