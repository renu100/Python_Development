number1 = int(input("Enter First Number"))
number2 = int(input("Enter Second Number"))


def palindrome(num1, num2):
    sum1 = 0
    sum2 = 0

    while num1 != 0:
        temp1 = num1 % 10
        sum1 = sum1 + (temp1 * temp1)
        num1 = num1 // 10
    while num2 != 0:
        temp2 = num2 % 10
        sum2 = sum2 + (temp2 * temp2)
        num2 = num2 // 10

    if sum1 == sum2:
        return True

    return False


if palindrome(number1, number2):
    print("Anagram Number")
else:
    print("Not Anagram Number")
