"""
    Description: 命令模式
    Author：Laurent Luo
    Date：2021.09.01
"""
"""

声明仅有一个执行方法的命令接口。

抽取请求并使之成为实现命令接口的具体命令类。 每个类都必须有一组成员变量来保存请求参数和对于实际接收者对象的引用。 所有这些变量的数值都必须通过命令构造函数进行初始化。

找到担任发送者职责的类。 在这些类中添加保存命令的成员变量。 发送者只能通过命令接口与其命令进行交互。 发送者自身通常并不创建命令对象， 而是通过客户端代码获取。

修改发送者使其执行命令， 而非直接将请求发送给接收者。

客户端必须按照以下顺序来初始化对象：

创建接收者。
创建命令， 如有需要可将其关联至接收者。
创建发送者并将其与特定命令关联。
"""
from abc import ABC,abstractmethod



class Receiver():
    def operation1(self, para1):
        print("do work 1")
    def operation2(self, para2):
        print("do work 2 ")

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Concrete_Command1(Command):
    def __init__(self, receiver, params):
        self.receiver = receiver
        self.params = params

    def execute(self):
        self.receiver.operation1(self.params)
        self.receiver.operation2(self.params)

class Concrete_Command2(Command):
    def __init__(self, receiver, params):
        self.receiver = receiver
        self.params = params

    def execute(self):
        self.receiver.operation2(self.params)
        self.receiver.operation1(self.params)

class Invoker():
    def set_command1(self, command1:Command):
        self._command1 = command1

    def set_command2(self, command2:Command):
        self._command2 = command2

    def execute_command12(self):
        """根据业务逻辑调用具体命令

        :return:
        """
        print("启动")
        self._command1.execute()

        print("暂停10s，继续执行")
        self._command2.execute()

if __name__ == '__main__':
    invoker = Invoker()
    rece = Receiver()
    cmd1 = Concrete_Command1(rece, "start")
    cmd2 = Concrete_Command2(rece,"end")
    invoker.set_command1(cmd1)
    invoker.set_command2(cmd2)
    invoker.execute_command12()
