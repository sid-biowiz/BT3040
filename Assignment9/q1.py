amino_acids = "ACDEFGHIKLMNPQRSTVWY"

seq1 = "AMENLNMDLLYMAAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA"
seq2 = "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"
seq3 = "MALLPAAPGAPARATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA"

def composition(seq):
    comp = []
    for aa in amino_acids:
        comp.append(100 * seq.count(aa) / len(seq))
    return comp

def hamming(seq_a, seq_b):
    comp_a = composition(seq_a)
    comp_b = composition(seq_b)
    dist = 0
    for i in range(20):
        dist += abs(comp_a[i] - comp_b[i])
    return dist

def euclidean(seq_a, seq_b):
    comp_a = composition(seq_a)
    comp_b = composition(seq_b)
    dist = 0
    for i in range(20):
        dist += (comp_a[i] - comp_b[i]) ** 2
    return dist ** 0.5

pairs = [("seq1 and seq2", seq1, seq2),
         ("seq1 and seq3", seq1, seq3),
         ("seq2 and seq3", seq2, seq3)]

print("Pair             Hamming    Euclidean")
ham_scores = []
euc_scores = []
for name, a, b in pairs:
    h = hamming(a, b)
    e = euclidean(a, b)
    ham_scores.append(h)
    euc_scores.append(e)
    print(f"{name}   {h:8.4f}   {e:8.4f}")

print()
print("Closest pair (Hamming):  ", pairs[ham_scores.index(min(ham_scores))][0])
print("Closest pair (Euclidean):", pairs[euc_scores.index(min(euc_scores))][0])