class Rover:
    CARDINAL_POINTS = ('N','E','S','W')

    def __init__(self,point,facing):
        self.point = point
        self._check_cardinal_point(facing)

        self.facing = facing

    def _check_cardinal_point(self,facing):
        if self._is_invalid_cardinal_point(facing):
            raise Exception('Error in starting facing') 

    def _is_invalid_cardinal_point(self,facing):  
        return facing not in self.CARDINAL_POINTS

    def __str__(self):
        return "Point x:{} y:{} Facing:{}".format(self.point.eye_x, self.point.eye_y,self.facing)


