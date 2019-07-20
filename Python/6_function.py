#function ใน Python มันจะมึนๆหน่อยตรงที่ว่าการสร้าง function ของ python จะต้องขึ้นต้นด้วย def

def printNumber(x):
    print(x)

def squareMyX(x):
    return x*x

def TellName(fname, lname):
    print("My name is " + fname + " " + lname)

x = 5
printNumber(x) #คำสั่งนี้จะ print ค่า x มาให้เรา
print(squareMyX(x))
TellName("Tharathep","Klinla-or")