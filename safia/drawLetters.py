class Writing():
    def __init__(self, name, sizex, sizey, movex, movey):
        self.name = name
        self.sizex = sizex
        self.sizey = sizey
        self.movex = movex
        self.movey = movey

    def draw(name, sizex, sizey, movex, movey):
        rect = Rect(movex, movey, sizex, sizey)
        screen.draw.filled_rect(room_desc, "red")
        screen.draw.textbox(name, color=("black"))