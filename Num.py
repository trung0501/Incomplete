def so_khong_day_du(x):
    tong = 0
    for i in range (1,x):
        if x % i == 0:
            tong = tong + i
    return tong < x

def so_giau_co(x):
    tong = 0
    for i in range (1,x):
        if x % i == 0:
            tong = tong + i
    return tong > x

n = int(input('Nhap so nguyen:'))
print()
print('Day cac so khong day du trong cac so tu 1 den',n,'la:')
for i in range (1, n+1):
    if so_khong_day_du(i):
        print(i,end = ' ')
print()
print()
print('Day cac so giau co trong cac so tu 1 den',n,'la:')
for i in range (1, n+1):
    if so_giau_co(i):
        print(i,end = ' ')