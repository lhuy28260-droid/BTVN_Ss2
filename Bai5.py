import sys

print("=== HỆ THỐNG KIOSK TIẾP NHẬN BỆNH NHÂN ===")
print("Vui lòng nhập các thông tin sau theo đúng định dạng được hướng dẫn:\n")

try:
    
    patient_name = input("1. Họ và tên bệnh nhân (VD: Nguyen Van A): ").strip()
    
    
    patient_age = int(input("2. Tuổi của bệnh nhân (VD: 25): "))
    spo2_level = float(input("3. Nồng độ oxy trong máu - SpO2 (%) (VD: 98): "))
    heart_rate = int(input("4. Nhịp tim (nhịp/phút) (VD: 85): "))
    
    # Sử dụng .lower() và .strip() để chuẩn hóa câu trả lời về định dạng chuẩn
    has_insurance = input("5. Bệnh nhân có thẻ BHYT không? (Chỉ gõ 'yes' hoặc 'no'): ").strip().lower()

except ValueError:
    print("\n[LỖI HỆ THỐNG] Dữ liệu nhập vào không đúng định dạng số! Vui lòng khởi động lại Kiosk.")
    sys.exit()



#  Quy tắc Phân luồng y khoa (Triage)
if spo2_level < 90 or heart_rate > 120:
    triage_result = "BÁO ĐỘNG ĐỎ (Cấp cứu khẩn)"
elif (90 <= spo2_level <= 95) or (100 <= heart_rate <= 120):
    triage_result = "BÁO ĐỘNG VÀNG (Theo dõi sát)"
else:
    triage_result = "XANH (Khám thường)"


BASE_FEE = 500000

if patient_age < 6 or patient_age >= 80:
    final_fee = 0
elif has_insurance == 'yes':
    final_fee = int(BASE_FEE * 0.5) # Giảm 50%
else:
    final_fee = BASE_FEE


# PHẦN 3: XUẤT BÁO CÁO 
print("\n" + "=" * 45)
print("PHIẾU KHÁM BỆNH ĐIỆN TỬ".center(45))
print("=" * 45)
print(f"Họ và tên     : {patient_name.title()}")
print(f"Tuổi          : {patient_age}")
print(f"Chỉ số sinh tồn: SpO2 = {spo2_level}%, Nhịp tim = {heart_rate} bpm")
print("-" * 45)
print(f"PHÂN LUỒNG    : {triage_result}")
print(f"TẠM ỨNG       : {final_fee:,} VNĐ")
print("=" * 45)


print("\n>>> SYSTEM LOG: KIỂM TRA KIỂU DỮ LIỆU <<<")
print(f"patient_name  : {type(patient_name)}")
print(f"patient_age   : {type(patient_age)}")
print(f"spo2_level    : {type(spo2_level)}")
print(f"heart_rate    : {type(heart_rate)}")
print(f"has_insurance : {type(has_insurance)}")
print(">>> END OF LOG <<<")