"""
    Description: 生成器模式
    Author：Laurent Luo
    Date：2021.08.29
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
"""
1.清晰地定义通用步骤， 确保它们可以制造所有形式的产品。

2.在基本生成器接口中声明这些步骤。

3.为每个形式的产品创建具体生成器类， 并实现其构造步骤。

4.实现获取构造结果对象的方法。

4.创建主管类。 它可以使用同一生成器对象来封装多种构造产品的方式。

5.客户端代码会同时创建生成器和主管对象。 构造开始前， 客户端必须将生成器对象传递给主管对象。 
    5.1 通常情况下， 客户端只需调用主管类构造函数一次即可。 主管类使用生成器对象完成后续所有制造任务。 
    5.2 还有另一种方式， 那就是客户端可以将生成器对象直接传递给主管类的制造方法。

6.只有在所有产品都遵循相同接口的情况下， 构造结果可以直接通过主管类获取。 否则， 客户端应当通过生成器获取构造结果。
"""

class Builder(ABC):
    """抽象生成器类
    声明所有类型生成的的通用产品接口
    """
    @property
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass

class Concrete_Builder1(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product1()

    @property
    def product(self):
        """为具体生成器类绑定特定的产品
        由于不同产品生成方式不相同，因此需要单独声明每一个生成器对应的产品（作为实例特性绑定）
        完成单个产品生成后，实例开始准备生成下一个产品

        :return:
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self):
        self._product.add("CB1 step A1")

    def produce_part_b(self):
        self._product.add("CB1 step B1")

    def produce_part_c(self):
        self._product.add("CB1 step C1")




class Director():
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()

    #
    # def make(self):
    #     print("use {} builder product".format(self.builder.__class__.__name__))
    #     product = self.builder.get_result()
    #     return product

class Product1():
    """
    产品实例与每一个具体生成器绑定，不同生成器生产的产品可能完全不同。因此不建议在生成器基类定义统一接口
    """
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print("Product parts: {}".format(', '.join(self.parts)))


if __name__ == '__main__':
    cb1 = Concrete_Builder1()
    director = Director()
    director.builder = cb1

    director.build_minimal_viable_product()
    cb1.product.list_parts()    # 嵌套调用的时候可以将中间方法构建为属性


    director.build_full_featured_product()
    # product1 = director.builder.product()
    director.builder.product.list_parts()
    #

    # 添加部件后，以product产品形式输出
    print("Custom product: ")
    cb1.produce_part_a()
    cb1.produce_part_b()
    cb1.product.list_parts()




