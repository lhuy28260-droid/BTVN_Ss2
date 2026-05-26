import sys

# NHẬP LIỆU VÀ XỬ LÝ BẪY DỮ LIỆU 

ten_benh_nhan = input("Nhập họ và tên bệnh nhân: ").strip()

# Tên bỏ trống hoặc chỉ toàn khoảng trắng
if not ten_benh_nhan:
    print("LỖI: Tên bệnh nhân không hợp lệ (không được để trống)!")
    sys.exit() # Dừng chương trình ngay lập tức

# Khối try-except giúp chống sập hệ thống nếu lễ tân vô tình gõ chữ thay vì gõ số
try:
    tuoi = int(input("Nhập tuổi của bệnh nhân: "))
except ValueError:
    print("LỖI: Tuổi phải là một số nguyên!")
    sys.exit()

#  Tuổi phi logic
if tuoi < 0 or tuoi > 150:
    print("LỖI: Tuổi nằm ngoài phạm vi con người (0-150)!")
    sys.exit()


#  XỬ LÝ QUY TẮC PHÂN LUỒNG TỰ ĐỘNG

if tuoi < 6:
    ket_qua = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
elif tuoi >= 80:
    ket_qua = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
else:
    ket_qua = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."


# BƯỚC 4: XUẤT PHIẾU KHÁM BỆNH ĐIỆN TỬ
print("\n" + "=" * 50)
print("             PHIẾU KHÁM BỆNH ĐIỆN TỬ")
print("=" * 50)
# Dùng hàm .title() để tự động viết hoa chữ cái đầu của mỗi từ trong tên
print(f"Họ và tên bệnh nhân : {ten_benh_nhan.title()}")
print(f"Tuổi                : {tuoi}")
print("-" * 50)
print(f"KẾT QUẢ PHÂN LUỒNG  : \n{ket_qua}")
print("=" * 50)