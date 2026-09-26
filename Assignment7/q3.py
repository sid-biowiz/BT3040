aa_code = {
    'A': 'Ala',
    'C': 'Cys',
    'D': 'Asp',
    'E': 'Glu',
    'F': 'Phe',
    'G': 'Gly',
    'H': 'His',
    'I': 'Ile',
    'K': 'Lys',
    'L': 'Leu',
    'M': 'Met',
    'N': 'Asn',
    'P': 'Pro',
    'Q': 'Gln',
    'R': 'Arg',
    'S': 'Ser',
    'T': 'Thr',
    'V': 'Val',
    'W': 'Trp',
    'Y': 'Tyr'
}

group_A = {
    'Ala': 8.47,
    'Asp': 5.97,
    'Cys': 1.39,
    'Glu': 6.32,
    'Thr': 5.79,
    'Phe': 3.91,
    'Gly': 7.82,
    'His': 2.26,
    'Ile': 5.71,
    'Val': 7.02,
    'Lys': 5.76,
    'Leu': 8.48,
    'Met': 2.21,
    'Asn': 4.54,
    'Trp': 1.44,
    'Pro': 4.63,
    'Gln': 3.82,
    'Arg': 4.93,
    'Ser': 5.94,
    'Tyr': 3.58
}

group_B = {
    'Ala': 8.95,
    'Asp': 5.91,
    'Cys': 0.47,
    'Glu': 4.78,
    'Thr': 6.54,
    'Phe': 3.68,
    'Gly': 8.54,
    'His': 1.25,
    'Ile': 4.77,
    'Val': 6.76,
    'Lys': 4.93,
    'Leu': 8.78,
    'Met': 1.56,
    'Asn': 5.74,
    'Trp': 1.24,
    'Pro': 3.74,
    'Gln': 4.75,
    'Arg': 5.24,
    'Ser': 8.05,
    'Tyr': 4.13
}

set1 = "RATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA"
set2 = "AAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA"
set3 = "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"

def aa_comp(set1):
    aa_set = "ACDEFGHIKLMNPQRSTVWY"

    aa_dict = {}

    for aa in aa_set:
        aa_dict[aa] = 0
        for i in range(len(set1)):
            if aa == set1[i]:
                aa_dict[aa] += 1

    for aa in aa_set:
        aa_dict[aa] = (aa_dict[aa]/len(set1))*100

    return aa_dict

aa_set = "ACDEFGHIKLMNPQRSTVWY"

def compare(set1):
    aa_dict1 = aa_comp(set1)
    Ascore = 0
    Bscore = 0
    for aa in aa_set:
        Ascore += abs(aa_dict1[aa] - group_A[aa_code[aa]])
        Bscore += abs(aa_dict1[aa] - group_B[aa_code[aa]])

    if Ascore < Bscore:
        print("Group A is the closer in terms of AA composition")

    else:
        print("Group B is the closer in terms of AA composition")

compare(set1)
compare(set2)
compare(set3)
    