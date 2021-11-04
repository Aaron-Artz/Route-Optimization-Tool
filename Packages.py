from HashTable import ChainedHashtable
from Distance import *
import HashTable
from HashTable import *
from LinkedList import *
import csv
from datetime import datetime
import datetime

# Gets data from Packages.csv
with open('Packages.csv') as csvFile:
    readCSV = csv.reader(csvFile, delimiter=',')

    packages_hash = ChainedHashtable()  # Creates a ChainedHashTable object to load with package details

    # Takes in each row from the Packages.csv file and adds them to packages_hash
    # Complexity is O(N) where N is the number of packages (or rows)
    for row in readCSV:
        package_id = row[0]
        package_address = row[1]
        package_city = row[2]
        package_state = row[3]
        package_zip = row[4]
        package_deadline = row[5]
        package_weight = row[6]
        package_notes = row[7]
        package_status = 'At Hub'  # Default value, possible values ('At Hub' 'En Route' 'delivery(time)'
        package_load_time = 0
        package_deliver_time = 0
        key = int(package_id)
        value = [package_id, package_address, package_city, package_state, package_zip, package_deadline,
                 package_weight, package_notes, package_status, package_load_time, package_deliver_time]
        if '9' == value[0]:  # Updates the package with the wrong address.
            value[1] = '410 S State St'
            value[4] = '84111'

        packages_hash.insert(key, value)  # adds all values in csv file to to a hash table

    #  Initialize a couple empty lists(trucks) to be filled with packages
    first_truck_packages = []
    second_truck_packages = []
    third_truck_packages = []  # This truck will have all late packages, leaves after truck 1 returns.

    # ***************** MANUALLY ADDING PACKAGES **************************

    # packages that must be on the same truck together
    first_truck_packages.append(packages_hash.get(7))
    first_truck_packages.append(packages_hash.get(11))
    first_truck_packages.append(packages_hash.get(13))
    first_truck_packages.append(packages_hash.get(14))
    first_truck_packages.append(packages_hash.get(15))
    first_truck_packages.append(packages_hash.get(16))
    first_truck_packages.append(packages_hash.get(19))
    first_truck_packages.append(packages_hash.get(20))
    first_truck_packages.append(packages_hash.get(22))
    first_truck_packages.append(packages_hash.get(23))
    first_truck_packages.append(packages_hash.get(27))
    first_truck_packages.append(packages_hash.get(31))
    first_truck_packages.append(packages_hash.get(35))
    first_truck_packages.append(packages_hash.get(40))

    # packages that must be on truck 2
    second_truck_packages.append(packages_hash.get(1))
    second_truck_packages.append(packages_hash.get(2))
    second_truck_packages.append(packages_hash.get(3))
    second_truck_packages.append(packages_hash.get(5))
    second_truck_packages.append(packages_hash.get(10))
    second_truck_packages.append(packages_hash.get(17))
    second_truck_packages.append(packages_hash.get(18))
    second_truck_packages.append(packages_hash.get(24))
    second_truck_packages.append(packages_hash.get(29))
    second_truck_packages.append(packages_hash.get(33))
    second_truck_packages.append(packages_hash.get(36))
    second_truck_packages.append(packages_hash.get(37))
    second_truck_packages.append(packages_hash.get(38))

    # Late arrivals and wrong address (ships after truck 1 gets back)
    third_truck_packages.append(packages_hash.get(4))
    third_truck_packages.append(packages_hash.get(6))
    third_truck_packages.append(packages_hash.get(8))
    third_truck_packages.append(packages_hash.get(9))
    third_truck_packages.append(packages_hash.get(12))
    third_truck_packages.append(packages_hash.get(21))
    third_truck_packages.append(packages_hash.get(25))
    third_truck_packages.append(packages_hash.get(26))
    third_truck_packages.append(packages_hash.get(28))
    third_truck_packages.append(packages_hash.get(30))
    third_truck_packages.append(packages_hash.get(32))
    third_truck_packages.append(packages_hash.get(34))
    third_truck_packages.append(packages_hash.get(39))
    hub = ['HUB', '4001 South 700 East', 'Salt Lake City', 'UT', '84107', 'non', '0', 'None', 'At Hub', 0, 0]
    first_sorted_truck = list()
    first_sorted_truck.append(hub)
    second_sorted_truck = list()
    second_sorted_truck.append(hub)
    third_sorted_truck = list()
    third_sorted_truck.append(hub)


    # Greedy algorithm approach to sorting the truck packages in the order to be delivered.
    # Takes in an unsorted list of packages and a current location (HUB is 0)
    # from current_loc picked the next destination with the shorted distance.
    # recursion calls the method until all packages have been added to the sorted_truck_list in order
    # then returns the sorted_truck list

    def sort_truck_packages(truck_list, current_loc, truck_id):

        if truck_id == 1:
            if len(truck_list) == 0:
                first_sorted_truck.append(hub)  # Adds the hub as the final destination
                return  # Driver must return before truck three can leave.
            else:
                current_loc = current_loc
                lowest_package = truck_list[0][1]
                lowest = get_loc_id(truck_list[0][1])
                distance = get_distance(current_loc, lowest)
                for row in range(len(truck_list)):
                    if get_distance(current_loc, get_loc_id(truck_list[row][1])) <= get_distance(current_loc, lowest):
                        lowest = get_loc_id(truck_list[row][1])
                        lowest_package = truck_list[row]
                        lowest_row = row

                first_sorted_truck.append(lowest_package)
                del (truck_list[lowest_row])
                sort_truck_packages(truck_list, lowest, truck_id)

        if truck_id == 2:
            if len(truck_list) == 0:
                second_sorted_truck.append(hub)  # Adds the hub as the final destination
                return
            else:
                current_loc = current_loc
                lowest_package = truck_list[0][1]
                lowest = get_loc_id(truck_list[0][1])
                for row in range(len(truck_list)):
                    if get_distance(current_loc, get_loc_id(truck_list[row][1])) <= get_distance(current_loc, lowest):
                        lowest = get_loc_id(truck_list[row][1])
                        lowest_package = truck_list[row]
                        lowest_row = row

                second_sorted_truck.append(lowest_package)
                del (truck_list[lowest_row])
                sort_truck_packages(truck_list, lowest, truck_id)

        if truck_id == 3:
            if len(truck_list) == 0:
                third_sorted_truck.append(hub)  # Adds the hub as the final destination
                return
            else:
                current_loc = current_loc
                lowest_package = truck_list[0][1]
                lowest = get_loc_id(truck_list[0][1])
                for row in range(len(truck_list)):
                    if get_distance(current_loc, get_loc_id(truck_list[row][1])) <= get_distance(current_loc, lowest):
                        lowest = get_loc_id(truck_list[row][1])
                        lowest_package = truck_list[row]
                        lowest_row = row

                third_sorted_truck.append(lowest_package)
                del (truck_list[lowest_row])
                sort_truck_packages(truck_list, lowest, truck_id)


    # First call runs algo to sort packages in order
    # second calls total distance method to add up distance between each package.
    # load_trucks assigns each package with a time the truck as been loaded and left the hub.
    # ship_truck method "ships" the packages, assigning delivery time and updating status.
    sort_truck_packages(first_truck_packages, 0, 1)
    first_truck_total = round(get_total_distance(first_sorted_truck), 4)
    load_trucks(first_sorted_truck, datetime.time(8, 00, 00))

    finished_first_truck = ship_truck(first_sorted_truck, datetime.time(8, 00, 00))

    sort_truck_packages(second_truck_packages, 0, 2)
    second_truck_total = round(get_total_distance(second_sorted_truck), 4)
    load_trucks(second_sorted_truck, datetime.time(8, 00, 00))

    finished_second_truck = ship_truck(second_sorted_truck, datetime.time(8, 00, 00))

    sort_truck_packages(third_truck_packages, 0, 3)
    third_truck_total = round(get_total_distance(third_sorted_truck), 4)
    load_trucks(third_sorted_truck,
                first_sorted_truck[len(first_sorted_truck) - 1][10])  # Ships after first truck returns

    finished_third_truck = ship_truck(third_sorted_truck, datetime.time(11, 30, 00))

    total_distance = round((first_truck_total + second_truck_total + third_truck_total), 4)

    #################################################################################
    #
    # LOOK UP FUNCTIONS
    #
    #################################################################################


    # Initialize list to store all final data of packages
    final_results = []

    # Range set to number of packages
    # Complexity O(n) where n is the number of packages.
    for i in range(40):
        final_results.append(packages_hash.get(i + 1))

    # Takes in a string
    # Searches packages for matching address then returns all packages
    # Complexity O(n)
    def search_by_address(address):
        results = ''
        for row in range(len(final_results)):
            if final_results[row][1] == address:
                results = results + '\n******************************' + \
                          '\nPackage ID: ' + str(final_results[row][0] + '\nPackage address: ' +
                                                 str(final_results[row][1] + ', ' + final_results[row][2])) + \
                          ', ' + final_results[row][3] + ' ' + final_results[row][4] + \
                          '\nWeight: ' + str(final_results[row][6]) + \
                          '\nShipped time: ' + str(final_results[row][9]) + \
                          '\nExpected delivery time: ' + str(final_results[row][10]) + \
                          '\n******************************'
        if len(results) == 0:
            print('There were no packages with the specified address.')
            return
        else:
            print(results)
            return


    # Takes in a string
    # Searches packages for matching ID then returns package information
    # Complexity O(n)
    def search_by_id(id):
        results = ''
        for row in range(len(final_results)):
            if final_results[row][0] == id:
                results = results + '\n******************************' + \
                                                        '\nPackage ID: ' + str(final_results[row][0] +'\nPackage address: ' +
                                                        str(final_results[row][1] + ', ' + final_results[row][2])) +\
                                                        ', ' + final_results[row][3] + ' ' + final_results[row][4] + \
                                                        '\nWeight: ' + str(final_results[row][6]) + \
                                                        '\nShipped time: ' + str(final_results[row][9]) + \
                                                        '\nExpected delivery time: ' + str(final_results[row][10]) + \
                                                        '\n******************************'
        if len(results) == 0:
            print("There are no packages with the specified ID")
            return
        else:
            print(results)
            return



    # Takes in a list and datetime.time
    # Returns the status of all packages at the time specified.
    # Complexity O(n)
    def status_by_time(time):
        print('********************************************************')
        for row in range(len(final_results)):
            if final_results[row][10] <= time:
                print('Package ID:', final_results[row][0], 'has been', final_results[row][8], 'at',
                      final_results[row][10])
            if final_results[row][9] <= time < final_results[row][10]:
                print('Package ID:', final_results[row][0], 'is currently in transit')
            if final_results[row][9] > time:
                print('Package ID:', final_results[row][0], 'is still at the HUB')
        print('********************************************************\n')

    def total_mileage():
        print('')
        print('*********************************************')
        print('The current total route mileage is', total_distance)
        print('*********************************************')
        print('')

    def mileage_by_truck():
        print('')
        print('*********************************************')
        print('The first truck total mileage is:', first_truck_total)
        print('The second truck total mileage is:', second_truck_total)
        print('The third truck total mileage is:', third_truck_total)
        print('*********************************************')
        print('')
