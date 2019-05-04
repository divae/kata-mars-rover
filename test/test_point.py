import unittest 
from src.point import Point
import re

class TestPoint(unittest.TestCase):  

    def test_has_error_in_starting_point(self):
        eye_x = None
        eye_y = 'E'
        start_position = [eye_x,eye_y]
        
        init_point = lambda: Point([eye_x,eye_y])

        self.assertRaises(Exception, init_point)

    def test_class_str(self):
        eye_x = 0
        eye_y = 0
        start_position = [eye_x,eye_y]
        pattern = '.*{}.*{}'.format(eye_x,eye_y)

        STRpoint = Point() 

        result = re.match(str(pattern),str(STRpoint))
        self.assertTrue(result)     
   



