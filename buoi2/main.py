import math
def is_prime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    for value in range(2,math.ceil(math.sqrt(n))+1):
        if n%value==0:
            return False
    return True
from collections import defaultdict
def phan_tich_thua_so(n):
    thua_so_map = defaultdict(int)
    for value in range(1,n+1):
        if not is_prime(value):
            continue
        while n%value == 0:
            thua_so_map[value] +=1
            n = n//value
    return thua_so_map
def ucln(*a):
    map_thua_so = {}
    thua_so_count = defaultdict(int)
    for value in a:
        map_thua_so[value] = phan_tich_thua_so(value)
        for thua_so in map_thua_so[value]:
            thua_so_count[thua_so] +=1
    uc = []
    for key in thua_so_count.keys():
        if thua_so_count[key] == len(a):
            uc.append(key)
    ucln = 1
    for value in uc:
        ucln*= value
    return ucln
def bcln(*a):
    map_thua_so = {}
    for value in a:
        map_thua_so[value] = phan_tich_thua_so(value)
        
    
        
if __name__ == "__main__":
    print(phan_tich_thua_so(20))
    print(ucln(10,20))