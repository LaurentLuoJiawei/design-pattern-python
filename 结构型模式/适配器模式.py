"""
    Description: 适配器模式
    Author：Laurent Luo
    Date：2021.08.29
"""

# 适配器案例基于方钉适配圆孔
# 适配器假扮成一个圆钉 （Round）， 其半径等于方钉 （Square） 横截面对角线的一半 （即能够容纳方钉的最小外接圆的半径）。
"""
确保至少有两个类的接口不兼容：

一个无法修改 （通常是第三方、 遗留系统或者存在众多已有依赖的类） 的功能性服务类。
一个或多个将受益于使用服务类的客户端类。
1.声明客户端接口， 描述客户端如何与服务交互。

创2.建遵循客户端接口的适配器类。 所有方法暂时都为空。

3.在适配器类中添加一个成员变量用于保存对于服务对象的引用。 
    3.1通常情况下会通过构造函数对该成员变量进行初始化， 
    3.2有时在调用其方法时将该变量传递给适配器会更方便。

4.依次实现适配器类客户端接口的所有方法。 
    4.1适配器会将实际工作委派给服务对象， 自身只负责接口或数据格式的转换。

5.客户端必须通过客户端接口使用适配器。
"""


class Target:
    """客户端接口
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
        服务端，与客户端接口不兼容部分
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """对服务端接口进行数据格式转换，并声明接口提供给客户端调用
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)