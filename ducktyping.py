#duck typing :where an object of an class is passed as an argument to another classes
class pycharm:
    def execute(self):
        print('it will execute')
        print('it will compile')
        print('it has various libaries')
        print('heavy compiler')

class vs_code:
    def execute(self):
        print('it will execute')
        print('it will compile')
        print('make u go made')
        print('connects to github repository')

class atom:
    def execute(self):
        print('it will execute')
        print('it will compile')
        print('it has various libaries')
        print('connects to github repository')
        print('light editor')

def all_compiler(obj):
    obj.execute()

x=pycharm()
all_compiler(x)
