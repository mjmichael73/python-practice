from abc import ABC, abstractmethod

class IFactory(ABC):
    @abstractmethod
    def create_a(self):
        pass

    @abstractmethod
    def create_b(self):
        pass

class Factory1(IFactory):
    def create_a(self):
        return ProductA1()
    
    def create_b(self):
        return ProductB1()

class Factory2(IFactory):
    def create_a(self):
        return ProductA2()
    
    def create_b(self):
        return ProductB2()

class ProductA(ABC):
    @abstractmethod
    def test_a(self):
        pass

class ProductB(ABC):
    @abstractmethod
    def test_b(self):
        pass

class ProductA1(ProductA):
    def test_a(self):
        print("test A1")

class ProductA2(ProductA):
    def test_a(self):
        print("test A2")

class ProductB1(ProductB):
    def test_b(self):
        print("test B1")

class ProductB2(ProductB):
    def test_b(self):
        print("test B2")

def check_factory(factory):
    product_a = factory.create_a()
    product_b = factory.create_b()
    product_a.test_a()
    product_b.tesT_b()

check_factory(Factory1())
check_factory(Factory2())

# Provides an interface for creating families of objects whose interfaces are known but concrete classes are not