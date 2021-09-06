"""
    Description: 抽象工厂模式
    Author：Laurent Luo
    Date：2021.08.28
"""
from __future__ import annotations
from abc import ABC, abstractmethod


"""
1.以不同的产品类型与产品变体为维度绘制矩阵。

2.为所有产品声明抽象产品接口。 然后让所有具体产品类实现这些接口。

3.声明抽象工厂接口， 并且在接口中为所有抽象产品提供一组构建方法。

4.为每种产品变体实现一个具体工厂类。

在应用程序中开发初始化代码。 该代码根据应用程序配置或当前环境， 对特定具体工厂类进行初始化。 然后将该工厂对象传递给所有需要创建产品的类。

找出代码中所有对产品构造函数的直接调用， 将其替换为对工厂对象中相应构建方法的调用。


"""
class AbstractFactory(ABC):
    """抽象工厂类
    声明不同创建不同产品的抽象方法

    """
    @abstractmethod
    def create_product_a(self)->AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self)->AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self)->AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self)->AbstractProductB:
        return ConcreteProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self)->AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self)->AbstractProductB:
        return ConcreteProductB2()

class AbstractProductA(ABC):
    """抽象产品类，声明产品类的创建的公开接口

    """
    @abstractmethod
    def useful_function_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self):
        return "创建产品具体产品类A1的实例"

class ConcreteProductA2(AbstractProductA):
    def useful_function_a(self):
        return  "创建产品具体产品类A2的实例"



class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self):
        pass
    @abstractmethod
    def other_useful_function_b(self, coolaborator:AbstractProductA):
        """声明组合产品生产接口，可以与a产品共同组合生产
        :return:
        """
        pass

class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self):
        return "创建产品具体产品类B1的实例"

    def other_useful_function_b(self, coolaborator:AbstractProductA):
        """声明组合产品生产接口，可以与a产品共同组合生产
        :return:
        """
        result = coolaborator.useful_function_a()       # 与产品A组合
        return "创建产品具体产品类B1 与 {}实例".format(result.__class__.__name__)

class ConcreteProductB2(AbstractProductB):
    def useful_function_b(self):
        return "创建产品具体产品类B2的实例"
    def other_useful_function_b(self, coolaborator:AbstractProductA):
        """声明组合产品生产接口，可以与a产品共同组合生产
        :return:
        """
        result = coolaborator.useful_function_a()       # 与产品A组合
        return "创建产品具体产品类B1 与 {}实例".format(result.__class__.__name__)

def client(factory:AbstractFactory)->None:
    """客户端代码

    :param factory:
    :return:
    """
    print("运行工厂 {}".format(factory.__class__.__name__))
    product_a = factory.create_product_a()
    print("创建产品A系列{}".format(product_a.__class__.__name__))
    product_b = factory.create_product_b()
    print("创建产品B系列{}".format(product_b.__class__.__name__))

if __name__ == '__main__':
    client(ConcreteFactory1())      # 调用特定工厂处理
    client(ConcreteFactory2())