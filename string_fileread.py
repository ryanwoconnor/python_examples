#!/usr/bin/env python


# Start our count at 0
count = 0

# Get each line in the accounts file
for line in open("accounts.txt").readlines():
    	# Increment the count by 1
	count = count + 1

# Print the total count of accounts 
print "The file contains", count, "lines."

