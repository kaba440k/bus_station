import time


def main():
    distance_stations = int(input("расстояние между остановками: "))
    distance_sveta = int(input("расстояние пройденное Светланой: "))
    start_time = time.time()
    previous_station = distance_sveta - distance_sveta // distance_stations * distance_stations
    next_station = distance_sveta // distance_stations * distance_stations + distance_stations - distance_sveta
    print(min(previous_station, next_station))
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()



