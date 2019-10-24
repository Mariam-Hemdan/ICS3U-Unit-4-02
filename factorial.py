#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : October 2019
# This program uses while loop


def main():
    # this program uses While loop
    factorial = 1
    loop_counter = 1

    # input
    positive_integer = int(input("Enter an integer: "))
    print("")

    # process & output
    while loop_counter <= positive_integer:
        factorial = factorial*loop_counter
        print(factorial)
        loop_counter = loop_counter + 1


if __name__ == "__main__":
    main()
