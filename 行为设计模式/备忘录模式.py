"""
    Description: 备忘录模式
    Author：Laurent Luo
    Date：2021.09.02
"""
from __future__ import annotations
from abc import ABC,abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters, digits
"""
1.原发器角色的类。 
    1.1明确程序使用的一个原发器中心对象
    1.2还是多个较小的对象。

2.创建备忘录基类。 
    2.1声明构造函数，备忘录只能通过构造函数一次性接收数据。 
    2.2备忘录中不能包含设置器
    2.3声明备忘录的时间戳格式，便于数据管理
    2.4声明备忘录的内部状态读取方法（负责人调用）
3.具体备忘录类
    3.1备忘录都必须与创建自己的原发器相连接
    3.1编程语言支持嵌套类情况：则可将备忘录嵌套在原发器中； 
    3.2如果不支持， 那么你可从备忘录类中抽取一个空接口， 然后让其他所有对象通过接口来引用备忘录。

4.在原发器中添加一个创建备忘录的方法。
    4.1原发器中通过备忘录构造函数完成备忘录实例的创建
    4.2将原发器的内部状态作为参数，输入备忘录的构造函数 

5.在原发器类中添加一个用于恢复自身状态的方法。 
    5.1该方法接受备忘录对象作为参数。 
    5.2如果你在之前的步骤中抽取了接口， 那么可将接口作为参数的类型。将输入对象强制转换为备忘录。

6.负责人必须要知道
    6.1何时向原发器请求新的备忘录、 
    6.2如何存储备忘录以及何时使用特定备忘录来对原发器进行恢复。

"""

class Originator():

    _state = None
    """
    For the sake of simplicity, the originator's state is stored inside a single
    variable.
    """

    def __init__(self, state: str) -> None:
        """
        原发器实例维护自身状态（属性）
        :param state:
        """
        self._state = state
        print(f"Originator: My initial state is: {self._state}")

    def do_something(self) -> None:
        """
        原发器业务逻辑，实现业务会引起实例状态的变化
        :return:
        """

        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to: {self._state}")

    def _generate_random_string(self, length: int = 10) -> None:
        """

        :param length:
        :return:
        """
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        """
        构造与自身绑定的备忘录，将实例此时刻状态作为参数传入备忘录类。
        :return:
        """
        """
        Saves the current state inside a memento.
        """

        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """
        实例恢复历史状态
        """

        self._state = memento.get_state()
        print(f"Originator: My state has changed to: {self._state}")


class Memento(ABC):
    """
    备忘录基类，声明备忘录保存格式（时间戳
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    """
    实现满足原发器状态保存需求的构造函数，接收原发器状态参数
    """
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        备忘录管理实例中数据的访问
        :return:
        """
        return self._state

    def get_name(self) -> str:
        """
        通过时间戳或其他格式 区分同一个原发器的不同时间节点的备忘录
        :return:
        """

        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date


class Caretaker():
    """
    负责人类对原发器的备忘录集合进行管理
    """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\nClient: Once more!\n")
    caretaker.undo()

