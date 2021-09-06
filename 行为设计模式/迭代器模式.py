"""
    Description: 迭代器模式
    Author：Laurent Luo
    Date：2021.09.01
"""
from __future__ import  annotations
from collections.abc import Iterator, Iterable
from typing import Any,List

# 类重构
# class Iterator():
#     def __iter__(self):
#         pass
#     def __next__(self):
#         pass
#     def __getitem__(self, item):
#         pass
#     def __len__(self):
#         pass


"""
1.声明迭代器接口。 该接口必须提供至少一个方法来获取集合中的下个元素。 但为了使用方便， 你还可以添加一些其他方法， 例如获取前一个元素、 记录当前位置和判断迭代是否已结束。

声明集合接口并描述一个获取迭代器的方法。 其返回值必须是迭代器接口。 如果你计划拥有多组不同的迭代器， 则可以声明多个类似的方法。

为希望使用迭代器进行遍历的集合实现具体迭代器类。 迭代器对象必须与单个集合实体链接。 链接关系通常通过迭代器的构造函数建立。

在你的集合类中实现集合接口。 其主要思想是针对特定集合为客户端代码提供创建迭代器的快捷方式。 集合对象必须将自身传递给迭代器的构造函数来创建两者之间的链接。

检查客户端代码， 使用迭代器替代所有集合遍历代码。 每当客户端需要遍历集合元素时都会获取一个新的迭代器。


"""

class Customized_Iterator(Iterator):
    # 记录当前迭代的位置
    _pos:int = None

    # 迭代策略（逆向开关）
    _reverse = False


    def __init__(self, collection: Customized_Collection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
        The __next__() method must return the next item in the sequence. On
        reaching the end, and in subsequent calls, it must raise StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value

class Customized_Collection:

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> Customized_Iterator:
        """
        The __iter__() method returns the iterator object itself, by default we
        return the iterator in ascending order.
        """
        return Customized_Iterator(self._collection)

    def get_reverse_iterator(self) -> Customized_Iterator:
        return Customized_Iterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)

if __name__ == '__main__':
    collection = Customized_Collection()
    collection.add_item('A')
    collection.add_item('B')
    collection.add_item('C')

    print("\t".join(collection))

    print("reverse")
    print("\n".join(collection.get_reverse_iterator()))