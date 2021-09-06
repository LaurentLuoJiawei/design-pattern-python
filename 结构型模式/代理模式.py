"""
    Description: 代理模式
    Author：Laurent Luo
    Date：2021.08.31
"""

"""
1。如果没有现成的服务接口， 需要创建一个接口来实现代理和服务对象的可交换性。 
    1。1从服务类中抽取接口并非总是可行的， 因为你需要对服务的所有客户端进行修改， 让它们使用接口。 
    1。2备选计划是将代理作为服务类的子类， 这样代理就能继承服务的所有接口了。

2。创建代理类， 其中必须包含一个存储指向服务的引用的成员变量。 
    2。1通常情况下， 代理负责创建服务并对其整个生命周期进行管理。 
    2。2在一些特殊情况下， 客户端会通过构造函数将服务传递给代理。

3。根据需求实现代理方法。代理在完成一些任务后应将工作委派给服务对象。

4。如果代理较多，可以构建代理池（抽象工厂模式）

5。可以考虑为服务对象实现延迟初始化。
"""

from abc import ABC,abstractmethod

class Service(ABC):
    @abstractmethod
    def request(self):
        pass

class Real_Service(Service):
    def request(self):
        print("Service Connection")

class Proxy(Service):
    def __init__(self, service:Service):
        self._service = service

    def request(self):
        result = None
        if self.check_access():
            result = self._service.request()
            self.log_access()

        return result

    def check_access(self):
        """访问权限控制

        :param request:
        :return:
        """
        print("Proxy: request accessible")
        return True

    def log_access(self):
        print("Proxy: log info")

def client(service:Service):
    result = service.request()
    return result

if __name__ == '__main__':
    real_service = Real_Service()
    client(real_service)

    proxy = Proxy(real_service)
    client(proxy)
