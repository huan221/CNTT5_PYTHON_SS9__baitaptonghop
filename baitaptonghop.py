branch_names = [
    "Highlands Nhà Thờ",
    "Highlands Bà Triệu",
    "Highlands Nguyễn Du",
    "Highlands Landmark 81",
    "Highlands Trần Hưng Đạo"
]

daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000]

target_achieved = [True, True, False, True, False]


# ==============================
# HÀM HIỂN THỊ MENU
# ==============================
def show_menu():
    print("\n===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====")
    print("1. Hiển thị báo cáo doanh thu tổng hợp")
    print("2. Thống kê chi nhánh Cao nhất / Thấp nhất")
    print("3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)")
    print("4. Thoát chương trình")
    print("================================================")


def show_report():
    print("\n--- BÁO CÁO DOANH THU ---")

    print(f"{'STT':<5}{'Chi nhánh':<30}{'Doanh thu (VNĐ)':<20}{'Trạng thái'}")

    for i in range(len(branch_names)):
        status = "Đạt" if target_achieved[i] else "Không Đạt"
        print(f"{i+1:<5}{branch_names[i]:<30}{daily_revenues[i]:<20}{status}")

    total = sum(daily_revenues)
    print("-" * 70)
    print(f"Tổng doanh thu: {total:,} VNĐ")


def show_max_min():
    max_value = max(daily_revenues)
    min_value = min(daily_revenues)

    max_index = daily_revenues.index(max_value)
    min_index = daily_revenues.index(min_value)

    print("\n--- THỐNG KÊ ---")
    print(f"Cao nhất: {branch_names[max_index]} - {max_value:,} VNĐ")
    print(f"Thấp nhất: {branch_names[min_index]} - {min_value:,} VNĐ")


def show_failed_branches():
    failed_branches = []

    for i in range(len(branch_names)):
        if not target_achieved[i]:
            failed_branches.append(branch_names[i])

    print("\n--- CƠ SỞ KHÔNG ĐẠT ---")

    if len(failed_branches) == 0:
        print("Tất cả cơ sở đều đạt chỉ tiêu.")
    else:
        print(failed_branches)



while True:
    show_menu()

    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    # Validate input
    if not choice.isdigit():
        print("[Lỗi] Vui lòng nhập số!")
        continue

    choice = int(choice)

    if choice < 1 or choice > 4:
        print("[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập từ 1 đến 4!")
        continue

    # Xử lý chức năng
    if choice == 1:
        show_report()

    elif choice == 2:
        show_max_min()

    elif choice == 3:
        show_failed_branches()

    elif choice == 4:
        print("Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
        break