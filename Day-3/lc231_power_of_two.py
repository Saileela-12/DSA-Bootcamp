def power_of_two(n):
    if n==1 :
        return True
    if n<=0 or n%2!=0:
        return False
    return power_of_two(n//2)

n = int(input("Enter a number:"))
result = power_of_two(n)
print(result)