#!/usr/bin/env python

# Gather Input in U.S. Dollars
money = input("How much money do you have in U.S. Dollars (enter a number, do not include units such as $)?")

# Print How Many Dollars Someone Has
print "You have", money, "Dollars"

# Calculate the Remainder using Modulus. Subtract that from 250 to find out how many more dollars we'll need for another unit
remainder = 250 - (money % 250)
print "You will need", remainder, "More Dollars before you can purchase another Wii"

# Find the Integer value of number of units we can purchase
units = money / 250
print "You can purchase", units, "Nintendo Wiis"
