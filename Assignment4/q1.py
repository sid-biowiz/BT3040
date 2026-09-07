import matplotlib.pyplot as plt

s1 = "MVHWTAEEKQLITGLWGKVNVAECGAEALARLLIVYPWTQRFFASFGNLSSPTAILGNPMVRAHGKKVLTSFGDAVKNLDNIKNTFSQLSELHCDKLHVDPENFRLLGDILIIVLAAHFSKDFTPECQAAWQKLVRVVAHALARKYH"
s2 = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"

x = []
y = []

for i, a1 in enumerate(s1):
    for j, a2 in enumerate(s2):
        if a1 == a2:
            x.append(i + 1)
            y.append(j + 1)

plt.figure(figsize=(8, 8))
plt.scatter(x, y, s=10)

plt.xlabel("Chicken")
plt.ylabel("Human")
plt.title("Dot Plot of Two Protein Sequences")

plt.xlim(1, len(s1))
plt.ylim(1, len(s2))
plt.show()

minlen = 4
segments = []

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] != s2[j]:
            continue
        if i > 0 and j > 0 and s1[i - 1] == s2[j - 1]:
            continue
        k = 0
        while i + k < len(s1) and j + k < len(s2) and s1[i + k] == s2[j + k]:
            k += 1
        if k >= minlen:
            segments.append((i + 1, j + 1, k, s1[i:i + k]))

print("Common segments of length", minlen, "or more:")
for a, b, k, seg in segments:
    print("s1", a, "to", a + k - 1, "| s2", b, "to", b + k - 1, "|", seg)

x2 = []
y2 = []

for i in range(20):
    for j in range(20):
        if s1[i] == s2[j]:
            x2.append(i + 1)
            y2.append(j + 1)

plt.figure(figsize=(6, 6))
plt.scatter(x2, y2, s=25)

plt.xlabel("Chicken")
plt.ylabel("Human")
plt.title("Dot Plot of Residues 1-20")

plt.xticks(range(1, 21))
plt.yticks(range(1, 21))
plt.grid(True, linewidth=0.3)
plt.show()
