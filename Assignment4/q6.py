s1 = "ACGTATCGCGTATA"
s2 = "GATGCGTATCG"

dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
dp[0][0] = 0

for i in range(1, len(dp)):
    dp[i][0] = max(dp[i - 1][0] - 2, 0)

for j in range(1, len(dp[0])):
    dp[0][j] = max(dp[0][j - 1] - 2, 0)



for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if s2[i - 1] == s1[j - 1]:
            dp[i][j] = max(dp[i - 1][j - 1] + 2, dp[i - 1][j] - 2, dp[i][j - 1] - 2, 0)
        else:
            dp[i][j] = max(dp[i - 1][j - 1] - 1, dp[i - 1][j] - 2, dp[i][j - 1] - 2, 0)

best = 0
bi = 0
bj = 0

for i in range(len(dp)):
    for j in range(len(dp[0])):
        if dp[i][j] > best:
            best = dp[i][j]
            bi = i
            bj = j

a1 = ""
a2 = ""
i = bi
j = bj

while i > 0 and j > 0 and dp[i][j] > 0:
    if s2[i - 1] == s1[j - 1]:
        d = dp[i - 1][j - 1] + 2
    else:
        d = dp[i - 1][j - 1] - 1

    if dp[i][j] == d:
        a1 = s1[j - 1] + a1
        a2 = s2[i - 1] + a2
        i -= 1
        j -= 1
    elif dp[i][j] == dp[i - 1][j] - 2:
        a1 = "-" + a1
        a2 = s2[i - 1] + a2
        i -= 1
    else:
        a1 = s1[j - 1] + a1
        a2 = "-" + a2
        j -= 1

print("Score of the Alignemnt Table is: ", best)
print("The Table is as follows: ")
for row in dp:
    print(row)
print("Best cell is at row", bi, "column", bj)
print("Local Alignment: ")
print(a1)
print(a2)
print("s1 from", j + 1, "to", bj)
print("s2 from", i + 1, "to", bi)