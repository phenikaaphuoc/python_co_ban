


def tongtien(so_tien=10,phan_tram_lai = 5.1,so_nam = 10):
    for _ in range(so_nam):
        so_tien+= (phan_tram_lai/100)*so_tien
    return so_tien
def min_nam(so_tien = 10,phan_tram_lai = 5.1,max_tien = 50):
    count = 0
    while so_tien < max_tien:
        so_tien = tongtien(so_tien,phan_tram_lai,1)
        count+=1
    return count
 
 
if __name__ == "__main__":
    print(f"Tong tien : {tongtien()}")
    print(f"So nam it nhat: {min_nam()}")