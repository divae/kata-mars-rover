import unittest 
from src.point import Point
import re

class TestPoint(unittest.TestCase):  

    def test_has_error_in_starting_point(self):
        axe_x = None
        axe_y = 'E'
        start_position = [axe_x,axe_y]
        
        init_point = lambda: Point([axe_x,axe_y])

        self.assertRaises(Exception, init_point)

    def test_class_str(self):
        axe_x = 0
        axe_y = 0
        start_position = [axe_x,axe_y]
        pattern = '.*{}.*{}'.format(axe_x,axe_y)

        STRpoint = Point() 

        result = re.match(str(pattern),str(STRpoint))
        self.assertTrue(result)     
   



