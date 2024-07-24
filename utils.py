import json
import os
import shutil
import typing

import pydantic

__all__ = [
    "Indexable",
    "read",
    "write",
    "read_json",
    "write_json",
    "default",
    "data",
    "parent",
]

json_indent = os.getenv("ENV", "prod") == "dev" and 4 or None
name = __name__
name = name.split('.')
if len(name) >= 2:
    name = name[:-1]
parent = os.path.join(os.getcwd(), *name if __name__ != "__main__" else '')
default = os.path.join(parent, "default")
data = os.path.join(parent, "data")


class Indexable(pydantic.BaseModel):
    """
    pydantic.BaseModel but allows for indexing like a dictionary :D
    """

    def __getitem__(self, item):
        return getattr(self, item)


def read(file: str) -> str:
    return open(file, "r").read()


def write(file: str, data: str):
    open(file, "w").write(data)


def read_json(file: str) -> typing.Dict:
    return json.loads(read(file))


def write_json(file: str, data: dict, indent: int = json_indent):
    write(file, json.dumps(data, indent=indent))


def write_default():
    if not os.path.exists(data):
        shutil.copytree(default, data)
    else:
        for file in os.listdir(default):
            if not os.path.exists(os.path.join(data, file)):
                shutil.copy(os.path.join(default, file), os.path.join(data, file))
