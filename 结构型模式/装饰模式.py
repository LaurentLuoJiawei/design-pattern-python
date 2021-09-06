"""
    Description: 装饰模式
    Author：Laurent Luo
    Date：2021.08.30
"""

"""
1.确保业务逻辑可用一个基本组件及多个额外可选层次表示。(确定基本组件)

2.找出基本组件和可选层次的通用方法，创建组件接口并在其中声明这些方法。

3.创建一个具体组件类， 并定义其基础行为。

4.创建装饰基类， 使用一个成员变量存储指向被封装对象的引用。 
    4.1该成员变量必须被声明为组件接口类型(Component)， 从而能在运行时连接具体组件和装饰。 
    4.2装饰基类必须将所有工作委派给被封装的对象。

5.确保所有类实现组件接口。

6.将装饰基类扩展为具体装饰。
    6.1具体装饰必须在调用父类方法 （总是委派给被封装对象） 之前或之后执行自身的行为。

7.客户端代码负责创建装饰并将其组合成客户端所需的形式。
"""

class Component:

    def operation(self):
        pass

class Concrete_Component(Component):
    def operation(self):
        return "{}".format(self.__class__.__name__)

class Decorator(Component):
    _component:Component = None
    def __init__(self, compoennt:Component):
        self._component = compoennt

    @property
    def component(self):
        return self._component

    def operation(self):
        return self._component.operation()

class Concrete_DecoratorA(Decorator):
    def operation(self):
        return "DecoratorA:{}".format(self.component.operation())

class Concrete_DecoratorB(Decorator):
    def operation(self):
        return "DecoratorB:{}".format(self.component.operation())

def client_code(component: Component):
    result = component.operation()
    print(result)


if __name__ == '__main__':
    simple = Concrete_Component()
    client_code(simple)

    dec1 = Concrete_DecoratorA(simple)
    dec2 = Concrete_DecoratorB(dec1)
    client_code(dec2)