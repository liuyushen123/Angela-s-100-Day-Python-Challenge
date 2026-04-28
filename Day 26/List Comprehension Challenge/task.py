PATH1 = "/Users/liuyuchen/Downloads/General Coding/Dr.Angela Yu's 100Day python challenge/Day 26/List Comprehension Challenge/file1.txt"
PATH2 = "/Users/liuyuchen/Downloads/General Coding/Dr.Angela Yu's 100Day python challenge/Day 26/List Comprehension Challenge/file2.txt"

with open(PATH1, "r") as file:
    list1 = file.readlines()
    print(list1)

with open(PATH2, "r") as file:
    list2 = file.readlines()
    print(list2)

result = [int(num) for num in list1 if num in list2]

print(result)
