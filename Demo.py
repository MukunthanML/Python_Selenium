class A:
    def process(self):
        print('A process')

class B(A):
    def process(self):
        print('B process')


class C(B):
    pass

def a():
    pass

b = a

b()
a()


obj = C()
obj.process()
# print(C.mro())   # print MRO for class C
