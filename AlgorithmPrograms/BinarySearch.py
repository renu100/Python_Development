def binSearch(word, listOfWord, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if word == listOfWord[mid]:
        return True
    elif word > listOfWord[mid]:
        return binSearch(word, listOfWord, mid + 1, high)
    elif word < listOfWord[mid]:
        return binSearch(word, listOfWord, low, mid - 1)


givenList = []
size = int(input("Enter how many elements you want to Enter: "))
for index in range(size):
    data = input("Enter word: ")
    givenList.append(data)
target = input("Enter the Element To be searched.")
if binSearch(target, givenList, 0, len(givenList)):
    print(target + " is Present in The List")
else:
    print("Element is not present in the List")
