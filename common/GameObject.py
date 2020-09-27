from sprite import Sprite

WIDTH = 1000
HEIGHT = 600

class GameObject:
    def __init__(self, filename, x, y, width, height, incx, incy):
        self.sprite = Sprite(filename, x, y, width, height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.incx = incx
        self.incy = incy

    def do(self):
        self.x += self.incx
        self.y += self.incy
        if self.x > WIDTH or self.x < 0:
            self.incx = -self.incx
            self.x = self.x + 2*self.incx
        if self.y > HEIGHT or self.y < 0:
            self.incy = -self.incy
            self.y = self.y + 2*self.incy
        self.sprite.moveTo(self.x, self.y)

    def draw(self):
        self.sprite.draw()