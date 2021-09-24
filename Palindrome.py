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
    print("{} is a Palindrome".format(input_string))
else:
    print("{} is not a Palindrome".format(input_string))

# Using while loop

message = "amma".lower()
start_index = 0
end_index = len(message) -1
is_palindrome = True

while (start_index <= end_index):
    if message[start_index] != message[end_index]:
        is_palindrome = False
        break
    start_index += 1
    end_index -= 1

if is_palindrome:
    print("{} is a Palindrome".format(message))
else:
    print("{} is not a Palindrome".format(message))

