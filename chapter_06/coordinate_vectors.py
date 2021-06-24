from abc import ABCMeta, abstractmethod
from vectors import add, scale

class Vec2():
    """Commom methods for vectors 2D operations
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v2):
        """[summary]

        Args:
            v2 (vector): Add to self.x, self.y

        Returns:
            tuple: returns sum of vectors
        """
        return Vec2(self.x + v2.x, self.y + v2.y)

    def scale(self, scalar):
        """Scale a vector by a scalar multiplication

        Args:
            scalar (int): value to scale for

        Returns:
            tuple: vector modyfied
        """
        return Vec2(scalar * self.x, scalar * self.y)

    def zero():
        return Vec2(0, 0)

    def __eq__(self, other):
        """Overriding the equality method. Avoid same vectors
            to be threated like different objects
        """
        return self.x == other.x and self.y == other.y

    def __add__(self, v2):
        # Operator overloading. Defines sum to be left to right
        return self.add(v2)
    
    def __mul__(self, scalar):
        # Operator overloading. Defines multiplication to be left to right
        return self.scale(scalar)

    def __rmul__(self, scalar):
        # Operator overloading. Defines multiplication to be left to right
        return self.scale(scalar)

    def __repr__(self) -> str:
        # Formats the output from a memory addres to a print
        return "Vec2({},{})".format(self.x, self.y)


class Vec3():
    """Commom methods for vectors 3D operations
    """
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def scale(self, scalar):
        return Vec3(scalar * self.x, scalar * self.y, scalar * self.z)

    def zero():
        return Vec2(0, 0)

    def __eq__(self, other):
        """Overriding the equality method. Avoid same vectors
            to be threated like different objects
        """
        return (self.x == other.x and self.y == other.y and self.z == other.z)

    def __add__(self, other):
        # Operator overloading. Defines sum to be left to right
        return self.add(other)

    def __mul__(self, scalar):
        # Operator overloading. Defines multiplication to be left to right
        return self.scale(scalar)

    def __rmul__(self, scalar):
        # Operator overloading. Defines multiplication to be left to right
        return self.scale(scalar)

    def __repr__(self):
        # Formats the output from a memory addres to a print       
        return "Vec3({},{},{})".format(self.x, self.y, self.z)


class Vector(metaclass=ABCMeta):
    """Abstract class: An abstract class can be considered as a blueprint 
    for other classes. It allows you to create a set of methods that must 
    be created within any child classes built from the abstract class. 
    """
    @abstractmethod
    def scale(self, scalar):
        pass
    
    @abstractmethod
    def add(self, other):
        pass

    @classmethod
    @abstractmethod
    def zero():
        pass
    
    def __neg__(self):
        # Negation
        return self.scale(-1)

    def __mul__(self, scalar):
        return self.scale(scalar)

    def __rmul__(self, scalar):
        return self.scale(scalar)

    def __add__(self,other):
        return self.add(other)

    def subtract(self, other):
        return self.add(-1 * other)

    def __sub__(self, other):
        return self.subtract(other)


class CoordinateVector(Vector):
    """Once we pick a dimension (say 6), we have a concrete class that we can instantiate:
    like:
    class Vec6(CoordinateVector):
        def dimension(self):
            return 6
    """
    @abstractmethod
    def dimensions(self):
        pass

    def __init__(self, *coordinates):
        self.coordinates = tuple(x for x in coordinates)
    
    def add(self, other):
        return self.__class__(*add(self.coordinates, other.coordinates))
    
    def scale(self, scalar):
        return self.__class__(*scale(scalar, self.coordinates))

    def __repr__(self):
        return "{}{}".format(self.__class__.__qualname__, self.coordinates)
    

def average(v1,v2):
    return 0.5 * v1 + 0.5 * v2