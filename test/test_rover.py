import unittest 
from src.rover import Rover
from src.point import Point 
import re
      
class TestRover(unittest.TestCase):  
    def test_start_initial_point(self):
        axe_x = 0
        axe_y = 0
        facing = 'N'
        pattern = '.*{}.*{}.*{}'.format(axe_x,axe_y,facing)

        end_point = Point()

        point = Point()
        rover = Rover(Point(),facing)

        result = re.match(str(pattern),str(rover))
        self.assertTrue(result)  

    