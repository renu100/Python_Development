def insertionSort(listOfWord):
    for i in range(0, len(listOfWord)):
        j = i - 1
        key = listOfWord[i]
        while j >= 0 and listOfWord[j] > key:
            listOfWord[j + 1] = listOfWord[j]
            j -= 1
        listOfWord[j + 1] = key


print("List is : ")
listOfString = ["suraj", "rushikesh", "mohini", "shivani"]
print(listOfString)
print("After Sorting : ")
insertionSort(listOfString)
print(listOfString)
