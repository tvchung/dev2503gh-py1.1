# Lệnh nhảy
# nhập số nguyên dương n; 
# in ra các số <n nếu gặp số nào là ước đầu tiên thì kết thúc
n = int(input("n="))
for x in range(2, n):
    if n % x == 0:
        break
    print (x, end="  ")

# continue
print("continue")
# in ra các số từ 1 - 10; nhưng không in số 5
for x in range(1,10):
    if(x==5):
        continue
    print(x, end=" ")
else:
    print("for finish")