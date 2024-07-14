import os
import shutil

name = __name__
name = name.split('.')
if len(name) >= 2:
    name = name[:-1]
parent = os.path.join(os.getcwd(), *name if __name__ != "__main__" else '')
default = os.path.join(parent, "default")
data = os.path.join(parent, "data")

# Missing data handler
if not os.path.exists(data):
    shutil.copytree(default, data)
else:
    for file in os.listdir(default):
        if not os.path.exists(f"data/{file}"):
            shutil.copy(f"default/{file}", f"data/{file}")

try:
    from .db import Problems, Submissions
    from .jugde import JudgeMode, JudgeResult, Limit, Language, Compiler, File, JudgeSession, Status
except ImportError:
    from db import Problems, Submissions
    from jugde import JudgeMode, JudgeResult, Limit, Language, Compiler, File, JudgeSession, Status

__all__ = [
    "Problems",
    "Submissions",
    "JudgeMode",
    "JudgeSession",
    "JudgeResult",
    "Limit",
    "Language",
    "Compiler",
    "File",
    "Status"
]
