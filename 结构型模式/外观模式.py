"""
    Description: 外观模式
    Author：Laurent Luo
    Date：2021.08.30
"""
from __future__ import annotations
from abc import ABC

"""
考虑能否在现有子系统的基础上提供一个更简单的接口。 如果该接口能让客户端代码独立于众多子系统类， 那么你的方向就是正确的。

在一个新的外观类中声明并实现该接口。 外观应将客户端代码的调用重定向到子系统中的相应对象处。 如果客户端代码没有对子系统进行初始化， 也没有对其后续生命周期进行管理， 那么外观必须完成此类工作。

如果要充分发挥这一模式的优势， 你必须确保所有客户端代码仅通过外观来与子系统进行交互。 此后客户端代码将不会受到任何由子系统代码修改而造成的影响， 比如子系统升级后， 你只需修改外观中的代码即可。

如果外观变得过于臃肿， 你可以考虑将其部分行为抽取为一个新的专用外观类。
"""

class Facade(ABC):
    _sub_sys_list = []
    def __init__(self, sub_sys1:Sub_System1, sub_sys2:Sub_System2):
       self.sub_sys1 = sub_sys1
       self.sub_sys2 = sub_sys2

    def add_sys(self, subsys):
        self._sys_list.append(subsys)

    def operation(self):
        results = []
        results.append(self.sub_sys1.operation_1())
        results.append(self.sub_sys1.operation_1n())


        # results = []
        results.append(self.sub_sys2.operation_1())
        results.append(self.sub_sys2.operation_2())
        return "\t".join(results)

class Additional_Facade(Facade):
    pass

class Sub_System1():
    def operation_1(self):
        return "opertioan1 {}".format(self.__class__.__name__)
    def operation_2(self):
        return "opertioan2 {}".format(self.__class__.__name__)
    def operation_1n(self):
        return "opertioan_1n {}".format(self.__class__.__name__)

class Sub_System2():
    def operation_1(self):
        return "opertioan1 {}".format(self.__class__.__name__)
    def operation_2(self):
        return "opertioan2 {}".format(self.__class__.__name__)
    def operation_1n(self):
        return "opertioan_1n {}".format(self.__class__.__name__)

def client(facade:Facade):
    print(facade.operation())

if __name__ == '__main__':
    sub1 = Sub_System1()
    sub2 = Sub_System2()
    facade = Facade(sub1,sub2)
    client(facade)