# --- EMERGENCY TRIAGE SYSTEM (FIXED) ---
print("--- EMERGENCY TRIAGE SYSTEM ---")
heart_rate = int(input("Enter patient's heart rate (bpm): "))

# Hệ thống phân loại ưu tiên đã được sửa lại logic
if heart_rate > 120:
    # Điều kiện khắt khe nhất (Nguy kịch) phải được kiểm tra đầu tiên
    print("Priority: RED - Critical condition! Immediate action required.")

elif heart_rate > 100:
    # Nếu rớt xuống đây, máy tính ngầm hiểu heart_rate <= 120 và > 100
    print("Priority: YELLOW - Abnormal. Monitor closely.")

elif heart_rate < 60:
    # Kiểm tra nhịp tim chậm
    print("Priority: BLUE - Bradycardia. Require ultrasound.")

else:
    # Các trường hợp còn lại: Nằm trong khoảng từ 60 đến 100
    print("Priority: GREEN - Stable. Please wait in the lobby.")

print("Triage process completed.")