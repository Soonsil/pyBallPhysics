from physics.vector import Vector


class Body(object):
    def __init__(self,
                 mass=1,
                 position=Vector(0, 0),
                 velocity=Vector(0, 0)):
        self.mass = mass
        self.position = position
        self.velocity = velocity

        self.acceleration = Vector(0, 0)

    def add_force(self, force):
        self.acceleration += force

    def integrate_force(self, dt=1):
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

        self.acceleration.x = 0
        self.acceleration.y = 0


# --------------------------------------------------------------

class Circle(Body):
    def __init__(self, radius=1, *args, **kwargs):
        super(Circle, self).__init__(*args, **kwargs)

        self.radius = radius


# --------------------------------------------------------------

class Polygon(Body):
    def __init__(self, vertices, *args, **kwargs):
        super(Polygon, self).__init__(*args, **kwargs)

        self.vertices = vertices
