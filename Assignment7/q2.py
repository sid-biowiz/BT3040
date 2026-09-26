aa_weight = {
    'A': 85,  'C': 115, 'D': 130, 'E': 145, 'F': 160,
    'G': 70,  'W': 200, 'H': 150, 'I': 125, 'K': 145,
    'L': 125, 'M': 143, 'N': 130, 'Y': 175, 'P': 110,
    'Q': 140, 'R': 170, 'S': 100, 'T': 115, 'V': 110
}

set1 = "RATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA"
set2 = "AAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA"
set3 = "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"

molweight1 = 0
for i in range(len(set1)):
    molweight1 += aa_weight[set1[i]]

molweight2 = 0
for i in range(len(set2)):
    molweight2 += aa_weight[set2[i]]

molweight3 = 0
for i in range(len(set3)):
    molweight3 += aa_weight[set3[i]]

print("Molecular Weight of Set1 Sequence: ", molweight1)
print("Molecular Weight of Set1 Sequence: ", molweight2)
print("Molecular Weight of Set1 Sequence: ", molweight3)