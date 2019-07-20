import sys

myNumber = [1,2,3,4,5] #วิธีสร้าง array
#อันนี้คือ array ตัวเลขลองเราซึ่งอันนี้คือการสร้างแบบ array ช่องที่ 0 ถึง 4
print(myNumber)
print(myNumber[0])
print(myNumber[2:])
print(myNumber[:4])
print(myNumber[2:4])
myNumber[0] = 3
print("My number after change: " + str(myNumber))

anotherNumber = [6,7,8,9,10]
myNumber.extend(anotherNumber) #ต่อ array เข้าด้วยกัน
print(myNumber)

myNumber.reverse() #คำสั่งสลับข้าง array
print(myNumber)

myNumber.remove(3) #มันจะเอาตัวเลข 3 ที่มันเจอตัวแรกออกไปให้
print(myNumber)

myNumber.clear() #ล้าง array ทิ้ง

#2D array (ใน Python เหมือนจะเรียกว่า list)
array2D = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]
print("2D array result")
print(array2D[2][1])

print("Stack Result")
#Stack ใน Python ฉบับ array
myStack = []
myStack.append(2) #เพิ่มตัวเลขนี้เข้าท้ายสุด
myStack.append(3)
print(myStack)

myStack.pop() #เอาตัวล่าสุดที่ใส่ไปออกมา
print(myStack)

print("Queue Result")
#Queue ใน Python ฉบับ array
myQueue = []
myQueue.append(3)
myQueue.append(4)
myQueue.append(5)
myQueue.append(6)
myQueue.append(5)

myQueue.pop(0)
print(myQueue) #เอาตัวแรกสุดออกไป

print(myQueue.index(5)) #print เลขตำแหน่งแรกที่มีเลข 5 อยู่

copyQueue = myQueue.copy() #ลอก myQueue เข้าไป copyQueue
