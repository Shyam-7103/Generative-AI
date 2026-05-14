# Problem - 1

# a = int(input("Enter the number"))
# b = int(input("Enter the number"))
# c = int(input("Enter the number"))
# d = int(input("Enter the number"))

# if(a > b & a>c & a>d):
#     print("A is greatest")
# elif(b>c & b>d):
#     print("B is greatest")
# elif(c>d):
#     print("C is greatest")
# else:
#     print("D is greatest")

# Problem - 2#

# a = int(input("Enter marks maths   :"))
# b = int(input("Enter marks science :"))
# c = int(input("Enter marks biology :"))

# totalmarks = ((a+b+c)*100)/300

# if(totalmarks >= 40 and a>33 and b>33 and c>33):
#     print("You are passed", totalmarks)
# else:
#     print("You are failed", totalmarks)

# Problem - 3

p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("Enter your message")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("Scam message")
else:
    print("Valid message")