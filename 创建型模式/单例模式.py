"""
    Description: 单例模式
    Author：Laurent Luo
    Date：2021.08.29
"""

"""
1.在类中添加一个私有静态成员变量用于保存单例实例。

2.声明一个公有静态构建方法用于获取单例实例。

3.在静态方法中实现"延迟初始化"(new) /(双重锁定机制，避免多线程场景下，创建多个实例)
    3.1该方法会在首次被调用时创建一个新对象， 并将其存储在静态成员变量中。 此后该方法每次被调用时都返回该实例。

4.将类的构造函数设为私有。 类的静态方法仍能调用构造函数， 但是其他对象不能调用。

5.检查客户端代码， 调用其静态构建方法。
"""
# 简单实现
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[instance] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
#线程安全
# from multiprocessing import Process,Lock
from threading import Thread,Lock


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")