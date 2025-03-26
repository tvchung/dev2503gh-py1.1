# Cấu trúc lặp lồng nhau: while, for
adj = ['red','big','tasty']
fruits = ['apple','banana','chery']

for x in adj:
    for y in fruits:
        print (x,y)

#In bảng cửu chương:
print("Bang cửu chương:")
for x in range(2,10):
    print(f"Bảng chương {x}")
    for y in range(1,11):
        print(f"{x} x {y} = {x*y}")

