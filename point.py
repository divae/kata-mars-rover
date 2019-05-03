class Point:

    def __init__(self,position,facing):
        self.CARDINAL_POINTS = ('N','E','S','W')

        self._check_positions(position[0],position[1])
        self._check_cardinal_point(facing)

        self._generate(position,facing)

    def position(self):
        return [self.eye_x,self.eye_y]

    def orientation(self):
        return self.facing        

    def _generate(self,position,facing):
        self.eye_x = position[0]
        self.eye_y = position[1]
        self.facing = facing

    def _check_positions(self,x,y):
        if self._is_valid_point(x,y) != True:
            raise Exception('Error in starting point') 
    
    def _check_cardinal_point(self,facing):
        if self._is_invalid_cardinal_point(facing):
            raise Exception('Error in starting facing') 

    def _is_invalid_cardinal_point(self,facing):  
        return facing not in self.CARDINAL_POINTS

    def _is_valid_point(self,x,y):
        return self._is_valid_ordinate(x) and self._is_valid_ordinate(y)

    def _is_valid_ordinate(self,ordinate):
        return (not ordinate is None) and (float(ordinate).is_integer())

    def __str__(self):
        return "Point x:{} y:{} orientation:{}".format(self.eye_x, self.eye_y,self.facing)


    