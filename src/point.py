class Point:

    def __init__(self,position=[0,0],facing='N'):
        self._check_positions(position[0],position[1])
        self._generate(position,facing)

    def axe_x(self):
        return self.axe_x

    def axe_y(self):
        return self.axe_y

    def _generate(self,position,facing):
        self.axe_x = position[0]
        self.axe_y = position[1]

    def _check_positions(self,x,y):
        if self._is_valid_point(x,y) != True:
            raise Exception('Error in starting point') 
    
    def _is_valid_point(self,x,y):
        return self._is_valid_ordinate(x) and self._is_valid_ordinate(y)

    def _is_valid_ordinate(self,ordinate):
        return (not ordinate is None) and (float(ordinate).is_integer())

    def __str__(self):
        return "Point x:{} y:{}".format(self.axe_x, self.axe_y)


    