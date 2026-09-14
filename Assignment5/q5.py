
human = ("MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKV"
         "KAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKE"
         "FTPPVQAAYQKVVAGVANALAHKYH")

chicken = ("MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMV"
           "RAHGKKVLTSFGDAVKNLDNIKNTFSQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKD"
           "FTPECQAAWQKLVRVVAHALARKYH")

# midline from the BLAST pairwise output in Q4
midline = ("MVH T EEK  +T LWGKVNV E G EAL RLL+VYPWTQRFF SFG+LS+P A++GNP V"
           "+AHGKKVL +F D + +LDN+K TF+ LSELHCDKLHVDPENFRLLG++L+ VLA HF K+"
           "FTP  QAA+QK+V  VA+ALA KYH")


# Q5
def find_positions(seq, peptide):
    positions = []
    for i in range(len(seq) - 4):
        if seq[i:i+5] == peptide:
            positions.append(i + 1)
    return positions


def matching_pentapeptides(seq1, seq2):
    done = []
    for i in range(len(seq1) - 4):
        peptide = seq1[i:i+5]
        if peptide in done:
            continue
        done.append(peptide)

        pos1 = find_positions(seq1, peptide)
        pos2 = find_positions(seq2, peptide)
        if pos2:
            print(peptide, "-> human:", len(pos1), "at", pos1,
                  "| chicken:", len(pos2), "at", pos2)


# Q6
def alignment_stats(seq1, seq2, align):
    identity = 0
    similarity = 0
    gaps = 0

    for ch in align:
        if ch.isalpha():
            identity += 1
            similarity += 1
        elif ch == "+":
            similarity += 1
        elif ch == "-":
            gaps += 1

    n = len(align)
    print("Sequence identity  = %.2f %%" % (100 * identity / n))
    print("Sequence similarity= %.2f %%" % (100 * similarity / n))
    print("Gap percentage     = %.2f %%" % (100 * gaps / n))
    print("Query coverage     = %.2f %%" % (100 * n / len(seq1)))


matching_pentapeptides(human, chicken)
print()
alignment_stats(human, chicken, midline)