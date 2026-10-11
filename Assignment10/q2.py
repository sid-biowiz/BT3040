#q2
import math

seqs = ["MVLSPADKTNVKGKVGAHAGEYGAAAW",
        "MKRLPADPPCVKGKVKAKAGDYGATTW",
        "MALSAADKTNVKSKVGGHAGEYGAATS",
        "MVLSAADKTNVKSKAGGNAGEWWAAAW",
        "MVLSAADKTNVKSKVLANAGEFGAAAW",
        "ALLPIRTTYHKKCASGHIPEEKDLNNV",
        "DEASSLKGHHIKKLEADALLIPLSASS"]

amino = "ACDEFGHIKLMNPQRSTVWY"

#count matrix to count the aa's per seq for a given idx
def count_matrix(seqs):
    counter_dict = []
    for i in range(len(seqs[0])):
        cnt = {}
        for aa in amino:
            cnt[aa] = 0
        for s in seqs:
            cnt[s[i]] += 1
        counter_dict.append(cnt)
    return counter_dict

#wt matrix comuptes the log(count[a] + prob)/(n+1)p) per element in mtrx
def weight_matrix(counts, N):
    p = (1/20)
    wt = []
    for cnt in counts:
        ele = {}
        for aa in amino:
            ele[aa] = math.log((cnt[aa] + p)/((N + 1)*p))
        wt.append(ele)
    return wt


counts = count_matrix(seqs)
wt_mat = weight_matrix(counts, len(seqs))
for i in range(len(wt_mat)):
    print(i + 1, [round(wt_mat[i][aa], 2) for aa in amino])