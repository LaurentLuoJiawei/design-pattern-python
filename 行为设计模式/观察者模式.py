"""
    Description: 观察者模式
    Author：Laurent Luo
    Date：2021.09.05
"""
from __future__ import annotations
from abc import ABC,abstractmethod
from typing import List

"""
1.主要业务逻辑拆分为两个部分：
    1.1独立于其他代码的核心功能将作为发布者
    1.2其他代码则将转化为一组订阅类。

2.声明订阅者接口。（update）

3.声明发布者接口
    3.1定义一些接口来在列表中添加和删除订阅对象，发布者通过订阅者接口进行交互。
    3.2确定存放实际订阅列表的位置并实现订阅方法。 
    3.3将订阅者列表放置在扩展自发布者接口的抽象类中。 如果你需要在现有的类层次结构中应用该模式，则可以考虑使用组合的方式： 将订阅逻辑放入一个独立的对象， 然后让所有实际订阅者使用该对象。
4.创建具体发布者
    4.1具体发布者会扩展该类从而继承所有的订阅行为。
    4.2实现通知更新的方法。每次发布者发生了重要事件时都必须通知所有的订阅者。
    
5.上下文数据传递：绝大部分订阅者需要一些与事件相关的上下文数据。
    5.1这些数据可作为通知方法的参数来传递。
    5.2订阅者接收到通知后直接从通知中获取所有数据。发布者必须通过更新方法将自身传递出去。 
    5.3另一种不太灵活的方式是通过构造函数将发布者与订阅者永久性地连接起来。

6.客户端必须生成所需的全部订阅者， 并在相应的发布者处完成注册工作。
"""

class Base_Publisher(ABC):
    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def add_observer(self):
        pass

    @abstractmethod
    def remove_observer(self):
        pass


class Base_Observer(ABC):
    @abstractmethod
    def update(self, publisher:Base_Publisher):
        pass


class Concrete_publsiher(Base_Publisher):
    _subs_list:List[Base_Observer] = []
    _state = None
    def __init__(self):
        self._state = "123"
    def change_state(self, state):
        self._state = state
        self.notify()

    def get_state(self):
        return self._state

    def notify(self):
        if self._subs_list:
            for sub in self._subs_list:
                sub.update(self)

    def add_observer(self, subscriber:Base_Observer):
        self._subs_list.append(subscriber)


    def remove_observer(self, subscriber:Base_Observer):
        if subscriber in self._subs_list:
            self._subs_list.remove(subscriber)


class Concrete_Observer1(Base_Observer):
    def update(self, publisher:Base_Publisher):
        if publisher._state == '222':
            print("通知收到，状态改变")
            self.operation()
        else:
            print("通知收到，状态未改变")
    def operation(self):
        return "执行操作"

class Concrete_Observer2(Base_Observer):
    def update(self, publisher:Base_Publisher):
        if publisher._state == '123':
            print("通知收到，状态改变")
            self.operation()
        else:
            print("通知收到，状态未改变")
    def operation(self):
        return "执行操作"

if __name__ == '__main__':
    publisher = Concrete_publsiher()
    ob1 =  Concrete_Observer1()
    ob2 = Concrete_Observer2()
    publisher.add_observer(ob1)
    publisher.add_observer(ob2)

    publisher.notify()

    publisher.change_state("222")
