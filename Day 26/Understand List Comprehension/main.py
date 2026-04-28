number = [1,2,3]

new_number = [new + 1 for new in number]

print(new_number)

numbers = [num * 2 for num in range(1,5)]

print(numbers)

student_names = ["Alex", "Yuchen", "Will", "Josh", "Jackson"]

short_names = [name for name in student_names if (len(name) <= 4)]

print(short_names)

number_list = ['1\n', '2\n', '3\n']
new_number_list = [int(n) for n in number_list]
print(new_number_list)
print(int(n) for n in number_list)

