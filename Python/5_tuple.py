#Tuple จะคล้ายๆ array แต่เป็น array ที่แก้ไม่ได้

myArray = [3,4] #วิธีสร้าง array แบบปกติ
myTuple = (3,4) #วิธีสร้าง tuple

myArray[0] = 6
#myTuple[0] = 6  <-- คำสั่งนี้จะ return error ออกมา

print(myArray[0])
print(myTuple[0])