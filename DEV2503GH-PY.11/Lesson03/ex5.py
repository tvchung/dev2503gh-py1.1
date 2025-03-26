'''
Bài toán tính tiền tiêu thụ nước của hộ gia đình yêu cầu tính toán số tiền mà một hộ gia đình phải trả cho lượng nước sử dụng trong một kỳ hóa đơn, dựa trên số nước tiêu thụ (m3) và các mức giá nước khác nhau tùy thuộc vào bậc sử dụng.

Các yếu tố cần xem xét trong bài toán:
Số lượng nước tiêu thụ: Số nước mà hộ gia đình sử dụng trong một kỳ hóa đơn, được tính bằng đơn vị mét khối (m³).
Đơn giá nước: Các mức giá cho từng bậc sử dụng. Giá nước có thể tăng dần theo số lượng nước tiêu thụ. Ví dụ, mức giá cho lượng nước sử dụng trong một khoảng từ 0 đến một giá trị nhất định sẽ rẻ hơn so với mức giá cho lượng nước vượt quá mức đó.
Các bậc giá nước: Mỗi mức tiêu thụ có một đơn giá khác nhau, ví dụ:
Bậc 1: 0 - 10 m³, giá 5,000 VND/m³.
Bậc 2: 11 - 20 m³, giá 8,000 VND/m³.
Bậc 3: Trên 20 m³, giá 12,000 VND/m³.
Các bước giải bài toán:
Tính toán số tiền cho mỗi bậc: Đối với mỗi bậc sử dụng nước, tính số tiền tương ứng và cộng dồn lại.
Nếu số nước tiêu thụ nhỏ hơn hoặc bằng giới hạn của một bậc, chỉ tính tiền cho bậc đó.
Nếu số nước tiêu thụ vượt qua giới hạn của một bậc, tính tiền cho toàn bộ số nước trong bậc đó và tiếp tục với các bậc cao hơn.
Kết quả trả về: Tổng số tiền phải trả cho việc sử dụng nước.
Ví dụ về cách tính tiền tiêu thụ nước:
Giả sử bạn có các bậc giá nước như sau:

Bậc 1: 0 - 10 m³, giá 5,000 VND/m³.
Bậc 2: 11 - 20 m³, giá 8,000 VND/m³.
Bậc 3: Trên 20 m³, giá 12,000 VND/m³.
Nếu hộ gia đình sử dụng 25 m³ nước, cách tính tiền sẽ như sau:

Tính tiền cho 10 m³ đầu tiên (Bậc 1): 10×5000=50,00010×5000=50,000 VND.
Tính tiền cho 10 m³ tiếp theo (Bậc 2):10×8000=80,00010×8000=80,000 VND.
Tính tiền cho 5 m³ còn lại (Bậc 3): 5×12000=60,0005×12000=60,000 VND.
Tổng tiền = 50,000 + 80,000 + 60,000 = 190,000 VND.
'''