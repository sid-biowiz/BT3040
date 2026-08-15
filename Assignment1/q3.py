dna_code = {
    "A": 'T',
    "T": 'A',
    "G": 'C',
    "C": 'G',
}


def complementary_dna(dna):
    dna_lister = list(dna)
    for i in range(len(dna)):
        dna_lister[i] = dna_code[dna_lister[i]]

    dna = "".join(dna_lister)
    return dna


dna = "CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCA"
ans = complementary_dna(dna)
print(ans)