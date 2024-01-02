# Import thư viện random để tạo số ngẫu nhiên
import random

# Tạo một hàm để tạo một câu hỏi cộng hoặc trừ hai số trong phạm vi 20
def tao_cau_hoi():
  # Chọn ngẫu nhiên một phép tính là cộng hoặc trừ
  phep_tinh = random.choice(["+", "-"])
  # Nếu là phép cộng, chọn ngẫu nhiên hai số a và b sao cho a + b <= 20
  if phep_tinh == "+":
    a = random.randint(0, 20)
    b = random.randint(0, 20 - a)
    # Tính kết quả của phép cộng
    ket_qua = a + b
  # Nếu là phép trừ, chọn ngẫu nhiên hai số a và b sao cho a >= b
  else:
    a = random.randint(0, 20)
    b = random.randint(0, a)
    # Tính kết quả của phép trừ
    ket_qua = a - b
  # Tạo một chuỗi chứa câu hỏi với cấu trúc cloze deletion
  # Ví dụ: {{c1::4}} + {{c2::5}} = {{c3::9}}
  cau_hoi = "{{c1::" + str(a) + "}} " + phep_tinh + " {{c2::" + str(b) + "}} = {{c3::" + str(ket_qua) + "}}"
  # Trả về câu hỏi
  return cau_hoi

# Tạo một hàm để tạo một danh sách n câu hỏi
def tao_danh_sach_cau_hoi(n):
  # Tạo một danh sách rỗng để lưu các câu hỏi
  danh_sach_cau_hoi = []
  # Lặp n lần
  for i in range(n):
    # Tạo một câu hỏi bằng hàm tao_cau_hoi
    cau_hoi = tao_cau_hoi()
    # Thêm câu hỏi vào danh sách
    danh_sach_cau_hoi.append(cau_hoi)
  # Trả về danh sách câu hỏi
  return danh_sach_cau_hoi

# Tạo một hàm để ghi một danh sách câu hỏi vào một file .txt
def ghi_file(danh_sach_cau_hoi, ten_file):
  # Mở file .txt với chế độ ghi
  file = open(ten_file, "w")
  # Lặp qua các câu hỏi trong danh sách
  for cau_hoi in danh_sach_cau_hoi:
    # Ghi câu hỏi vào file, kèm theo dấu tab và dòng mới
    file.write(cau_hoi + "\t\n")
  # Đóng file
  file.close()

# Sử dụng các hàm đã tạo để tạo và ghi một danh sách 10 câu hỏi vào file on_tap_toan.txt
danh_sach_cau_hoi = tao_danh_sach_cau_hoi(10)
ghi_file(danh_sach_cau_hoi, "on_tap_toan.txt")