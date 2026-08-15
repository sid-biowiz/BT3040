def matches(dna, subdna):
    match = 0
    position = []
    for i in range(len(dna)):
        for j in range(len(subdna)):
            if i + j <= len(dna) - 1 and subdna[j] == dna[i + j]:
                if j == len(subdna) - 1:
                    position.append(i)
                    match += 1
                else:
                    continue
            else:
                break

    return match, position

dna = "GACATTGTGAACAGTAAAAAAGTCCATGCAATGCGCAAGGAGCAGAAGAGGAAGCAGGGCAAGCAGCGCTCCATGGGCTCTCCCATGGACTACTCTCCTCTGCCCATCGACAAGCATGAGCCTGAATTTGGTCCATGCAGAAGAAAACTGGATGGG"
n_substr = input("Enter the number of strings you want to add:")
for i in range(int(n_substr)):
    subdna = input("Enter a String:")
    tot_match, pos = matches(dna, subdna)
    print("Total Matches:", tot_match)
    print("Position of Match:", pos)

# subdna = input("Enter a String:")
# tot_match, pos = matches(dna, subdna)





