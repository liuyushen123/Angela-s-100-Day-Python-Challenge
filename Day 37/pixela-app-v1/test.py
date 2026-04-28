s = "the sky is blue"

s = s.split()
s = s[::-1]
sum = ""
for i in s:
    sum += i + " "
print(sum)
