class Figure(object):
    positionX: None
    positionY: None
    startingPositionX: None
    startingPositionY: None

    def __init__(self, x, y):
        self.positionX = x
        self.positionY = y
        self.startingPositionX = x
        self.startingPositionY = y

    def __str__(self):
        return str(self.__class__) + '\n' + '\n'.join(
            ('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__))

    def move_figure(self, x, y):
        self.positionX = x
        self.positionY = y
