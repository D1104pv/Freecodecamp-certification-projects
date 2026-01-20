from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def set_width(self):
        pass
    
    @abstractmethod
    def set_height(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_diagonal(self):
        pass

    @abstractmethod
    def get_picture(self):
        pass

    @abstractmethod
    def get_amount_inside(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Rectangle(Polygon):
    def __init__(self, width: int, height: int) -> None:
        self._width = width
        self._height = height

    def __str__(self) -> str:
        return f"Rectangle(width={self._width}, height={self._height})"
    
    @property
    def get_width(self) -> int:
        return self._width
    
    @get_width.setter
    def set_width(self, new_width: int) -> None:
        print(f"Changing width to: {new_width}!")
        self._width = new_width
    
    @property
    def get_height(self) -> int:
        return self._height
    
    @get_height.setter
    def set_height(self, new_height: int) -> None:
        print(f"Changing height to: {new_height}!")
        self._height = new_height
    
    @property
    def get_area(self) -> float:
        return self._width * self._height
    
    @property
    def get_perimeter(self) -> int:
        return 2 * (self._width + self._height)
    
    @property
    def get_diagonal(self) -> float:
        return (self._width ** 2 + self._height ** 2) ** 1/2
    


    
# test = Rectangle(5, 10)
# print(test)