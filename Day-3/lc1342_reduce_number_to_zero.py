def number_of_steps(num) :
    if num==0 :
        return 0
    if num%2 == 0 :
        return 1 + number_of_steps(num//2)
    return 1 + number_of_steps(num-1)

num = int(input("Enter a number:"))
result = number_of_steps(num)
print(result)