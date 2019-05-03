import unittest 
from point import Point 
import re

class TestPoint(unittest.TestCase):  

    def test_has_error_in_starting_point(self):
        eye_x = None
        eye_y = 'E'
        start_position = [eye_x,eye_y]
        facing = 'N'

        init_point = lambda: Point([eye_x,eye_y],facing)

        self.assertRaises(Exception, init_point)

    def test_exception_direction_error(self):
        eye_x = 0
        eye_y = 0
        start_position = [eye_x,eye_y]
        facing = 'T'

        init_point = lambda: Point(start_position,facing)

        self.assertRaises(Exception, init_point )

    def test_class_str(self):
        eye_x = 1
        eye_y = 0
        start_position = [eye_x,eye_y]
        facing = 'W'
        pattern = '.*{}.*{}.*{}'.format(eye_x,eye_y,facing)


        STRpoint = Point(start_position,facing) 
        print(STRpoint)

        result = re.match(str(pattern),str(STRpoint))

        self.assertTrue(result)     
   



