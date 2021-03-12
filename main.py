from abc import ABCMeta, abstractmethod

class myABSClass:
    @abstractmethod
    def __init__(self, num = 0):
        self.number = num

class myClass(myABSClass):
    def __init__(self, num):# конструктор для инициализации
        super().__init__(num)

    def myFunc(self, arg):
        if arg >= 0 and arg <= 7:
            print("Вам в детский сад!")
        elif arg >= 7 and arg <= 18:
            print("Вам в школу!")
        elif arg >= 18 and arg <= 25:
            print("Вам в профессиональное учебное заведение!")
        elif arg >= 25 and arg <= 60:
            print("Вам на работу!")
        elif arg >= 60 and arg <= 120:
            print("Вам предоставляется выбор")
        else:
            for i in range(5):
                print("Ошибка!")

# chislo = int(input("Введите число : "))
#
# obj = myClass(chislo)
#
# print(obj.myFunc(chislo))

# class myClass:
#     def __init__(self, num):# конструктор для инициализации
#         self.n = num
#
#     def myFunc(self, arg):
#         if arg >= 0 and arg <= 7:
#             print("Вам в детский сад!")
#         elif arg >= 7 and arg <= 18:
#             print("Вам в школу!")
#         elif arg >= 18 and arg <= 25:
#             print("Вам в профессиональное учебное заведение!")
#         elif arg >= 25 and arg <= 60:
#             print("Вам на работу!")
#         elif arg >= 60 and arg <= 120:
#             print("Вам предоставляется выбор")
#         else:
#             for i in range(5):
#                 print("Ошибка!")
#
# chislo = int(input("Введите число : "))
#
# obj = myClass(chislo)
#
# print(obj.myFunc(chislo))

class myClass1:
    def __init__(self, arg):
        self.arg = int(arg)

    def one_three(self, arg):
        pass
        if 1 <= arg <= 3:
            s = input('Введите строку : ')
            i = int(input('Сколько раз повторить число : '))
            for j in range(i):
                print(s)

    def four_six(self, arg):
        if 4 <= arg <= 6:
            st = int(input('Введите степень : '))
            import math
            print(math.pow(int(arg),st))
    def seven_nine(self, arg):
        if 7 <= arg <= 9:
            for i in range(10):
                arg += 1
    def excep(self):
        print('ERROR!')

# q = int(input('Введите число : '))
# obj = myClass1(q)
#
# print(obj.one_three(q))
# print(obj.four_six(q))
# print(obj.seven_nine(q))
# print(obj.excep())
#
#
class myClass3(myClass,myClass1):
    def __init__(self, num1, num2):
        self.n = num1
        self.n2 = num2
    def show(self):
        print(self.n,self.n2)

obj3 = myClass3(4,5)
print(obj3.show())
