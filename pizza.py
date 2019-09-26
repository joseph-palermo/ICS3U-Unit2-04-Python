#!/usr/bin/env python3

# Created by: Joseph Palermo
# Created on: Sep 2019
# This program calculates the cost of pizza


import constants1


def main():
    # this function calculates the cost of pizza

    # input
    diameter = int(input("Enter the diameter of the pizza you would like" +
                         " (inch): "))

    # process
    sub_total = constants1.LABOUR + constants1.RENT + \
        (diameter * constants1.COST_PER_INCH)
    total = sub_total + (sub_total * constants1.HST)

    # output
    print("")
    print("The cost for a {0} inch pizza is: ${1:,.2f}"
          .format(diameter, total))


if __name__ == "__main__":
    main()
