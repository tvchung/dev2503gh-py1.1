# Cấu trúc lặp while
# In ra các số nguyên từ 1 - n (n nhập từ người dùng)
n = int(input('Nhập số n='))
# Tạo biến lặp ((khởi tạo))
i=1
while(i <= n):
    print(f"Giá trị thứ : {i}")
    i = i+1
# Câu lệnh sau ở ngoài vòng lặp
print("finish")

# In ra các số chẵn trong khoảng từ 1 - n;
i=2
while i<=n:
    print(f"Số chẵn thứ {i}")
    i = i + 2

# Các khác
print("Cách khác\n")
i=2
while i <= n:
    if i % 2 ==0:
        print(f"Số chẵn thứ:{i}")
    i = i + 1
##


