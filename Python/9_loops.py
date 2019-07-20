i = 0
while i < 5:
    print("i = " + str(i))
    i += 1
print("จบ while loop")

for i in range(10):
    print(i)
    #อันนี้มันจะ resent ค่า i ให้กลายเป็น 0
print("จบ for loop i = 0 -> 10")

for i in range(2,5):
    print(i)
print("จบ for loop i = 2 -> 5")

for i in range (2,30,5):
    print(i)
print("จบ for loop i = 2 -> 7 -> 12 -> ... -> 27")

for x in ["A","B","C"]:
    print(x)
print("จบ loop A B C")

my2Darray = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]
for row in my2Darray:
    print(row)

for row in my2Darray:
    for col in row:
        print(col)


#สร้าง array 2 มิติแบบเรากำหนดเอง
custom2Dmatrix = [[0 for x in range(3)] for y in range(3)]