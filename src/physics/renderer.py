import Tkinter
from abc import ABCMeta, abstractmethod

from physics.body import *


class Entity(object):
    __slots__ = ('body', 'item', 'coordinates')

    def __init__(self, body, item, coordinates):
        self.body = body
        self.item = item
        self.coordinates = coordinates


# --------------------------------------------------------------

class Renderer(Tkinter.Frame, object):
    __metaclass__ = ABCMeta

    def __init__(self, width=400, height=300, dt=0.002):
        self.width = width
        self.height = height
        self.dt = dt

        self.root = Tkinter.Tk()
        self.root.title('Physics')

        super(Renderer, self).__init__(self.root)

        self.board = Tkinter.Canvas(
            self.root,
            width=self.width,
            height=self.height,
            bg='white',
            highlightthickness=0
        )

        self.board.pack()

        self.on_create()
        self.play_animation()

    def run(self):
        self.root.mainloop()

    def add_entity(self, shape, color='blue', *args, **kwargs):
        if shape == 'circle':
            body = Circle(*args, **kwargs)
            coordinates = (-body.radius, -body.radius, body.radius, body.radius)

            item = self.board.create_oval(
                *coordinates,
                fill=color,
                outline='black'
            )

            return Entity(body, item, coordinates)
        elif shape == 'polygon':
            body = Polygon(*args, **kwargs)
            coordinates = []

            for vertex in body.vertices:
                coordinates.append(vertex.x)
                coordinates.append(vertex.y)

            item = self.board.create_polygon(
                *coordinates,
                fill=color,
                outline='black'
            )

            return Entity(body, item, coordinates)

    def draw_entity(self, entity):
        coordinates_entity = entity.coordinates
        coordinates_board = []
        x, y = entity.body.position.x, entity.body.position.y

        for i in xrange(0, len(coordinates_entity), 2):
            coordinates_board.append(coordinates_entity[i] + x)
            coordinates_board.append(coordinates_entity[i + 1] + y)

        self.board.coords(entity.item, *coordinates_board)

    def play_animation(self):
        self.on_frame()
        self.root.after(int(self.dt * 1000), self.play_animation)

    @abstractmethod
    def on_create(self):
        return

    @abstractmethod
    def on_frame(self):
        return
