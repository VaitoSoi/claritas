import json
import os
import typing

json_indent = os.getenv("ENV", "prod") == "dev" and 4 or None

def read(file: str) -> str:
    return open(file, "r").read()

def write(file: str, data: str):
    open(file, "w").write(data)

def read_json(file: str) -> typing.Dict:
    return json.loads(read(file))

def write_json(file: str, data: dict, indent: int = json_indent):
    write(file, json.dumps(data, indent=indent))

name = __name__
name = name.split('.')
if len(name) >= 2:
    name = name[:-1]
parent = os.path.join(os.getcwd(), *name if __name__ != "__main__" else '')
default = os.path.join(parent, "default")
data = os.path.join(parent, "data")
