import json


class BytesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj)[2:-1]

        return super().default(self, obj)
