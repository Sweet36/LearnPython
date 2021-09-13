'''

定义一个类
'''

class Person:

    #静态属性
    name = None
    gender = "男"
    age = 0
    #私有属性
    __money = 3000


    def __init__(self,name,gender,age):
        self.name = name
        self.age = age
        self.gender = gender
        pass
    #动态方法
    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print("sleep")
    def running(self):
        print("running")
    def have_money(self):
        return self.__money

#实例化一个人
person1 = Person("张三","男","23")
print(person1.name)
person1.eat()

# person2 =  Person()
# print(person2.age)
person2 =Person('李四','女','24')
print(person2.age)
print(person2.have_money())
print(dir(person2))