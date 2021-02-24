def distance(strand_a, strand_b):
    hamming_distance = 0
    a_len = len(strand_a)
    b_len = len(strand_b)

    if a_len != b_len:
        raise ValueError("Strands are not of equal length.")
    else:
        for i in range(a_len):
            letter_in_strand_a = strand_a[i]
            letter_in_strand_b = strand_b[i]
            lettersAreEqual = letter_in_strand_a == letter_in_strand_b
            hamming_distance = (hamming_distance + 1) if not lettersAreEqual else hamming_distance
            
    return hamming_distance



