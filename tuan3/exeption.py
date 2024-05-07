# 
def bai1():

    try:
        a = int(input("Nhap vao so a: "))
        b = int(input("Nhap vao so b: "))
        print(a/b)
    except TypeError:
        raise ("Gia tri phai la so")
    except ValueError:
        raise ("Gia tri phai la so nguyen")
    except ZeroDivisionError as e:
        raise("Nhap sai gia tri b phai khac 0")
def bai2():
    try:
        a = float(input("Nhap vao so a: "))
        b = float(input("Nhap vao so b: "))
        c = float(input("Nhap vao so c: "))
        if a<=0 or b <=0 or c<=0:
            raise ValueError("Gia tri lon hon 0 ")
        if a+b <= c or b+c <= a or a+c <= b:
            raise ValueError("Day khong phai la 3 canh tam giac ")
            
    except TypeError:
        raise("Gia tri phai la so")

    
    
# bai1()
bai2()