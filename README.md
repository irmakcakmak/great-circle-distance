Calculates [great-circle distance](https://en.wikipedia.org/wiki/Great-circle_distance) between two coordinates, using haversine formula.

Example implementation reads from a file with lines having data with the following format:
```json
{"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}
```
and finds users within the given perimeter and logs their data.

Run with command:
```bash
python3 main.py --file <file_path>
```

Run tests:
```bash
python3 -m unittest discover
```

