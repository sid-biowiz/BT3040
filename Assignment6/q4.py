import math
aa = "ACDEFGHIKLMNPQRSTVWY"

def read_aln(file):
    seqs = {}
    name = ""
    for line in open(file):
        if line.startswith(">"):
            name = line[1:].split()[0]
            seqs[name] = ""
        elif name != "":
            seqs[name] += line.strip()
        elif line[0] not in " \n":
            parts = line.split()
            seqs[parts[0]] = seqs.get(parts[0], "") + parts[1]
    return seqs


def read_blosum(file):
    blosum = {}
    for line in open(file):
        row = line.split()
        if line[0] == "#" or row == []:
            continue
        if line[0] == " ":
            cols = row
        else:
            for j in range(len(cols)):
                blosum[row[0] + cols[j]] = float(row[j + 1])
    return blosum


#q4
def scores(msa, blosum):
    allres = "".join(msa)
    n = len(allres) - allres.count("-")
    bg = {}
    for a in aa:
        bg[a] = allres.count(a) / n

    result = []
    for i in range(len(msa[0])):
        col = [s[i] for s in msa if s[i] != "-"]
        f = {}
        for a in set(col):
            f[a] = col.count(a) / len(col)

        ent = 0
        sop = 0
        for a in f:
            ent += f[a] * math.log(f[a])
            for b in f:
                sop += f[a] * f[b] * blosum[a + b]

        var = 0
        for a in aa:
            var += (f.get(a, 0) - bg[a]) ** 2

        result.append([i + 1, msa[0][i], round(ent, 3), round(math.sqrt(var), 3), round(sop, 3)])
    return result


# Q5
def entropy_per_residue(file, ref):
    seqs = read_aln(file)
    ent = []
    for r in scores(list(seqs.values()), blosum):
        if seqs[ref][r[0] - 1] != "-":
            ent.append(r[2])
    return ent


def compare(clustal_file, mafft_file, muscle_file):
    ref = list(read_aln(clustal_file))[0]
    c = entropy_per_residue(clustal_file, ref)
    m = entropy_per_residue(mafft_file, ref)
    u = entropy_per_residue(muscle_file, ref)

    same = 0
    for i in range(len(c)):
        if c[i] == m[i] == u[i]:
            same += 1
        else:
            print("residue", i + 1, ":", c[i], m[i], u[i])
    print("same:", same, "/", len(c))


blosum = read_blosum("BLOSUM62")

set1 = list(read_aln("set1_clustal.aln-clustal_num").values())
set2 = list(read_aln("set2_clustal.aln-clustal_num").values())

print("Set 1")
for r in scores(set1, blosum)[:10]:
    print(r)
print("Set 2")
for r in scores(set2, blosum)[:10]:
    print(r)

print("\nQ5 Set 1")
compare("set1_clustal.aln-clustal_num", "set1_mafft.aln-fasta", "set1_muscle.aln-clustalw")
print("\nQ5 Set 2")
compare("set2_clustal.aln-clustal_num", "set2_mafft.aln-fasta", "set2_muscle.aln-clustalw")
