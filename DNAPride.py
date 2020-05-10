
numCases = int(input())
output = []

for i in range(numCases):
    numBases = int(input())
    basesString = input()
    output = ""
    rna = False
    for j in range(numBases):
        base = basesString[j]
        if base == 'A':
            output += 'T'
        elif base == 'T':
            output += 'A'
        elif base == 'G':
            output += 'C'
        elif base == 'C':
            output += 'G'
        else:
            rna = True
    if not(rna):
        print(output)
    else:
        print("Error RNA nucleobases found!")
