
def decor(func):

    def wrap():
        print("I am doing some boring work before executing " + func.__name__)
        func()
        print("I am doing some boring work after executing "+ func.__name__)
    return wrap


@decor
def simple():
    print('I am simple')


simple()
simple = decor(simple)
# print('After decoration\n\n ')
simple()
