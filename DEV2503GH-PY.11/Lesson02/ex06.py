#Toán tử membership

a = [1,3,5,7,2]

# in
result = 3 in a # kết quả trả về là True
print(result)

print(6 in a) # False

# not in
print ("6 not in a:", 6 not in a) # True

# Chuỗi
str = "Hello world"
 
print("'H' in str => ", 'H' in str) # True
print("'hello' in str => ", 'hello' in str) # False
print("'Hello' in str => ", 'Hello' in str) # True

# Sử dụng với set

mySet = {11,2,33,55,66}

print("1 in mySet:", 1 in mySet)
print("11 in mySet:", 11 in mySet)
print("11 not in mySet:", 11 not in mySet)