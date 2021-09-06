"""
    Description: 桥接模式模式
    Author：Laurent Luo
    Date：2021.08.30
"""

from __future__ import annotations
from abc import ABC, abstractmethod
import sys

"""
1.明确类中独立的维度。 抽象/平台， 域/基础设施， 前端/后端或接口/实现。

2.抽象基类中定义业务方法

3.具体抽象类,调用通用实现接口中声明抽象部分所需的业务（统一接口）实现业务方法。

4.为你域内的所有平台创建实现类， 但需确保它们遵循实现部分的接口。

5.在抽象类中添加指向实现类型的引用成员变量。 抽象部分会将大部分工作委派给该成员变量所指向的实现对象。
    5.1如果你的高层逻辑有多个变体， 则可通过扩展抽象基类为每个变体创建一个精确抽象。

6.客户端代码必须将实现对象传递给抽象部分的构造函数才能使其能够相互关联。 此后， 客户端只需与抽象对象进行交互， 无需和实现对象打交道。
"""

class Abstraction:
    """定义所有抽象类的统一接口
        客户端调用抽象基类声明的接口
        维护一个实现类实例
    """
    def __init__(self, implementation: Implementation):
        self.implementation = implementation

    def operation(self):
        return "self.operation.operation_implementation {}".format(self.implementation.operation_implementation)


class ExtendAbstraction(Abstraction):
    def operation(self):
        # super().operation()
        return "self.operation.operation_implementation {}".format(sys._getframe().f_code.co_name)



class Implementation(ABC):
    def operation_implementation(self):
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "concreteImplementationA : customize for A"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "concreteImplementationB : customize for B"

def client_code(abstraction:Abstraction)->None:
    print(abstraction.operation())


if __name__ == '__main__':
    imp = ConcreteImplementationA()
    absA = Abstraction(imp)
    client_code(absA)

    imp = ConcreteImplementationB()
    absA = ExtendAbstraction(imp)
    client_code(absA)
