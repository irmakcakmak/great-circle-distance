import json
from json import JSONDecodeError

import logging

logging.basicConfig()
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.ERROR)

VALID_FIELDS = ["latitude", "longitude", "user_id", "name"]


def read(filename):
    with open(filename, 'r') as f:
        for line in f:
            try:
                data = json.loads(line)
            except JSONDecodeError as ex:
                # Log and continue to next line
                LOGGER.error("Malformed data: {}".format(ex.msg))
                continue
            # if all fields present, yield; else log and continue
            if all([field in data for field in VALID_FIELDS]):
                yield data
            else:
                LOGGER.error("Missing field in data. Valid fields are {}".format(", ".join(VALID_FIELDS)))
