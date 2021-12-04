K = int(input("расстояние между остановками: "))
N = int(input("расстояние пройденное: "))
number_station = 1
distance = K
dist_station = distance*-1
while K < N:
    K = distance*number_station
    number_station += 1
    dist_station += distance
K -= N
dist_station = N-dist_station
if K < dist_station or K == dist_station:
    print(K)
else:
    print(dist_station)
