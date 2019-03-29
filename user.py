class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __lt__(self, other):
        if isinstance(other, User):
            return self.user_id < other.user_id
        else:
            raise NotImplementedError

    @classmethod
    def from_record(cls, data):
        """ Inits user from data.

        :param data: dict with user_id and name fields
        :return: instance
        """
        try:
            obj = cls(data["user_id"], data["name"])
        except KeyError:
            raise ValueError("Required fields: user_id, name")
        return obj

    def __str__(self):
        return "user_id: {} name: {}".format(self.user_id, self.name)
