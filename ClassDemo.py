class Demo:
    cls_var = 5000

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = 100
        print('Initiator called for object having id', id(self))
        print('Init method invoked')

    @classmethod
    def class_method(cls):
        print('Class method')

    @staticmethod
    def some_value():
        return 500

    def instance(self):
        print('instance method')


obj = Demo(2, 5)

obj.test = 'My own var'

Demo.cls_var =600

obj2= Demo(5,6)
print(obj.test)

obj.some_value()
Demo.some_value()

obj.instance()     ###  instance(obj)
Demo.class_method()  #### class_method(Demo)






