# Cấu trúc if
#1. if đơn
x = int(input("x="));
y = int(input("y="));

if (x>y):
    print(x,">", y)

#2. if đầy đủ
if(x>y):
    print(f"Giá trị lớn x={x}")
else:
    print(f"Giá trị lớn là y={y}")

#3. if ... elif...: if bậc thang
# kiểm tra 2 số x, y: x>y; x<y; x=y?
if(x>y):
    print(f"{x}>{y}")
elif(x<y):
    print(f"{x}<{y}")
else:
    print(f"{x}={y}")

#4. nested if (if lồng nhau)
# có 3 số x,y, z
# Kiểm tra xem nếu x>y thì in ra x lớn hơn y;
# nếu x không lớn hơn y thì kiểm tra xem: NẾU y lớn hơn z
# => sẽ in ra "y lơn z và nhỏ hơn x", ngược lại "z lớn hơn y"

z=int(input("z="))
if(x>y):
    print("x lớn hơn y")
else:
    if(y>z):
        print("y lớn hơn z nhưng nhỏ hơn x")
    else:
        print("z lớn hơn y")