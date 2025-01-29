import unittest
from point import Point

class testPoint(unittest.TestCase):
    # setup is execute dbefore each test
    def setUp(self):
        self.point = Point(3,5)
    # each test name must begin with test....
    def testMoveBy(self):
        self.point.moveBy(-5, -2)
        self.assertEqual(self.point.display(), (-2, 3))


if __name__ == "__main__":
    unittest.main()