
# Chuong trinh tinh diem trung binh sinh vien

print("CHUONG TRINH TINH DIEM TRUNG BINH")

ten = input("Nhap ho ten sinh vien: ")

diem1 = float(input("Nhap diem mon 1: "))
diem2 = float(input("Nhap diem mon 2: "))
diem3 = float(input("Nhap diem mon 3: "))

trung_binh = (diem1 + diem2 + diem3) / 3

print("\n--- KET QUA ---")
print("Ho ten:", ten)
print("Diem trung binh:", round(trung_binh, 2))

if trung_binh >= 8:
    print("Xep loai: Gioi")
elif trung_binh >= 6.5:
    print("Xep loai: Kha")
elif trung_binh >= 5:
    print("Xep loai: Trung binh")
else:
    print("Xep loai: Yeu")
