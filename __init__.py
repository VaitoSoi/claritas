import os
import shutil

try:
    from .utils import default, data
except ImportError:
    from utils import default, data

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
