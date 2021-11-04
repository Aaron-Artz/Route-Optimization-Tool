#############################################################
#           C950 Final Project
#           Aaron Joseph Artz
#           Student ID: 000871650
#           9/17/2020
#############################################################
from Packages import *
from Distance import *
from HashTable import *

while True:
    print('******************************************************')
    print('Western Governors University Parcel Service')
    print('******************************************************')
    print('')
    print('****** MENU ******')
    print('-------------------')
    print('1 - Look-up package.')
    print('2 - Check all package status')
    print('3 - Check route statistics')
    print('4 - Exit')
    print('-------------------')
    print('')

    user_input = input('Enter number: ')

    if user_input not in ('1', '2', '3', '4'):
        print('')
        print('Invalid input')
        print('')
        continue

    if user_input == '1':
        while True:

            print('****** Package Look-Up ******')
            print('-------------------')
            print('1 - Search by package ID')
            print('2 - Search by package address')
            print('3 - Back')
            print('-------------------')
            print('')
            search_input = input('Select option: ')

            if search_input == '1':
                input_id = input('Enter Package ID: ')
                search_by_id(input_id)
                print('')
                print('Search for another package?')
                while True:
                    answer = input('Enter: yes / no : ')
                    if answer in ('yes', 'no'):
                        break
                    print('Invalid Input')
                if answer == 'yes':
                    continue
                else:
                    print('Goodbye')
                    break

            if search_input == '2':
                input_address = input('Enter address: ')
                search_by_address(input_address)
                print('')
                print('Search for another package?')
                while True:
                    answer = input('Enter: yes / no : ')
                    if answer in ('yes', 'no'):
                        break
                    print('Invalid Input')
                if answer == 'yes':
                    continue
                else:
                    print('Goodbye')
                    break
            if search_input == '3':
                break

    if user_input == '2':
        while True:
            print('****** Check Package Status ******')
            print('-------------------')
            print('1 - Check package status at specified time')
            print('2 - Back')
            print('-------------------')
            check_input = input('Select option:')
            if check_input not in ('1', '2'):
                print('')
                print('Invalid input')
                print('')
                continue

            if check_input == '1':
                input_time = input('Enter time (HH:MM:SS):')
                time_at = datetime.datetime.strptime(input_time, '%H:%M:%S').time()
                status_by_time(time_at)

            if check_input == '2':
                break

    if user_input == '3':
        while True:
            print('****** Current Route Statistics ******')
            print('1 - Get total mileage')
            print('2 - Get mileage by truck')
            print('3 - Back')
            statistics_input = input('Select option:')
            if statistics_input not in ('1', '2', '3'):
                print('')
                print('Invalid input')
                print('')
                continue

            if statistics_input == '1':
                total_mileage()

            if statistics_input == '2':
                mileage_by_truck()

            if statistics_input == '3':
                break

    if user_input == '4':
        print('Goodbye')
        break
