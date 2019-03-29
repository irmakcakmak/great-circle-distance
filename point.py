import math


EARTH_RADIUS = 6378.137  # km


class Point:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    @classmethod
    def from_record(cls, data):
        try:
            obj = cls(float(data["latitude"]), float(data["longitude"]))
        except KeyError:
            raise ValueError("Required fields: latitude, longitude")
        return obj

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.lat - other.lat, self.lon - other.lon)
        else:
            raise NotImplementedError

    class PointRad:
        def __init__(self, lat, lon):
            self.lat = lat
            self.lon = lon

        @classmethod
        def from_decimal(cls, lat, lon):
            return cls(math.radians(lat), math.radians(lon))

        def __sub__(self, other):
            if isinstance(other, Point.PointRad):
                return Point.PointRad(self.lat - other.lat, self.lon - other.lon)
            else:
                raise NotImplementedError

    @property
    def radians(self):
        return Point.PointRad.from_decimal(self.lat, self.lon)

    def dist_to(self, other, radius=EARTH_RADIUS):
        """ Calculates distance between two points on a sphere

        :param radius: radius of the sphere
        :param other:
        :return:
        """
        diff = self.radians - other.radians
        A = math.sin(abs(diff.lat) / 2) ** 2
        B = math.cos(self.radians.lat) * math.cos(other.radians.lat) * math.sin(abs(diff.lon) / 2) ** 2
        haversine = 2 * math.asin(math.sqrt(A + B))
        return radius * haversine

    def within_dist(self, other: "Point", max_dist: float,):
        """ Returns if other point is within given radius

        :param max_dist: within perimeter?
        :param other: Point
        :return: bool
        """
        return self.dist_to(other) <= max_dist
