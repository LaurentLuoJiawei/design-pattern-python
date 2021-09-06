"""
    Description: 中介者模式
    Author：Laurent Luo
    Date：2021.09.02
"""
from __future__ import annotations
from abc import ABC,abstractmethod
"""
1.找到一组当前紧密耦合， 且提供其独立性能带来更大好处的类 （例如更易于维护或更方便复用）。

2.声明中介者接口并描述中介者和各种组件之间所需的交流接口。 
    2.1在绝大多数情况下， 一个接收组件通知的方法就足够了。 
    2.2如果你希望在不同情景下复用组件类， 组件与中介的通信接口将非常重要。
    只要组件使用通用接口与其中介者合作， 你就能将该组件与不同实现中的中介者进行连接。

3.实现具体中介者类。 该类可从自行保存其下所有组件的引用中受益。
    3.1让中介者负责组件对象的创建和销毁。中介者可能会与工厂或外观类似。

4.组件必须保存对于中介者对象的引用（property）。
    4.1该连接通常在组件的构造函数中建立， 该函数会将中介者对象作为参数传递。

5.修改组件代码， 使其可调用中介者的通知方法， 
    5.1抽取代码调用其他组件的到中介者类中， 具体中介者类接收到该组件通知时执行这些代码。
"""


class Mediator:
    def notify(self,sender:object, event:str):
        pass


class Base_Component():
    def __init__(self, mediator:Mediator=None):
        #维护中介对象的引用
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator
    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator


class ComponentA():

    def call_mediator(self):
        print("send request to meditor")
        self._mediator.notify(self, 'A')

class ComponentB():

    def call_mediator(self):
        print("send request to meditor")
        self._mediator.notify(self, 'B')


class Concrete_Mediator(Mediator):
    def __init__(self,component_dict):
        self._components = {}
        for id, component in component_dict.items():
            self._components[id] = component
            component._mediator = self

    def notify(self,sender, event):
        print("sender from {}, event is {}".format(sender.__class__.__name__, event))
        if event == 'A':
            return self.react_A()
        if event == 'B':
            return self.react_B()

    def react_A(self):
        return "react_A"

    def react_B(self):
        return "react_B"

if __name__ == '__main__':
    ca= ComponentA()
    cb= ComponentB()
    component_dict = dict(ca=ca,cb=cb)
    med = Concrete_Mediator(component_dict)
    ca.call_mediator()
    cb.call_mediator()


