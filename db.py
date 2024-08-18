import os

from . import utils

permission_json = os.path.join(utils.data, "permission.json")
Permission: list[str] = utils.read_json(permission_json)
