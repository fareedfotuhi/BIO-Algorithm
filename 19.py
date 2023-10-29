import numpy as np
def process_file(filename):
    file = open('C:/Users/Fareed/Downloads/rosalind_ba7b.txt')
    data = file.readlines()
    dim = int(data[0])
    del data[0]
    matrix = []
    for line in data:
        matrix.append( [ int (x) for x in line.split() ] )
    return (dim, matrix)

def limbLength(matrix, j):
    result = None
    for i in range(n):
        for k in range(n):
            if i != l and k != l:
                temp = matrix[i][j] + matrix[k][j] - matrix[i][k] 
                if result == None:
                    result = temp
                elif result > temp:
                    result = temp
    result = result//2
    return result

def find(matrix):
    """
    find i, k s.t. Di,k = Di,n + Dn,k
    """
    for k in range(matrix.shape[0]-1):
        arr = matrix[k] - matrix[-1]
        index = np.where(arr == matrix[k, -1])
        if len(index[0]) > 0:
            return (index[0][0], k)
    return None

def nearest(edge, weight, x, i, k):
    """
    find the nearest two nodes on path i->k
    to insert new node, BFS
    """
    queue = [[i]]
    visited = set([i])
    findPath = []
    while len(queue) > 0:
        path = queue.pop()
        node = path[-1]
        visited.add(node)
        if node == k:
            findPath = path
            break
        for next_node in edge[node]:
            if next_node not in visited:
                queue.append(path+[next_node])
    
    dist = 0
    for k in range(len(findPath)-1):
        i, j = findPath[k], findPath[k+1]
        if dist+weight[(i, j)] > x:
            return (i, j, x-dist, dist+weight[(i, j)]-x)
        dist += weight[(i, j)]
    
    

def additivePhylogeny(matrix, n, inner_n):

    if n == 2:
        edge = {}
        edge[0] = [1]
        edge[1] = [0]
        weight = {}
        weight[(0, 1)] = matrix[0, 1]
        weight[(1, 0)] = matrix[0, 1]
        return (edge, weight, inner_n)

    limb = limbLength(matrix, n-1)
    matrix[:-1,-1] -= limb
    matrix[-1,:-1] -= limb
    i, k = find(matrix)
    x = matrix[i, -1]
    edge, weight, inner_n = additivePhylogeny(matrix[:-1, :-1], n-1, inner_n)
    
    i_near, k_near, i_x, n_x = nearest(edge, weight, x, i, k)
    new_node = i_near

    if i_x != 0:
        new_node = inner_n
        inner_n += 1
        edge[i_near].remove(k_near)
        edge[k_near].remove(i_near)
        edge[i_near].append(new_node)
        edge[k_near].append(new_node)
        edge[new_node] = [i_near, k_near]

        weight[(new_node, i_near)] = i_x
        weight[(i_near, new_node)] = i_x
        weight[(new_node, k_near)] = n_x
        weight[(k_near, new_node)] = n_x
        del weight[(i_near, k_near)]
        del weight[(k_near, i_near)]
    edge[new_node].append(n-1)
    edge[n-1] = [new_node]
    weight[(n-1, new_node)] = limb
    weight[(new_node, n-1)] = limb
    return (edge, weight, inner_n)