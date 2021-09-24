### check a string for Palindrome
# Palindrome eg: Madam ; spelled backwards == spelled forward
# cat != tac

# Step1: Revers a String
# Step2: Compare revesed string with original

input_string = "olla".lower()
reversed_string = ""

for i in input_string[::-1]:
    reversed_string += i

if reversed_string == input_string:
    print("{}} is a Palindrome".format(input_string))
else:
    print("{} is not a Palindrome".format(input_string))

