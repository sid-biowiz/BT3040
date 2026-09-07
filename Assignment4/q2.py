string1 = 'AATCTATA'
string2 = 'AAG--ATA'

score = 0
for i in range(len(string1)):
    if string1[i] != '-' and string2[i] != '-':
        if string1[i] == string2[i]:
            score += 1
        else:
            continue

    else:
        score -= 1
        if i == 0:
            score -= 2
        else:
            if string1[i] == '-':
                if string1[i - 1] != '-':
                    score -= 2
                else:
                    continue

            else:
                if string2[i - 1] != '-':
                    score -= 2
                else:
                    continue

print("The Alignment Score for the given strings are: ", score)