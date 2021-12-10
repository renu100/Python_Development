def check(s1, s2):
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings NOT anagrams.")


s1 = input("Enter First String :")
s2 = input("Enter Second String :")
check(s1, s2)
