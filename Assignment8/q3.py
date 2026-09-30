import matplotlib.pyplot as plt

H = {'A': 13.85, 'D': 11.61, 'C': 15.37, 'E': 11.38, 'F': 13.93, 'G': 13.34, 'H': 13.82,
     'I': 15.28, 'K': 11.58, 'L': 14.13, 'M': 13.86, 'N': 13.02, 'P': 12.35, 'Q': 12.61,
     'R': 13.10, 'S': 13.39, 'T': 12.70, 'V': 14.56, 'W': 15.48, 'Y': 13.88}
MIN_LEN = 10   # shortest stretch above the avg is counted as an TM segment

seq = ""
for line in open("Q2.fasta"):
    if not line.startswith(">"):
        seq += line.strip()


def window_profile(seq, w):
    x = []
    y = []
    for i in range(len(seq) - w + 1):
        total = 0
        for c in seq[i:i + w]:
            total += H[c]
        x.append(i + w // 2 + 1)        #from center residue, 1based indexing
        y.append(total / w)
    return x, y


def tm_segments(x, y, cutoff):
    segs = []
    start = None
    for i in range(len(y)):
        if y[i] > cutoff and start is None:
            start = i
        if (y[i] <= cutoff or i == len(y) - 1) and start is not None:
            end = i if y[i] > cutoff else i - 1
            if end - start + 1 >= MIN_LEN:
                segs.append((x[start], x[end]))
            start = None
    return segs


fig, ax = plt.subplots(2, 1, figsize=(10, 7))
for k, w in enumerate([9, 19]):
    x, y = window_profile(seq, w)
    avg = sum(y) / len(y)
    segs = tm_segments(x, y, avg)

    print("Window", w, "| cutoff (average) =", round(avg, 2))
    for s in segs:
        print("  TM segment:", s[0], "-", s[1], seq[s[0] - 1:s[1]])
    print()

    ax[k].plot(x, y, "k-", lw=1)
    ax[k].axhline(avg, color="grey", ls="--")
    for s in segs:
        ax[k].axvspan(s[0], s[1], color="orange", alpha=0.4)
    ax[k].set_title("Window length " + str(w))
    ax[k].set_xlabel("Residue number")
    ax[k].set_ylabel("Hydrophobicity")

plt.tight_layout()
plt.savefig("q3_profile.png", dpi=200)
plt.show()