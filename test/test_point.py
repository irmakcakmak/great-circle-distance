import unittest

from point import Point


class PointTest(unittest.TestCase):
    def test_dist_to(self):
        a = Point(0, 0)  # origin meridian on the Equator
        b = Point(1, 0)  # first meridian on the Equator
        self.assertAlmostEqual(a.dist_to(b), 111.3, places=1)

    def test_within_dist(self):
        a = Point(0, 0)
        b = Point(1, 0)
        self.assertTrue(a.within_dist(b, 112))

    def test_not_within_dist(self):
        a = Point(0, 0)
        b = Point(1, 0)
        self.assertFalse(a.within_dist(b, 110))

    def test_radian_conversion(self):
        point = Point(53.339428, -6.257664)
        self.assertAlmostEqual(point.radians.lat, 0.93, places=2)
        self.assertAlmostEqual(point.radians.lon, -0.11, places=2)

    def test_point_rad_from_decimal(self):
        point = Point.PointRad.from_decimal(41, 29)  # istanbul
        self.assertAlmostEqual(point.lat, 0.72, places=2)
        self.assertAlmostEqual(point.lon, 0.51, places=2)

    def test_point_subtraction(self):
        a = Point(53.01, 6.01)
        b = Point(41.23, 29.23)
        diff = a - b
        self.assertIsInstance(diff, Point)
        self.assertAlmostEqual(diff.lat, 11.78, places=2)
        self.assertAlmostEqual(diff.lon, -23.22, places=2)

    def test_rad_subtraction(self):
        a = Point.PointRad(0.93, -0.10)
        b = Point.PointRad(0.71, 0.50)
        diff = a - b
        self.assertIsInstance(diff, Point.PointRad)
        self.assertAlmostEqual(diff.lat, 0.22, places=2)
        self.assertAlmostEqual(diff.lon, -0.6, places=2)

    def test_point_from_malformed_data(self):
        with self.assertRaises(ValueError):
            Point.from_record({"lat": 41, "lon": 29})