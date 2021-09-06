"""
    Description: 策略模式
    Author：Laurent Luo
    Date：2021.09.06
"""
from __future__ import annotations
from abc import ABC, abstractmethod
"""
1.拆解目标算法流程的步骤
    1.1 从子类继承考虑，考虑哪些步骤能够通用，哪些步骤各不相同。

2.创建抽象基类并声明一个模板方法和代表算法步骤的一系列抽象方法。 
    2.1声明默认步骤与抽象定制步骤
    2.2根据算法结构依次调用相应步骤。 可用 final最终修饰模板方法以防止子类对其进行重写。
    2.3可考虑在算法的关键步骤之间添加钩子（非必须重写流程）。

3.为每个算法变体新建一个具体子类，
    3.1必须实现所有的抽象步骤， 也可以重写部分可选步骤。

"""
class Abstract_class:
    def template_operations(self):
        """
        声明算法流程步骤
        :return:
        """
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.hook1()
        self.required_operation2()
        self.hook2()

    def base_operation1(self):
        pass

    def base_operation2(self):
        pass

    # 用于子类必须重写的方法
    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def required_operation2(self):
        pass

    # 声明钩子方法，为非必须重写、非默认的步骤提供接口
    def hook1(self):
        pass

    def hook2(self):
        pass

class Concrete_class1(Abstract_class):
    def required_operation1(self):
        print("concreteclass 1 cunstomized operation1")

    def required_operation2(self):
        print("concreteclass 1 customized operation2")

class Concrete_Class2(Abstract_class):
    def required_operation1(self):
        print("concreteclass 2 cunstomized operation 1")

    def required_operation2(self):
        print("concreteclass 2 customized operation 2")

def client(abstract_class:Abstract_class):
    abstract_class.template_operations()

if __name__ == '__main__':
    client(Concrete_class1())
    client(Concrete_Class2())