class Location:
    def __init__(self, index, name, desc, item, character):
        self.index = index
        self. name = name
        self.description = desc
        self.item = item
        self.Forward = None 
        self.Backward = None
        self.Right = None
        self.Left = None
        self.character = character
        self.itemIsVisible = True

    def get_index(self):
        return self. index
    def get_name(self):
        return self.name
    def get_desc(self):
        return self.description
    def get_item(self):
        return self.item
    def get_character(self):
        return self.character
    def get_location_forward(self):
        return self.Forward
    def get_location_backward(self):
        return self.Backward
    def get_location_right(self):
        return self.Right
    def get_location_left(self):
        return self.Left
    def set_locations(self, f, b, r, l):
        self.Forward = f
        self.Backward = b
        self.Right = r
        self.Left = l
    def leave_location(self):    
        print("leaving the room "+self.name)
        self.itemIsVisible = False
        print(self.itemIsVisible)
    def get_isItemVisible(self):    
        return self.itemIsVisible
