
strg = "Do I have any vowels?"

count = 0
for i in strg.lower():
    if i in "aeiou":
        count += 1
if count:
    print("There are {} vowels in this sentence".format(count))
