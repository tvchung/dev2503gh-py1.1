a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

epsilon = 1e-6
sides = sorted([a, b, c])
a, b, c = sides

if a + b <= c:
    print("Không phải tam giác")
else:
    if abs(a - b) < epsilon and abs(b - c) < epsilon:
        print('Tam giac deu')
    else:
        vuong_can = (abs(a - b) < epsilon) and (abs(a**2 + b**2 - c**2) < epsilon)
        if vuong_can:
            print('Tam giac vuong can')
        else: 
            if abs(a**2 + b**2 - c**2) < epsilon:
                print('Tam giac vuong')
            else: 
                can = (abs(a - b) < epsilon) or (abs(b - c) < epsilon) or (abs(a - c) < epsilon)
                if can:
                    print("Tam giác cân")
                else: 
                    print("Tam giác thường")