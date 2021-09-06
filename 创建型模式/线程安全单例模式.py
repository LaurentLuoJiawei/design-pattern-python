"""
    Description: 线程安全单例模式
    Author：Laurent Luo
    Date：2021.08.29
"""


#线程安全
# from multiprocessing import Process,Lock
from threading import Thread,Lock
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
class SingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    _value : str = None

    def __init__(self, value):
        self._value = value
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton._value)

if __name__ == "__main__":
    # The client code.
    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
