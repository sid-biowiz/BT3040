aa_set = "ACDEFGHIKLMNPQRSTVWY"

set1 = "RATPTRWPVGCFNRPWTKWSYDEALDGIKAAGYAWTGLLTASKPSLHHATATPEYLAALKQKSRHAA"
set2 = "AAAVMMGLAAIGAAIGIGILGGKFLEGAARQPDLIPLLRTQFFIVMGLVDAIPMIAVGLGLYVMFAVA"
set3 = "AADVSAAVGATGQSGMTYRLGLSWDWDKSWWQTSTGRLTGYWDAGYTYWEGGDEGAGKHSLSFAPVFVYEFAGDSIKPFIEAGIGVAAFSGTRVGDQNLGSSLNFEDRIGAGLKFANGQSVGVRAIHYSNAGLKQPNDGIESYSLFYKIPI"

aa_dict1 = {}
aa_dict2 = {}
aa_dict3 = {}


for aa in aa_set:
    aa_dict1[aa] = 0
    for i in range(len(set1)):
        if aa == set1[i]:
            aa_dict1[aa] += 1

for aa in aa_set:
    aa_dict2[aa] = 0
    for i in range(len(set2)):
        if aa == set2[i]:
            aa_dict2[aa] += 1

for aa in aa_set:
    aa_dict3[aa] = 0
    for i in range(len(set3)):
        if aa == set3[i]:
            aa_dict3[aa] += 1

for aa in aa_set:
    aa_dict1[aa] = (aa_dict1[aa]/len(set1))*100
    aa_dict2[aa] = (aa_dict2[aa]/len(set2))*100
    aa_dict3[aa] = (aa_dict3[aa]/len(set3))*100

print("Amino Acid Frequency for Set1: ", aa_dict1)
print("Amino Acid Frequency for Set2: ", aa_dict2)
print("Amino Acid Frequency for Set3: ", aa_dict3)


