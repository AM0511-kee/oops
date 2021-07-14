#we are inheriting the classes
class A:
    def __init__(self):
        print('in A init')

    def func(self):
        print('in func A')

class B(A):
    def __init__(self):
        #super(). can be used for inheriting all the functions of parent class
        super(). __init__()
        print('in B init')

    def func(self):
        print('in B func')

# multi-level inheriting
class C(B):
    def __init__(self):
        super(). __init__()
        print('in C init ')

    def func(self):
        print('in c func')

o=C()
o.func()

#multiple inheriting

class D():
    def __init__(self):
        print('in D init ')

    def func(self):
        print('in D func')

class E():
    def __init__(self):
        print('in E init ')

    def func(self):
        print('in E func')

class F(E,D):
    def __init__(self):
        super(). __init__()
        print('in F init ')
    
    def func(self):
        print('in F func')

f=F()
f.func
