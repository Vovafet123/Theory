
class Geom:
    name = 'Geom'

    def set_coords(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2


class Line(Geom):
    def draw(self):
        print('Рисование линии')


class Rect(Geom):
    def draw(self):
        print('Рисование прямоугольника')


g = Geom()
l = Line()

print(l.name)

l.set_coords(1, 2, 3, 4)
print(l.__dict__)
