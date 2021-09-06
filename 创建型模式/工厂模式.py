"""
    Description: 工厂模式
    Author：Laurent Luo
    Date：2021.08.28
"""
from __future__ import annotations
from abc import ABC, abstractmethod

"""
    1.让所有产品都遵循同一接口。
    2.在创建类中添加一个空的工厂方法。 该方法的返回类型必须遵循通用的产品接口。
    3.在创建者代码中找到对于产品构造函数的所有引用。 创建产品的代码移入工厂方法。
    4.工厂方法switch分支运算符， 用于选择各种需要实例化的产品类。
    5.现在， 为工厂方法中的每种产品编写一个创建者子类， 然后在子类中重写工厂方法， 并将基本方法中的相关创建代码移动到工厂方法中。
    6.如果应用中的产品类型太多， 那么为每个产品创建子类并无太大必要， 这时你也可以在子类中复用基类中的控制参数。
    7.如果代码经过上述移动后， 基础工厂方法中已经没有任何代码， 你可以将其转变为抽象类。 如果基础工厂方法中还有其他语句， 你可以将其设置为该方法的默认行为。
"""


class Creator(ABC):
    """创建工厂方法
        声明通用产品创建接口
    """
    @abstractmethod
    def factory_method(self):
        """声明产品创建抽象方法
        :return:
        """
        pass

    def some_operation(self):
        """声明外部接口
        :return:
        """
        product = self.factory_method()
        result = "创造类实例：: {}".format(product.__class__.__name__)
        return result

class ConcreteCreator1(Creator):
    """方法的签名仍是creator，外部对象统一调用creator类的统一接口
    """
    def factory_method(self) ->Product:
        print("生成产品{}".format(self.__class__.__name__))
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) ->Product:
        print("生成产品{}".format(self.__class__.__name__))
        return ConcreteProduct2()


class Product(ABC):
    """抽象产品类
        声明了具体产品类的统一外部调用接口

    """
    pass

class ConcreteProduct1(Product):
    def operation(self)->str:
        return "operation result from ConcreteProduct1 "

class ConcreteProduct2(Product):
    def operation(self)->str:
        return "operation result from ConcreteProduct1 "


def cilent_mode(creator:Creator)->None:
    """客户端方法
    调用具体工厂类

    :param creator:
    :return:
    """

    print("客户端生成相应产品, {}".format(creator.some_operation()))

if __name__ == '__main__':
    cilent_mode(ConcreteCreator1())
    cilent_mode(ConcreteCreator2())

