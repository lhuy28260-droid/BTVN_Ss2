print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

# Hệ thống kiểm tra điều kiện hiến máu
# Sử dụng toán tử 'and' để bắt buộc ĐỒNG THỜI thỏa mãn 2 điều kiện
if donor_age >= 18 and donor_weight >= 50:
    print("\nResult: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("\nResult: NOT ELIGIBLE. Thank you for your interest.")
    
    # Phân tích và nêu rõ lý do từ chối
    print("Lý do từ chối:")
    if donor_age < 18 and donor_weight < 50:
        print("- Chưa đủ tuổi quy định (Yêu cầu >= 18).")
        print("- Không đủ cân nặng tiêu chuẩn (Yêu cầu >= 50kg).")
    elif donor_age < 18:
        print("- Chưa đủ tuổi quy định (Yêu cầu >= 18).")
    elif donor_weight < 50:
        print("- Không đủ cân nặng tiêu chuẩn (Yêu cầu >= 50kg).")