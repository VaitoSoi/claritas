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