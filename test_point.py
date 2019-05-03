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

    def test_generate_starting_point(self):
        eye_x = 0
        eye_y = 1
        start_position = [eye_x,eye_y]
        facing = 'N'

        eye_x_objective = 0
        eye_y_objective = 1
        actualy_point = [eye_x_objective,eye_y_objective]

        point = Point(start_position,facing)

        self.assertEqual(point.position(), actualy_point)

    def test_exception_direction_error(self):
        eye_x = 0
        eye_y = 0
        start_position = [eye_x,eye_y]
        facing = 'T'

        init_point = lambda: Point(start_position,facing)

        self.assertRaises(Exception, init_point )


    def test_west_right_correction(self):
        eye_x = 0
        eye_y = 0
        start_position = [eye_x,eye_y]
        facing = 'W'

        point = Point(start_position,facing)   

        self.assertEqual(point.orientation(), 'W')

    def test_class_str(self):
        eye_x = 0
        eye_y = 0
        start_position = [eye_x,eye_y]
        facing = 'W'
        pattern = '.*{}.*{}.*{}'.format(eye_x,eye_y,facing)
        
        STRpoint = Point(start_position,facing) 
        result = re.match(str(pattern),str(STRpoint))

        self.assertTrue(result)     
   



