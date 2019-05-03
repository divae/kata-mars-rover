import unittest 
from point import Point 
      
class TestPoint(unittest.TestCase):  

    def test_has_error_in_starting_point(self):
        eye_x = None
        eye_y = 'E'
        start_position = [eye_x,eye_y]
        facing = ['N']

        self.assertRaises(Exception, lambda: Point(start_position,facing))

    def test_generate_starting_point(self):
        eye_x = 0
        eye_y = 1
        start_position = [eye_x,eye_y]
        facing = ['N']

        eye_x_objective = 0
        eye_y_objective = 1
        actualy_point = [eye_x_objective,eye_y_objective]

        point = Point(start_position)

        self.assertTrue(point.position(), actualy_point)


   



