"""
    Description: 访问者模式
    Author：Laurent Luo
    Date：2021.09.06
"""
from __future__ import annotations
from abc import ABC,abstractmethod
from typing import List
"""
1.确定访问者和元素类。
    1.1在访问者接口中声明一组 “访问” 方法， 分别对应程序中的每个具体元素类。
2.声明元素接口。 
    2.1如果程序中已有元素类层次接口， 
        可在层次结构基类中添加抽象的 “接收” 方法。 该方法必须接受访问者对象作为参数。

3.在所有具体元素类中实现接收方法。 
    3.1这些方法必须将调用重定向到【当前元素】对应的【访问者对象】中的【访问者方法】。（双分派机制）

4.元素类只能通过访问者接口与访问者进行交互。 
    4.1不过访问者必须知晓所有的具体元素类（这些类在访问者方法中都被作为参数类型引用）

5.为每个无法在元素层次结构中实现的行为创建一个具体访问者类并实现所有的访问者方法。

6.访问者破坏原有封装，访问元素类的部分私有成员变量：
    6.1将这些变量或方法设为公有， 这将破坏元素的封装； 
    6.2将访问者类嵌入到元素类中。 
7.客户端必须创建访问者对象并通过 “接收” 方法将其传递给元素。
"""

class Visitor(ABC):
    """
    声明调用所有元素类的接口，将元素实例作为参数输入，双分派机制
    """
    @abstractmethod
    def visit_a(self, element:Element):
        pass
    @abstractmethod
    def visit_b(self, element:Element):
        pass

class Element(ABC):
    """
    声明与访问者交互的接口
    """
    @abstractmethod
    def accept(self, visitor:Visitor):
        pass

class Concrete_Element_A(Element):
    def feature_a(self):
        return "A"
    def accept(self, visitor:Visitor):
        visitor.visit_a(self)

class Concrete_Element_B(Element):
    def feature_b(self):
        return "B"
    def accept(self,visitor:Visitor):
        """
        visitor对象作为参数
        :param visitor:
        :return:
        """

        visitor.visit_b(self)

class Concrete_Visitor1(Visitor):
    def visit_a(self, element:Element):
        element.feature_a()
        print("concrete visitor 1 visit a")

    def visit_b(self, element:Element):
        element.feature_b()
        print("concrete visitor 1 visit b")


class Concrete_Visitor2(Visitor):
    def visit_a(self, element:Element):
        element.feature_a()
        print("concrete visitor 2 visit a")

    def visit_b(self, element:Element):
        element.feature_b()
        print("concrete visitor 2 visit b")

def client_code(elements_list: List[Element], visitor:Visitor):
    for element in elements_list:
        element.accept(visitor)     # 双分派机制

if __name__ == '__main__':
    element_list = [Concrete_Element_A(), Concrete_Element_B()]
    v1 = Concrete_Visitor1()
    v2 = Concrete_Visitor2()
    client_code(element_list,v1)
    client_code(element_list,v2)