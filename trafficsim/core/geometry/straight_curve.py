from .segment import Segment


class StraightCurve(Segment):
    def __init__(self, points):
        super().__init__(points)

    def compute_x(self, t):
        pass

    def compute_y(self, t):
        pass

    def compute_dx(self, t):
        pass

    def compute_dy(self, t):
        pass
