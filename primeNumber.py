from math import sqrt

def is_prime(num):
    if (num <= 1):
        return False
        
    for i in range(2, int(sqrt(num))+1):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()
