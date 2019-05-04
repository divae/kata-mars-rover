import unittest 
from rover import Rover
from point import Point 
import re
      
class TestRover(unittest.TestCase):  
    def test_start_initial_point(self):
        eye_x = 0
        eye_y = 0
        facing = 'N'
        pattern = '.*{}.*{}.*{}'.format(eye_x,eye_y,facing)

        end_point = Point()

        point = Point()
        rover = Rover(Point(),facing)

        result = re.match(str(pattern),str(rover))
        self.assertTrue(result)  

    