# Bài toán tính tiền điện
'''
    # mô tả bài toán:
    - Đơn giá điện có thể thay đổi tùy theo định mức sử dụng;
    - Tính giá điện tùy theo định mức
    - Các bậc giá điện theo định mức:
        + Bậc 1: từ 0kWh đến 50kWh, giá 1000 vnd/kWh
        + Bậc 2: từ 51kWh đến 100kWh, giá 1500 vnd/kWh
        + Bậc 3: trên 100kWh, giá 2000 vnd/kWh
    - ví dụ:
     Người dùng tiêu thụ: 120kWh
     Giá:
     50kWh đầu tiên = 50*1000 = 50,000
     50kWh tiếp theo (100-50): 50*1500 = 75,000
     20kWh tiếp theo (còn lại): 20*2000=40,000
     Tổng: 50,000+75,000+40,000 = 165,000 vnd
10p

#input: soKwhTieuThu
#output: thanhTien
'''
# Nhập số kw tiêu thụ
sokWh = int(input("Nhập số kWh tiêu thụ:"))
bac_1=50
bac_2=100
gia_bac_1 = 1000
gia_bac_2 = 1500
gia_bac_3 = 2000

if sokWh <= bac_1:
    tien = sokWh*gia_bac_1
elif sokWh <=bac_2:
    tien = bac_1*gia_bac_1 + (sokWh-bac_1)*gia_bac_2
else:
    tien = bac_1*gia_bac_1 + (bac_2-bac_1)*gia_bac_2 + (sokWh-bac_2) * gia_bac_3
    
print(f"Số tiền thanh toán: {tien:.2f} VNĐ")


