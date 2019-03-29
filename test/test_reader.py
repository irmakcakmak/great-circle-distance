import unittest
import reader


class ReaderTest(unittest.TestCase):
    def test_read(self):
        records = []
        for record in reader.read("test/resources/test_file.json"):
            records.append(record)
        self.assertEqual(len(records), 1)
        record = records[0]
        fields = [key for key in record.keys()]
        fields.sort()
        expected = ["latitude", "longitude", "user_id", "name"]
        expected.sort()
        self.assertListEqual(fields, expected)

    def test_missing_field(self):
        records = []
        for record in reader.read("test/resources/test_missing_field_file.json"):
            records.append(record)
        self.assertEqual(len(records), 2)

    def test_invalid_json(self):
        records = []
        for record in reader.read("test/resources/test_invalid_data.json"):
            records.append(record)
        self.assertEqual(len(records), 1)
