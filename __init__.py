import os
import shutil

# Missing data handler
if not os.path.exists("data"):
    shutil.copytree("default", "data")
else:
    for file in os.listdir("default"):
        if not os.path.exists(f"data/{file}"):
            shutil.copy(f"default/{file}", f"data/{file}")

try:
    from .db import Problems, Submissions
    from .jugde import JugdeMode, JudgeResult, Limit, Language, Compiler
except ImportError:
    from db import Problems, Submissions
    from jugde import JugdeMode, JudgeResult, Limit, Language, Compiler

__all__ = [
    "Problems",
    "Submissions",
    "JugdeMode",
    "JudgeResult",
    "Limit",
    "Language",
    "Compiler",
]
