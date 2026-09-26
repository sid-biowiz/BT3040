import numpy as np

amino_acids = list("ACDEFGHIKLMNPQRSTVWY")


def compute(seq):

    n = len(seq)
    aa_freq = {}

    for aa in amino_acids:
        aa_freq[aa] = seq.count(aa)

    pair_freq = {}

    for aa1 in amino_acids:
        pair_freq[aa1] = {}
        for aa2 in amino_acids:
            pair_freq[aa1][aa2] = 0

    #pair counting
    for i in range(n - 1):
        aa1 = seq[i]
        aa2 = seq[i + 1]
        pair_freq[aa1][aa2] += 1

    pref_a = np.zeros((20, 20))
    pref_b = np.zeros((20, 20))
    pref_c = np.zeros((20, 20))

    for i, aa1 in enumerate(amino_acids):
        for j, aa2 in enumerate(amino_acids):
            nij = pair_freq[aa1][aa2]
            ni = aa_freq[aa1]
            nj = aa_freq[aa2]

            if ni + nj != 0:
                pref_a[i][j] = nij * 100 / (ni + nj) #a

            pref_b[i][j] = nij * 100 / (n - 1) #b

            if ni * nj != 0:
                pref_c[i][j] = nij * 100 / (ni * nj) #c

    return pair_freq, pref_a, pref_b, pref_c


def top_10(matrix):
    pairs = []
    for i in range(20):
        for j in range(20):
            pair = amino_acids[i] + amino_acids[j]
            value = matrix[i][j]
            pairs.append((pair, value))

    #sorting
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            if pairs[j][1] > pairs[i][1]:
                temp = pairs[i]
                pairs[i] = pairs[j]
                pairs[j] = temp

    return pairs[:10]


set1 = "RATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA"
set2 = "AAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA"
set3 = "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"


for number, seq in enumerate([set1, set2, set3], 1):
    pair_freq, a, b, c = compute(seq)
    print("SEQUENCE", number)

    print("\nNij matrix:")
    print("    ", " ".join(f"{aa:>5}" for aa in amino_acids))

    for i, aa in enumerate(amino_acids):
        print(
            f"{aa:>3} ",
            " ".join(f"{pair_freq[aa][bb]:5}" for bb in amino_acids)
        )

    print("\nPreference (a):")
    print(a)

    print("\nPreference (b):")
    print(b)

    print("\nPreference (c):")
    print(c)

    print("\nTop 10 pairs for preference (a):")
    print(top_10(a))

    print("\nTop 10 pairs for preference (b):")
    print(top_10(b))

    print("\nTop 10 pairs for preference (c):")
    print(top_10(c))