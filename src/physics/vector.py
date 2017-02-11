from math import sin, cos, sqrt, atan2


class Vector(object):
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.add(-other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.inner(other)
        else:
            return self.scale(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        return self.scale(1.0 / other)

    def __str__(self):
        return '(%.4f, %.4f)' % (self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __copy__(self):
        return self.copy()

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def scale(self, c):
        return Vector(self.x * c, self.y * c)

    def inner(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, c):
        return Vector(self.y * c, -self.x * c)

    def rotate(self, angle):
        x, y = self.x, self.y
        c, s = cos(angle), sin(angle)

        return Vector(x * c - y * s, x * s + y * c)

    def norm(self):
        x, y = self.x, self.y
        return sqrt(x * x + y * y)

    def angle(self):
        return atan2(self.y, self.x)

    def proj(self, other):
        size_other = other.norm()

        if size_other == 0:
            return (Vector(0, 0), self.copy())
        else:
            vec_parallel = other.scale(self.inner(other) / (size_other * size_other))
            vec_orthogonal = self - vec_parallel

            return vec_parallel, vec_orthogonal

    def copy(self):
        return Vector(self.x, self.y)
