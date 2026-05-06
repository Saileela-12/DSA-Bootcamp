number = int(input("Enter anumber:"))

number = abs(number)

for i in range(number//2) :
    number -= 2  #used subtract 2 again and agin approach
    
if number == 0 :
    print("Even")
else :
    print("Odd")

  