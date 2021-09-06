"""
    Description: 组合模式
    Author：Laurent Luo
    Date：2021.08.30
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
"""
确保应用的核心模型能够以树状结构表示。 尝试将其分解为简单元素和容器。 记住， 容器必须能够同时包含简单元素和其他容器。

声明组件接口及其一系列方法， 这些方法对简单和复杂元素都有意义。

创建一个叶节点类表示简单元素。 程序中可以有多个不同的叶节点类。

创建一个容器类表示复杂元素。 在该类中， 创建一个数组成员变量来存储对于其子元素的引用。 该数组必须能够同时保存叶节点和容器， 因此请确保将其声明为组合接口类型。

实现组件接口方法时， 记住容器应该将大部分工作交给其子元素来完成。

最后， 在容器中定义添加和删除子元素的方法。

记住， 这些操作可在组件接口中声明。 这将会违反_接口隔离原则_， 因为叶节点类中的这些方法为空。 但是， 这可以让客户端无差别地访问所有元素， 即使是组成树状结构的元素。
"""

class Component:
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self,parent:Component):
        self._parent = parent

    def add(self, component:Component):
        pass

    def remove(self, component:Component):
        pass

    def is_composite(self)->bool:
        return False

    @abstractmethod
    def operation(self):
        """声明组合模式树结构所有叶子、枝节点的公开接口

        :return:
        """
        pass

class Leaf(Component):
    def operation(self):
        return "leaf"

class Composite(Component):
    def __init__(self):
        self._children:List[Component] = []

    def add(self, component:Component):
        self._children.append(component)
        component.parent = self

    def remove(self, component:Component):
        self._children.remove(component)
        component.parent = None

    def is_composite(self):
        return True

    def operation(self):
        results = []
        for child in self._children:
            results.append(child.operation())
        return ",".join(results)

def client(component):
    result = component.operation()
    print(result)

def client2(component1:Component, compoennt2:Component):
    if component1.is_composite():
        component1.add(compoennt2)
    results = compoennt2.operation()
    print(results)

if __name__ == '__main__':
    # 简单模式
    simple = Leaf()
    client(simple)

    # 复杂模式
    tree = Composite()
    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)

    client(tree)