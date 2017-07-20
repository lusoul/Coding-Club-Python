#coding=utf-8

class Animal(object):
    def run(self):
        print "Animal is running"

class Dog(Animal):
    def run(self):
        print "Dog is running"

class Cat(Animal):
    def run(self):
        print "Cat is running"

dog = Dog()
cat = Animal() # 这句话其实没意义，变成 子=父？ 我们要的是父=子
dog.run() # Dog is running
cat.run() # Animal is running
print isinstance(dog, Animal) # True

# 多肽
def runTwice(animal):
    animal.run()
    animal.run()

runTwice(Dog()) # Dog is running & Dog is running
runTwice(Animal()) # Animal is running & Animal is running

print dir(dog)

class MyDog(object):
    def __len__(self):
        return 100
    def __hash__(self):
        return 1000 # 必须返回integer，否则会出错
print len(MyDog()) # 100
print hash(MyDog()) # 1000
