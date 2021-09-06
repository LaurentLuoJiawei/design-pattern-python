
"""
    Description: 状态模式
    Author：Laurent Luo
    Date：2021.09.05
"""
from __future__ import annotations
from abc import ABC,abstractmethod

"""
1.上下文类
    1.1它可能是包含依赖于状态的代码的已有类； 
    1.2如果特定于状态的代码分散在多个类中， 那么它可能是一个新的类。

2.声明状态接口。 
    2.1可能会需要完全复制上下文中声明的所有方法， 
    2.2但把关注点放在那些可能包含特定于状态的行为的方法上。

3.为每个实际状态创建一个继承于状态接口的类。 
    3.1检查上下文中的方法
    3.2将与特定状态相关的所有代码抽取到新建的类中。

4.移动到状态类的过程中，对于依赖于上下文中的一些私有成员的代码。 
    4.1将这些成员变量或方法设为公有。
    4.2将需要抽取的上下文行为更改为上下文中的公有方法， 然后在状态类中调用。 
    4.3将状态类嵌套在上下文类中。 这种方式需要你所使用的编程语言支持嵌套类。
    4.4在上下文类中添加一个状态接口类型的引用成员变量， 以及一个用于修改该成员变量值的公有设置器。

5.再次检查上下文中的方法， 将空的条件语句替换为相应的状态对象方法。

6.上下文状态切换，可以在一下对象中完成：
    6.1上下文
    6.2状态间
    6.3客户端
"""
class Context:
    _state = None
    def __init__(self, state:Base_Sate):
        self.change_state(state)

    def change_state(self, state:Base_Sate):
        """
        业务逻辑引起的上下文状态变换
        :return:
        """
        self._state = state
        self._state.context = self
    def request1(self):
        self._state.do_this()

    def request2(self):
        self._state.do_that()

class Base_Sate(ABC):
    @abstractmethod
    def do_this(self, context:Context):
        pass

    @abstractmethod
    def do_that(self, context:Context):
        pass

    # 绑定对应的上下文实例
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context:Context):
        self._context = context




class Concrete_State1(Base_Sate):

    def do_that(self):
        print("ST1 process request 2")
        self.context.change_state(Concrete_State2())

    def do_this(self,):
        print("ST1 process request 1")
        self.context.change_state(Concrete_State2())

class Concrete_State2(Base_Sate):

    def do_that(self):
        print("ST2 process request 2")

    def do_this(self):
        print("ST2 process request 1")


if __name__ == '__main__':
    context = Context(Concrete_State1())
    context.request1()
    context.request2()