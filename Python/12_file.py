myFile = open("e:/Programming Code Practice/Python/ReadMe.txt","r") #อ่านไฟล์จาก directory


#print(myFile.readable) #มันจะบอกว่าไฟล์นี้อ่านได้มั้ย
#print(myFile.read()) #อันนี้มันจะอ่านไฟล์ทั้งหมดเลย

print(myFile.readline())
print(myFile.readline())
#เวลาเปิดไฟล์ต้องปิดตลอด

myFile.close()

myFile = open("e:/Programming Code Practice/Python/ReadMe.txt","a")
myFile.write("\nFanta, 15THB")

myFile.close()