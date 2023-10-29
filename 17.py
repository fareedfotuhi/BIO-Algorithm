from collections import defaultdict

file = open('C:/Users/Fareed/Downloads/rosalind_ba7a.txt')
data = file.readlines()
n = int(data[0])
del data[0]
adj = defaultdict(list)
for i in data:  
	x, temp = i.strip().split("->")  
	y, w = temp.split(":")
	adj[int(x)].append((int(y), int(w)))


def DFS(i,j,path=[]):
    if i ==j:
         return 0
    d = float('inf')
    for node,weight in adj[i]:
        if node==j:
            return weight
        if node in path:
            continue
        test = weight + DFS(node,j,path+[node])
        if test<d:
            d=test
    return d



distMatrix = [[0]*n for _ in range(n)]
for i in range(n):
	for j in range(n):
		distMatrix[i][j] = DFS(i, j)
                
x = '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in distMatrix])
print(x)

