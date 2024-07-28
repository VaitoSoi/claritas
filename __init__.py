try:
    from . import utils
    from . import judge
except ImportError:
    import utils
    import judge

# Missing data handler
utils.write_default()

# Load language and compiler data
judge.load()

try:
    # from .db import Problems, Submissions
    from .judge import JudgeMode, JudgeResult, Limit, Language, Compiler, JudgeSession, Status, TestType
    from .utils import Indexable
except ImportError:
    # from db import Problems, Submissions
    from judge import JudgeMode, JudgeResult, Limit, Language, Compiler, JudgeSession, Status, TestType
    from utils import Indexable

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
