from db import Problems, Submissions
from jugde import JugdeMode, JudgeResult, Limit, Language, Compiler
import os
import shutil

__all__ = [
    "Problems",
    "Submissions",
    "JugdeMode",
    "JudgeResult",
    "Limit",
    "Language",
    "Compiler"
]

if not os.path.exists("data"):
    shutil.copytree("default", "data")
else:
    for file in os.listdir("default"):
        if not os.path.exists(f"data/{file}"):
            shutil.copy(f"default/{file}", f"data/{file}")