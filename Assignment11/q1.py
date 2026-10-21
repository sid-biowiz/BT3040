import math

seq = ("LGASGIAAFAFGSTAILIILFNMAAEVHFDPLQFFRQFFWLGLYPPKAQY"
       "GMGIPPLHDGGWWLMAGLFMTLSLGSWWIRVYSRARALGLGTHIAWNFAA"
       "AIFFVLCIGCIHPTLVGSWSEGVPFGIWPHIDWLTAFSIRYGNFYYCPWH"
       "GFSIGFAYGCGLLFAAHGATILAVARFGGDREIEQITDRGTAVERAALFW")

ss = ("XHHHHHHHHHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXX"
      "XXXXXXXXXXHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHXXHHHHHHHH"
      "HHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXHHH"
      "HHHHHHHHHHHHHHHHHHHHHHHXXXXXXXXXXXXXXXXXXXXXXXXXXX")

amino_acids = "ACDEFGHIKLMNPQRSTVWY"


def count_residues(seq, ss):
    total = {}
    helix = {}

    for aa in amino_acids:

        total[aa] = 0
        helix[aa] = 0

    for i in range(len(seq)):
        total[seq[i]] += 1
        if ss[i] == "H":
            helix[seq[i]] += 1

    return total, helix


def propensity(total, helix, N, NH):

    P = {}
    for aa in amino_acids:
        P[aa] = ((helix[aa]/total[aa])/(NH/N))

    return P


def information(total, helix, N, NH):

    I = {}
    background = math.log(NH / (N - NH))
    for aa in amino_acids:
        h = helix[aa]
        not_h = total[aa] - h
        if h == 0:
            I[aa] = -math.inf
        elif not_h == 0:
            I[aa] = math.inf
        else:
            I[aa] = math.log(h / not_h) - background

    return I


N = len(seq)
NH = ss.count("H")
total, helix = count_residues(seq, ss)
P = propensity(total, helix, N, NH)
I = information(total, helix, N, NH)

print("N =", N, " N_H =", NH)
print("aa   n   n_H   P_alpha   I")

for aa in amino_acids:
    print(aa, " ", total[aa], " ", helix[aa], "  %.6f" % P[aa], "  %.6f" % I[aa])