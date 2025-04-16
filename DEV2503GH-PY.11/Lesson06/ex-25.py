'''
Một số nguyên dương có n chữ số được gọi là số Armstrong khi tổng các lũy thừa bậc n
của các chữ số của nó bằng chính nó. Hãy kiểm tra xem một số nguyên dương N nhập
vào từ bàn phím có phải là số Armstrong hay không. Nếu phải thì xuất 'YES', ngược lại
là 'NO'.

xyz  = x^3 + y^3 + z^3 ; 153 = 1^3 + 5^3 + 3^3
abcd = a^4+b^4+c^4+d^4

'''

# Nhập số nguyên dương N
N = int(input("Nhập số nguyên dương N=")) # N=153


# Đếm số chữ số
str_num = str(N) # str_num = "153"
# Số chữ số
n = len(str_num)  # n= len("153") = 3

# Duyệt các số trong chuỗi str_num, và tính tổng lũy thừa n
t = 0
for num in str_num: 
    #print(num)
    t = t + int(num)**n

# so sánh
if (N == t):
    print ("YES")
else:
    print("NO")

# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# --- mở rộng bài toán: in ra các số amstrong <=N
# 10p


for x in range(11, N+1):
    str_x = str(x)
    n = len(str_x)
    # t=0
    # Tinh tong luy thua bac n
    # for  y in str_x:
    #     t += int(y)**n
    tong =sum(int(y)**n for y in str_x)
    # end for y
    if tong ==x :
        print(x, end=' ')
# end for x