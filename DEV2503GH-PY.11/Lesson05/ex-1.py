'''
Viết chương trình thực hiện việc in ra các số nguyên tố từ 2 đến 100 
(Chú ý: Số nguyên tố là số chỉ chia hết cho 1 và chính nó)
'''

#in
for num in range(2, 101):
    # Kiểm tra số num?
    flag = True # Giả sử số num là số nguyên tố
    for x in range(2, int(num/2) +1):
        if(num % x == 0):
            flag=False # tìm thấy ước => num không phải là nguyên tố
    
    if flag == True:
        print (num, end="  ")
    
# end/

