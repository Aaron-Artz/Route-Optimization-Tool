import csv
import datetime

with open('Distance.csv') as distance_csv:
    read_dist = csv.reader(distance_csv, delimiter=',')
    read_dist = list(read_dist)

with open('Locations.csv') as location_csv:
    read_loc = csv.reader(location_csv, delimiter='|')
    read_loc = list(read_loc)

    start = 1
    end = 2


    #  Gets the distance between two points where Start and End are Location number ID's
    #  Complexity is O(1)
    def get_distance(start, end):
        distance = read_dist[start][end]
        distance = float(distance)
        return distance


    #  Gets the Location ID from a given street address
    def get_loc_id(street):
        for row in read_loc:
            if row[2] == street:
                return int(row[0])


    #  Gets the total distance traveled from a truck
    #  Takes in sorted truck list from Packages.py
    def get_total_distance(truck_list):
        total_distance = 0
        for row in range(len(truck_list)):
            if row > len(truck_list) - 2:
                return total_distance
            else:
                total_distance = total_distance + get_distance(get_loc_id(truck_list[row][1]),
                                                               get_loc_id(truck_list[row + 1][1]))


    #  Method used to add time to an existing datetime.time object
    #  Complexity is O(1)
    def add_time(tm, seconds):
        full_date = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
        full_date = full_date + datetime.timedelta(seconds=seconds)
        return full_date.time()


    #  Loads the packages onto the truck, setting a load time and changing the package status to In Transit
    # Complexity O(n)
    def load_trucks(truck_list, time):
        for row in range(len(truck_list)):
            truck_list[row][8] = 'In Transit'
            truck_list[row][9] = time


    # Function calculates the delivery time for each package
    # Takes in a sorted list of packages and a start time.
    # Complexity is O(n)
    def ship_truck(truck_list, start_time):
        total_distance = 0
        deliver_time = start_time
        for row in range(len(truck_list)):
            if row > len(truck_list) - 2:
                return truck_list
            else:
                total_distance = total_distance + get_distance(get_loc_id(truck_list[row][1]),
                                                               get_loc_id(truck_list[row + 1][1]))

                distance = get_distance(get_loc_id(truck_list[row][1]),
                                        get_loc_id(truck_list[row + 1][1]))

                time_traveled = distance / .005

                deliver_time = add_time(deliver_time, time_traveled)

                truck_list[row + 1][8] = 'Delivered'
                truck_list[row + 1][10] = deliver_time
