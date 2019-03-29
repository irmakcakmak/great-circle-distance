import argparse
import logging

from point import Point
from user import User
import reader

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

ORIGIN = (53.339428, -6.257664)
MAX_DIST = 100  # km


def latitude(lat):
    lat = float(lat)
    if lat < -90.0 or lat > 90.0:
        raise argparse.ArgumentTypeError("Latitude is between -90 and 90")
    return lat


def longitude(lon):
    lon = float(lon)
    if lon < -180.0 or lon > 180.0:
        raise argparse.ArgumentTypeError("Longitude is between -180 and 180")
    return lon


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=True, help="Path to data file")
    parser.add_argument("--max-dist", type=float, default=MAX_DIST, help="Max distance in kilometers")
    parser.add_argument("--lat", type=latitude, default=ORIGIN[0], help="Origin latitude to calculate distances from")
    parser.add_argument("--lon", type=longitude, default=ORIGIN[1], help="Origin longitude to calculate distances from")
    args = parser.parse_args()

    # initialise variables, check if within given distance
    users_to_invite = []
    origin = Point(args.lat, args.lon)
    for record in reader.read(args.file):
        point = Point.from_record(record)
        if point.within_dist(origin, args.max_dist):
            users_to_invite.append(User.from_record(record))

    # sort users
    users_to_invite.sort()

    # log
    LOGGER.info("Users to invite:")
    for user in users_to_invite:
        LOGGER.info(user)
