import matplotlib.pyplot as plt

H = {'A': 13.85, 'D': 11.61, 'C': 15.37, 'E': 11.38, 'F': 13.93, 'G': 13.34, 'H': 13.82,
     'I': 15.28, 'K': 11.58, 'L': 14.13, 'M': 13.86, 'N': 13.02, 'P': 12.35, 'Q': 12.61,
     'R': 13.10, 'S': 13.39, 'T': 12.70, 'V': 14.56, 'W': 15.48, 'Y': 13.88}

#basically after serializing Ie just look for this combination while running a window through the loop
HELIX = ["1100", "0011"]    
STRAND = ["1010", "0101"]   #taken 4 because in q2 its 8/6


def read_fasta(filename):
    headers = []
    seqs = []
    for line in open(filename):
        line = line.strip()
        if line == "":
            continue
        if line.startswith(">"):
            headers.append(line[1:])
            seqs.append("")
        else:
            seqs[-1] += line
    return headers, seqs

#returning alpha/beta positions
def find_stretches(binary, patterns):
    positions = set()
    n = len(patterns[0])
    for i in range(len(binary) - n + 1):
        if binary[i:i + n] in patterns:
            for j in range(i, i + n):
                positions.add(j)

    return positions


def to_ranges(positions):
    ranges = []
    for p in sorted(positions):
        if ranges and p == ranges[-1][1] + 1:
            ranges[-1][1] = p
        else:
            ranges.append([p, p])
    return [str(a + 1) + "-" + str(b + 1) for a, b in ranges]   #1based indexing


headers, seqs = read_fasta("q1.fasta")
fig, ax = plt.subplots(len(seqs), 1, figsize=(10, 3.5 * len(seqs)), squeeze=False)

for k in range(len(seqs)):
    seq = seqs[k]
    profile = [H[c] for c in seq]
    avg = sum(profile) / len(profile)
    binary = ""
    for v in profile:
        binary += "1" if v >= avg else "0"

    helix = find_stretches(binary, HELIX)
    strand = find_stretches(binary, STRAND)

    print("Sequence", k + 1, ":", headers[k])
    print("Average hydrophobicity =", round(avg, 2))
    print("Helix residues :", to_ranges(helix))
    print("Strand residues:", to_ranges(strand))
    print()

    a = ax[k][0]
    x = range(1, len(seq) + 1)
    a.plot(x, profile, "k-o", markersize=3)
    a.axhline(avg, color="grey", ls="--")
    for p in helix:
        a.axvspan(p + 0.5, p + 1.5, color="blue", alpha=0.3)
    for p in strand:
        a.axvspan(p + 0.5, p + 1.5, color="red", alpha=0.3)
    a.set_title("Sequence " + str(k + 1) + " (blue = helix, red = strand)")
    a.set_xlabel("Residue number")
    a.set_ylabel("Hydrophobicity")

plt.tight_layout()
plt.savefig("q1_profile.png", dpi=200)
plt.show()