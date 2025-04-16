'''
Viết chương trình nhập vào năm x tháng y sau đó in ra số ngày trong tháng năm đó.
'''

thang = int(input("Nhập tháng:"))
nam = int(input("Nhập nam:"))

so_ngay= None
if thang in [1,3,5,7,8,10,12]:
    so_ngay=31
elif thang in [4,6,9,11]:
    so_ngay=30
elif thang ==2:
    if (nam % 4 == 0) and (nam % 100 !=0 or nam % 400 ==0):
        so_ngay=29
    else:
        so_ngay=28

if so_ngay:
    print (f" Tháng {thang}, năm {nam} có {so_ngay} ngày!")
else:
    print("Tháng nhập vào không hợp lệ.")
    
