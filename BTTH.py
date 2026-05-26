import datetime

ten = input("Nhập tên bệnh nhân: ").strip()
if not ten:
    print("Lỗi: Tên không được để trống")
    exit()

nam_sinh = int(input("Nhập năm sinh: "))
nam_hien_tai = datetime.date.today().year
if nam_sinh < 1900 or nam_sinh > nam_hien_tai:
    print(f"Lỗi: Năm sinh phải từ 1900 đến {nam_hien_tai}")
    exit()

so_ngay_benh = int(input("Nhập số ngày bị bệnh: "))
if so_ngay_benh < 0:
    print("Lỗi: Số ngày bị bệnh không được nhỏ hơn 0")
    exit()

nhiet_do = float(input("Nhập nhiệt độ cơ thể (°C): "))
if nhiet_do < 30 or nhiet_do > 45:
    print("Lỗi: Nhiệt độ không hợp lệ (phải từ 30°C đến 45°C)")
    exit()

chi_phi_kham = float(input("Nhập chi phí khám: "))
if chi_phi_kham <= 0:
    print("Lỗi: Chi phí khám phải lớn hơn 0")
    exit()

# --- TÍNH TOÁN THÔNG TIN ---
tuoi = nam_hien_tai - nam_sinh
phu_phi = 0.1 * chi_phi_kham
tong_chi_phi = chi_phi_kham + phu_phi

# --- PHÂN LOẠI SỨC KHỎE ---
if nhiet_do > 38 and so_ngay_benh > 3:
    tinh_trang = "Nguy hiểm"
elif nhiet_do > 38:
    tinh_trang = "Sốt cao"
elif nhiet_do > 37.5:
    tinh_trang = "Sốt nhẹ"
else:
    tinh_trang = "Bình thường"


if tinh_trang == "Nguy hiểm":
    uu_tien = "Cấp cứu" if tuoi > 60 else "Ưu tiên cao"
else:
    uu_tien = "Bình thường"

# -- ĐÁNH GIÁ CHI PHÍ (Toán tử 3 ngôi) --
muc_chi_phi = "Cao" if tong_chi_phi > 500000 else "Thấp"

# --- XUẤT KẾT QUẢ ---
print("-" * 40)
print(f"BỆNH NHÂN: {ten.upper()} - {tuoi} TUỔI")
print(f"Tình trạng: {tinh_trang}")
print(f"Mức độ ưu tiên: {uu_tien}")
print(f"Tổng chi phí: {tong_chi_phi:,.0f} VNĐ ({muc_chi_phi})")
print("-" * 40)