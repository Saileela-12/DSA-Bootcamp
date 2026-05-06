a = int(input("Enter a first number:"))
b = int(input("Enter a second number:"))

x,y = a,b

while y!=0 :
    num = y
    y = x%y
    x = num

hcf =  x
lcm = a*b//hcf  #LCM finding via HCF

print("LCM:",lcm)

