'''
Viết chương trình tính tổng các số chẵn và không chia hết cho 3 
với các số <=n ( n nguyên dương, nhập từ bàn phím)
'''

# Nhập số nguyên dương n từ bàn phím
n = int(input("Nhập n = "))

# Khởi tạo biến tông
tong = 0

# Lặp (Duyệt)
s=""
for i in range(2, n+1 , 2): # Chỉ duyệt các số chẵn
    if (i % 3 != 0):
        tong +=i
        #print(i,end="+")
        s += str(i) + "+"
# tong; in 
s = s[:len(s)-1]
print(f"Biểu thức {s} = {tong}")

