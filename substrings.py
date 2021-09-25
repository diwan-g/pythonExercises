# Program checks if str1 is substring of str2
# i.e. all characters of str1 is present in str2
# order is important, str1= "apke" is not a substring of str2="ahlpek"
# Given s1 and s2 check if s1 is a subsequence of s2. I.e. all characters of s1 appears in s2


s1 = "cdngmutes"
s2 = "coding minutse"

str1_start_idx = 0
str2_start_idx = 0
st1len = len(s1)
str2len = len(s2)

    #Traverse both str1 and str2
    # Compare current character of str2 with
    # first unmatched character of str1
    # If matched, then move ahead in str1

while str1_start_idx < st1len and str2_start_idx < str2len:
    if s1[str1_start_idx] == s2[str2_start_idx]:
        str1_start_idx += 1
    str2_start_idx += 1

# if all char matched then idx == len
if str1_start_idx == st1len:
    print("{} is a substring of {}".format(s1, s2))
else:
    print("{} is not a substring of {}".format(s1, s2))


