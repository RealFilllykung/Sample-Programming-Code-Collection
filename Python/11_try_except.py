#try except มันคือ try catch ในภาษาอื่น

try:
    number = int(input("ใส่เลขมา 1 เลข: ")) #ถ้าใส่อย่างอื่นที่ไม่ใช่ int จะ return ValueError
    division = 10/number #ถ้าใส่เลข 0 มามันจะ DivideByZeroError
except ZeroDivisionError: 
    print("หาร 0 ไม่ได้")
except ValueError:
    print("Value Error นะ")