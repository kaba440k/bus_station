K=int(input()) #метры от начала улицы
N=int(input()) #расстояние пройденное
H=1
M=K
G=M*-1
while K<N:
    K=M
    K*=H
    H+=1
    G+=M
K-=N
G=N-G
if K<G or K==G:
    print(K)
else:
    print(G)

