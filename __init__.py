from . import judge
from . import utils
# from .db import Problems, Submissions

# Missing data handler
utils.write_default()

# Load language and compiler data
judge.load()


from .utils import Indexable, PydanticIndexable
from .judge import JudgeMode, JudgeResult, Limit, Language, Compiler, JudgeSession, Status, TestType

__all__ = [
    "utils",
    "judge",
    "Indexable",
    # "Problems",
    # "Submissions",
    "JudgeMode",
    "JudgeSession",
    "JudgeResult",
    "Limit",
    "TestType",
    "Language",
    "Compiler",
    "Status"
]
