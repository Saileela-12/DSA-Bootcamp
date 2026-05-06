a = int(input("Enter a first number:"))
b = int(input("Enter a second number:"))

x,y = a,b

while y!=0 : #Euclidean Algorithm
    num = y
    y = x%y
    x = num
print("HCF: ", x)

