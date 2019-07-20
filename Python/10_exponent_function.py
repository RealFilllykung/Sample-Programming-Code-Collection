print(str(2**3)) # = 2^3

#คราวนี้ลองมาสร้าง function exponent function กัน

def myExponent(x,y):
    temp = x
    for i in range(y-1):
        x *= temp
    print(x)

myExponent(2,3)