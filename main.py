import logging

from point import Point
from user import User
import reader

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

ORIGIN = (53.339428, -6.257664)
MAX_DIST = 100


if __name__ == "__main__":
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=True, help="Path to data file")
    args = parser.parse_args()

    # initialise variables, check if within given distance
    users_to_invite = []
    origin = Point(*ORIGIN)
    for record in reader.read(args.file):
        point = Point.from_record(record)
        if point.within_dist(origin, MAX_DIST):
            users_to_invite.append(User.from_record(record))

    # sort users
    users_to_invite.sort()

    # log
    LOGGER.info("Users to invite:")
    for user in users_to_invite:
        LOGGER.info(user)
