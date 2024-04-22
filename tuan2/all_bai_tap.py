
def bai1_tao_tap_hop():
    for i in range(100):
        print(i)
def bai2_tao_tap_hop_le():
    for i in range(1,200,2):
        print(i)
def bai3_max_min():
    data = [float(i) for i in  input("Nhap vao 1 chuoi so nguyen cach nhau boi dau cach: ").split(" ")]
    print(f"Max: {max(data)} , Min: {min(data)}")
def bai4_ten_hoc_sinh():
    all_ten  = []
    while True:
        data = input("Nhap vao ten: ")
        all_ten.append(data)
        if len(data.replace(" ","")) == "":
            break
    for ten in all_ten:
        print(ten)
def bai5_so_duong(N):
    N = abs(N)
    result = []
    for i in range(1,N+1):
        if N%i==0:
            result.append(i)
    return result
def bai6_uoc_chung(a,b):
    uoc_a , uoc_b = bai5_so_duong(a),bai5_so_duong(b)
    return set(uoc_a) & set(uoc_b)
def bai7_dem_so_khac_nhau(data):
    data = set([float(i) for i in data.split(";") ])
    return len(data)
def bai8_vietlot():
    so_nguoi = int(input("Nhap vao so nguoi: "))
    all_bo_so = {}
    for i in range(so_nguoi):
        all_bo_so[i] = []
        for so_th in range(6):
            all_bo_so[i].append(input(f"Nhap so thu {so_th} cua nguoi thu {i+1}:"))
    first_price = []
    for i in range(6):
        first_price.append(input(f"Nhap so thu {i} cua giai dac biet: "))
    first_price = set(first_price)
    for nguoi in all_bo_so.keys():
        bo_so = all_bo_so[nguoi]
        if len(set(bo_so) & first_price) >= 5:
            print(f"Nguoi thu {nguoi} thang cuoc voi bo so ",bo_so)
bai8_vietlot()
