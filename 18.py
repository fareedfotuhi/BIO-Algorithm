file = open('C:/Users/Fareed/Downloads/rosalind_ba7b.txt')
data = file.readlines()
n = int(data[0])
l = int(data[1])
del data[0]
del data[0]
distMatrix = []
#print(data)
#print(type(data))
for line in data:
    distMatrix.append( [ int (x) for x in line.split() ] )
#print(distMatrix)
result = None
for i in range(n):
    for j in range(n):
        if i != l and j != l:
            temp = distMatrix[i][l] + distMatrix[j][l] - distMatrix[i][j] 
            if result == None:
                result = temp
            elif result > temp:
                result = temp
result = result//2
print(result)