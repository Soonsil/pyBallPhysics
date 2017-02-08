from math import sqrt


class CirclePolygonCollision(object):
    def __init__(self, circle):
        self.circle = circle

    def is_touching_line(self, line_start, line_end):
        d = line_end - line_start
        f = line_start - self.circle.position
        r = self.circle.radius

        a = d.inner(d)
        b = 2.0 * f.inner(d)
        c = f.inner(f) - r * r

        det = b * b - 4.0 * a * c

        if det < 0:
            return False
        else:
            det = sqrt(det)
            t1 = (-b - det) / (2.0 * a)
            t2 = (-b + det) / (2.0 * a)

            if t1 >= 0 and t1 <= 1:
                return True

            if t2 >= 0 and t2 <= 1:
                return True

            return False

    def rebound(self, line_start, line_end, preserve):
        d = line_end - line_start
        v1, v2 = self.circle.velocity.proj(d)

        r = self.circle.radius
        x0, y0 = self.circle.position.x, self.circle.position.y
        x1, y1 = line_start.x, line_start.y
        x2, y2 = line_end.x, line_end.y

        l = d.norm()
        f = v2.norm()

        if l != 0 and f != 0:
            q = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1) / l
            self.circle.position -= v2.scale((r - q) / f)

        self.circle.velocity = v1 - v2.scale(preserve)

    def try_collide_polygon(self, polygon, preserve=1.0):
        v = polygon.vertices + (polygon.vertices[0],)
        p = polygon.position

        for i in xrange(len(v) - 1):
            line_start, line_end = v[i] + p, v[i + 1] + p
            if self.is_touching_line(line_start, line_end):
                self.rebound(line_start, line_end, preserve)
