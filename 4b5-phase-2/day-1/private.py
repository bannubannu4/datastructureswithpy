#private
class encap:
    __a=10
    print("a=",__a)
    #b=40
    def encapfuntion(self):
        __c=200
        print("Encap function=accessing private:", self.__a+50)
       # print(self._a+50)
obj=encap()
#print(obj._a)
obj.encapfuntion()
print("b=",obj.__b)