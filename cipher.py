#!/usr/bin/env python

# Create the plain text input
plain_text = raw_input("What data do you want to encrypt?")

# Create the cipher text outside the loop
ciphertext = ""

# Look at each plain text character and rotate it by 1
for c in plain_text:
	# Gets the character
	new_c = chr(ord(c)+1)
	# Append it to the ciphertext
	ciphertext = ciphertext + new_c

# Print the ciphertext
print(ciphertext)
