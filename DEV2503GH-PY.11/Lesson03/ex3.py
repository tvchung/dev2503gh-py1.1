# Giải phương trình bậc 2
# ax^2 + bx + c = 0
import math
# Nhập các hệ số:
a=float(input("hệ số a = "))
b=float(input("hệ số b = "))
c=float(input("hệ số c = "))

if(a!=0):
    delta = b**2 - 4*a*c
    if(delta > 0):
        # Phương trình có 2 nghiệm
        x1=(-b + math.sqrt(delta))/(2*a)
        x2=(-b - math.sqrt(delta))/(2*a)
        print(f"Nghiệm x1={x1}")
        print(f"Nghiệm x2={x2}")
    elif delta == 0:
        # Phương trình có nghiệm kép
        x = -b / (2*a)
        print(f"Nghiệm x1=x2={x}")
    else:
        # Phương trình vô nghiệm
        print("Phương trình vô nghiệm")
else: # a=0
    # Giải phương trình bậc 1: bx+c = 0
    if b !=0:
        # Phương trình có nghiệm
        x= -c/b
        print(f"Nghiệm x={x}")
    else:
        if c==0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
## the-end

        