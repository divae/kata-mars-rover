class Point:
    def __init__(self,position,direction):
        self._check(position[0],position[1])

        self.eye_x = position[0]
        self.eye_y = position[1]

        self.direction = direction   

    def generate(self):
        return [self.eye_x,self.eye_y]

    def _check(self,x,y):
        if self._is_valid_point(x,y) != True:
            raise Exception('Error in starting point') 

    def _is_valid_point(self,x,y):
        return self._is_valid_ordinate(x) and self._is_valid_ordinate(y)

    def _is_valid_ordinate(self,ordinate):
        return (not ordinate is None) and (float(ordinate).is_integer())

    