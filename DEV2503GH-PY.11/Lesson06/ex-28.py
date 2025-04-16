'''
28. Nhập vào 1 số nguyên ở hệ thập phân, yêu cầu xuất ra 1 số ở hệ nhị phân.
ví dụ:
N=13 (Hệ thập phân) => 1101

13 | 2
 6 | 2 -> 1
 3 | 2 -> 0
 1 | 2 -> 1
 0 | 2 -> 1

'''

# Các dùng hàm bin()
n = int(input("Nhập n = "))
print(f"Số {n} chuyển sang nhị phân là:", bin(n)[2:])

# Tự viết
if n==0:
    print(f"Số {n} ở hệ nhị phân là 0")
else:
    binary = ""
    while(n>0):
        binary = str(n%2) + binary
        n//=2

print(f"Số {n} ở hệ nhỉ phân {binary}")