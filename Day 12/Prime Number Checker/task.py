
for num in range(2,1000000):
    if num > 2:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")
    else:
        print(f"{num} is not a prime number")
