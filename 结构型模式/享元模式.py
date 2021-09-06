"""
    Description: 享元模式
    Author：Laurent Luo
    Date：2021.08.31
"""



"""
1。将需要改写为享元的类成员变量拆分为两个部分：

    1。1内在状态： 包含不变的、 可在许多对象中重复使用的数据的成员变量。
    1。2外在状态： 包含每个对象各自不同的情景数据的成员变量
    1。3保留类中表示内在状态的成员变量， 并将其属性设置为不可修改。 这些变量仅可在构造函数中获得初始数值。

2。找到所有使用外在状态成员变量的方法， 为在方法中所用的每个成员变量新建一个参数， 并使用该参数代替成员变量。

3。你可以有选择地创建工厂类来管理享元缓存池， 它负责在新建享元时检查已有的享元。 如果选择使用工厂， 客户端就只能通过工厂来请求享元， 它们需要将享元的内在状态作为参数传递给工厂。

4。客户端必须存储和计算外在状态 （情景） 的数值， 因为只有这样才能调用享元对象的方法。 为了使用方便， 外在状态和引用享元的成员变量可以移动到单独的情景类中。
"""

import json
from typing import Dict

class Flyweight():
    def __init__(self, shared_state:str):
        self._shared_state = shared_state

    def operation(self, unique_state:str):
        s = json.dumps(self._shared_state)
        u = json.dumps(unique_state)
        print(r"unique {} shared {}".format(u,s))

class FlyweightFactory():
    _flyweights:Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweight:Dict) -> None:
        for state in initial_flyweight:
            self._flyweights[self.get_key(state)] = Flyweight(state)

    def get_key(self, state:Dict):
        return  "_".join(sorted(state))

    def get_flyweight(self, shared_state):
        key = self.get_key(shared_state)
        if not self._flyweights.get(key):
            print("initialize a new flyweight with state {}".format(shared_state))
            self._flyweights[key] = Flyweight(shared_state)
        else:
            print("already has a instance with state {}".format(shared_state))
        return self._flyweights[key]

    def list_flyweights(self):
        count = len(self._flyweights)
        print("factory has {} flyweights".format(count))
        print("kesy: {}".join(map(str, self._flyweights.keys())))

def add_item_to_database(factory:FlyweightFactory, plates, owner, brand, model, color):
    print("add car to database")
    flyweight = factory.get_flyweight([brand, model, color])
    flyweight.operation([plates, owner])

if __name__ == '__main__':
    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweights()

    add_item_to_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_item_to_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    factory.list_flyweights()