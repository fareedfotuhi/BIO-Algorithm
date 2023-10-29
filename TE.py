n = 4
grah = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
for i in range(n):
    for j in range(n):
        if j != i:
            path = [grah[k] for k in range(i,j+1)]
            print(path)
            print('___________________________')