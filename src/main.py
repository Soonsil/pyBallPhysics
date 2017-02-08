from physics.vector import Vector
from physics.collision import CirclePolygonCollision
from physics.renderer import Renderer


class MyRenderer(Renderer):
    def on_create(self):
        self.ball = self.add_entity(
            shape='circle',
            radius=10,
            position=Vector(40, 10)
        )

        self.rocks = [
            self.add_entity(
                shape='polygon',
                color='green',
                vertices=(Vector(0, 0), Vector(70, 20), Vector(0, 20)),
                position=Vector(20, 80)
            ),
            self.add_entity(
                shape='polygon',
                color='dark green',
                vertices=(Vector(0, 0), Vector(150, -30), Vector(80, 10)),
                position=Vector(100, 150)
            ),
            self.add_entity(
                shape='polygon',
                color='yellow',
                vertices=(Vector(0, 0), Vector(60, 30),
                          Vector(120, 25), Vector(170, 40),
                          Vector(200, 80), Vector(30, 40)),
                position=Vector(10, 200)
            ),
            self.add_entity(
                shape='polygon',
                color='light blue',
                vertices=(Vector(0, 0), Vector(50, -70), Vector(50, 0)),
                position=Vector(250, 280)
            )
        ]

        self.collision = CirclePolygonCollision(self.ball.body)

        self.draw_entity(self.ball)
        map(self.draw_entity, self.rocks)

    def on_frame(self):
        self.ball.body.add_force(Vector(0, 0.7))
        self.ball.body.integrate_force()

        for rock in self.rocks:
            self.collision.try_collide_polygon(rock.body, preserve=0.0)

        self.draw_entity(self.ball)

MyRenderer().run()
