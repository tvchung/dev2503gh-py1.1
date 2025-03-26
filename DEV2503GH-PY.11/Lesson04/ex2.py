# Cấu trúc lặp for
# Lặp trong một tập hợp: 
'''
    for phan_tu in tap_hop:
        # Các câu lệnh
'''
# Ví dụ: danh sách
fruits = ["apple","banana","cherry"]
print(fruits)

# vòng lặp for
for fruit in fruits:
    print(fruit)

# Ví dụ: duyệt từng ký tự

message = "Hello World"
print("In từng ký tự")
for character in message:
    print(character)

#========= vòng lặp dùng với range()
for x in range(6): # lặp từ 0,... 5 
    print(x)

#  range(m, n)
print("m->n")
for x in range(2,6):
    print (x)

# range(m,n, step)
print("range(m,n, step)")
for x in range(1,30, 3):
    print(x, end="  ")

print("Số chẵn")
for x in range(2,10,2):
    print(x, end="  ")