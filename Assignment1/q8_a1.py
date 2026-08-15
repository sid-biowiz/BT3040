avg_base_energy = {
    "AA": -4, "AT": -7, "AC": -5, "AG": -11, "TA": -7, "TT": -2, "TC": -3, "TG": -4,"CA": -9,"CT": -5, "CC": -6, "CG": -7, "GA": -9, "GT": -6, "GC": -4, "GG": -11,
}

def base_stacking(dna):
    energy = 0
    for i in range(len(dna) - 1):
        energy += avg_base_energy[dna[i:i + 2]]
    return energy

dna = "CTCGGATTTGTAAAGATCATGATCTCATACATAGTACCTAGCCA"
total_energy = base_stacking(dna)
stacking_energy = base_stacking(dna)/(len(dna) - 1)
print("Total energy for the given DNA sequence:", total_energy)
print("The average base stacking energy for the given dna sequence is:", stacking_energy)