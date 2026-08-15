codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

def dna_clean(dna):
    return dna.replace("T", "U")

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
    return dna[::-1]


def protein_translation(dna):
    protein_list = []
    for j in range(3):
        protein1 = ""
        for i in range(j, len(dna), 3):
            if len(dna[i:i+3]) == 3 :
                protein1 += codon_table[dna[i:i+3]]
        protein_list.append(protein1)

        # protein2 = ""
        # for i in range(len(dna) - j  - 3, -1, -3):
        #     if len(dna[i:i+3]) == 3 :
        #         protein2 += codon_table[dna[i:i+3]]
        # protein_list.append(protein2)

    return protein_list


dna = "GACATTGTGAACAGTAAAAAAGTCCATGCAATGCGCAAGGAGCAGAAGAGGAAGCAGGGCAAGCAGCGCTCCATGGGCTCTCCCATGGACTACTCTCCTCTGCCCATCGACAAGCATGAGCCTGAATTTGGTCCATGCAGAAGAAAACTGGATGGG"
rna = dna_clean(dna)
comp_rna = dna_clean(complementary_dna(dna))

protein = protein_translation(rna)
protein1 = protein_translation(comp_rna)

print(protein)
print(protein1)

