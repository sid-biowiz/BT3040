Hgm = {"A": 13.85, "D": 11.61, "C": 15.37, "E": 11.38, "F": 13.93,
    "G": 13.34, "H": 13.82, "I": 15.28, "K": 11.58, "L": 14.13,
    "M": 13.86, "N": 13.02, "P": 12.35, "Q": 12.61, "R": 13.10,
    "S": 13.39, "T": 12.70, "V": 14.56, "W": 15.48, "Y": 13.88}

Ca = {"A": 20.0, "D": 26.0, "C": 25.0, "E": 33.0, "F": 46.0,
    "G": 13.0, "H": 37.0, "I": 39.0, "K": 46.0, "L": 35.0,
    "M": 43.0, "N": 28.0, "P": 22.0, "Q": 36.0, "R": 55.0,
    "S": 20.0, "T": 28.0, "V": 33.0, "W": 61.0, "Y": 46.0}

Et = {"A": 1.90, "D": 1.52, "C": 2.04, "E": 1.54, "F": 1.86,
    "G": 1.90, "H": 1.76, "I": 1.95, "K": 1.37, "L": 1.97,
    "M": 1.96, "N": 1.56, "P": 1.70, "Q": 1.52, "R": 1.48,
    "S": 1.75, "T": 1.77, "V": 1.98, "W": 1.87, "Y": 1.69}

set1 = "RATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA"
set2 = "AAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA"
set3 = "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"

def compute(seq):
    n = len(seq)
    tot_hgm = 0
    ca = 0
    et = 0
    for i in range(n):
        tot_hgm += Hgm[seq[i]]
        ca += Ca[seq[i]]
        et += Et[seq[i]]

    hgm = tot_hgm / n

    return hgm, ca, et


hgm1, ca1, et1 = compute(set1)
print("For set1, the Average Hydrophobicity is: ", hgm1)
print("For set1, the Helical Contact Area is: ", ca1)
print("For set1, the Total Non-Bonded Energy is: ", et1)
print()

hgm2, ca2, et2 = compute(set2)
print("For set2, the Average Hydrophobicity is: ", hgm2)
print("For set2, the Helical Contact Area is: ", ca2)
print("For set2, the Total Non-Bonded Energy is: ", et2)
print()

hgm3, ca3, et3 = compute(set3)
print("For set3, the Average Hydrophobicity is: ", hgm3)
print("For set3, the Helical Contact Area is: ", ca3)
print("For set3, the Total Non-Bonded Energy is: ", et3)