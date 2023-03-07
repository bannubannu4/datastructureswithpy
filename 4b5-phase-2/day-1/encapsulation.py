#protected
class encap:
    _a=10
    b=40
    def encapfuntion(self):
        _c=200
        print("Encap function=accessing protection:", self._a+50)
       # print(self._a+50)
obj=encap()
print(obj._a)
obj.encapfuntion()
print("b=",obj.b)