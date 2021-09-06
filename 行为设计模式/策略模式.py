
"""
    Description: 策略模式
    Author：Laurent Luo
    Date：2021.09.06
"""
from __future__ import annotations
from abc import ABC,abstractmethod
"""
从上下文类中找出修改频率较高的算法 （也可能是用于在运行时选择某个算法变体的复杂条件运算符）。

声明该算法所有变体的通用策略接口。

将算法逐一抽取到各自的类中， 它们都必须实现策略接口。

在上下文类中添加一个成员变量用于保存对于策略对象的引用。 然后提供设置器以修改该成员变量。 上下文仅可通过策略接口同策略对象进行交互， 如有需要还可定义一个接口来让策略访问其数据。

客户端必须将上下文类与相应策略进行关联， 使上下文可以预期的方式完成其主要工作。
"""

class Contenxt:
    def __init__(self):
        self._strategy =None
    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy:Base_strategy):
        self._strategy = strategy

    def operation(self):
        self._strategy.exexute()

class Base_strategy(ABC):
    @abstractmethod
    def execute(self):
        pass

class Concrete_strategy1(Base_strategy):
    def execute(self):
        print("strategy 1")


class Concrete_strategy2(Base_strategy):
    def execute(self):
        print("strategy 2")


def client(context:Contenxt):
    print("running")
    context.operation()

if __name__ == '__main__':
    context = Contenxt()
    context.strategy = Concrete_strategy1()
    client(context)
    context.strategy = Concrete_strategy2()
    client(context)

