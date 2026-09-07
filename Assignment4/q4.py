s1 = "ACCGTCCG"
s2 = "ACAGTCGAACG"

dp = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
dp[0][0] = 0

for i in range(1, len(dp)):
    dp[i][0] = dp[i - 1][0] - 2

for j in range(1, len(dp[0])):
    dp[0][j] = dp[0][j - 1] - 2


for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
        if s2[i - 1] == s1[j - 1]:
            dp[i][j] = max(dp[i - 1][j - 1] + 2, dp[i - 1][j] - 2, dp[i][j - 1] - 2)
        else:
            dp[i][j] = max(dp[i - 1][j - 1] - 1, dp[i - 1][j] - 2, dp[i][j - 1] - 2)

a1 = ""
a2 = ""
i = len(s2)
j = len(s1)

while i > 0 or j > 0:
    if i > 0 and j > 0:
        if s2[i - 1] == s1[j - 1]:
            d = dp[i - 1][j - 1] + 2
        else:
            d = dp[i - 1][j - 1] - 1
    else:
        d = None

    if d is not None and dp[i][j] == d:
        a1 = s1[j - 1] + a1
        a2 = s2[i - 1] + a2
        i -= 1
        j -= 1
    elif i > 0 and dp[i][j] == dp[i - 1][j] - 2:
        a1 = "-" + a1
        a2 = s2[i - 1] + a2
        i -= 1
    else:
        a1 = s1[j - 1] + a1
        a2 = "-" + a2
        j -= 1

print("Score of the Alignemnt Table is: ", dp[len(s2)][len(s1)])
print("The Table is as follows: ")
for row in dp:
    print(row)
print("Alignment: ")
print(a1)
print(a2)