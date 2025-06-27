import pandas as pd

cot_chi_tieu = ["Ăn sáng", "Ăn trưa", "Ăn tối"]

ngay_tuan1 = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật"]
du_lieu_tuan1 = [
    [0, 0, 0],
    [0, 0, 20],
    [15, 25 + 2200000, 20],
    [18, 28 + 123000, 0],
    [20, 35, 20 + 25],
    [0, 20, 30],
    [15, 30, 0],
]

df1 = pd.DataFrame(du_lieu_tuan1, columns=cot_chi_tieu)
df1.insert(0, "Ngày", ngay_tuan1)
df1["Tổng cộng"] = df1[cot_chi_tieu].sum(axis=1)

ngay_tuan2 = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật"]
du_lieu_tuan2 = [
    [3, 18, 30],
    [20, 30, 40 + 22],
    [20, 18, 170],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]

df2 = pd.DataFrame(du_lieu_tuan2, columns=cot_chi_tieu)
df2.insert(0, "Ngày", ngay_tuan2)
df2["Tổng cộng"] = df2[cot_chi_tieu].sum(axis=1)

with pd.ExcelWriter("chi_tieu_tuan.xlsx") as writer:
    df1.to_excel(writer, sheet_name="Tuần 1", index=False)
    df2.to_excel(writer, sheet_name="Tuần 2", index=False)

print("Đã tạo file chi_tieu_tuan.xlsx thành công!")
