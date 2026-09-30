import re
from Bio import SeqIO
filepath = r'D:\BT3040\Assignment8\Q4.fasta'

#using regex for q5 on q4 fasta seq
patterns = {
    "A  [SV]-T-[VT]-[DERK](2)-{IL}": "(?=([SV]T[VT][DERK]{2}[^IL]))",
    "B  [FILV]Qxxx{RK}Gxxx[RK]xx[FILVWY]": "(?=([FILV]Q...[^RK]G...[RK]..[FILVWY]))",
}

records = list(SeqIO.parse(filepath, "fasta-pearson"))

for name in patterns:
    print("Pattern", name)
    count = 0
    for k in range(len(records)):
        for m in re.finditer(patterns[name], str(records[k].seq)):
            count += 1
            print(" ", records[k].description, " position", m.start() + 1, m.group(1))
    print("Total matches =", count)
    print()