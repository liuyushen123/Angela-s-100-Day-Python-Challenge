import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_json(filename):
    path = os.path.join(BASE_DIR, "data", filename)
    with open(path, encoding="utf-8") as f:
        return json.load(f)
