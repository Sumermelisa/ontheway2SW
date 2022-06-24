print("""(result values are approximate)
(please do not enter values except whole numbers)""")

print("*" * 40)
print("celsius to fahrenheit-1")
print("fahrenheit to celsius-2")
print("*" * 40)

choice= int(input("converting choice:"))

if choice==1:
    celsius= float(int(input("celsius:")))
    fahrenheit= (celsius * 2) +32
    print("{} celsius is equal to {} fahrenheit".format(celsius,fahrenheit))
elif choice==2:
    fahrenheit= float(int(input("fahrenheit:")))
    celsius= (fahrenheit-32)/2
    print("{} fahrenheit is equal to {} celsius".format(fahrenheit,celsius))
else:
    print("CONGRATULATİONS!")