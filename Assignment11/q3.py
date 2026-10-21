import matplotlib.pyplot as plt

seq3 = ("KVFGRCELAAAMKRHGLDNYRGYSLGNWVCAAKFESNFNTQATNRNTDGSTDYGILQINSRWWCNDGRTPGSRNLCN"
        "IPCSALLSSDITASVNCAKKIVSDGNGMNAWVAWRNRCKGTDVQAWIRGCRL")

P_alpha = {"E": 1.53, "A": 1.45, "L": 1.34, "H": 1.24, "M": 1.20, "Q": 1.17, "W": 1.14, "V": 1.14, "F": 1.12, "K": 1.07, "I": 1.00, "D": 0.98, "T": 0.82, "S": 0.79, "R": 0.79, "C": 0.77, "N": 0.73, "Y": 0.61, "P": 0.59, "G": 0.53}
P_beta = {"M": 1.67, "V": 1.65, "I": 1.60, "C": 1.30, "Y": 1.29, "F": 1.28, "Q": 1.23, "L": 1.22, "T": 1.20, "W": 1.19, "A": 0.97, "R": 0.90, "G": 0.81, "D": 0.80, "K": 0.74, "S": 0.72, "H": 0.71, "N": 0.65, "P": 0.62, "E": 0.26}

helix_score = {"E": 1, "A": 1, "L": 1, "H": 1, "M": 1, "Q": 1, "W": 1, "V": 1, "F": 1, "K": 0.5, "I": 0.5, "D": 0, "T": 0, "S": 0, "R": 0, "C": 0, "N": -1, "Y": -1, "P": -1, "G": -1}
strand_score = {"M": 1, "V": 1, "I": 1, "C": 1, "Y": 1, "F": 1, "Q": 1, "L": 1, "T": 1, "W": 1, "A": 0.5, "R": 0, "G": 0, "D": 0, "K": -1, "S": -1, "H": -1, "N": -1, "P": -1, "E": -1}


def find_segments(seq, P, score, window, cutoff, tail):

    segments = []
    i = 0
    while i <= len(seq) - window:
        s = 0

        for aa in seq[i:i + window]:
            s += score[aa]

        if s >= cutoff:
            end = i + window
            while end < len(seq):
                last = 0
                for aa in seq[end - tail + 1:end + 1]:
                    last += P[aa]
                if last < tail:
                    break
                end += 1
            segments.append([i, end - 1])
            i = end

        else:
            i += 1

    return segments


def total_P(seq, start, end, P):
    s = 0
    for aa in seq[start:end + 1]:
        s += P[aa]
    return s


def final_structure(seq, helices, strands):
    label = ["-"] * len(seq)
    for h in helices:
        for k in range(h[0], h[1] + 1):
            label[k] = "H"
    for st in strands:
        for k in range(st[0], st[1] + 1):
            label[k] = "E"

    print("\nOverlaps:")
    for h in helices:
        for st in strands:
            start = max(h[0], st[0])
            end = min(h[1], st[1])
            if start > end:
                continue
            pa = total_P(seq, start, end, P_alpha)
            pb = total_P(seq, start, end, P_beta)
            winner = "E"
            if pa > pb:
                winner = "H"
            for k in range(start, end + 1):
                label[k] = winner
            print(start + 1, "-", end + 1, seq[start:end + 1],
                  " Pa = %.6f  Pb = %.6f ------->" % (pa, pb), winner)
    return "".join(label)


def segments_of(label, ch):
    segments = []
    i = 0
    while i < len(label):
        if label[i] == ch:
            j = i
            while j + 1 < len(label) and label[j + 1] == ch:
                j += 1
            segments.append([i, j])
            i = j + 1
        else:
            i += 1
    return segments


def show(name, segments, seq):
    print("\n" + name + ":")
    for s in segments:
        print(s[0] + 1, "-", s[1] + 1, seq[s[0]:s[1] + 1])


def plot(helices, strands, label, n):
    tracks = [("Helix", helices, "red"), ("Strand", strands, "blue"),
              ("Final", segments_of(label, "H"), "red"), ("Final", segments_of(label, "E"), "blue")]
    y = {"Helix": 30, "Strand": 20, "Final": 10}
    fig, ax = plt.subplots(figsize=(12, 3))
    for name, segs, colour in tracks:
        bars = []
        for s in segs:
            bars.append((s[0] + 1, s[1] - s[0] + 1))
        ax.broken_barh(bars, (y[name], 6), facecolors=colour)
    ax.set_yticks([13, 23, 33])
    ax.set_yticklabels(["Final", "Strand", "Helix"])
    ax.set_xlim(1, n + 1)
    ax.set_xlabel("Residue number")
    ax.set_title("Chou-Fasman prediction (red = helix, blue = strand)")
    plt.tight_layout()
    plt.savefig("q3_plot.png", dpi=200)
    plt.show()


helices = find_segments(seq3, P_alpha, helix_score, 6, 4, 4)
strands = find_segments(seq3, P_beta, strand_score, 5, 3, 3)
show("Helix segments", helices, seq3)
show("Strand segments", strands, seq3)

label = final_structure(seq3, helices, strands)
show("Final helices", segments_of(label, "H"), seq3)
show("Final strands", segments_of(label, "E"), seq3)
print("\n" + seq3 + "\n" + label)

plot(helices, strands, label, len(seq3))