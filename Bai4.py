import sys

print("--- HỆ THỐNG SÀNG LỌC TIỀN PHẪU THUẬT ---")
try:
    tuoi = int(input("Nhập tuổi bệnh nhân (Age): "))
    huyet_ap = int(input("Nhập huyết áp tâm thu (mmHg): "))
    duong_huyet = int(input("Nhập đường huyết (mg/dL): "))
except ValueError:
    print("LỖI CÚ PHÁP: Vui lòng chỉ nhập số nguyên!")
    sys.exit()


if tuoi < 0 or huyet_ap < 0 or duong_huyet < 0:
    print("LỖI: Dữ liệu nhập vào không hợp lệ (Chỉ số y khoa không được là số âm).")
    sys.exit()


print("\n" + "=" * 45)
print("KẾT QUẢ SÀNG LỌC".center(45))
print("=" * 45)

if tuoi >= 75:
    print("=> TỪ CHỐI PHẪU THUẬT.")
    print("   Lý do: Bệnh nhân đã trên ngưỡng 75 tuổi.")

elif huyet_ap < 90 or huyet_ap > 140:
    print("=> TỪ CHỐI PHẪU THUẬT.")
    print(f"   Lý do: Huyết áp ({huyet_ap} mmHg) nằm ngoài giới hạn an toàn (90-140).")

elif duong_huyet >= 150:
    print("=> TỪ CHỐI PHẪU THUẬT.")
    print(f"   Lý do: Đường huyết ({duong_huyet} mg/dL) vượt mức cho phép (< 150).")

else:
    # Nếu vượt qua tất cả các "bức tường" phía trên, bệnh nhân đủ điều kiện
    print("=> ĐỦ ĐIỀU KIỆN PHẪU THUẬT.")
    print("   Bệnh nhân đáp ứng toàn bộ các chỉ số sinh tồn cơ bản.")

print("=" * 45)