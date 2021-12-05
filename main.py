K = int(input("расстояние между остановками: "))
N = int(input("расстояние пройденное Светланой: "))
number_station = 1
distance = K
previous_station = distance*-1  # предыдущая остановка
while K < N:
    K = distance*number_station
    number_station += 1
    previous_station += distance
K -= N  # расстояние от следующей остановки до Светланы
dist_station = N-previous_station  # расстояние от предыдущей остановки до Светланы
if K < dist_station or K == dist_station:
    print(K)
else:
    print(dist_station)