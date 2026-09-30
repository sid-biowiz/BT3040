import re

#using regex for q5 on q4 fasta seq
patterns = {
    "A  [SV]-T-[VT]-[DERK](2)-{IL}": "(?=([SV]T[VT][DERK]{2}[^IL]))",
    "B  [FILV]Qxxx{RK}Gxxx[RK]xx[FILVWY]": "(?=([FILV]Q...[^RK]G...[RK]..[FILVWY]))",
}

headers = []
seqs = []
for line in open("q4.fasta"):
    line = line.strip()
    if line.startswith(">"):
        headers.append(line[1:])
        seqs.append("")
    elif line != "":
        seqs[-1] += line

for name in patterns:
    print("Pattern", name)
    count = 0
    for k in range(len(seqs)):
        for m in re.finditer(patterns[name], seqs[k]):
            count += 1
            print(" ", headers[k], " position", m.start() + 1, m.group(1))
    print("Total matches =", count)
    print()