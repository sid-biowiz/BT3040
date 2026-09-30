H = {'A': 13.85, 'D': 11.61, 'C': 15.37, 'E': 11.38, 'F': 13.93, 'G': 13.34, 'H': 13.82,
     'I': 15.28, 'K': 11.58, 'L': 14.13, 'M': 13.86, 'N': 13.02, 'P': 12.35, 'Q': 12.61,
     'R': 13.10, 'S': 13.39, 'T': 12.70, 'V': 14.56, 'W': 15.48, 'Y': 13.88}

HELIX = ["00110011", "11001100"]
STRAND = ["010101", "101010"]

headers = []
seqs = []
for line in open("q1.fasta"):
    line = line.strip()
    if line.startswith(">"):
        headers.append(line[1:])
        seqs.append("")
    elif line != "":
        seqs[-1] += line


def helix_index(s):
    a1 = (H[s[0]] + H[s[4]]) / 2
    a2 = (H[s[1]] + H[s[5]]) / 2
    a3 = (H[s[2]] + H[s[6]]) / 2
    a4 = (H[s[3]] + H[s[7]]) / 2
    return abs((a1 + a2) - (a3 + a4))


def strand_index(s):
    b1 = (H[s[0]] + H[s[2]] + H[s[4]]) / 3
    b2 = (H[s[1]] + H[s[3]] + H[s[5]]) / 3
    return abs(b1 - b2)


for k in range(len(seqs)):
    seq = seqs[k]
    avg = 0
    for c in seq:
        avg += H[c]
    avg = avg / len(seq)

    binary = ""
    for c in seq:
        binary += "1" if H[c] >= avg else "0"

    print("Sequence", k + 1)
    found = 0
    for i in range(len(seq) - 7):
        if binary[i:i + 8] in HELIX:
            print("Helix of length 8 found at position", i + 1,
                  "with amphipathicity", round(helix_index(seq[i:i + 8]), 3))
            found += 1
    if found == 0:
        print("No helices of length 8 were found")

    found = 0
    for i in range(len(seq) - 5):
        if binary[i:i + 6] in STRAND:
            print("Strand of length 6 found at position", i + 1,
                  "with amphipathicity", round(strand_index(seq[i:i + 6]), 3))
            found += 1
    if found == 0:
        print("No strands of length 6 were found")
    print()