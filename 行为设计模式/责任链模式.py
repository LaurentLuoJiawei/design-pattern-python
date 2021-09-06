"""
    Description: 责任链模式
    Author：Laurent Luo
    Date：2021.09.01
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any,Optional
"""
1.声明处理者接口并描述请求处理方法的签名。

2.确定客户端请求数据传递方法。 
    2.1将请求转换为对象， 
    2.2以参数的形式传递给处理函数。

3.为了在具体处理者中消除重复的样本代码， 
    3.1根据处理者接口创建抽象处理者基类。

4.该类需要有一个成员变量来存储指向链上下个处理者的引用。 
    4.1将其设置为不可变类。 
    4.2定义一个设定方法来修改引用成员变量的值。实现责任链的动态调整

5.实现处理方法的默认行为。 
    5。1如果还有剩余对象， 该方法会将请求传递给下个对象。 
    5。2具体处理者还能够通过调用父对象的方法来使用这一行为。

6。依次创建具体处理者子类并实现其处理方法。 每个处理者在接收到请求后都必须做出两个决定：
    6。1是否自行处理这个请求/否将该请求沿着链进行传递。
7。客户端可以自行组装链，。
    7。1或者从其他对象处获得预先组装好的链。 但必须实现工厂类以根据配置或环境设置来创建链。

8。客户端可以触发链中的任意处理者， 而不仅仅是第一个。 请求将通过链进行传递， 直至某个处理者拒绝继续传递， 或者请求到达链尾。

9。由于链的动态性， 客户端需要准备好处理以下情况：
    9。1链中可能只有单个链接。
    9。2部分请求可能无法到达链尾。
    9。3其他请求可能直到链尾都未被处理。
"""

class Handler(ABC):
    """职责链的两个主要方法
    1。处理请求
    2。绑定后继处理者

    """
    @abstractmethod
    def operation(self, request)->Optional:
        pass
    @abstractmethod
    def set_sucessor(self, successor:Handler):
        pass

class AbstractHandler(Handler):
    _successor = None
    def set_sucessor(self, successor:Handler):
        self._successor = successor

    def operation(self,request):
        if self.can_handle(request):
            return "{} can process the request {}".format(self.__class__.__name__, request)
        elif self._successor:
            return self._successor.operation(request)
        else:
            return None

    def can_handle(self,request):
        return False

class MonkeyHandler(AbstractHandler):
    def can_handle(self,request):
        if request == 'banana':
            return True
        else:
            return False

class DogHandler(AbstractHandler):
    def can_handle(self,request):
        if request == 'meat ball':
            return True
        else:
            return False

class SquirrelHandler(AbstractHandler):
    def can_handle(self,request):
        if request == 'nut':
            return True
        else:
            return False

def client(handler):
    for food in ['nut','banana','tea']:
        result = handler.operation(food)
        if result:
            print("{}".format(result))
        else:
            print("{} failed".format(result) )

if __name__ == '__main__':
    sqhandler = SquirrelHandler()
    dghandler = DogHandler()
    mkhandler = MonkeyHandler()
    sqhandler.set_sucessor(dghandler)
    dghandler.set_sucessor(mkhandler)

    client(sqhandler)