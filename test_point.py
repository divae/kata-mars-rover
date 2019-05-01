import unittest 
from point import Point 
      
class TestPoint(unittest.TestCase):  

    def test_assert_is_instante(self):
        eye_x = 0
        eye_y = 0
        position = [eye_x,eye_y]
        direction = ['N']

        eye_x_objective = 0
        eye_y_objective = 0
        new_point = [eye_x_objective,eye_y_objective]

        point = Point(position,direction)

        self.assertIsInstance(point, Point)

    def test_has_error_in_starting_point(self):
        eye_x = None
        eye_y = 'E'
        position = [eye_x,eye_y]
        direction = ['N']

        self.assertRaises(Exception, lambda: Point(position,direction))

    def test_generate_starting_point(self):
        eye_x = 0
        eye_y = 1
        position = [eye_x,eye_y]
        direction = ['N']

        eye_x_objective = 0
        eye_y_objective = 1
        new_point = [eye_x_objective,eye_y_objective]

        point = Point(position,direction)

        self.assertTrue(point.generate(), new_point)


   



